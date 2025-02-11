import tkinter as tk
import qrcode
import datetime
from PIL import Image, ImageTk
import time

def generate_qr_code():
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    
    qr = qrcode.make(current_time)
    
    qr_img = ImageTk.PhotoImage(qr)
    
    return qr_img

def update_qr_code():
    qr_img = generate_qr_code()
    qr_label.config(image=qr_img)
    qr_label.image = qr_img
    window.after(1000, update_qr_code)

window = tk.Tk()
window.title("QR Code Clock")

qr_label = tk.Label(window)
qr_label.pack(padx=20, pady=20)

update_qr_code()

window.mainloop()
