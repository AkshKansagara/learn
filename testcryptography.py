import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

# Function to generate and display a new encryption key
def generate_key():
    key = Fernet.generate_key()
    key_entry.delete(0, tk.END)
    key_entry.insert(0, key.decode())

# Function to encrypt the message
def encrypt_message():
    key = key_entry.get().encode()
    try:
        fernet = Fernet(key)
        message = message_entry.get("1.0", tk.END).strip()
        encrypted_message = fernet.encrypt(message.encode())
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, encrypted_message.decode())
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to decrypt the message
def decrypt_message():
    key = key_entry.get().encode()
    try:
        fernet = Fernet(key)
        encrypted_message = message_entry.get("1.0", tk.END).strip()
        decrypted_message = fernet.decrypt(encrypted_message.encode()).decode()
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, decrypted_message)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Encryption and Decryption Tool")

# Create the labels, entries, and buttons
key_label = tk.Label(root, text="Encryption Key:")
key_label.grid(row=0, column=0, padx=10, pady=10)

key_entry = tk.Entry(root, width=50)
key_entry.grid(row=0, column=1, padx=10, pady=10)

generate_key_btn = tk.Button(root, text="Generate Key", command=generate_key)
generate_key_btn.grid(row=0, column=2, padx=10, pady=10)

message_label = tk.Label(root, text="Enter Message:")
message_label.grid(row=1, column=0, padx=10, pady=10)

message_entry = tk.Text(root, height=5, width=50)
message_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

encrypt_btn = tk.Button(root, text="Encrypt", command=encrypt_message)
encrypt_btn.grid(row=2, column=1, padx=10, pady=10, sticky="e")

decrypt_btn = tk.Button(root, text="Decrypt", command=decrypt_message)
decrypt_btn.grid(row=2, column=2, padx=10, pady=10, sticky="w")

result_label = tk.Label(root, text="Result:")
result_label.grid(row=3, column=0, padx=10, pady=10)

result_text = tk.Text(root, height=5, width=50)
result_text.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
