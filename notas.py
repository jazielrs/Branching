import tkinter as tk
from tkinter import messagebox

def guardar_nota():
    nota = text_area.get("1.0", tk.END)
    with open("nota.txt", "w") as archivo:
        archivo.write(nota)
    messagebox.showinfo("Guardar Nota", "Nota guardada con éxito.")
def cargar_nota():
    try:
        with open("nota.txt", "r") as archivo:
            nota = archivo.read()
            text_area.delete("1.0", tk.END)  # Limpiar el área de texto
            text_area.insert(tk.END, nota)  # Cargar la nota
    except FileNotFoundError:
        messagebox.showwarning("Cargar Nota", "No se encontró el archivo de nota.")
        
ventana = tk.Tk()
ventana.title("Notas Rápidas")
text_area = tk.Text(ventana, width=40, height=10)
text_area.pack()
# Botones
tk.Button(ventana, text="Guardar Nota", command=guardar_nota).pack()
tk.Button(ventana, text="Cargar Nota", command=cargar_nota).pack()

ventana.mainloop()

