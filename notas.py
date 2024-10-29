import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Notas Rápidas")
text_area = tk.Text(ventana, width=40, height=10)
text_area.pack()

def guardar_nota():
    nota = text_area.get("1.0", tk.END)
    with open("nota.txt", "w") as archivo:
        archivo.write(nota)
    messagebox.showinfo("Guardar Nota", "Nota guardada con éxito.")