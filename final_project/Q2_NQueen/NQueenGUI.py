from tkinter import *
from NQueen import NQueen
nqueen_instance = NQueen()

class NQueenGUI:
    def __init__(self) -> None:
        # 创建Tkinter GUI窗口
        win = Tk()
        win.title("N 皇后问题")
        Label(win, text="N皇后问题求解程序").grid(columnspan=3, sticky=W+E+N+S)
        Label(win, text="请输入皇后的个数N: ").grid(sticky=E)

        # 皇后数量输入框和“求解”按钮
        self.entry1 = Entry(win)
        self.entry1.grid(row=1, column=1, columnspan=2)
        solveButton = Button(win, text='求解', command=self.solutionNumShow)
        solveButton.grid(row=2,column=0,rowspan=1, columnspan=3, sticky=W+E+N+S)

        # 显示N皇后问题解个数的标签
        self.solutionNumLabel = Label(win)
        self.solutionNumLabel.grid(row=3,column=0,rowspan=1, columnspan=3, sticky=W+E+N+S)

        # 用于显示解的图像标签设置
        photo = PhotoImage(file='./Queen150px.png')
        self.label = Label(image=photo)
        self.label.image = photo
        self.label.grid(row=4, column=0, columnspan=3, rowspan=2, sticky=W+E+N+S, padx=5, pady=5)
        self.countLabel = Label(win)
        self.countLabel.grid(row=6, column=0, columnspan=3)

        # 用户交互部分：提示用户输入想要查看第几种解法和读取用户输入的文本框
        Label(win, text="请输入您想查看第几个解: ").grid(row=7,column=0)
        self.entry2 = Entry(win)
        self.entry2.grid(row=7, column=1, columnspan=2)

        # 三个按钮：功能分别是上一个解、查看输入框中的解和下一个解
        buttonPrev = Button(win, text=' <- ', command=self.drawSolutionPrev)
        buttonPrev.grid(row=8, column=0, sticky=W)
        buttonView = Button(win, text='查看', command=self.drawSolution)
        buttonView.grid(row=8, column=1, sticky=W)
        buttonNext = Button(win, text=' -> ', command=self.drawSolutionNext)
        buttonNext.grid(row=8, column=2, sticky=E)

        mainloop()

    # 求解N皇后问题的函数
    def solutionNumShow(self):
        msg = ''
        # 异常处理：检查用户输入是否合法
        try:
            N = int(self.entry1.get())
            if ((N == 0) or (N < 0)):
                msg = "输入不能为0或负数。"
            else:
                # 调用NQueen类中的函数解N皇后问题
                nqueen_instance.solver(N)
                msg = str(N)+ " 皇后问题有 " + str(nqueen_instance.ansNum) + " 个解。"
        except Exception:
            msg = "皇后的数量不合法，请检查输入。"   
        # 更新窗口中Label显示的信息 
        self.solutionNumLabel.config(text=msg, bg="white", fg="blue")   
    
    # 显示用户指定的第n种N皇后问题解法的函数
    def drawSolution(self):
        msg = ''
        # 异常处理
        try:
            # 读取用户输入的解法序号
            strn = self.entry2.get()
            n = int(strn) - 1
            N = nqueen_instance.ansNum
            # 检查用户是否已经进行了求解、问题是否有解
            if (N <= 0):
                msg = "此问题无解或没有进行求解。"
            elif ((n < 0) or (n >= N)):
                msg = "请输入1到" + str(N) + "之间的整数。"
            else:
                # 调用NQueen类中的画图函数绘制第n个解，并且更新图像
                nqueen_instance.draw(n)
                msg = "第 " + strn + "/" + str(N) + "个解"
                newImage = PhotoImage(file='solution_image.png')
                self.label.config(image=newImage)
                self.label.image = newImage
        except Exception:
                # 用户输入不合法（如未输入、输入字符）时进行异常处理
                msg = "输入数值不合法，请检查输入。"
        # 更新窗口中显示的解法序号        
        self.countLabel.config(text=msg, bg="white", fg="blue")

    # 显示前一种N皇后问题解法的函数
    def drawSolutionPrev(self):
        N = nqueen_instance.ansNum
        # 异常处理：检查用户输入是否合法
        # 若用户未输入数字或输入不合法则直接从最后一种解法开始展示
        try:
            strn = self.entry2.get()
            n = int(strn) - 1
            if ((n < 1) or (n >= N) or (N==-1)):
                n = N - 1
            else:
                n = n - 1
        except Exception:
            n = N - 1
        
        # 检查问题是否有解和用户是否已经进行了求解操作
        if (n >= 0):
            # 绘制第n个解并且更新图像
            nqueen_instance.draw(n)
            msg = "第 " + str(n+1) + "/" + str(N) + "个解"
            self.entry2.delete(0, END)
            self.entry2.insert(0, str(n+1))
            newImage = PhotoImage(file='solution_image.png')
            self.label.config(image=newImage)
            self.label.image = newImage
        else:
            msg = "此问题无解或没有进行求解。"
        self.countLabel.config(text=msg, bg="white", fg="blue")

    def drawSolutionNext(self):
        N = nqueen_instance.ansNum
        # 异常处理：检查用户输入是否合法
        # 若用户未输入数字或输入不合法则直接从第一种解法开始展示
        try:
            strn = self.entry2.get()
            n = int(strn) - 1
            if (N == -1):
                n = -1
            elif ((n < 0) or (n >= N-1)):
                n = 0
            else:
                n = n + 1
        except Exception:
            n = -1 if (N==-1) else 0

        if (n >= 0):
            # 绘制第n个解并且更新图像
            nqueen_instance.draw(n)
            msg = "第 " + str(n+1) + "/" + str(N) + "个解"
            self.entry2.delete(0, END)
            self.entry2.insert(0, str(n+1))
            # Update image
            newImage = PhotoImage(file='solution_image.png')
            self.label.config(image=newImage)
            self.label.image = newImage
        else:
            msg = "此问题无解或没有进行求解。"
        self.countLabel.config(text=msg, bg="white", fg="blue")
#GUI_instance = NQueenGUI()
