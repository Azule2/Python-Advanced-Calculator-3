from tkinter import *

root = Tk()
root.title('Advanced Calculator')
#root.geometry('500x350')


e = Entry(root, width=35, borderwidth=5)
e.grid(row=0,column=0, columnspan=3, padx=15, pady=15)

def button_click(number):
	#e.delete(0, END)
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))
def button_clear():
	e.delete(0, END)

def button_plus():
	first_num = e.get()
	global f_num
	global math
	math = 'addition'
	f_num = int(first_num)
	e.delete(0, END)

def button_equal():
	second_num = e.get()
	e.delete(0,END)
	
	if math == 'addition':
		e.insert(0, f_num + int(second_num))

	elif math == 'multiplication':
		e.insert(0, f_num * int(second_num))

	elif math == 'subtraction':
		e.insert(0, f_num - int(second_num))
	else:
		e.insert(0, f_num / int(second_num))

def button_subtract():

	first_num = e.get()
	global f_num
	global math
	math = 'subtraction'
	f_num = int(first_num)
	e.delete(0, END)

def button_multiply():

	first_num = e.get()
	global f_num
	global math
	math = 'multiplication'
	f_num = int(first_num)
	e.delete(0, END)

def button_divid():

	first_num = e.get()
	global f_num
	global math
	math = 'division'
	f_num = int(first_num)
	e.delete(0, END)

# Define Buttons
btn1 = Button(root, text='1', padx=40,pady=20, command=lambda: button_click(1))
btn2 = Button(root, text='2', padx=40,pady=20, command=lambda: button_click(2))
btn3 = Button(root, text='3', padx=40,pady=20, command=lambda: button_click(3))
btn4 = Button(root, text='4', padx=40,pady=20, command=lambda: button_click(4))
btn5 = Button(root, text='5', padx=40,pady=20, command=lambda: button_click(5))
btn6 = Button(root, text='6', padx=40,pady=20, command=lambda: button_click(6))
btn7 = Button(root, text='7', padx=40,pady=20, command=lambda: button_click(7))
btn8 = Button(root, text='8', padx=40,pady=20, command=lambda: button_click(8))
btn9 = Button(root, text='9', padx=40,pady=20, command=lambda: button_click(9))
btn0 = Button(root, text='0', padx=40,pady=20, command=lambda: button_click(0))

btn_plus = Button(root, text='+', padx=39,pady=20, command= button_plus)
btn_equal = Button(root, text='=', padx=73,pady=20, width=10, command=button_equal)
btn_Clear = Button(root, text='Clear ', padx=73,pady=20, width=10,command=lambda: button_clear())
btn_subtract = Button(root, text='-', padx=41, pady=20, command=button_subtract)
btn_multiply = Button(root,text='*', padx=40, pady=20, command=button_multiply)
btn_divid = Button(root,text='/', padx=40, pady=20, command=button_divid)


btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)

btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)

btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)
btn9.grid(row=1,column=2)

btn0.grid(row=4,column=0)

btn_Clear.grid(row=4,column=1, columnspan=2)
btn_plus.grid(row=5,column=0)
btn_equal.grid(row=6,column=1, columnspan=2)
btn_subtract.grid(row=5,column=1)
btn_multiply.grid(row=5,column=2)
btn_divid.grid(row=6,column=0)
root.mainloop()
