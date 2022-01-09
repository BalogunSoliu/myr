from pymongo import MongoClient
from tkinter import *
from tkinter import messagebox

conn = MongoClient() #Creating a connection to Mongodb
Voting = conn["Voting"] #database
voters = Voting["voters"] #collection

def Vt():
   name = voter.get()
   choice = party.get()
   if name and choice:
       vote = {name:choice.upper()}  # collection data
       insert = voters.insert_one(vote)
       print("Vote casted successfully")
       messagebox.showinfo("Vote casted successfully")
       query = voters.find()
       for insert in query:
           print(insert)
   else:
       print("Error")#date:Date()
       messagebox.showinfo("Error")

root  = Tk()

root.title("Votesheet")
root.geometry("500x400")
root.configure(bg="cyan")
Label(root, text="Name:", font=(12), bg="cyan").place(x=50,y=50)
Label(root, text="Party:", font=(12), bg="cyan").place(x=50,y=90)
voter = Entry(root, width=40, borderwidth=2)
party = Entry(root, width=40, borderwidth=2)
voter.place(x=140,y=50)
party.place(x=140,y=90)

Button(text="Vote" ,font=(12), height=2, width=20, bg="blue", fg="white",command=Vt).place(x=140,y=140)

"""query = voters.find()
for insert in query:
    print(insert)"""

root.mainloop() #makes the field visible
"""def result():
    for i in range(0,len(vote)):
        if vote[party] == "PDP":
            print(len(vote))
print(result)"""





