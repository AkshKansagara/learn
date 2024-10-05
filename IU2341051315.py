import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import qrcode

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

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("500x500")

title_label = tk.Label(root, text="QR Code Generator", font=("Arial", 20))
title_label.pack(pady=20)

url_label = tk.Label(root, text="Enter URL:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate QR Code", bg="green", fg="white", command=generate_qr_code)
generate_button.pack(pady=10)

qr_label = tk.Label(root, text="QR Code will be displayed here")
qr_label.pack()

save_button = tk.Button(root, text="Save QR Code", command=save_qr_code, state="disabled")
save_button.pack(pady=10)

root.mainloop()