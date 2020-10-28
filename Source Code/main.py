import tkinter as tk
import Scrap

# Exit function

def close_root():
    root.destroy() 

#Reset Function    

def reset():
    URL_entry.delete(0, 'end')
    text_widget.delete(1.0, tk.END)       

root = tk.Tk()

root.title('Web Crawler'.center(200))
root.resizable(0,0)

root.configure(
            border = 1,
            )

root.iconbitmap('spider.ico')            

f_head = tk.Frame(
                master = root,
                borderwidth = 2,
                pady = 2,
                )

f_head.grid(
        row = 0,
        column = 0,
        )

title = tk.Label(
                f_head,
                text = "Welcome to our Scrapping tool",
                bg = 'grey',
                fg = 'black',
                height = '5',
                width = 60,
                font = "Helvitica 15 bold",
                )

title.grid(
           row = 0,
           column = 0
           )

title.pack()

f_body = tk.Frame(
                root,
                borderwidth = 3,
                pady = 6,
                )

f_body.grid(row = 1, column = 0)

f_body_1 = tk.Frame(
            f_body,
            borderwidth = 2,
            padx = 3,
            pady = 3,
            relief = 'raised',
            )

URL = tk.Label(
        f_body_1,
        text = "Enter the URL:    ",
        )

URL.pack(
    side = "left",
    pady = 2,
    )

get_URL = tk.StringVar()

URL_entry = tk.Entry(
                f_body_1,
                textvariable = URL,
                width = 44,
                border = 4,
                )

URL_entry.insert(
            0,
            "Ex: https://facebook.com",
            )
URL_entry.pack(
                side = "right",
                padx = 5,
                pady = 6,
                )


f_body_1.pack(
            fill = 'x',
            pady = 2,
            )

f_tail = tk.Frame(
                root,
                borderwidth = 2,
                pady = 2,
                )

button_1 = tk.Button(
                f_tail,
                text = "Start scraping",
                command = Scrap.scrapped,
                bg = 'dark green',
                fg = 'white',
                relief = 'raised',
                width = 13,
                font = "Helvitica 9 bold",
                )

button_1.grid(
            column = 0,
            row = 0,
            sticky = 'w',
            padx = 100,
            pady = 2,
            )

button_2 = tk.Button(
                f_tail,
                text = "Exit",
                command = close_root,
                bg = 'dark red',
                fg = 'white',
                relief = 'raised',
                width = 13,
                font = "Helvitica 9 bold",
                )

button_2.grid(
            column = 1,
            row = 0,
            sticky = 'e',
            padx = 100,
            pady = 2,
            )

button_reset = tk.Button(
                f_tail,
                text = "Reset All",
                command = reset,
                bg = 'dark red',
                fg = 'white',
                relief = 'raised',
                width = 13,
                font = "Helvitica 9 bold",
                )

button_reset.place(
            relx = 0.5,
            rely = 0.5,
            anchor = 'center',
)

f_tail.grid(
            row = 2,
            column = 0,
            )

f_text = tk.Frame(
                root,
                borderwidth = 4,
                pady = 32,
                )

f_text.grid(
            row = 3,
            column = 0,
)   

my_scroll = tk.Scrollbar(
                f_text,
                orient = tk.VERTICAL
                )

text_widget = tk.Text(
                f_text,
                height = 20,
                width = 80,
                # state = 'disabled',
                yscrollcommand = my_scroll.set,
                bg = "light yellow",
                bd = 3,
)

my_scroll.config(
            command = text_widget.yview
)

my_scroll.pack(side = tk.RIGHT, fill = tk.Y)

text_widget.pack()

f_copyright = tk.Frame(
                    root,
                    borderwidth = 4,
                    pady = 22,
                    )

f_copyright.grid(
                row = 4,
                column = 0,
                )

copyright_text = tk.Label(
                    f_copyright,
                    text = "Copyright:- 2020 Made with ❤",
                    font = "helvitica 8 bold",                   
                    )
                    
copyright_text.pack()

root.mainloop()