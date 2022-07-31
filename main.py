import tkinter as tk
from tkinter import ttk


class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry("300x300")
        self.title("Top level Window")
        ttk.Button(self,
                   text="Close",
                   command=self.destroy).pack(expand=True)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.title("Main Window")

        ttk.Button(self,
                   text="Open Window",
                   command=self.open_window).pack(expand=True)

    def open_window(self):
        window = Window(self)
        window.grab_set()


if __name__ == "__main__":
    app = App()
    app.mainloop()

