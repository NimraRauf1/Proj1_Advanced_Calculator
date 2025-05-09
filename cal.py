#Tkinter is the standard GUI library in Python
import tkinter as tk
from tkinter import font #Importing Font class from tk library
import math

# Function to evaluate mathematical expressions
def click(event):
    btn_text = event.widget.cget("text")
#when user press =
    if btn_text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
#when user press AC
    elif btn_text == "AC":
        entry.delete(0, tk.END)
#when user press ⌫
    elif btn_text == "⌫":
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current[:-1])
#if user press sin, cos, tan, log, sqrt (mathematical func)
    elif btn_text in ["sin", "cos", "tan", "log", "sqrt"]:
        try:
            value = float(entry.get())
            if btn_text == "sin":
                result = math.sin(math.radians(value))
            elif btn_text == "cos":
                result = math.cos(math.radians(value))
            elif btn_text == "tan":
                result = math.tan(math.radians(value))
            elif btn_text == "log":
                result = math.log10(value)
            elif btn_text == "sqrt":
                result = math.sqrt(value)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    else:
        entry.insert(tk.END, btn_text)

# GUI Setup
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")
root.configure(bg="#ff69b4")  # Dark pink background
root.resizable(False, False)

#Uses the tkinter.font class to create two font styles: heading_font (bold and large) and button_font (slightly smaller)
try:
    heading_font = font.Font(family="Arial", size=20, weight="bold")
    button_font = font.Font(family="Arial", size=16)
except:
    heading_font = ("Arial", 20, "bold")
    button_font = ("Arial", 16)

# Heading label (font style, size, border thickness, bg color, text color)
title_label = tk.Label(root, text="Scientific Calculator", font=heading_font, bg="#ff69b4", fg="white")
title_label.pack(pady=(10, 5))

# Entry field at the top (font style, size, border thickness, bg color, text color)
entry = tk.Entry(root, font=("Arial", 20), bd=5, relief=tk.FLAT, justify=tk.RIGHT, bg="white", fg="#333")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

# Button layout inspired by iPhone Cal
btn_texts = [
    ["AC", "+/-", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", "⌫"],
    ["sin", "cos", "tan", "log"],
    ["(", ")", "sqrt", "^"]
]

# Create button using for-loop
for row in btn_texts:
    frame = tk.Frame(root, bg="#ff69b4")
    frame.pack(expand=True, fill='both')
    for item in row:
        btn = tk.Button(
            frame,
            text=item,
            font=button_font,
            bd=0,
            relief=tk.FLAT,
            bg="#ffd1dc",               # Baby pink
            fg="#333333",
            activebackground="#ffb6c1", # Light pink on click
            activeforeground="#000",
            highlightthickness=0,
            highlightbackground="#ffd1dc"
        )
        btn.pack(side=tk.LEFT, expand=True, fill='both', padx=4, pady=4)
        btn.bind("<Button-1>", click)

root.mainloop()
