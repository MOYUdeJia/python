# 使用tkinter做一个简单的GUI应用
import tkinter
import tkinter.messagebox

def main():
    flag =True
    # 修改标签上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color,msg = ('red','Hello,world')\
            if flag else ('blue','Goodbye,world!')
        label.config(text=msg,fg=color)

    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示','您确定要退出吗'):
            top.quit()

    top = tkinter.Tk()  #创建窗口
    top.geometry('240x160')#窗口大小 (用字母x）
    top.title('小游戏')#窗口标题

    # 创建标签对象并添加到顶层窗口
    label = tkinter.Label(top,text = 'Hello,world!',font = 'Arial -32',fg = 'red')
    label.pack(expand=1)

    panel = tkinter.Frame(top)# 创建一个装按钮的容器
    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel,text = '修改',command = change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel,text = '退出',command = confirm_to_quit)
    button2.pack(side = 'bottom')
    panel.pack(side = 'bottom')

    # 开启主循环
    tkinter.mainloop()


if __name__ == '__main__':
    main()

