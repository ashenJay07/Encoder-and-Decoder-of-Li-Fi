import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        screen_width = app.winfo_screenwidth()
        screen_height = app.winfo_screenheight()
        desired_width = int(0.75 * screen_width)
        desired_height = int(0.75 * screen_height)
        image = image.resize((desired_width, desired_height))
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.photo = photo  # Prevent garbage collection

app = tk.Tk()
app.title("Image Viewer")

upload_button = tk.Button(app, text="Upload Image", command=open_image)
upload_button.pack()

image_label = tk.Label(app)
image_label.pack()

app.mainloop()
