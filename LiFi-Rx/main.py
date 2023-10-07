import tkinter as tk
import base64
import io
import PIL.Image
import PIL.ImageTk
import serial
import threading

# Create a function to update the image label
def update_image(encoded_image):
    try:
        # Decode the Base64 encoded image
        decoded_image = base64.b64decode(encoded_image)

        # Create a PIL image from the decoded data
        image_data = io.BytesIO(decoded_image)
        img = PIL.Image.open(image_data)

        # Update the Tkinter label with the new image
        img = PIL.ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img  # Keep a reference to avoid garbage collection issues
    except Exception as e:
        print(f"Error updating image: {str(e)}")

# Function to read and process data from the serial port
def read_serial():
    while True:
        try:
            # Read data from the serial port
            data = ser.readline().decode().strip()

            # Check if the data is a valid Base64 encoded image
            if data.startswith("data:image/jpeg;base64,"):
                encoded_image = data.replace("data:image/jpeg;base64,", "")
                update_image(encoded_image)
        except Exception as e:
            print(f"Serial port error: {str(e)}")

# Create the main application window
app = tk.Tk()
app.title("Li-Fi Image Decoder")

# Create a label to display the image
image_label = tk.Label(app)
image_label.pack()

# Create a serial connection (modify the port and baud rate as needed)
ser = serial.Serial('COM3', baudrate=9600)

# Start a thread to read and process data from the serial port
serial_thread = threading.Thread(target=read_serial)
serial_thread.daemon = True  # Set the thread as a daemon so it exits when the main app is closed
serial_thread.start()

# Start the Tkinter main loop
app.mainloop()
