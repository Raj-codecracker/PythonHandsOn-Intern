import tkinter as tk
from tkinter import font

ALLOWED_CHARS = set('0123456789+-*/.() ')

class SimpleCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Simple Calculator')
        self.configure(bg='#1e1e1f')
        self.resizable(False, False)

        # fonts
        self.display_font = font.Font(size=30, weight='bold')
        self.btn_font = font.Font(size=16)
        self.small_font = font.Font(size=10)

        # state
        self.current = ''
        self.history = []

        # layout
        self._create_widgets()
        self._bind_keys()

    def _create_widgets(self):
        # top frame (display)
        top = tk.Frame(self, bg='#1e1e1f', padx=10, pady=10)
        top.grid(row=0, column=0, sticky='nsew')

        self.display_var = tk.StringVar(value='0')
        display = tk.Label(top, textvariable=self.display_var, anchor='e',
                           bg='#2b2b2d', fg='white', padx=12, pady=14,
                           font=self.display_font, relief='flat', width=18)
        display.pack(fill='both', expand=True)

        # main frame for buttons and history
        main = tk.Frame(self, bg='#1e1e1f')
        main.grid(row=1, column=0, sticky='nsew')

        # buttons frame
        btn_frame = tk.Frame(main, bg='#1e1e1f')
        btn_frame.g