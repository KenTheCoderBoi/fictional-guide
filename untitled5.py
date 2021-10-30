from tkinter import *
import random#imports random package

root = Tk()#creates window
root.title("cavity giver")#sets name of window
root.geometry("400x400")#sets size of window]
def generate():
    randomnumber = random.randint(1,8)
    itemnum["text"] = "take item "+str(randomnumber)+" out of the bag"

items = "Bottle,","Chocolate,","Lolypop,","M16,","Deagle,","Homework,","Hydrogen bomb"
listed_items = Label(root,text=items)
button = Button(root,text="choose",command=generate)
itemnum = Label(root,text="")

listed_items.place(relx = 0.5,rely = 0.4,anchor=CENTER)
button.place(relx = 0.5,rely = 0.5,anchor=CENTER)
itemnum.place(relx = 0.5,rely = 0.6,anchor=CENTER)
root.mainloop()