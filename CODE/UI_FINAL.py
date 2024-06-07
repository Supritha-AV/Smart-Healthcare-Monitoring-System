import pickle
model=pickle.load(open("LL.pkl","rb"))

import requests
import telepot
import os
from tkinter.filedialog import askopenfilename
import sys
import shutil
from pres import display
bot=telepot.Bot("6170275891:AAEqqSi8XszNVqlnm-lgUECGzgpzCA97nMY")
chatid="1405147528"


data=requests.get("https://api.thingspeak.com/channels/2055536/feeds.json?api_key=BRXLVE3VLJ1JQ403&results=2")
hb_t=float(data.json()['feeds'][-1]['field1'])
temp_t=float(data.json()['feeds'][-1]['field2'])
oxy_t=float(data.json()['feeds'][-1]['field3'])



from tkinter import *
import tkinter as tk



root = tk.Tk()
root.title('Virtual Doctor')
root.geometry('1920x1080')
root.configure(background="#ffffff")
from PIL import Image,ImageTk

img=Image.open("aa.jpg")
img=img.resize((1920,1080))
bg=ImageTk.PhotoImage(img)
lbl=Label(root,image=bg)
lbl.place(x=0,y=0)

label = Label( root, text="patient survilence" ,font=('arial',22,'bold'),background="#4cd2e0")

label.place(x=500,y=20)


label_1 = tk.Label(root, text ='NAME',font=("Helvetica", 20),background="#4cd2e0")
label_1.place(x=100,y=100)


    
Entry_0= Entry(root,font=("Helvetica", 20),background="#4cd2e0",justify=CENTER)
Entry_0.place(x=500,y=100)

label_1 = tk.Label(root, text ='AGE',font=("Helvetica", 20),background="#4cd2e0")
label_1.place(x=100,y=170)


    
Entry_01= Entry(root,font=("Helvetica", 20),background="#4cd2e0",justify=CENTER)
Entry_01.place(x=500,y=170)

label8=tk.Label(root,text="Gender",bg="#4cd2e0",fg="black",font=("times",20))
label8.place(x=100,y=240)

#############################################################################333
def sel():
    global opt
    opt=""
    if var.get()==1:
        opt='MALE'
    elif var.get()==2:
        opt='FEMALE'
    else:
        opt='Others'
    gen_val=int(var.get())
    selection = "Selected : \n " + str(opt)
    label.config(text = selection)
##root = Tk()
var = IntVar()
R1 = Radiobutton(root, text="M", variable=var, value=1,command=sel,bg="#4cd2e0",fg="black",font=("times",20))
R1.place(x=500,y=240)
R2 = Radiobutton(root, text="F", variable=var, value=2,command=sel,bg="#4cd2e0",fg="black",font=("times",20))
R2.place(x=600,y=240)
R3 = Radiobutton(root, text="O", variable=var, value=3,command=sel,bg="#4cd2e0",fg="black",font=("times",20))
R3.place(x=700,y=240)
label = Label(root,bg="#4cd2e0",fg="black",font=("times",20))
label.place(x=800,y=240)


label_1 = tk.Label(root, text ='Blood pressure',font=("Helvetica", 20),background="#4cd2e0")
label_1.place(x=100,y=310)


    
Entry_1= Entry(root,font=("Helvetica", 20),background="#4cd2e0",justify=CENTER)
Entry_1.place(x=500,y=310)

label_2 = tk.Label(root, text ='SpO2',font=("Helvetica", 20),background="#4cd2e0")
label_2.place(x=100,y=380)


    
Entry_2 = Entry(root,font=("Helvetica", 20),background="#4cd2e0",justify=CENTER)
Entry_2.place(x=500,y=380)
Entry_2.insert(0,oxy_t)
    
    
label_3 = tk.Label(root, text ='Heart beat',font=("Helvetica", 20),background="#4cd2e0")
label_3.place(x=100,y=450)


    
Entry_3 = Entry(root,font=("Helvetica", 20),background="#4cd2e0",justify=CENTER)
Entry_3.place(x=500,y=450)
Entry_3.insert(0,hb_t)

label_4 = tk.Label(root, text ='ECG rate',font=("Helvetica", 20),background="#4cd2e0")
label_4.place(x=100,y=520)


    
Entry_4= Entry(root,font=("Helvetica", 20),background="#4cd2e0",justify=CENTER)
Entry_4.place(x=500,y=520)



