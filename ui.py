import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

THEME_COLOR = "#375362"


class Interface:
    def __init__(self):
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

        self.window.mainloop()

    def display_image(self, filename):
        image = Image.open(filename)
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.photo = photo
        self.status_label.config(text=f"Image loaded: {filename}")

    def upload_action(self):
        f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]
        filename = filedialog.askopenfilename(filetypes=f_types)

        if filename:
            self.display_image(filename)
