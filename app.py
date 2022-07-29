from time import strftime
from tkinter import Label, Tk

# Configuring window 
window = Tk()
window.title("")
window.geometry("200x80")
#Sets the background colour for the clock
window.configure(bg="black")  
# Sets the window size that is static
window.resizable(False, False)  

clock_label = Label(
    window, bg="black", fg="yellow", font=("Arial", 30, "bold"), relief="flat"
)
clock_label.place(x=30, y=30)


def update_label():
    """
    Function to update the time

    every 50 milliseconds
    """
    current_time = strftime("%H: %M: %S\n %d-%m-%Y ")
    clock_label.configure(text=current_time)
    clock_label.after(50, update_label)
    clock_label.pack(anchor="center")


update_label()
window.mainloop()

