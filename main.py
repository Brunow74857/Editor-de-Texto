from tkinter import *
from tkinter import filedialog
import os

app : Tk = Tk()
app.geometry("645x390")
app.title("Editor de texto - Sem titulo")
app.resizable(False, False)
arquvioAberto : bool = False
caminho : str = ""

def mudar_titulo(nome : str) -> None:
    app.title(f"Editor de texto - {nome}")

def carregarArquivo() -> None:

    file = filedialog.askopenfilename(
        title="Selecione um arquivo:",
        filetypes=[("Arquvios de texto", "*.txt"),("Arquvios de html", "*.html"),("Arquvios python", "*.py"),("Arquvios C#", "*.cs"), ("Todos os arquivos", "*.*")]
    )
    
    if file == "":
        return None
    
    global caminho
    global arquvioAberto
    mudar_titulo(os.path.basename(file))
    caminho = file
    arquvioAberto = True

    with open(file, "r", encoding="UTF-8") as abrir:
        abrir = abrir.read()
        texto.delete("1.0", END)
        texto.insert("1.0", abrir)

def salvarcomo() -> None:
    
    file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        title="Salvar como...",
        filetypes=[("Arquvios de texto", "*.txt"),("Arquvios de html", "*.html"),("Arquvios python", "*.py"),("Arquvios C#", "*.cs"), ("Todos os arquivos", "*.*")]
    )

    if file == "":
        return None
    
    global arquvioAberto
    global caminho
    arquvioAberto = True
    caminho = file
    filetext = texto.get("1.0", END)
    mudar_titulo(os.path.basename(file))
    with open(file, "w", encoding="UTF-8") as w:
        w.write(filetext)

def salvar() -> None:
    
    if arquvioAberto == False or caminho == "":
        return None
    
    filetext = texto.get("1.0", END)
    with open(caminho, "w", encoding="UTF-8") as w:
        w.write(filetext)


def salvando() -> None:

    if arquvioAberto == True:
        salvar()
    else:
        salvarcomo()

menus = Menu(app)
arquivo = Menu(menus, tearoff=0)
arquivo.add_command(label="Abrir", command=carregarArquivo)
arquivo.add_command(label="Salvar", command=salvando)
arquivo.add_command(label="Salvar como", command=salvarcomo)
arquivo.add_separator()
arquivo.add_command(label="Fechar", command=app.quit)
menus.add_cascade(label="Arquivo", menu=arquivo)

texto : Text = Text(app)
texto.grid(column=0, row=0)

app.config(menu=menus)
app.mainloop()