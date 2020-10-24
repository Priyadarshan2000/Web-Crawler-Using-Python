# from tkinter import *
import tkinter as tk

root = tk.Tk()

root.geometry('700x600')
root.title('Web Crawler'.center(200))
root.configure(bg = 'skyblue')

tk.Label(root, text = "Enter the URL        ").grid(row = 0)

e1 = tk.Entry(root)

e1.grid(row = 0, column = 1)

button = tk.Button(root, text = "Proceed", bd = 4, pady = 15, padx = 10, font = "cursive").grid(row = 15)

root.mainloop()