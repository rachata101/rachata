from tkinter import *
import math
def clickButton(event):
    BMI = int(textbox1Weight.get())/math.pow(int(textboxHight.get())/100,2)
    if BMI >= 30:
        labelBMI.configure(text="อ้วนไป")
    elif BMI >=25:
        labelBMI.configure(text="อ้วน")
    elif BMI >= 23:
        labelBMI.configure(text="น้ำหนักเกิน")
    elif BMI >= 18.6:
        labelBMI.configure(text="น้ำหนักปกติ เหมาะสม")
    elif BMI <= 18.5:
        labelBMI.configure(text="ผอมเกินไป")

mainwidow = Tk()
labelHight = Label(mainwidow,text = "ส่วนสูง (CM):")
labelHight.grid(row=0,column=0)
textboxHight = Entry(mainwidow)
textboxHight.grid(row=0,column=1)
labelWeight = Label(mainwidow,text = "น้ำหนัก (KG):")
labelWeight.grid(row=1,column=0)
textbox1Weight = Entry(mainwidow)
textbox1Weight.grid(row=1,column=1)
Calbutton = Button(mainwidow,text = "calculator")
Calbutton.grid(row=2,column=0)
Calbutton.bind('<Button-1>',clickButton)
labelBMI = Label(mainwidow,text = "BMI")
labelBMI.grid(row=2,column=1)

mainwidow.mainloop()