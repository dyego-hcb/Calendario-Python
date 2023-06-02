from tkinter import *
import calendar

def show_calendar():
    year = int(entry_year.get())
    calendar_text.config(state=NORMAL)
    calendar_text.delete('1.0', END)
    for month in range(1, 13):
        cal = calendar.month(year, month)
        calendar_text.insert(END, cal)
    calendar_text.config(state=DISABLED)

root = Tk()
root.title("Exibir Calendário")
root.geometry("600x500")

label_year = Label(root, text="Digite um ano:", font=("Arial", 14))
label_year.pack(pady=10)

entry_year = Entry(root, font=("Arial", 14))
entry_year.pack()

button_show = Button(root, text="Exibir Calendário", font=("Arial", 14), command=show_calendar)
button_show.pack(pady=10)

calendar_text = Text(root, font=("Courier", 12))
calendar_text.pack()

root.mainloop()
