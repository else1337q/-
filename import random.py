import random
import time
import tkinter as tk

def play_game():
    revolver = "заряжен", "не заряжен"
    revolver_chosen = random.choice(revolver)

    if revolver_chosen == "заряжен":
        label.config(text="Револьвер заряжен. Вы проиграли.")
        time.sleep(2)
        return

    label.config(text="Револьвер не заряжен. Вы выиграли!")
    time.sleep(2)

def start_game():
    global running
    running = True
    play_game()

def quit_game():
    global running
    running = False
    window.destroy()

def show_error_window():
    error_window = tk.Tk()
    error_window.title("Ошибка")
    error_label = tk.Label(error_window, text="Я понимаю, я не самый обаятельный и приятный парень на свете, но чтоб никто... sudo rm -rf / load...")
    error_label.pack(pady=10)
    error_window.mainloop()

window = tk.Tk()
window.title("Русская рулетка")
window.geometry("400x300")

label = tk.Label(window, text="Добро пожаловать в игру 'Русская рулетка'!")
label.pack(pady=10)

start_button = tk.Button(window, text="сыгрануть", command=start_game)
start_button.pack(pady=10)

quit_button = tk.Button(window, text="Выйти с позором", command=show_error_window)
quit_button.pack(pady=10)

window.mainloop()