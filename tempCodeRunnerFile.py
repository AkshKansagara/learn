import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import qrcode

def generate_qr_code():
    # Get the URL from the input field
    url = url_entry.get()
    
    # Check if the URL is empty
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL")
        return

    try:
        # Generate the QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Display the QR code
        img = img.resize((200, 200))
        photo = ImageTk.PhotoImage(img)
        qr_label.config(image=photo)
        qr_label.image = photo

        # Enable the save button
        save_button.config(state="normal")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def save_qr_code():
    # Get the file path
    filepath = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=(("PNG files", "*.png"), ("All files", "*.*"))
    )

    # Check if the file path is valid
    if not filepath:
        return

    try:
        # Save the QR code to the file
        qr_label.image.save(filepath)
        messagebox.showinfo("Success", "QR code saved successfully")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("500x500")

# Create the title label
title_label = tk.Label(root, text="QR Code Generator", font=("Arial", 20))
title_label.pack(pady=20)

# Create the URL input field
url_label = tk.Label(root, text="Enter URL:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)

# Create the generate button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack(pady=10)

# Create the QR code label
qr_label = tk.Label(root, text="QR Code will be displayed here")
qr_label.pack()

# Create the save button
save_button = tk.Button(root, text="Save QR Code", command=save_qr_code, state="disabled")
save_button.pack(pady=10)

# Start the main event loop
root.mainloop()