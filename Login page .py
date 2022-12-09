from tkinter import *

root = Tk()
root.configure(bg="pink")
root.title("Login Page")

Label(root, text="Login page", font=("Georgia", 30, "bold"), bg="pink", fg="red").pack()

Label(root, text="User Name", bg="pink").pack()

input1 = Entry()
input1.pack()

Label(root, text="Phone-number", bg="pink").pack()

input2 = Entry()
input2.pack()

Label(root, text="Email", bg="pink").pack()

input3 = Entry()
input3.pack()

Label(root, text="Password", bg="pink").pack()

input4 = Entry()
input4.pack()

spy = StringVar()
Label(root, text="Select the gender", bg="pink").pack()
spy.set("MALE")
Radiobutton(root, text="Female", variable=spy, bg="pink", value="FEMALE").pack()
Radiobutton(root, text="male", variable=spy, bg="pink", value="MALE").pack()


def Window():
    top = Toplevel()
    top.configure(bg="Pink")
    top.title("Details Page")

    Label(top, text="Details About You", bg="pink", font=("Arieal", 50, "bold"), fg="red").pack()

    l = Label(top, text="username : " + input1.get(), bg="pink")
    l.pack()

    l = Label(top, text="Phone Number : " + input2.get(), bg="pink")
    l.pack()

    l = Label(top, text="Email : " + input3.get(), bg="pink")
    l.pack()

    l = Label(top, text="Password : " + input4.get(), bg="pink")
    l.pack()

    l = Label(top, text="Gender : " + spy.get(), bg="pink")
    l.pack()
    self.frame = Frame(top)


b = Button(root, text="login now", command=Window)
b.pack()

root.mainloop()
