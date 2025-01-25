# Custom Web Browser #
from tkinter import *
import webbrowser


def open_website():
    url = website_entry.get()
    if not url.startswith(("http://", "https://")):
        url = "http://" + url
    webbrowser.open(url, new=2)


def go_back():
    webbrowser.get().back()


def go_forward():
    webbrowser.get().forward()


def refresh_page():
    webbrowser.get().refresh()


window = Tk()
window.title("Simple Web Browser")
window.configure(bg="#f0f0f0")

main_frame = Frame(window, bg="#f0f0f0")
main_frame.pack(padx=20, pady=20)

website_label = Label(main_frame, text="Enter Website URL:", bg="#f0f0f0", fg="#333")
website_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
website_entry = Entry(main_frame, width=50, bg="lightgray", borderwidth=2)
website_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

open_button = Button(main_frame, text="Open", command=open_website, bg="#4CAF50", fg="white", padx=10, pady=5)
open_button.grid(row=1, column=0, padx=5, pady=5)
back_button = Button(main_frame, text="Back", command=go_back, bg="#2196F3", fg="white", padx=10, pady=5)
back_button.grid(row=1, column=1, padx=5, pady=5)
forward_button = Button(main_frame, text="Forward", command=go_forward, bg="#FFC107", fg="white", padx=10, pady=5)
forward_button.grid(row=1, column=2, padx=5, pady=5)
refresh_button = Button(main_frame, text="Refresh", command=refresh_page, bg="#9C27B0", fg="white", padx=10, pady=5)
refresh_button.grid(row=1, column=3, padx=5, pady=5)

window.mainloop()
