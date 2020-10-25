import tkinter as tk

# A button that will close the window. 
# Will implement this function later in a button

def close_root():
    root.destroy()

def scrap():
    print("good")    

root = tk.Tk()

# root.geometry('700x600')
root.title('Web Crawler'.center(200))
root.resizable(0,0)
# root.configure(bg = 'skyblue')

f_head = tk.Frame(master = root, borderwidth = 2, pady = 2)
f_head.grid(row = 0, column = 0)

title = tk.Label(f_head, text = "Welcome to our Scrapping tool", bg = 'grey', fg = 'black', height = '5', width = 60, font = "Helvitica 15 bold")
title.grid(row = 0, column = 0)
title.pack()

f_body = tk.Frame(root, borderwidth = 3, pady = 6)
f_body.grid(row = 1, column = 0)

f_body_1 = tk.Frame(f_body,borderwidth = 6, padx = 3, pady = 3, relief = 'sunken')

URL = tk.Label(f_body_1, text = "Enter the URL:    ")
URL.pack(side = "left", pady = 2)

URL_entry = tk.Entry(f_body_1, textvariable = URL, width = 44)
URL_entry.insert(0, "Ex: https://facebook.com")
URL_entry.pack(side = "right", padx = 5, pady = 6)

# URL_entry.bind("<KeyRelease>", small_caps)

get_URL = tk.StringVar()

f_body_1.pack(fill = 'x', pady = 2)

f_tail = tk.Frame(root, borderwidth = 2, pady = 2)

button_1 = tk.Button(f_tail, text = "Start scraping", command = scrap, bg = 'dark green', fg = 'white', relief = 'raised', width = 13, font = "Helvitica 9 bold")
button_1.grid(column = 0, row = 0, sticky = 'w', padx = 100, pady = 2)

button_2 = tk.Button(f_tail, text = "Exit", command = close_root, bg = 'dark red', fg = 'white', relief = 'raised', width = 13, font = "Helvitica 9 bold")
button_2.grid(column = 1, row = 0, sticky = 'e', padx = 100, pady = 2)

f_tail.grid(row = 2, column = 0)

f_copyright = tk.Frame(root, borderwidth = 8, pady = 32)
f_copyright.grid(row = 3, column = 0)

copyright_text = tk.Label(f_copyright, text = "Copyright:- 2020 Made with ❤")
copyright_text.pack()

root.mainloop()