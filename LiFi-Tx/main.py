import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import base64


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

        # Encode the image in base64
        with open(file_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode("utf-8")
        print("Base64 encoded image:")
        print(base64_image)


app = tk.Tk()
app.title("Image Viewer")

upload_button = tk.Button(app, text="Upload Image", command=open_image)
upload_button.pack()

image_label = tk.Label(app)
image_label.pack()

app.mainloop()
