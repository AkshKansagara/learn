import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import qrcode
import cv2

qr_image = None  

def generate_qr_code():
    global qr_image 
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL")
        return

    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="black", back_color="white")  
        img = qr_image.resize((200, 200))
        
        photo = ImageTk.PhotoImage(img)
        qr_label.config(image=photo)
        qr_label.image = photo

        save_button.config(state="normal")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def save_qr_code():
    global qr_image  
    if qr_image is None:
        messagebox.showerror("Error", "No QR code generated to save.")
        return

    filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=(("PNG files", "*.png"), ("All files", "*.*")))
    if not filepath:
        return

    try:
        qr_image.save(filepath) 
        messagebox.showinfo("Success", "QR code saved successfully")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def reset_qr_generator():
    url_entry.delete(0, tk.END)
    qr_label.config(image="", text="QR Code will be displayed here")
    save_button.config(state="disabled")

def reset_qr_reader():
    qr_data_text.delete(1.0, tk.END)

def read_qr_code():
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if not filepath:
        return

    detector = cv2.QRCodeDetector()
    try:
        img = cv2.imread(filepath)
        data, bbox, _ = detector.detectAndDecode(img)  
        if data:
            qr_data_text.delete(1.0, tk.END)  
            qr_data_text.insert(tk.END, data)  
        else:
            messagebox.showwarning("No QR Code Detected", "No QR code could be detected in the image.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("QR Code Generator and Reader")

root.attributes('-fullscreen', True)

def exit_fullscreen(event=None):
    root.attributes('-fullscreen', False)

root.bind("<Escape>", exit_fullscreen)

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

generate_tab = ttk.Frame(notebook)
notebook.add(generate_tab, text="Generate QR Code")

read_tab = ttk.Frame(notebook)
notebook.add(read_tab, text="Read QR Code")

title_label = tk.Label(generate_tab, text="QR Code Generator", font=("Arial", 20))
title_label.pack(pady=20)

url_label = tk.Label(generate_tab, text="Enter URL or Text:", font=("Calibri", 14, "bold"))
url_label.pack()

url_entry = tk.Entry(generate_tab, width=50)
url_entry.pack(pady=10)

generate_button = tk.Button(generate_tab, text="Generate QR Code", height="2", width=23, bg="#00bd56", fg="white", command=generate_qr_code)
generate_button.pack(pady=10)

qr_label = tk.Label(generate_tab,) 
qr_label.pack()

save_button = tk.Button(generate_tab, text="Save QR Code", height="2", width=23, bg="#1089ff", fg="white", command=save_qr_code, state="disabled")
save_button.pack(pady=10)

reset_button = tk.Button(generate_tab, text="Reset", height="2", width=23, bg="#ed3833", fg="white", command=reset_qr_generator)
reset_button.pack(pady=10)

reader_title_label = tk.Label(read_tab, text="Click below button to select the image of QRCode", font=("Arial", 15))
reader_title_label.pack(pady=20)

read_button = tk.Button(read_tab, text="Read QR Code", height="2", width=23, bg="#ffd700", fg="black", command=read_qr_code)
read_button.pack(pady=20)

qr_data_text = tk.Text(read_tab, height=1, width=40, font=("Calibri", 12))
qr_data_text.pack(pady=10)

reset_reader_button = tk.Button(read_tab, text="Reset", height="2", width=23, bg="#ed3833", fg="white", command=reset_qr_reader)
reset_reader_button.pack(pady=10)

root.mainloop()