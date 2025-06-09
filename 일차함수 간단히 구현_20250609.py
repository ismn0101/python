import tkinter

# 창 설정
window=tkinter.Tk()
window.title("일차함수 그래프")
window.geometry("280x300+100+100")
window.resizable(False, False)

# label 설정
label1 = tkinter.Label(text="y = ax + b", font=("Arial", 15))
label1.place(x=90, y=20)

label_a = tkinter.Label(text = "a : ", font=("Arial", 14))
label_a.place(x=10, y=55)

label_b = tkinter.Label(text = "b : ", font=("Arial", 14))
label_b.place(x=10, y=95)

# entry 설정
entry_a = tkinter.Entry()
entry_a.place(x=40, y=63)

entry_b = tkinter.Entry()
entry_b.place(x=40, y=103)

# listbox 설정
listbox1 = tkinter.Listbox(width=39, height=9)
listbox1.place(x=1, y=140)

# 함수 설정
def solution():
    a = float(entry_a.get())
    b = float(entry_b.get())
    listbox1.delete(0)


    for i in range(10):
        y2 = a * i + b
        listbox1.insert(0, f'({float(i)}, {y2})')
    listbox1.insert(0, '---------(x, y)---------')
    x = (-1*b) / a # x절편
    y = b # y절편
    listbox1.insert(0, f'x절편 : {x}')
    listbox1.insert(0, f'y절편 : {y}')
    listbox1.insert(0,f'y = {a}x + {b}')

# button 설정
button1 = tkinter.Button(text="입력", background="green", font=("Arial",14), command=solution)
button1.place(x=205, y=70)

window.mainloop()