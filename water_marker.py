import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

THEME_COLOR = "#375362"


class WaterMarker:
    def __init__(self, water_text=""):
        self.images_paths = None
        self.watermark_text = water_text

        # Create the UI
        self.window = tk.Tk()
        self.window.title("Watermark v.1.0.0")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.text_widget = tk.Text(self.window, wrap=tk.WORD, height=15, width=35, bg=THEME_COLOR)
        self.open_button = tk.Button(self.window, text="Open Image", command=self.open_file_dialog,
                                     highlightbackground=THEME_COLOR)
        self.open_button.pack(padx=20, pady=10)
        self.image_label = tk.Label(self.window, bg=THEME_COLOR)
        self.image_label.pack(padx=20, pady=20)
        self.status_label = tk.Label(self.window, text="", padx=20, pady=10, bg=THEME_COLOR)
        self.status_label.pack()

        self.convert_button = tk.Button(self.window, text="Convert", command=self.create_watermark,
                                        highlightbackground=THEME_COLOR)
        self.convert_button.pack(padx=20, pady=10)

        self.window.mainloop()

    def display_images(self):
        """Load image from saved paths, show preview on the screen and show status in the label"""
        image = Image.open(self.images_paths)
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo, height=400)
        self.image_label.photo = photo
        self.set_status(f"Image loaded: {self.images_paths}")

    def open_file_dialog(self):
        """Open the file dialog to choose the file"""
        f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]
        filename = filedialog.askopenfilename(filetypes=f_types)

        if filename:
            self.images_paths = filename
            self.display_images()

    def create_watermark(self):
        """Open the image from saved paths, load the font, add text on the image, save the file and show status"""
        try:
            img = Image.open(self.images_paths)
            draw = ImageDraw.Draw(img)

            font = ImageFont.truetype("sans-serif.ttf", 16)

            draw.text((0, 0), f"{self.watermark_text}", (255, 255, 255), font=font)
            img = img.convert('RGB')
            img.save('sample-out.jpg')

            self.images_paths = "sample-out.jpg"
            self.display_images()
            self.set_status("Watermark successfully added!")
        except Exception as e:
            print(f"There was error: {e}")
            self.set_status("Error!")

    def set_status(self, text):
        self.status_label.config(text=f"{text}")