label_5 = tk.Label(root, text ='Temperature',font=("Helvetica", 20),background="#4cd2e0")
label_5.place(x=100,y=590)


    
Entry_5 = Entry(root,font=("Helvetica", 20),background="#4cd2e0",justify=CENTER)
Entry_5.place(x=500,y=590)
Entry_5.insert(0,temp_t)


label8=tk.Label(root,text="Cough",bg="#4cd2e0",fg="black",font=("times",20))
label8.place(x=100,y=650)

#############################################################################333
def selc():
    global optc
    optc=[]
    if varc.get()==1:
        optc='YES'
    else:
        optc='NO'
    gen_val=int(varc.get())
    selection = "Selected :  " + str(optc)
    labelc.config(text = selection)
##root = Tk()
varc = IntVar()
R1 = Radiobutton(root, text="YES", variable=varc, value=1,command=selc,bg="#4cd2e0",fg="black",font=("times",20))
R1.place(x=500,y=650)
R2 = Radiobutton(root, text="NO", variable=varc, value=2,command=selc,bg="#4cd2e0",fg="black",font=("times",20))
R2.place(x=600,y=650)

labelc = Label(root,bg="#4cd2e0",fg="black",font=("times",20))
labelc.place(x=700,y=650)

def del_displayed():
    label_rem.configure(text="")
    label_rem.configure(font=("Arial",16),height=0,width=0)
    output.configure(text="")
    if out[0] != 1:
        b3.destroy()
    Entry_01.delete(0,END)  #  Entry_0,Entry_1,Entry_2,Entry_3,Entry_3,Entry_5
    Entry_0.delete(0,END)
    Entry_1.delete(0,END)
    Entry_2.delete(0,END)
    Entry_3.delete(0,END)
    Entry_4.delete(0,END)
    Entry_5.delete(0,END)
    

def reset():
    b_reset = Button(root, text = 'RECHECK',font=("Helvetica", 20),background="#4cd2e0",command = del_displayed)
    b_reset.place(x=950,y=500)
    
    
    

    


def fever():
    med="Diagnosis Drugs for Fever  \n  Paracetamol \n acetaminophen \n Tylenol  \n aspirin \n  Acephen  \n Ecpirin \n"
    if varc.get()==1:
        cough=" Dry cough :  Benadryl DR Syrup \n Wet cough : cofsils wet cough syrup "
        label_rem.configure(text=str(med)+" for Cough \n " +str(cough))
        label_rem.configure(font=("Arial",16),height=10,width=35)
        bot.sendMessage(chatid,str("Patient  :  "+str(name)+ "\n Age  :  "+str(agee)+ "\n Gender  :  "+str(opt)+ "\n Status  :  "+str(res)+" \n  Medicine Provided  :  "+str(med)+" \n For Cough \n "+str(cough)))
    else:
        label_rem.configure(text=med)
        label_rem.configure(font=("Arial",16),height=13,width=35)
        bot.sendMessage(chatid,str("Patient  :  "+str(name)+ "\n Age  :  "+str(agee)+ "\n Gender  :  "+str(opt)+ "\n Status  :  "+str(res)+" \n  Medicine Provided  :  "+str(med)))
    reset()
  
def chest_pain():
    med="Diagnosis Drugs for chest_pain \n Amlodipine \n Nadroparin \n Isosorbide \n Nifedipine \n Atenolol \n Diltiazem \n"
    if varc.get()==1:
        cough=" Dry cough :  Benadryl DR Syrup \n Wet cough : cofsils wet cough syrup "
        label_rem.configure(text=str(med)+" for Cough \n " +str(cough))
        label_rem.configure(font=("Arial",16),height=10,width=35)
        bot.sendMessage(chatid,str("Patient  :  "+str(name)+ "\n Age  :  "+str(agee)+ "\n Gender  :  "+str(opt)+ "\n Status  :  "+str(res)+" \n  Medicine Provided  :  "+str(med)+" \n For Cough \n "+str(cough)))
    else:
        label_rem.configure(text=med)
        label_rem.configure(font=("Arial",16),height=13,width=35)
        bot.sendMessage(chatid,str("Patient  :  "+str(name)+ "\n Age  :  "+str(agee)+ "\n Gender  :  "+str(opt)+ "\n Status  :  "+str(res)+" \n  Medicine Provided  :  "+str(med)))
    reset()
