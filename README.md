# 🟩 Wordle en Python

Un clon del popular juego **Wordle** desarrollado en Python con interfaz gráfica usando Tkinter.


---

## 📸 Vista previa

> El juego muestra un tablero de 6 filas × 5 columnas donde el jugador intenta adivinar la palabra secreta.


<img width="516" height="731" alt="image" src="https://github.com/user-attachments/assets/e71065b2-b5d8-4d30-b338-6fd3ae5ff52b" />
---

## 🎮 ¿Cómo jugar?

1. Escribe una palabra de 5 letras usando el teclado.
2. Presiona **Enter** para confirmar tu intento.
3. Usa **Backspace** para borrar letras.
4. Los colores te darán pistas:

| Color | Significado |
|-------|-------------|
| 🟩 Verde | La letra está en la posición correcta |
| 🟨 Amarillo | La letra existe pero está en otra posición |
| ⬛ Gris | La letra no está en la palabra |

Tienes **6 intentos** para adivinar la palabra. ¡Buena suerte!

---


### Requisitos

- Python 3.x
- Tkinter
- 
> **Nota:** Asegúrate de tener el archivo `data.txt` en el mismo directorio con las palabras válidas (una por línea, 5 letras).

---

## 📁 Estructura del proyecto

```
wordle-python/
├── wordle.py      
├── data.txt        
├── progreso.json   
└── README.md
```

---

## 📊 Estadísticas

El juego guarda automáticamente tu progreso en `progreso.json`:

- **Jugadas** — Total de partidas jugadas
- **Ganadas** — Total de partidas ganadas
- **Racha** — Racha actual de victorias consecutivas
- **Mejor Racha** — Tu mejor racha histórica

---

## 🛠️ Tecnologías utilizadas

- **Python 3** — Lenguaje principal
- **Tkinter** — Interfaz gráfica
- **JSON** — Persistencia de estadísticas

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.
