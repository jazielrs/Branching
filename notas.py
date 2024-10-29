import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Notas Rápidas")
text_area = tk.Text(ventana, width=40, height=10)
text_area.pack()