# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 14:02:35 2021

@author: li ziwei
"""

import tkinter
import tkinter.filedialog
import tkinter.colorchooser
import tkinter.messagebox
import tkinter.scrolledtext


def Open():
    global filename
    #如果内容已改变，先保存
    if textChanged.get():
        yesno = tkinter.messagebox.askyesno(title='Save or not?',
                                            message='Do you want to save?')
        if yesno == tkinter.YES:
            Save()
            
    filename = tkinter.filedialog.askopenfilename(title='Open file',
                                           filetypes=[('Text files', '*.txt')])
    if filename:
        #清空内容
        txtContent.delete(0.0, tkinter.END)
        fp = open(filename, 'r')
        txtContent.insert(tkinter.INSERT, ''.join(fp.readlines()))
        fp.close()
        #标记为尚无修改
        textChanged.set(0)

def Save():
    global filename
    #如果是第一次保存新建文件，则打开“另存为”窗口
    if not filename:
        SaveAs()
    #如果内容发生改变，保存
    elif textChanged.get():
        content =  txtContent.get(0.0, tkinter.END)
        fp = open(filename, 'w')
        fp.write(content)
        fp.close()
        #标记为尚无修改
        textChanged.set(0)
        txtContent.edit_modified(False)
        
def SaveAs():
    global filename
    newfilename = tkinter.filedialog.asksaveasfilename(title='Save As',
                            initialdir=r'c:\\', initialfile='new.txt')
    if newfilename:
        content =  txtContent.get(0.0, tkinter.END)
        fp = open(newfilename, 'w')
        fp.write(content)
        fp.close()
        filename = newfilename

def Clear():
    global filename
    txtContent.delete(0.0, tkinter.END)
    filename = ''

def Copy():
    txtContent.clipboard_clear()
    txtContent.clipboard_append(txtContent.selection_get())

def Cut():
    Copy()
    txtContent.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
 
def Paste():
    try:
        txtContent.insert(tkinter.SEL_FIRST, txtContent.clipboard_get())
        txtContent.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
        return
    except Exception as e:
        pass
    txtContent.insert(tkinter.INSERT, txtContent.clipboard_get())    

def About():
    tkinter.messagebox.showinfo(title='About', message='My Notepad, version 0.0')


# 创建应用程序窗口
app = tkinter.Tk()
app.title('My Notepad')
app['width'] = 400
app['height'] = 300

# 标记文本是否修改，取0时为尚无修改
textChanged = tkinter.IntVar()
textChanged.set(0)

# 文件名
filename = ''

# 创建菜单
menu = tkinter.Menu(app)

# 创建File子菜单
submenu = tkinter.Menu(menu, tearoff=0)
submenu.add_command(label='Open', command=Open)
submenu.add_command(label='Save', command=Save)
submenu.add_command(label='SaveAs', command=SaveAs)
submenu.add_separator()
submenu.add_command(label='Clear', command=Clear)
menu.add_cascade(label='File', menu=submenu)

# 创建Edit子菜单
submenu = tkinter.Menu(menu, tearoff=0)
submenu.add_command(label='Copy', command=Copy)
submenu.add_command(label='Cut', command=Cut)
submenu.add_command(label='Paste', command=Paste)
menu.add_cascade(label='Edit', menu=submenu)

# 创建Help子菜单
submenu = tkinter.Menu(menu, tearoff=0)
submenu.add_command(label='About', command=About)
menu.add_cascade(label='Help', menu=submenu)

#将创建的菜单关联到应用程序窗口
app.config(menu=menu)

# 添加文本框内容发生改变时的处理函数
def on_text_change(event):
    textChanged.set(1)

# 创建文本编辑组件
txtContent = tkinter.scrolledtext.ScrolledText(app, wrap=tkinter.WORD)
txtContent.pack(fill=tkinter.BOTH, expand=tkinter.YES)

txtContent.bind("<<Modified>>", on_text_change)

# 主循环
app.mainloop()