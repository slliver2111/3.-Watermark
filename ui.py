import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

THEME_COLOR = "#375362"


class Interface:
    def __init__(self, water_text=""):
        self.images_paths = None
        self.watermark_text = water_text

        self.window = tk.Tk()
        self.window.title("Watermark Adder")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.text_widget = tk.Text(self.window, wrap=tk.WORD, height=15, width=35, bg=THEME_COLOR)
        self.open_button = tk.Button(self.window, text="Open Image", command=self.upload_action,
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
        image = Image.open(self.images_paths)
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo, height=400)
        self.image_label.photo = photo
        self.status_label.config(text=f"Image loaded: {self.images_paths}")

    def upload_action(self):
        f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]
        filename = filedialog.askopenfilename(filetypes=f_types)

        if filename:
            self.images_paths = filename
            self.display_images()

    def create_watermark(self):
        try:
            img = Image.open(self.images_paths)
            draw = ImageDraw.Draw(img)
            # font = ImageFont.truetype(<font-file>, <font-size>)
            font = ImageFont.truetype("sans-serif.ttf", 16)
            # draw.text((x, y),"Sample Text",(r,g,b))
            draw.text((0, 0), f"{self.watermark_text}", (255, 255, 255), font=font)
            img = img.convert('RGB')
            img.save('sample-out.jpg')
            self.status_label.config(text="Watermark successfully added!")
            #self.display_images()
        except Exception as e:
            print(f"There was error: {e}")
            self.status_label.config(text="Error!")
