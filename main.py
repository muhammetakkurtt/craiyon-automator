import sys
import asyncio
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from craiyon_generator import main as craiyon_main
from threading import Thread
from tkinter import font as tkfont

class CraiyonGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Craiyon Image Generator')
        self.geometry('600x500')
        self.configure(bg='#2C3E50')  

        self.title_font = tkfont.Font(family="Helvetica", size=16, weight="bold")
        self.normal_font = tkfont.Font(family="Helvetica", size=12)
        
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        
        self.style.configure('TButton', font=self.normal_font, padding=10, background='#3498DB', foreground='white')
        self.style.map('TButton', background=[('active', '#2980B9')])

        self.style.configure('TLabel', font=self.normal_font, background='#2C3E50', foreground='white')
        
        self.initUI()

    def initUI(self):
        main_frame = tk.Frame(self, bg='#2C3E50')
        main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        title_label = ttk.Label(main_frame, text='Craiyon Image Generator', font=self.title_font, style='TLabel')
        title_label.pack(pady=(0, 20))

        self.prompt_input = ScrolledText(main_frame, wrap=tk.WORD, width=50, height=10, font=self.normal_font, bg='#34495E', fg='white', insertbackground='white')
        self.prompt_input.pack(pady=20, fill=tk.BOTH, expand=True)
        self.prompt_input.insert(tk.INSERT, "Enter one prompt per line...")

        button_frame = tk.Frame(main_frame, bg='#2C3E50')
        button_frame.pack(pady=20)

        self.generate_button = ttk.Button(button_frame, text='Generate Images', command=self.generate_images, style='TButton')
        self.generate_button.pack(side=tk.LEFT, padx=(0, 10))

        self.status_label = ttk.Label(main_frame, text='Ready', style='TLabel')
        self.status_label.pack(pady=10)

    def generate_images(self):
        prompts = self.prompt_input.get("1.0", tk.END).strip().split('\n')
        prompts = [prompt.strip() for prompt in prompts if prompt.strip()]

        if not prompts:
            messagebox.showwarning("Warning", "Please enter at least one prompt.")
            return

        self.status_label.config(text='Generating images...')
        self.generate_button.config(state=tk.DISABLED)

        thread = Thread(target=self.run_worker, args=(prompts,))
        thread.start()

    def run_worker(self, prompts):
        asyncio.run(craiyon_main(prompts))
        self.on_finished()

    def on_finished(self):
        self.status_label.config(text='Images generated and saved.')
        self.generate_button.config(state=tk.NORMAL)

if __name__ == '__main__':
    app = CraiyonGUI()
    app.mainloop()