def Critical():
    med="You are critical \n concern the doctor nearby"
    if varc.get()==1:
        cough=" Dry cough :  Benadryl DR Syrup \n Wet cough : cofsils wet cough syrup "
        label_rem.configure(text=str(med)+" for Cough \n " +str(cough))
        label_rem.configure(font=("Arial",16),height=10,width=35)
        bot.sendMessage(chatid,str("Patient  :  "+str(name)+ "\n Age  :  "+str(agee)+ "\n Gender  :  "+str(opt)+ "\n Status  :  "+str(res)+" \n  Medicine Provided  :  "+str(med)+" \n For Cough \n "+str(cough)+" \n LOCATION   : https://maps.app.goo.gl/ftDTGkrZBpgXdNGs9"))
    else:
        label_rem.configure(text=med)
        label_rem.configure(font=("Arial",16),height=13,width=35)
        bot.sendMessage(chatid,str("Patient  :  "+str(name)+ "\n Age  :  "+str(agee)+ "\n Gender  :  "+str(opt)+ "\n Status  :  "+str(res)+" \n  Medicine Provided  :  "+str(med)+" \n LOCATION   : https://maps.app.goo.gl/ftDTGkrZBpgXdNGs9"))
    reset()
   
    
    

def predict():
    global name,agee        # Entry_0,Entry_1,Entry_2,Entry_3,Entry_3,Entry_5
    agee=int(Entry_01.get())
    name=str(Entry_0.get())
    bp =  float(Entry_1.get())
    oxy = float(Entry_2.get())
    hb = float(Entry_3.get())
    ecg = float(Entry_4.get())
    temp =  float(Entry_5.get())
    global res,b3,out
    out = model.predict([[float(bp),
    float(oxy),
    float(hb),
    float(ecg),
    float(temp)]])     ##float(area)

    


    print(out[0])
    
    res=""
    # if bp<30 or bp >100 or oxy <40 or oxy > 140 or hb< 40 or hb > 150 or ecg < 100 or ecg > 1200 or temp > 110:
    #     res=" Critical or Check the \n Hardware Misplaced"
    if out[0] == 1 :
        res="NORMAL"       
    elif out[0] == 2: 
        res="FEVER"
        
        b3=tk.Button(root,text="fever",bg="#4cd2e0",fg="black",font=("Arial",16),width=10,command=fever)
        b3.place(x=1100,y=70)
        
    elif out[0] == 3:
        res="CHEST PAIN"
        b3=tk.Button(root,text="chest_pain",bg="#4cd2e0",fg="black",font=("Arial",16),width=10,command=chest_pain)
        b3.place(x=1100,y=70)
        
    elif out[0] == 4:
        res="Critical"
        b3=tk.Button(root,text="viral_fever",bg="#4cd2e0",fg="black",font=("Arial",16),width=10,command=Critical)
        b3.place(x=1100,y=70)
    
    print(res)
    output.configure(text=res)
        
def openphoto():
    dirPath = "testpicture"
    fileList = os.listdir(dirPath)
    for fileName in fileList:
        os.remove(dirPath + "/" + fileName)
    # C:/Users/sagpa/Downloads/images is the location of the image which you want to test..... you can change it according to the image location you have  
    fileName = askopenfilename(initialdir='test', title='Select image for analysis ',
                           filetypes=[('image files', '.jpg')])
    dst = "testpicture"
    print(fileName)
    print (os.path.split(fileName)[-1])
    shutil.copy(fileName, dst)
    display(fileName)
##    img.grid(column=0, row=1, padx=10, pady = 10) 



b1 = Button(root, text = 'predict',font=("Helvetica", 20),background="#4cd2e0",command = predict)
b1.place(x=950,y=580)
b1 = Button(root, text = 'UPLOAD \n OLD PRESCRIPTION',font=("Helvetica", 20),background="#4cd2e0",command = openphoto)
b1.place(x=950,y=700)
    
global label_rem,output
output = Label(root,text=" ",font=("Helvetica", 20),background="#4cd2e0")
output.place(x=1100,y=650)


label_rem= Label(root,fg="black",font=("Arial",16),height=0,width=0)
label_rem.place(x=950,y=150)                 


root.mainloop()



