import time
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from pynput.keyboard import Key, Controller
import webbrowser as web

t=Tk()
t.geometry("600x400")
t.title("刷屏鸡~~~")

sitting = True

def 刷屏():
    try:
        entry_get = int(entry.get())
        entry_get_1 = entry_1.get()
        entry_get_2 = float(entry_2.get())
        def ok():
            question = askretrycancel('确定？', '%s' % '最后一遍，是否刷屏（可能造成卡顿）')
            if question:
                if sitting:
                    j = 5
                    showinfo('准备', '%s' % '开始计时5秒钟')
                    for i in range(5):  # 倒计时
                        print('倒计时:' + str(j))
                        j = j - 1
                        time.sleep(1)

                    for i in range(entry_get):  # 次数
                        jp.type(entry_1.get() + '（刷屏机刷的）')
                        jp.press(Key.enter)
                        jp.press(Key.enter)
                        time.sleep(entry_get_2)
                else:
                    j = 5
                    showinfo('准备', '%s' % '开始计时5秒钟')
                    for i in range(5):  # 倒计时
                        print('倒计时:' + str(j))
                        j = j - 1
                        time.sleep(1)

                    for i in range(entry_get):  # 次数
                        jp.type(entry_get_1)
                        jp.press(Key.enter)
                        jp.press(Key.enter)
                        time.sleep(entry_get_2)
        if entry_get >= 50:
            question = askquestion('确定？', '%s' % '确定要刷大于50遍吗？')
            if question == 'yes':
                if len(entry_get_1) >= 15:
                    question = askquestion('确定？', '%s' % '确定要字数刷大于15个字吗？')
                    if question == 'yes':
                        ok()
                        if entry_get_2 <= 1:
                            question = askquestion('确定？', '%s' % '确定要刷间隔小于1秒吗？')
                            if question == 'yes':
                                ok()
                        else:
                            ok()
                elif entry_get_2 <= 1:
                    question = askquestion('确定？', '%s' % '确定要刷间隔小于1秒吗？')
                    if question == 'yes':
                        ok()
                else:
                    ok()

        elif len(entry_get_1) >= 15:
            question = askquestion('确定？', '%s' % '确定要字数刷大于15个字吗？')
            if question == 'yes':
                ok()
                if entry_get_2 <= 1:
                    question = askquestion('确定？', '%s' % '确定要刷间隔小于1秒吗？')
                    if question == 'yes':
                        ok()
                else:
                    ok()
        elif entry_get_2 <= 1:
            question = askquestion('确定？', '%s' % '确定要刷间隔小于1秒吗？')
            if question == 'yes':
                ok()
        else:
            ok()
    except Exception as x:
        showerror('错误', '%s' % x)

def 设置():
    global sitting
    sitting = askquestion('设置', '%s' % '是否在刷屏字符后加上刷屏机声明？')
    if sitting == 'yes':
        sitting = True
    else:
        sitting = False

def github():
    web.open('')

jp = Controller()

label = Label(t ,text="制作：小井井")
label.pack()

label_1 = Label(t ,text="次数")
label_1.place(relx=0.3,rely=0.3)

label = Label(t ,text="内容")
label.place(relx=0.3,rely=0.4)

label_2 = Label(t ,text="间隔")
label_2.place(relx=0.3,rely=0.5)

entry = Entry(t)
entry.place(relx=0.5, rely=0.3)

entry_1 = Entry(t)
entry_1.place(relx=0.5, rely=0.4)

entry_2 = Entry(t)
entry_2.place(relx=0.5, rely=0.5)

button = Button(t ,text="开始刷屏",command=刷屏)
button.place(relx=0.5 ,rely=0.6)

button_1 = Button(t ,text="设置",command=设置)
button_1.place(relx=0.5 ,rely=0.7)

t.mainloop()