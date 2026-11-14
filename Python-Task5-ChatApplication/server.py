"""Multi-client chat server using Python TCP sockets."""
import json
import socket
import threading
from datetime import datetime

HOST = "0.0.0.0"
PORT = 5000
clients = {}
clients_lock = threading.Lock()


def timestamp():
    return datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S")


def send_json(client_socket, payload):
    data = (json.dumps(payload, ensure_ascii=False) + "\n").encode("utf-8")
    client_socket.sendall(data)


def broadcast(payload, exclude=None):
    with clients_lock:
        recipients = list(clients.items())
    dead = []
    for sock, _username in recipients:
        if sock is exclude:
            continue
        try:
            send_json(sock, payload)
        except OSError:
            dead.append(sock)
    for sock in dead:
        remove_client(sock)


def remove_client(client_socket):
    with clients_lock:
        username = clients.pop(client_socket, None)
    try:
        client_socket.close()
    except OSError:
        pass
    if username:
        broadcast({
            "type": "system",
            "text": f"{username} left the chat.",
            "timestamp": timestamp(),
        })


def handle_client(client_socket, address):
    username = None
    buffer = ""
    try:
        reader = client_socket.makefile("r", encoding="utf-8")
        first_line = reader.readline()
        if not first_line:
            return
        join_data = json.loads(first_line)
        username = str(join_data.get("username", "")).strip()[:24]
        if not username:
            send_json(client_socket, {"type": "error", "text": "A username is required."})
            return

        with clients_lock:
            clients[client_socket] = username

        send_json(client_socket, {
            "type": "system",
            "text": f"Welcome, {username}! Type /quit to leave.",
            "timestamp": timestamp(),
        })
        broadcast({
            "type": "system",
            "text": f"{username} joined the chat.",
            "timestamp": timestamp(),
        }, exclude=client_socket)
        print(f"[+] {username} connected from {address}")

        for line in reader:
            try:
                message = json.loads(line)
            except json.JSONDecodeError:
                continue
            text = str(message.get("text", "")).strip()
            if not text:
                continue
            if text == "/quit":
                break
            broadcast({
                "type": "message",
                "username": username,
                "text": text[:2000],
                "timestamp": timestamp(),
            })
    except (OSError, json.JSONDecodeError):
        pass
    finally:
        remove_client(client_socket)
        if username:
            print(f"[-] {username} disconnected")


def start_server():
    print(f"Chat server listening on {HOST}:{PORT}")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()
        try:
            while True:
                client_socket, address = server.accept()
                threading.Thread(
                    target=handle_client,
                    args=(client_socket, address),
                    daemon=True,
                ).start()
        except KeyboardInterrupt:
            print("\nServer shutting down...")


if __name__ == "__main__":
    start_server()
