import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox
from cryptography.fernet import Fernet
import time

KEY_FILE = "encryption.key"

def load_or_generate_key():
    try:
        with open(KEY_FILE, 'rb') as f:
            return f.read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as f:
            f.write(key)
        return key

cipher = Fernet(load_or_generate_key())

def encrypt_message(message):
    return cipher.encrypt(message.encode())

def decrypt_message(message):
    try:
        return cipher.decrypt(message).decode()
    except Exception as e:
        print(f"Error decrypting message: {e}")
        return None

def add_timestamp(message):
    return f"{time.strftime('%H:%M:%S')} - {message}"

def receive_messages(sock, chat_display, display_name):
    while True:
        try:
            message, _ = sock.recvfrom(4096)
            decrypted_message = decrypt_message(message)
            if decrypted_message:
                timestamped_message = add_timestamp(f"{display_name}: {decrypted_message}")
                chat_display.config(state=tk.NORMAL)
                chat_display.insert(tk.END, f"\n{timestamped_message}")
                chat_display.config(state=tk.DISABLED)
        except (socket.error, ValueError) as e:
            print("Error receiving message:", e)
            break

def send_message(sock, peer_address, message_entry, chat_display):
    message = message_entry.get()
    if message:
        try:
            encrypted_message = encrypt_message(message)
            sock.sendto(encrypted_message, peer_address)
            timestamped_message = add_timestamp(f"You: {message}")
            chat_display.config(state=tk.NORMAL)
            chat_display.insert(tk.END, f"\n{timestamped_message}")
            chat_display.config(state=tk.DISABLED)
            message_entry.delete(0, tk.END)
        except Exception as e:
            print(f"Error sending message: {e}")

def clear_chat(chat_display):
    chat_display.config(state=tk.NORMAL)
    chat_display.delete(1.0, tk.END)
    chat_display.config(state=tk.DISABLED)


def main():
    host = "127.0.0.1"  # Localhost for testing
    port = int(simpledialog.askstring("Port Input", "Enter your listening port:"))
    peer_ip = simpledialog.askstring("Peer Input", "Enter peer's IP:")
    peer_port = int(simpledialog.askstring("Peer Port Input", "Enter peer's port:"))
    
    display_name = simpledialog.askstring("Display Name", "Enter your display name:")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))

    # GUI setup
    root = tk.Tk()
    root.title("P2P Chat")

    chat_display = scrolledtext.ScrolledText(root, state=tk.DISABLED, width=50, height=20)
    chat_display.pack(pady=10)

    message_entry = tk.Entry(root, width=40)
    message_entry.pack(side=tk.LEFT, padx=5)

    send_button = tk.Button(root, text="Send", command=lambda: send_message(sock, (peer_ip, peer_port), message_entry, chat_display, display_name))
    send_button.pack(side=tk.RIGHT, padx=5)

    clear_button = tk.Button(root, text="Clear Chat", command=lambda: clear_chat(chat_display))
    clear_button.pack(side=tk.LEFT, padx=5)

    def on_enter(event=None):
        send_message(sock, (peer_ip, peer_port), message_entry, chat_display, display_name)
    
    message_entry.bind("<Return>", on_enter)

    receive_thread = threading.Thread(target=receive_messages, args=(sock, chat_display, display_name), daemon=True)
    receive_thread.start()

    root.mainloop()

    sock.close()

if __name__ == "__main__":
    main()
