#program2

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
root.title("QR Code Generator by IU2341051315")
root.geometry("550x550")

title_label = tk.Label(root, text="QR Code Generator", font=("Arial", 20))
title_label.pack(pady=20)

url_label = tk.Label(root, text="Enter URL or Text :", font=("Calibri",14,"bold"))
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate QR Code", height="2", width=23, bg="#00bd56", fg="white", command=generate_qr_code)
generate_button.pack(pady=10)
generate_button.default_bg = generate_button['background']
generate_button.default_fg = generate_button['foreground']
generate_button.default_width = generate_button['width'] 
generate_button.default_height = 2  

qr_label = tk.Label(root, text="QR Code will be displayed here", font=("Calibri",12))
qr_label.pack()

save_button = tk.Button(root, text="Save QR Code", height="2", width=23, bg="#1089ff", fg="white", command=save_qr_code, state="disabled")
save_button.pack(pady=10)
save_button.default_bg = save_button['background']
save_button.default_fg = save_button['foreground']
save_button.default_width = save_button['width']
save_button.default_height = 2

reset_button = tk.Button(root, text="Reset", height="2", width=23, bg="#ed3833", fg="white", command=reset)
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

root.mainloop()
