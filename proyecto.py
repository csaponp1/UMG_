""" 
universidad mariano galvez 
facultad de ingeniería en sistema plan sabado 
catedrático: ing. Zacarias 
Nombre: Chrisitan Fernando Sapón Pérez 
Carne: 0910-21-16654 
""" 
import tkinter as tk 
from tkinter import filedialog,messagebox
import Levenshtein as lev 
 
def MetodoPrincipalAUTOMATAS(): 
    file_path = filedialog.askopenfilename(filetypes=[("Visual Basic Files", "*.vb")]) 
    if file_path: 
        with open(file_path, "rb") as file: 
            content = file.read() 
            # Identificar y eliminar el BOM (si existe) 
            if content.startswith(b'\xef\xbb\xbf'): 
                content = content[3:] 
            # Decodificar los bytes a texto usando UTF-8 
            #recuerde que un archivo binario es, ya que se abrio en modo rb 
            #por lo tanto debemos usar un estandar como el UTF-8 
 
            #declaracion de la variable 
            code = content.decode("utf-8") 
 
            #empezar a eliminar lo que no se usará 
            code_text.delete("1.0", tk.END) 
            code_text.insert(tk.END, code) 
 
def save_file(): 
    file_path = filedialog.asksaveasfilename(defaultextension=".vb", filetypes=[("Visual Basic Files", "*.vb")]) 
    if file_path: 
        with open(file_path, "w") as file: #SE ABRE EL ARCHIVO EN MODO ESCRITURA 
            file.write(code_text.get("1.0", tk.END)) #ESCRIBE UN CODIGO UTF EN NUESTRO ARCHIVO DE VISUAL BASIC Y LO ALMACENA 
 
def get_tokens(): 
    code = code_text.get("1.0", tk.END) 
    tokens = code.split() 
    results_text.delete("1.0", tk.END) 
    results_text.insert(tk.END, "Tokens:\n") 
    for token in tokens: 
        results_text.insert(tk.END, f"{token}\n") 
 
def classify_tokens(): 
    code = code_text.get("1.0", tk.END) 
    tokens = code.split() 
    keyword = "if" 
    results_text.delete("1.0", tk.END) 
    results_text.insert(tk.END, f"Occurrences of '{keyword}': {tokens.count(keyword)}\n") 
    similar_tokens = [token for token in tokens if lev.distance(keyword, token.lower()) <= 1] 
    results_text.insert(tk.END, f"Similar tokens to '{keyword}': {', '.join(similar_tokens)}\n") 

#FUNCIÓN PARA GUARDAR CAMBIOS SI SE DETECTA UN CAMBIO
def on_close():
    if code_text.edit_modified():
        response = messagebox.askyesnocancel("Save Changes?", "Do you want to save changes before closing?")
        if response is None:
            return
        if response:
            MetodoPrincipalAUTOMATAS()
    root.destroy()
 
# Crear la ventana principal 
root = tk.Tk() 
root.title("Analizador de texto Visual Basic") 
 
# Cuadro de texto para mostrar el código fuente 
code_text = tk.Text(root, wrap=tk.WORD, width=40) 
code_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True) 
 
# Cuadro de texto para mostrar los resultados 
results_text = tk.Text(root, wrap=tk.WORD, width=40) 
results_text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True) 
 
# Barra de menú 
menu_bar = tk.Menu(root) 
root.config(menu=menu_bar) 
 
# Menú "Archivo" 
file_menu = tk.Menu(menu_bar, tearoff=0) 
menu_bar.add_cascade(label="Archivo", menu=file_menu) 
file_menu.add_command(label="Abrir", command=MetodoPrincipalAUTOMATAS)# UN METODO LLAMADO ASI POR SU UNICA FUNCIONAALIDAD QUE EN ESTE CASO ES LEER 
file_menu.add_command(label="Guardar", command=save_file)# EL GUARDAR SOLO GUARDARÁ EL ARCHIVO EN LA MISMA UBICACIÓN DONDE SE ENCUENTRA. 
file_menu.add_command(label="Guardar como", command=save_file)#EL GUARDAR SOLO GUARDARÁ EL ARCHIVO EN LA MISMA UBICACIÓN DONDE SE ENCUENTRA. CON LA SALVERDAD QUE PREGUNTARÁ SI SE GUARDARÁ ALLI O EN OTRO DIRECTORIO 
file_menu.add_command(label="Cerrar", command=root.destroy)# EL COMANDO DESTROY ES UNA FUNCIÓN QUE CIERRA LA VENTANA 
 
# TOKENS" 
tokens_menu = tk.Menu(menu_bar, tearoff=0) 
menu_bar.add_cascade(label="Tokens", menu=tokens_menu) 
tokens_menu.add_command(label="Obtener", command=get_tokens) 
tokens_menu.add_command(label="Clasificar", command=classify_tokens) 

root.protocol("WM_DELETE_WINDOW", on_close)
# EL MAINLOOP ES UN BUCLE QUE DEBE DE REPETIRSE INDEFINIDAMENTE PARA QUE SE PUEDA MOSTRAR EL MODAL 
root.mainloop()