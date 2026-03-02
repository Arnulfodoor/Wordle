from tkinter import Tk, Frame, Label, Button, messagebox
import random
import string
import json
import os

class Wordle:
    def __init__(self, master):
        self.master = master
        self.master.title("Wordle ")
        self.master.geometry("520x700")
        self.master.config(bg="black")
        self.master.resizable(False, False)

        self.filas = 6
        self.columnas = 5
        self.fila_actual = 0
        self.columna_actual = 0

        self.verde = '#19C065'
        self.amarillo = '#E3B30E'
        self.gris = '#3A3A3C'
        self.vacio = '#121213'

        self.cargar_palabras()
        self.palabra_secreta = random.choice(self.lista)

        self.cargar_progreso()
        self.crear_ui()

        self.master.bind("<Key>", self.tecla_presionada)


    def crear_ui(self):
        self.frame_tablero = Frame(self.master, bg="black")
        self.frame_tablero.pack(pady=20)

        self.tablero = []
        for f in range(self.filas):
            fila = []
            for c in range(self.columnas):
                label = Label(
                    self.frame_tablero,
                    text="",
                    width=4,
                    height=2,
                    font=("Arial", 24, "bold"),
                    bg=self.vacio,
                    fg="white",
                    relief="solid",
                    bd=2
                )
                label.grid(row=f, column=c, padx=5, pady=5)
                fila.append(label)
            self.tablero.append(fila)

        self.frame_stats = Frame(self.master, bg="black")
        self.frame_stats.pack(pady=10)

        self.stats_label = Label(
            self.frame_stats,
            text="",
            fg="white",
            bg="black",
            font=("Arial", 12)
        )
        self.stats_label.pack()

        self.actualizar_stats()

        Button(
            self.master,
            text="Reiniciar",
            command=self.reiniciar,
            bg="darkred",
            fg="white"
        ).pack(pady=10)

    def cargar_palabras(self):
        with open("data.txt", "r", encoding="utf-8") as f:
            self.lista = [pal.strip().upper() for pal in f.readlines()]

    def cargar_progreso(self):
        if os.path.exists("progreso.json"):
            with open("progreso.json", "r") as f:
                self.progreso = json.load(f)
        else:
            self.progreso = {
                "jugadas": 0,
                "ganadas": 0,
                "racha": 0,
                "mejor_racha": 0
            }

    def guardar_progreso(self):
        with open("progreso.json", "w") as f:
            json.dump(self.progreso, f)

    def actualizar_stats(self):
        self.stats_label.config(
            text=f"Jugadas: {self.progreso['jugadas']} | "
                 f"Ganadas: {self.progreso['ganadas']} | "
                 f"Racha: {self.progreso['racha']} | "
                 f"Mejor Racha: {self.progreso['mejor_racha']}"
        )

    def tecla_presionada(self, event):
        if self.fila_actual >= self.filas:
            return

        if event.keysym == "BackSpace":
            if self.columna_actual > 0:
                self.columna_actual -= 1
                self.tablero[self.fila_actual][self.columna_actual]["text"] = ""

        elif event.keysym == "Return":
            if self.columna_actual == 5:
                self.verificar_palabra()

        elif event.char.upper() in string.ascii_uppercase and len(event.char) == 1:
            if self.columna_actual < 5:
                self.tablero[self.fila_actual][self.columna_actual]["text"] = event.char.upper()
                self.columna_actual += 1

    def obtener_palabra_actual(self):
        return "".join(
            self.tablero[self.fila_actual][c]["text"]
            for c in range(self.columnas)
        )

    def verificar_palabra(self):
        palabra = self.obtener_palabra_actual()

        palabra_temp = list(self.palabra_secreta)
        colores = [self.gris] * 5

        for i in range(5):
            if palabra[i] == palabra_temp[i]:
                colores[i] = self.verde
                palabra_temp[i] = None

        for i in range(5):
            if colores[i] == self.gris and palabra[i] in palabra_temp:
                colores[i] = self.amarillo
                palabra_temp[palabra_temp.index(palabra[i])] = None

        for i in range(5):
            self.tablero[self.fila_actual][i]["bg"] = colores[i]

        if palabra == self.palabra_secreta:
            self.progreso["jugadas"] += 1
            self.progreso["ganadas"] += 1
            self.progreso["racha"] += 1

            if self.progreso["racha"] > self.progreso["mejor_racha"]:
                self.progreso["mejor_racha"] = self.progreso["racha"]

            self.guardar_progreso()
            self.actualizar_stats()

            messagebox.showinfo("GANASTE 🎉", "¡Felicidades!")
            self.reiniciar()
            return

        self.fila_actual += 1
        self.columna_actual = 0

        if self.fila_actual == self.filas:
            self.progreso["jugadas"] += 1
            self.progreso["racha"] = 0
            self.guardar_progreso()
            self.actualizar_stats()

            messagebox.showinfo("PERDISTE ❌", f"La palabra era: {self.palabra_secreta}")
            self.reiniciar()

    def reiniciar(self):
        for fila in self.tablero:
            for label in fila:
                label.config(text="", bg=self.vacio)

        self.fila_actual = 0
        self.columna_actual = 0
        self.palabra_secreta = random.choice(self.lista)


if __name__ == "__main__":
    root = Tk()
    juego = Wordle(root)
    root.mainloop()