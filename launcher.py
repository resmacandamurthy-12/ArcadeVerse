import tkinter as tk
import subprocess

root = tk.Tk()
root.title("ArcadeVerse")
root.state("zoomed")
root.configure(bg="#111827")
root.resizable(False, False)

title = tk.Label(
    root,
    text="ARCADEVERSE",
    font=("Arial", 32, "bold"),
    fg="#a855f7",
    bg="#111827"
)
title.pack(pady=30)

name_label = tk.Label(
    root,
    text="Enter Your Name",
    font=("Arial", 16),
    fg="white",
    bg="#111827"
)
name_label.pack(pady=10)

name_entry = tk.Entry(
    root,
    font=("Arial", 16),
    width=25,
    justify="center"
)
name_entry.pack(pady=10)

greet = tk.Label(
    root,
    text="",
    font=("Arial", 18),
    fg="white",
    bg="#111827"
)
greet.pack(pady=15)


def play_snake():
    subprocess.run(["python", "main.py"], cwd="snake")


def play_pong():
    subprocess.run(["python", "main.py"], cwd="pong")


def play_crossing():
    subprocess.run(["python", "main.py"], cwd="crossing")


btn_style = {
    "font": ("Arial", 16),
    "width": 20,
    "height": 2,
    "bg": "#1f2937",
    "fg": "white"
}

snake_btn = tk.Button(
    root,
    text="🐍 Snake Game",
    command=play_snake,
    **btn_style
)

pong_btn = tk.Button(
    root,
    text="🏓 Pong Game",
    command=play_pong,
    **btn_style
)

cross_btn = tk.Button(
    root,
    text="🐢 Turtle Crossing",
    command=play_crossing,
    **btn_style
)

tech_label = tk.Label(
    root,
    text="Python • Tkinter • Turtle Graphics",
    font=("Arial", 11, "italic"),
    fg="#9ca3af",
    bg="#111827"
)
tech_label.pack(pady=15)

exit_btn = tk.Button(
    root,
    text="Exit",
    command=root.destroy,
    font=("Arial", 16),
    width=15,
    bg="#dc2626",
    fg="white"
)


def start_app():
    name = name_entry.get().strip()

    if not name:
        name = "Player"

    greet.config(text=f"Hello, {name}! 👋")

    with open("player.txt", "w") as file:
        file.write(name)

    start_btn.pack_forget()

    snake_btn.pack(pady=15)
    pong_btn.pack(pady=15)
    cross_btn.pack(pady=15)
    exit_btn.pack(pady=40)


start_btn = tk.Button(
    root,
    text="Start",
    command=start_app,
    font=("Arial", 14),
    bg="#a855f7",
    fg="white"
)
start_btn.pack(pady=10)

root.mainloop()
