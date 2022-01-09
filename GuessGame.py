from tkinter import *
from tkinter import messagebox
GuessList = ['1','2','5','6','9','0']
def login():
   name = entry1.get()
   guess = entry2.get()
   if  guess in GuessList:
       print("You are correct")
       messagebox.showinfo(f"Thumbs Up {name}! Correct...!")
   else:
       print("Guess Incorrect!")#date:Date()
       messagebox.showinfo(f"{name} you submitted a wrong number, Try again...!")
root  = Tk()

root.title("My Guess")
root.geometry("500x400")
root.configure(bg="cyan")
Label(root, text="Name:", font=(12), bg="cyan").place(x=50,y=50)
Label(root, text="Guess a number:", font=(12), bg="cyan").place(x=50,y=90)

entry1 = Entry(root, width=40, borderwidth=2)
entry2 = Entry(root, width=40, borderwidth=2)
entry1.place(x=140,y=50)
entry2.place(x=180,y=90)

Button(text="Submit Guess",font=(12), height=2, width=20, bg="blue", fg="white",command=login).place(x=140,y=140)

root.mainloop()