from tkinter import Tk, StringVar, Label, Entry, Button


root = Tk()
root.title("First TKinter Window")
root.geometry("600x400")

name_var = StringVar()
pass_var = StringVar()

def Sumit():
    name = name_var.get()
    password = pass_var.get()

    print(f"Ten tai khoan la: {name}")
    print(f"Mat khau la: {password}")

    name_var.set("")
    pass_var.set("")

name_label = Label(root, text = "Nhap tai khoan: ", font = ('calibre', 10, 'bold'))
name_entry = Entry(root, textvariable=name_var, font=("calibre", 10, "normal"))
pass_label = Label(root, text="Nhap mat khau: ", font=("calibre", 10, "bold"))
pass_entry = Entry(root, textvariable=pass_var, font=("calibre", 10, "normal"), show = '*')

sub_btn = Button(root, text= "Submit")

name_label.grid(column= 0, row=0)
name_entry.grid(column= 1, row= 0)
pass_label.grid(column= 0, row=1)
pass_entry.grid(column=1, row= 1)
sub_btn.grid(column=1, row= 2)
root.mainloop()
