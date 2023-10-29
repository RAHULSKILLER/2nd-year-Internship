from tkinter import *
import math


def click(value):
    #print(value)
    ex=entryField.get()
    answer=''

    try:
         
        if value=='C':
            ex=ex[0:len(ex)-1]
            entryField.delete(0,END)
            entryField.insert(0,ex)
            return        

        elif value=='CE':
                entryField.delete(0,END)
                return
        

        elif value=='√':
            answer=math.sqrt(eval(ex))
            

        elif value=='cosθ':
            answer=math.cos(math.radians(eval(ex)))

        
        elif value=='tanθ':
            answer=math.tan(math.radians(eval(ex)))


        elif value=='sinθ':
            answer=math.sin(math.radians(eval(ex)))


        elif value=='cos h':
            answer=math.cosh(eval(ex))


        elif value=='tan h':
            answer=math.tanh(eval(ex))


        elif value=='sin h':
            answer=math.sinh(eval(ex))


        elif value=='\u00D7':
            entryField.insert(END,'*')
            return


        elif value==chr(8731):
            answer=eval(ex)**(1/3)

            
        elif value=='x\u02b8':    #7**2
            entryField.insert(END,'**')
            return


        elif value=='x\u00B3':
            answer=eval(ex) ** 3


        elif value=='x\u00B2':
            answer=eval(ex) ** 2


        elif value=='ln':
            answer=math.log2(eval(ex))


        elif value=='deg':
            answer=math.degrees(eval(ex))

        
        elif value=='rad':
            answer=math.radians(eval(ex))


        elif value=='e':
            answer=math.e


        elif value=='log10()':
            answer=math.log10(eval(ex))


        elif value=='x!':
            answer=math.factorial(eval(ex))


        elif value==chr(247):    
            entryField.insert(END,'/')
            return


        elif value=='=':
            answer=eval(ex)


        else:
            if value=='π':
                entryField.insert(END,math.pi)
            
            elif value=='2π':
                entryField.insert(END,(2*math.pi))

            else:
                entryField.insert(END,value)

            return


        entryField.delete(0,END)
        entryField.insert(0,answer)



    except (SyntaxError,ZeroDivisionError):
       entryField.delete(0,END)
       entryField.insert(0,'Invalid!!') 



root=Tk()
root.title('Calculator')
root.config(bg='#0e387a')
root.geometry('680x486+100+100')

logo=PhotoImage(file='logo.png')
logoLabel=Label(root,image=logo,bg='#0e387a')
logoLabel.grid(row=0,column=0)


logo1=PhotoImage(file='logo1.png')
logo1Label=Label(root,image=logo1,bg='#0e387a')
logo1Label.grid(row=0,column=7)


entryField=Entry(root,font=('arial',20,'bold'),bg='#9fafca',fg='white',bd=10,relief=GROOVE,width=30)
entryField.grid(row=0,column=0,columnspan=8)

button_list=['<-','CE','√','+','π','cosθ','tanθ','sinθ',
             '1','2','3','-','2π','cos h','tan h','sin h',
             '4','5','6','\u00D7',chr(8731),'x\u02b8','x\u00B2','x\u00B3',
             '7','8','9',chr(247),'ln','deg','rad','e',
             '0','.','%','=','log10()','(',')','x!']

row_value=1
column_value=0

for i in button_list:
    button=Button(root,width=5,height=2,bd=2,relief=SUNKEN,text=i,bg='#0e387a',fg='white',font=('arial',18,'bold'),activebackground='#0e387a',command=lambda button=i: click(button))
    button.grid(row=row_value,column=column_value,pady=1)
    column_value+=1
    if column_value>7:
        row_value+=1
        column_value=0




root.mainloop()