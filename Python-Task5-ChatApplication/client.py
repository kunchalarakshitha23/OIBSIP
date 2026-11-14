"""Terminal chat client using Python TCP sockets."""
import json
import socket
import sys
import threading

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 5000


def receive_messages(client_socket):
    try:
        reader = client_socket.makefile("r", encoding="utf-8")
        for line in reader:
            try:
                message = json.loads(line)
            except json.JSONDecodeError:
                continue

            kind = message.get("type")
            stamp = message.get("timestamp", "")
            if kind == "message":
                print(f"\n[{stamp}] {message.get('username', 'Unknown')}: {message.get('text', '')}")
            elif kind == "system":
                print(f"\n[{stamp}] * {message.get('text', '')}")
            elif kind == "error":
                print(f"\nError: {message.get('text', '')}")
    except OSError:
        pass
    finally:
        print("\nDisconnected from the chat server.")


def main():
    host = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_HOST
    port = int(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_PORT
    username = input("Enter your chat name: ").strip()
    if not username:
        print("A username is required.")
        return

    try:
        with socket.create_connection((host, port), timeout=10) as client_socket:
            client_socket.settimeout(None)
            client_socket.sendall(
                (json.dumps({"username": username}) + "\n").encode("utf-8")
            )
            receiver = threading.Thread(
                target=receive_messages,
                args=(client_socket,),
                daemon=True,
            )
            receiver.start()

            print("Connected! Send a message, or type /quit to exit.")
            while True:
                try:
                    text = input()
                except (EOFError, KeyboardInterrupt):
                    text = "/quit"
                payload = (json.dumps({"text": text}) + "\n").encode("utf-8")
                try:
                    client_socket.sendall(payload)
                except OSError:
                    break
                if text.strip() == "/quit":
                    break
    except (OSError, ValueError) as error:
        print(f"Could not connect to {host}:{port}: {error}")


if __name__ == "__main__":
    main()
