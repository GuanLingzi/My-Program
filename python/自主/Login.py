import tkinter as tk
import tkinter.messagebox
import pickle

window = tk.Tk()

window.title('登陆窗口')

window.geometry('400x300')

tk.Label(window, text='用户名:', font=('Arial', 14)).place(x=10, y=170)
tk.Label(window, text='密码:', font=('Arial', 14)).place(x=10, y=210)

# 用户名
var_usr_name = tk.StringVar()
var_usr_name.set('Admin')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name, font=('Arial', 14))
entry_usr_name.place(x=120,y=175)
# 用户密码
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, font=('Arial', 14), show='*')
entry_usr_pwd.place(x=120,y=215)

def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    # 这里设置异常捕获，当我们第一次访问用户信息文件时是不存在的。
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        # 在没有读取到`usr_file`的时候，程序会创建一个`usr_file`这个文件，并将管理员的用户和密码写入，即用户名为`admin`密码为`admin`。
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)
            usr_file.close()    # 必须先关闭，否则pickle.load()会出现EOFError: Ran out of input

    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tkinter.messagebox.showinfo(title='欢迎', message='你好吗? ' + usr_name)
        else:
            tkinter.messagebox.showerror(message='错误, 你输入的密码不正确，重新输入。')
    else:  # 如果发现用户名不存在
        is_sign_up = tkinter.messagebox.askyesno('欢迎！ ', '你还没有注册，现在注册吗?')
        # 提示需不需要注册新用户
        if is_sign_up:
            usr_sign_up()

def usr_sign_up():
    def sign_to_Hongwei_Website():
        # 获取注册时所输入的信息
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()

        # 将注册信息读出
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if np != npf:
            tkinter.messagebox.showerror('错误', '两次输入的密码不一致!')
        # 如果用户名已经在我们的数据文件中，则提示Error, The user has already signed up!
        elif nn in exist_usr_info:
            tkinter.messagebox.showerror('错误', '这个用户名已经注册了!')
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tkinter.messagebox.showinfo('欢迎', '你已成功登录!')
            # 然后销毁窗口。
            window_sign_up.destroy()

    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('300x200')
    window_sign_up.title('注册窗口')

    new_name = tk.StringVar()  # 将输入的注册名赋值给变量
    new_name.set('admin')
    tk.Label(window_sign_up, text='用户名: ').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_new_name.place(x=130, y=10)  # `entry`放置在坐标（150,10）.

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='密码: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=130, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='核对密码: ').place(x=10, y=90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=130, y=90)

    btn_comfirm_sign_up = tk.Button(window_sign_up, text='登录', command=sign_to_Hongwei_Website)
    btn_comfirm_sign_up.place(x=180, y=120)

btn_login = tk.Button(window, text='登录', command=usr_login)
btn_login.place(x=120, y=240)
btn_sign_up = tk.Button(window, text='没有账号？注册', command=usr_sign_up)
btn_sign_up.place(x=200, y=240)

window.mainloop()
