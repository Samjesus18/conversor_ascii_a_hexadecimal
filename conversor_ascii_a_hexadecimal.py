import tkinter as tk
import time
import psutil 

cadena = str("")
lista = []
lista2 = []
detener=False

def convertir():
    global lista
    global lista2
    global hex_string
    
    
    cadena = texto1.get("1.0", tk.END)
    hex_string = cadena.encode("utf-8").hex()
    #print(hex_string)

def seleccionador():
    lista = [hex_string[i:i+4] + " = " for i in range(0, len(hex_string), 4)] 
    
    for elemento in lista:
        #print(elemento)
        ventana.update()
        time.sleep(0.05)
        if detener:
            break

    lista2 = "\n".join(lista)
    texto2.insert(tk.END, str(hex_string + "\n" + "\n" + "Mismo codigo pero organizado" + "\n") + "\n")
    texto2.insert(tk.END, str(lista2) + "\n")
    texto2.insert(tk.END, str("Proceso culminado"+"\n"))

def detener_proceso():
    global detener
    detener = True
    
def activador():
    convertir()
    seleccionador()

def mostrar_menu(event):
    menu_contextual.post(event.x_root, event.y_root)

def borrar_contenido():
    texto1.delete('1.0', tk.END)
    texto2.delete('1.0', tk.END)

def mostrar_contenido_ram():
    ram = psutil.virtual_memory()
    contenido_ram = f"Memoria Total: {ram.total}\nMemoria Disponible: {ram.available}\nPorcentaje de Uso: {ram.percent}%"
    texto2.insert(tk.END, contenido_ram)

#---------------------------------------Interfaz grafica---------------------------------

ventana = tk.Tk()
ventana.title("Conversor de ASCII a hexadecimal")
ventana.geometry("615x450")
ventana.resizable(0,0)
ventana.configure(background='#25232d')
ventana.iconbitmap("C:\\Users\\Sam\\Documents\\Programacion_prueba\\Codigo terminado\\calculadora.ico")

label1 = tk.Label(ventana, text="Ingrese el codigo a convertir",font=20)
label1.place(x=200, y=8)

texto1 = tk.Text(ventana)
texto1.configure(width=60, height=10)
texto1.place(x=10, y=40)

scrollbar = tk.Scrollbar(ventana, command=texto1.yview)
scrollbar.place(x=490, y=40, width=20, height=164)

texto1.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=texto1.yview)

def cortar():
    texto1.event_generate("<<Cut>>")

def copiar():
    texto1.event_generate("<<Copy>>")

def pegar():
    texto1.event_generate("<<Paste>>")

def seleccionar_todo():
    texto1.tag_add("sel", "1.0", "end")


menu_contextual = tk.Menu(ventana, tearoff=0)
menu_contextual.add_command(label="Cortar", command=cortar)
menu_contextual.add_command(label="Copiar", command=copiar)
menu_contextual.add_command(label="Pegar", command=pegar)
menu_contextual.add_command(label="Seleccionar todo", command=seleccionar_todo)

texto1.bind("<Button-3>", lambda event: menu_contextual.post(event.x_root, event.y_root))

label2 = tk.Label(ventana, text="Codigo convertido y organizado", font=20)
label2.place(x=200, y=210)

texto2 = tk.Text(ventana)
texto2.configure(width=60, height=10)
texto2.place(x=10, y=240)

scrollbar = tk.Scrollbar(ventana,command=texto2.yview, width=14)
scrollbar.place(x=490, y=240, width=20, height=164)

texto2.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=texto2.yview)

def cortar1():
    texto2.event_generate("<<Cut>>")

def copiar1():
    texto2.event_generate("<<Copy>>")

def pegar1():
    texto2.event_generate("<<Paste>>")

def seleccionar_todo1():
    texto2.tag_add("sel", "1.0", "end")

menu_contextual2 = tk.Menu(ventana, tearoff=0)
menu_contextual2.add_command(label="Cortar", command=cortar1)
menu_contextual2.add_command(label="Copiar", command=copiar1)
menu_contextual2.add_command(label="Pegar", command=pegar1)
menu_contextual2.add_command(label="Seleccionar todo", command=seleccionar_todo1)

texto2.bind("<Button-3>", lambda event: menu_contextual2.post(event.x_root, event.y_root))

boton1 = tk.Button(ventana, text="Convertir", font=20, command=activador, width=8, height=2)
boton1.place(x=520, y=40)

boton2 = tk.Button(ventana, text="Borrar", font=20, command=borrar_contenido, width=8, height=2)
boton2.place(x=520, y=100)

boton3 = tk.Button(ventana, text="Romper", font=20, command=detener_proceso, width=8, height=2)
boton3.place(x=520, y=160)

boton4 = tk.Button(ventana, text="Ver Ram",font=20, command=mostrar_contenido_ram, width=8, height=2)
boton4.place(x=520, y=220)

ventana.mainloop()



