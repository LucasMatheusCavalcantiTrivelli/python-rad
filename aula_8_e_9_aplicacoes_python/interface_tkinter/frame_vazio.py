# Demonstra como criar e empacotar Frames independentes para
# organizar os elementos da janela.

import tkinter as tk

janela = tk.Tk()

frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master = frame_a, text = "Frame A")
label_a.pack()

label_b = tk.Label(master = frame_b, text = "Frame B")
label_b.pack()

frame_a.pack()  # Invertendo a ordem dessas .pack() irá inverter os frames na janela.
frame_b.pack()

janela.mainloop()