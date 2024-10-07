import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import qrcode
import cv2

qr_image = None  # Initialize a global variable

# Function to generate QR code
def generate_qr_code():
    global qr_image  # Use the global variable
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL")
        return

    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="black", back_color="white")  # Save the original image
        img = qr_image.resize((200, 200))
        
        photo = ImageTk.PhotoImage(img)
        qr_label.config(image=photo)
        qr_label.image = photo

        save_button.config(state="normal")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to save QR code image
def save_qr_code():
    global qr_image  # Access the global variable
    if qr_image is None:
        messagebox.showerror("Error", "No QR code generated to save.")
        return

    filepath = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=(("PNG files", "*.png"), ("All files", "*.*")))
    if not filepath:
        return

    try:
        qr_image.save(filepath)  # Save the original image
        messagebox.showinfo("Success", "QR code saved successfully")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def reset():
    url_entry.delete(0, tk.END)
    qr_label.config(image="", text="QR Code will be displayed here")
    save_button.config(state="disabled")

def read_qr_code():
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if not filepath:
        return

    detector = cv2.QRCodeDetector()  # Create an instance of QRCodeDetector
    try:
        img = cv2.imread(filepath)
        # Use the detectAndDecode method to read QR code
        data, bbox, _ = detector.detectAndDecode(img)  # Call the detectAndDecode method
        if data:
            messagebox.showinfo("QR Code Data", f"Decoded Data: {data}")
        else:
            messagebox.showwarning("No QR Code Detected", "No QR code could be detected in the image.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main application window
root = tk.Tk()
root.title("QR Code Generator and Reader")
root.geometry("600x600")

# QR Code Generator section
title_label = tk.Label(root, text="QR Code Generator", font=("Arial", 20))
title_label.pack(pady=20)

url_label = tk.Label(root, text="Enter URL or Text:", font=("Calibri", 14, "bold"))
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate QR Code", height="2", width=23, bg="#00bd56", fg="white", command=generate_qr_code)
generate_button.pack(pady=10)

qr_label = tk.Label(root, text="QR Code will be displayed here", font=("Calibri", 12))
qr_label.pack()

save_button = tk.Button(root, text="Save QR Code", height="2", width=23, bg="#1089ff", fg="white", command=save_qr_code, state="disabled")
save_button.pack(pady=10)

read_button = tk.Button(root, text="Read QR Code", height="2", width=23, bg="#ffd700", fg="black", command=read_qr_code)
read_button.pack(pady=20)

reset_button = tk.Button(root, text="Reset", height="2", width=23, bg="#ed3833", fg="white", command=reset)
reset_button.pack(pady=10)
# Run the tkinter main loop
root.mainloop()