import tkinter as tk


def create_main_window():
    """
    THis function creates a new window using the tkinter module, adds a text label and a button which calls the
    show_picture function
    """
    master_window = tk.Tk()
    master_window.geometry("200x100")
    label = tk.Label(master_window, text="What's my favorite NBA team?")
    label.pack()
    btn = tk.Button(master_window, text="Click to find out")
    btn.bind("<Button>",
             lambda e: show_picture(master_window))
    btn.pack()
    master_window.mainloop()


def show_picture(window):
    """
    The function displays a picture of my favourite NBA team's logo
    :param window: A Tkinter window
    :type window: Tkinter window
    The function shows an image on the given window
    """
    img = tk.PhotoImage(file=r'../images/celtics_logo.png')
    label = tk.Label(window, image=img)
    label.pack()
    window.geometry("300x300")
    window.mainloop()


def main():
    create_main_window()


if __name__ == "__main__":
    create_main_window()
