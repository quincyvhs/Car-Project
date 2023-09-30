from tkinter import *
import tkinter as tk

window = Tk()
window.title("car maker")
window.geometry("1280x720")
window.resizable(False,False)
title=Label(window,text="Car Maker").pack(anchor="nw")

wheel_img=[]
wheel_img.append(PhotoImage(file="64xWheel 0.png"))
wheel_img.append(PhotoImage(file="64xWheel 1.png"))
def test(animal):
    print(animal)

wheelBtn0=Button(window,image=wheel_img[0],command=lambda:test("cat")).pack()
wheelBtn1=Button(window,image=wheel_img[1],command=lambda:test("dog")).pack()





def main():
    window.mainloop()
main()