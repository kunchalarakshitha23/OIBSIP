# Python Task 5 – Real-Time Chat Application

**Oasis Infobyte Python Programming Internship — Task 5**

A terminal-based, real-time chat application built with Python TCP sockets. Multiple clients can connect to one server, exchange messages instantly, and see timestamps and join/leave notifications.

## Features

- Client-server communication using TCP sockets.
- Multiple simultaneous clients handled with threads.
- Live message broadcasting to all connected users.
- Username shown with every message.
- Date and time displayed for messages and system notifications.
- Graceful exit using `/quit`.
- Uses only Python's standard library; no third-party packages required.

## Project files

| File | Description |
| --- | --- |
| `server.py` | Starts the TCP server and broadcasts messages. |
| `client.py` | Connects a user to the chat server. |
| `requirements.txt` | Lists external dependencies (none). |

## Requirements

- Python 3.8 or later.
- Two or more terminal windows for testing multiple users.
- Clients on different computers must be on the same network (or have a reachable server address and permitted firewall port).

## How to run

### 1. Open a terminal in this folder

### 2. Start the server

```bash
python server.py
```

The server listens on port `5000`.

### 3. Start the first client in another terminal

```bash
python client.py
```

Enter a username when prompted.

### 4. Start more clients

Open another terminal and run:

```bash
python client.py
```

Each client can now send and receive messages in real time.

### Connect from another computer

Find the server computer's local IP address. On the client computer, run:

```bash
python client.py SERVER_IP_ADDRESS 5000
```

Allow inbound TCP traffic on port `5000` in the server computer's firewall if needed. Do not expose the server to the public internet without adding suitable security controls.

### Leave the chat

Type `/quit` and press Enter.

## How it works

1. The server creates a TCP socket, binds to port 5000, and listens for connections.
2. Every accepted client is handled by a separate thread.
3. Clients send newline-delimited JSON messages to the server.
4. The server broadcasts each chat message with the sender's username and timestamp.
5. The client uses a receiving thread so incoming messages appear while the user is typing.

## Notes

This is an educational project intended for local-network demonstration. It does not include authentication, encryption, message history, or moderation.

## Author

Kunchala Rakshitha

Oasis Infobyte Python Programming Internship – Task 5
