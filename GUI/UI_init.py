from tkinter import *
from tkinter import ttk
from UI_Function import ui_func






root = Tk()
root.title('Medium Grabber')
root.geometry('{}x{}'.format(460, 350))

txt_pdf = 1

'''def send_string():
    text.delete(1.0,END)
    text.insert(END, "Searching for '" + search_entry.get() + "' ....")
    search_entry.delete(0, END)'''

def Get_Credentials():
    global user,psswd
    user = username_widget.get()
    psswd = password_widget.get()
    display.insert(END,'Now choose file format(by default PDF)\n')
    print(user)

def txt_pdf_func(n):
    global txt_pdf
    txt_pdf = n
    if txt_pdf==1:
        display.insert(END,'You chose PDF\n')
    else:
        display.insert(END,'You chose Text\n')
    print(txt_pdf)


def button_func(topic):
    print(topic)
    ui_func(topic,user,psswd,txt_pdf)
    display.insert(END,'Finished\n')


nb = ttk.Notebook(root)
nb.pack(expan=1, fill='both')

user = 'gsfg'
psswd = ''


tab1 = ttk.Frame(nb)
nb.add(tab1 , text='Medium Grabber')
tab1['padding'] = (5,10)


topFrame1 = ttk.Frame(tab1, padding=5)
topFrame1.pack(side=TOP, fill='x')

topFrame2 = ttk.Frame(tab1, padding=5)
topFrame2.pack(side=TOP, fill='x')

topFrame3 = ttk.Frame(tab1, padding=5)
topFrame3.pack(side=TOP, fill='x')

topFrame4 = ttk.Frame(tab1, padding=5)
topFrame4.pack(side=TOP, fill='x')

centre1 = ttk.Frame(tab1,padding=5)
centre1.pack(fill='x')

centre2 = ttk.Frame(tab1, padding=5)
centre2.pack(fill='x')

bottomFrame = ttk.Frame(tab1)
bottomFrame.pack(side=BOTTOM, fill='x')

userLabel = Label(topFrame1, text='Username :')
username_widget = Entry(topFrame1, width=15)
userLabel.pack(side=LEFT)
username_widget.pack(side=LEFT, fill='x', expand=2)

passLabel = Label(topFrame2, text=' Password :')
password_widget = Entry(topFrame2, show="*", width=100)
passLabel.pack(side=LEFT)
password_widget.pack(side=LEFT, fill='x', expand=2)

submit_button = Button(topFrame3, text='Submit', command = Get_Credentials)
submit_button.pack()

choose_label = Label(topFrame4, text='CHOOSE :  ')
choose_label.pack(side=LEFT)

text = Button(topFrame4, text='TEXT', width=20, command=lambda m=2: txt_pdf_func(m))
text.pack(side=LEFT)

pdf = Button(topFrame4, text='PDF',width=20, command=lambda m=1: txt_pdf_func(m))
pdf.pack(side=LEFT)



button1 = Button(centre1, text='TECHNOLOGY', width=14, command=lambda m=1: button_func(m))
button1.pack(side=LEFT)

button2 = Button(centre1, text='CULTURE', width=14, command=lambda m=2: button_func(m))
button2.pack(side=LEFT)

button3 = Button(centre1, text='ENTREPRENEURSHIP', width=15, command=lambda m=3: button_func(m))
button3.pack(side=LEFT)

button4 = Button(centre1, text='CREATIVITY', width=14, command=lambda m=4: button_func(m))
button4.pack(side=LEFT)

button5 = Button(centre2, text='SELF', width=14, command=lambda m=5: button_func(m))
button5.pack(side=LEFT)

button6 = Button(centre2, text='PRODUCTIVITY', width=14, command=lambda m=6: button_func(m))
button6.pack(side=LEFT)

button7 = Button(centre2, text='DESIGN', width=15, command=lambda m=7: button_func(m))
button7.pack(side=LEFT)

button8 = Button(centre2, text='POPULAR', width=14, command=lambda m=8: button_func(m))
button8.pack(side=LEFT)

display = Text(bottomFrame, width=50, height= 20)
display.pack()


'''tab2 = ttk.Frame(nb)
nb.add(tab2 , text='Tab2')
tab2['padding'] = (5,5)

text = Text(tab2, width=40, height=10)
search_label = Label(tab2, text='Search:')
search_entry = Entry(tab2, width=40)
search_button = Button(tab2, text='Search', command=send_string)


text.pack(side=BOTTOM)
search_entry.pack()
search_button.pack()'''



root.mainloop()




