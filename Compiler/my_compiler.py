from tkinter import *

compiler= Tk()
compiler.title("My Fantastic Editor")

def saveas():
    path = 
def run():
    code=editor.get('1.0',END)
    #exec(code)
menu_bar = Menu(compiler)


file_menu = Menu(menu_bar,tearoff=0)
file_menu.add_command(label='Open',command=run)
file_menu.add_command(label='Save',command=run)
file_menu.add_command(label='Save as',command=saveas)
file_menu.add_command(label='Exit',command=exit)
menu_bar.add_cascade(label='File',menu=file_menu)

run_bar = Menu(menu_bar,tearoff=0)
run_bar.add_command(label='Run',command=run)
menu_bar.add_cascade(label='Run & Debug',menu=run_bar)
compiler.config(menu=menu_bar)


editor= Text()
editor.pack()

compiler.mainloop()