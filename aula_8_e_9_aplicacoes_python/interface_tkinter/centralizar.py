# NOTA: Este código foi projetado especificamente para o ambiente Windows.
# O uso de 'iconbitmap' e do comando Tcl 'tk::PlaceWindow' para centralizar 
# a janela pode não funcionar corretamente em sistemas macOS ou Linux.

from pathlib import Path
from tkinter import Tk

janela = Tk()
janela.title("Nós ❤️ Python 🐍")
icone = Path(__file__).with_name("icon.ico")

if icone.exists():
    janela.iconbitmap(str(icone))

janela.geometry("600x250")
janela.eval('tk::PlaceWindow . center')
janela.mainloop()