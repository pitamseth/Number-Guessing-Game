from tkinter import * 
import random
import tkinter.messagebox as tmsg

#Root Configuration
root = Tk()
root.minsize(400,400)
root.maxsize(400,400)
root.title("Number Guessing Game")
root.configure(bg="aqua")

# Global Variables
starting_num = IntVar()
ending_num = IntVar()
guessing_num = IntVar()
chance = -2
num = 0

def exit_game():
    ans = tmsg.askyesno("Message","Do you want to quit the game?")
    if ans == True:
        exit(0)

def checking():
    global chance, num
    if chance < 0:
        tmsg.showinfo("Warning","Please Try Again")
    else:
        if chance > 0:
            try:
                if num == guessing_num.get():
                    l1.configure(text="Congratulations!!!\n You have guess \nthe correct number")
                    chance = -1
                    back.configure(text="Try Again")
                elif num > guessing_num.get() and chance != 1:
                    l1.configure(text=f"OOPs!!!\n You have guess \nless than the number\n {chance-1} chance left")
                elif num < guessing_num.get() and chance != 1:
                    l1.configure(text=f"OOPs!!!\n You have guess \nmore than the number\n {chance-1} chance left")
                elif chance == 1:
                    l1.configure(text=f"You Lost\n The number was {num}\n Better luck next time")
                    back.configure(text="Try Again")
                    chance = -1
            except:
                tmsg.showerror("Error","Please enter a valid number")
                chance = chance + 1
    chance = chance - 1
    

def game():
    list = root.pack_slaves()
    for l in list:
        l.destroy()
    guessing_num.set(0)
    root.configure(bg="purple")
    game_frame = Frame(root, bg="purple")
    game_frame.pack(padx=10, pady=10)
    Label(game_frame, text="Enter the number you have guess", bg="purple", fg="gray", font=("tacoma", 10, "bold")).pack(side=TOP)
    st_point = Entry(game_frame, textvariable=guessing_num, font=("tacoma", 15, "bold"), width=10)
    st_point.pack(anchor='center', padx=20, pady=30)
    Button(game_frame, text="Check", bg="pink", font=("tacoma", 10, "bold"), command=checking).pack()
    global l1
    l1 = Label(game_frame, text="Best OF Luck", bg="purple", fg="green", font=("tacoma", 10, "bold"))
    l1.pack(side=TOP, pady=20)
    global back
    back = Button(game_frame, text="Back", bg="brown", font=("tacoma", 10, "bold"), command=start)
    back.pack()
    exit_frame = Frame(root, bg="aqua")
    exit_frame.pack(side=BOTTOM, anchor='e', padx=10, pady=10)
    Button(exit_frame, text="Exit Game", bg="red", font=("tacoma", 10, "bold"), command=exit_game).pack()
    try:
        global num
        num = random.randint(starting_num.get(),ending_num.get())
    except:
        tmsg.showerror("Error","Please enter a valid range")
        start()
    global chance
    chance = 3

def start():
    list = root.pack_slaves()
    for l in list:
        l.destroy()
    root.configure(bg="blue")
    starting_num.set(0)
    ending_num.set(0)
    mid_frame = Frame(root, bg="blue")
    mid_frame.pack(padx=10, pady=10)
    Label(mid_frame, text="Enter the range", bg="blue", fg="yellow", font=("tacoma", 20, "bold")).pack(side=TOP)
    inp_frame = Frame(mid_frame, bg="blue")
    inp_frame.pack(padx=10, pady=30, side=TOP)
    st_point = Entry(inp_frame, textvariable=starting_num, font=("tacoma", 15, "bold"), width=10)
    st_point.pack(side=LEFT, padx=10, pady=5)
    en_point = Entry(inp_frame, textvariable=ending_num, font=("tacoma", 15, "bold"), width=10)
    en_point.pack(side=LEFT, padx=10, pady=5)
    Button(mid_frame, text="Start", bg="green", font=("tacoma", 10, "bold"), command=game).pack(padx=50, pady=30, side=TOP)
    Label(mid_frame, text="Note: You have 3 chance only!!!", bg="blue", fg="gray", font=("tacoma", 10, "bold")).pack(side=TOP, pady=15)
    exit_frame = Frame(root, bg="aqua")
    exit_frame.pack(side=BOTTOM, anchor='e', padx=10, pady=10)
    Button(exit_frame, text="Exit Game", bg="red", font=("tacoma", 10, "bold"), command=exit_game).pack()
    

starting_frame = Frame(root, bg="aqua")
starting_frame.pack(padx=50, pady=60)
Label(starting_frame, text="Guess the number\n if you can", bg="aqua", font=("tacoma", 20, "bold")).pack()
Button(starting_frame, text="Let's Start", bg="yellow", font=("tacoma", 10, "bold"), command=start).pack(side=TOP, padx=10, pady=50)
exit_frame = Frame(root, bg="aqua")
exit_frame.pack(side=BOTTOM, anchor='e', padx=10, pady=10)
Button(exit_frame, text="Exit Game", bg="red", font=("tacoma", 10, "bold"), command=exit_game).pack()

root.mainloop()