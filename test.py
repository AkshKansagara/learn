import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import qrcode
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    key_entry.delete(0, tk.END)
    key_entry.insert(0, key.decode())

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

def generate_qr_code():
    url = url_entry.get()
    
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL")
        return

    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        img = img.resize((200, 200))
        photo = ImageTk.PhotoImage(img)
        qr_label.config(image=photo)
        qr_label.image = photo

        save_button.config(state="normal")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def save_qr_code():
    filepath = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=(("PNG files", "*.png"), ("All files", "*.*"))
    )

    if not filepath:
        return

    try:
        qr_label.image.save(filepath)
        messagebox.showinfo("Success", "QR code saved successfully")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def reset():
    url_entry.delete(0, tk.END)
    qr_label.config(image="", text="QR Code will be displayed here")
    save_button.config(state="disabled")

def on_enter(e):
    e.widget['foreground'] = 'black'    
    e.widget['width'] = e.widget.default_width + 2  
    e.widget['height'] = e.widget.default_height + 1  

def on_leave(e):
    e.widget['background'] = e.widget.default_bg 
    e.widget['foreground'] = e.widget.default_fg 
    e.widget['width'] = e.widget.default_width  
    e.widget['height'] = e.widget.default_height 

root = tk.Tk()
root.title("Cryptography & QR Code Generator by IU2341051315")
root.geometry("600x600")

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

crypto_tab = ttk.Frame(notebook)
notebook.add(crypto_tab, text="Cryptography Tool")

key_label = tk.Label(crypto_tab, text="Encryption Key:")
key_label.grid(row=0, column=0, padx=10, pady=10)

key_entry = tk.Entry(crypto_tab, width=50)
key_entry.grid(row=0, column=1, padx=10, pady=10)

generate_key_btn = tk.Button(crypto_tab, text="Generate Key", bg="blue", fg="white", command=generate_key)
generate_key_btn.grid(row=0, column=2, padx=10, pady=10)

message_label = tk.Label(crypto_tab, text="Enter Message:")
message_label.grid(row=1, column=0, padx=10, pady=10)

message_entry = tk.Text(crypto_tab, height=5, width=50)
message_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

encrypt_btn = tk.Button(crypto_tab, text="Encrypt", command=encrypt_message, bg="green", fg="white", height="1", width="12")
encrypt_btn.grid(row=2, column=1, padx=10, pady=10, sticky="e")

decrypt_btn = tk.Button(crypto_tab, text="Decrypt", command=decrypt_message, bg="red", fg="white", height="1", width="12")
decrypt_btn.grid(row=2, column=2, padx=10, pady=10, sticky="w")

result_label = tk.Label(crypto_tab, text="Result:")
result_label.grid(row=3, column=0, padx=10, pady=10)

result_text = tk.Text(crypto_tab, height=5, width=50)
result_text.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

qr_tab = ttk.Frame(notebook)
notebook.add(qr_tab, text="QR Code Generator")

title_label = tk.Label(qr_tab, text="QR Code Generator", font=("Arial", 20))
title_label.pack(pady=20)

url_label = tk.Label(qr_tab, text="Enter URL or Text :", font=("Calibri", 14, "bold"))
url_label.pack()

url_entry = tk.Entry(qr_tab, width=50)
url_entry.pack(pady=10)

generate_button = tk.Button(qr_tab, text="Generate QR Code", height="2", width=23, bg="#00bd56", fg="white", command=generate_qr_code)
generate_button.pack(pady=10)
generate_button.default_bg = generate_button['background']
generate_button.default_fg = generate_button['foreground']
generate_button.default_width = generate_button['width']
generate_button.default_height = 2  

qr_label = tk.Label(qr_tab, text="QR Code will be displayed here", font=("Calibri", 12))
qr_label.pack()

save_button = tk.Button(qr_tab, text="Save QR Code", height="2", width=23, bg="#1089ff", fg="white", command=save_qr_code, state="disabled")
save_button.pack(pady=10)
save_button.default_bg = save_button['background']
save_button.default_fg = save_button['foreground']
save_button.default_width = save_button['width']
save_button.default_height = 2

reset_button = tk.Button(qr_tab, text="Reset", height="2", width=23, bg="#ed3833", fg="white", command=reset)
reset_button.pack(pady=10)
reset_button.default_bg = reset_button['background']
reset_button.default_fg = reset_button['foreground']
reset_button.default_width = reset_button['width']
reset_button.default_height = 2

generate_button.bind("<Enter>", on_enter)
generate_button.bind("<Leave>", on_leave)

save_button.bind("<Enter>", on_enter)
save_button.bind("<Leave>", on_leave)

reset_button.bind("<Enter>", on_enter)
reset_button.bind("<Leave>", on_leave)

encrypt_btn.bind("<Enter>", on_enter)
encrypt_btn.bind("<Leave>", on_leave)

decrypt_btn.bind("<Enter>", on_enter)
decrypt_btn.bind("<Leave>", on_leave)

generate_key_btn.bind("<Enter>", on_enter)
generate_key_btn.bind("<Leave>", on_leave)

root.mainloop()