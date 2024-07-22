from random import *
from tkinter import *
import tkinter as ttk
import os

#root = ttk.Tk()
#root.geometry("400x350")
#root.title("Randomizer")

#frame = Frame(root)

def random_choice():
    while True:
        objects = []

        while True:
            a = input("Введите название раздела или нажмите на клавишу Enter чтобы закончить ввод: ")
            if a == "":
                break
            else:
                objects.append(a)

        if not objects:  # если список пустой
            print("1")
        else:
            result = choice(objects)  # или result = objects[randint(0, len(objects) - 1)]
            print(f"Выпадает: {result}")

            reset = input("Для продолжения нажмите Enter, для выхода нажмите 0 или q для полного выхода: ").lower()
            if reset == "0":
                break
            elif reset == "q":
                SystemExit()
            else:
                continue


random_choice()