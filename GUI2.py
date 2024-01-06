from tkinter import *

def getvals():
    print("submitted")
    print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emercontactvalue.get(), payvalue.get(), foodservicevalue.get() }")
    with open("records.txt","a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emercontactvalue.get(), payvalue.get(), foodservicevalue.get() }")

root=Tk()
root.geometry("444x333")
Label(root, text="welcome", font="comicsans 13 bold", pady=15).grid(row=0,column=3)
name=Label(root, text="Name")
phone=Label(root, text="phone")
gender=Label(root, text="gender")
emercontact=Label(root, text="emergency contact")
pay=Label(root, text="payment mode")

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emercontact.grid(row=4,column=2)
pay.grid(row=5,column=2)

namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emercontactvalue=StringVar()
payvalue=StringVar()
foodservicevalue=IntVar()

nameentry=Entry(root, textvariable=namevalue)
phoneentry=Entry(root, textvariable=phonevalue)
genderentry=Entry(root, textvariable=gendervalue)
emercontactentry=Entry(root, textvariable=emercontactvalue)
payentry=Entry(root, textvariable=payvalue)

foodservice=Checkbutton(text="want prebook your meals", variable=foodservicevalue )
foodservice.grid(row=6, column=3)

nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emercontactentry.grid(row=4,column=3)
payentry.grid(row=5,column=3)

Button(text="submit",command=getvals).grid(row=7,column=3)



root.mainloop()