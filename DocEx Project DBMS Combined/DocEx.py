
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,ttk,Radiobutton,IntVar
import tkinter

#--------------------------------------------------------------------------------------------------------------------
#File Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\63947\Documents\College\DBMS PROJECT\DocEx Project DBMS Combined\assets\frame0")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
#--------------------------------------------------------------------------------------------------------------------
#Sign up Window
def create_account():
    sign_up_window = tkinter.Toplevel()
    sign_up_window.title("Sign Up")
    sign_up_window.geometry("500x550")
    sign_up_window.configure(bg = "#DBDBDB")

    canvas = Canvas(sign_up_window,bg = "#DBDBDB",height = 550,width = 500,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)
    image_bg_sign_up_image = PhotoImage(
        file=relative_to_assets("image_bg_sign_up.png"))
    image_bg_sign_up = canvas.create_image(147.0,346.0,image=image_bg_sign_up_image)
#--------------------------------------------------------------------------------------------------------------------
    #First Name
    def on_enter(e):
        Name.delete(0,'end')
    def on_leave(e):
        name=Name.get()
        if name == '':
            Name.insert(0,"First Name")
    Name = Entry(sign_up_window, width=25, fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    Name.place(x=28.0,y=120.0,)
    Name.insert(0,'First Name')
    Name.bind('<FocusIn>',on_enter)
    Name.bind('<FocusOut>',on_leave)
#--------------------------------------------------------------------------------------------------------------------
    #Last Name
    def on_enter(e):
        Last.delete(0,'end')
    def on_leave(e):
        Last=Name.get()
        if Last == '':
            Last.insert(0,"Last Name")
    Last = Entry(sign_up_window, width=25, fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    Last.place(x=265.0,y=120.0,)
    Last.insert(0,'Last Name')
    Last.bind('<FocusIn>',on_enter)
    Last.bind('<FocusOut>',on_leave)
#--------------------------------------------------------------------------------------------------------------------
    #Username
    def on_enter(e):
        Username.delete(0,'end')
    def on_leave(e):
        Username=Username.get()
        if Last == '':
            Last.insert(0,"Username")
    Username = Entry(sign_up_window, width=25, fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    Username.place(x=28.0,y=181.0,)
    Username.insert(0,'Username')
    Username.bind('<FocusIn>',on_enter)
    Username.bind('<FocusOut>',on_leave)
#--------------------------------------------------------------------------------------------------------------------
    #Password
    def on_enter(e):
        password.delete(0,'end')
    def on_leave(e):
        name=Name.get()
        if name == '':
            password.insert(0,"password")
    password = Entry(sign_up_window, width=25, fg='black',show="*",border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    password.place(x=28.0,y=242.0,)
    password.insert(0,'Password')
    password.bind('<FocusIn>',on_enter)
    password.bind('<FocusOut>',on_leave)
    #Show password fx
    def show_password():
        if password.cget('show') == '*':
            password.config(show='')
        else:
            password.config(show='*')
#--------------------------------------------------------------------------------------------------------------------
    #Birth date
    date = ['January', 'February', 'March','April','May','June','July','August','September','October','November','December']
    cb1 = ttk.Combobox(sign_up_window,values=date,width=9,state='readonly',font=('Microsoft YaHei UI Light',15),justify='center')
    cb1.place(x=30,y=312)
    cb1.current(1)

    day = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    cb2 = ttk.Combobox(sign_up_window,values=day,width=9,state='readonly',font=('Microsoft YaHei UI Light',15))
    cb2.place(x=190,y=312)
    cb2.current(1)

    year = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]
    cb3 = ttk.Combobox(sign_up_window,values=year,width=9,state='readonly',font=('Microsoft YaHei UI Light',15))
    cb3.place(x=350,y=312)
    cb3.current(1)
#--------------------------------------------------------------------------------------------------------------------
    #GENDER
    gender_button = IntVar()
    Radiobutton(sign_up_window, text='Male',width=8,font=('Microsoft YaHei UI Light',15),relief='groove',activebackground='purple4',cursor='hand2',variable = gender_button, value="Male").place(x=30,y=385)
    Radiobutton(sign_up_window, text='Female',width=8,font=('Microsoft YaHei UI Light',15),relief='groove',activebackground='purple4',cursor='hand2',variable = gender_button, value="Female").place(x=190,y=385)
    Radiobutton(sign_up_window, text='Other',width=8,font=('Microsoft YaHei UI Light',15),relief='groove',activebackground='purple4',cursor='hand2',variable = gender_button, value="Other").place(x=350,y=385)
#--------------------------------------------------------------------------------------------------------------------
    #Texts
    canvas.create_text(23.0,430.0,anchor="nw",fill="#000000",font=("Inter Regular", 10 * -1),
        text="Revolutionizing Document Compilation for Streamlined Workflow, Enhanced Collaboration, and")
    canvas.create_text(23.0,442.0,anchor="nw",fill="#000000",font=("Inter Regular", 10 * -1),
        text="Time-Saving Efficiency.\n\nBy clicking Sign Up, you agree to our Terms and Privacy Policy.")
    canvas.create_text(20.0,7.0,anchor="nw",fill="#4C0C7E",font=("Inter SemiBold", 40 * -1),
        text="Sign Up ")
    canvas.create_text(28.0,55.0,anchor="nw",fill="#000000",font=("Inter Regular", 14 * -1),
        text="It’s quick and easy")
    canvas.create_rectangle(-1.0,91.0,500.0,92.0,fill="#000000",outline="")
#--------------------------------------------------------------------------------------------------------------------
    #Exit
    def exit():
        sign_up_window.destroy()
    exit_btn_image_1 = PhotoImage(
        file=relative_to_assets("exit_btn.png"))
    exit_btn = Button(sign_up_window,
        image=exit_btn_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=exit,
        relief="flat"
    )
    exit_btn.place(
        x=460.0,
        y=7.0,
        width=29.0,
        height=29.0
    )

    sign_up_btn_image = PhotoImage(
        file=relative_to_assets("sign_up_btn.png"))
    sign_up_btn = Button(sign_up_window,
        image=sign_up_btn_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    sign_up_btn.place(
        x=165.0,
        y=496.0,
        width=170.0,
        height=40.0
    )

    gender_image_image = PhotoImage(
        file=relative_to_assets("gender_image.png"))
    gender_image = canvas.create_image(
        48.0,
        371.0,
        image=gender_image_image
    )

    bday_image_image = PhotoImage(
        file=relative_to_assets("bday_image.png"))
    bday_image = canvas.create_image(
        51.0,
        298.0,
        image=bday_image_image
    )

    label_sign_up_image_image = PhotoImage(
        file=relative_to_assets("label_sign_up_image.png"))
    label_sign_up_image = canvas.create_image(
        250.0,
        192.0,
        image=label_sign_up_image_image
    )

    view_pass_sign_up_image = PhotoImage(
        file=relative_to_assets("view_pass_sign_up.png"))
    view_pass_sign_up = Button(sign_up_window,
        image=view_pass_sign_up_image,
        borderwidth=0,
        highlightthickness=0,
        command=show_password,
        relief="flat"
    )
    view_pass_sign_up.place(
        x=449.0,
        y=242.0,
        width=22.0,
        height=19.0
    )
    sign_up_window.resizable(False, False)
    sign_up_window.mainloop()
#--------------------------------------------------------------------------------------------------------------------
#Log in Window
login_window = Tk()
login_window.title("DocEx Log In")
login_window.geometry("1200x700")
login_window.configure(bg = "#DBDBDB")


canvas = Canvas(
    login_window,
    bg = "#DBDBDB",
    height = 700,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
log_in_logo_image = PhotoImage(
    file=relative_to_assets("log_in_logo.png"))
log_in_logo = canvas.create_image(
    273.0,
    269.0,
    image=log_in_logo_image
)

canvas.create_rectangle(
    640.0,
    127.00000000000003,
    1040.0,
    497.0,
    fill="#F9F9F9",
    outline="")

canvas.create_rectangle(
    664.0,
    388.0,
    1015.0,
    389.0,
    fill="#000000",
    outline="")

canvas.create_text(
    118.00000000000001,
    333.0,
    anchor="nw",
    text="Unleash the Power of Efficient ",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    118.00000000000001,
    359.0,
    anchor="nw",
    text="Document Compilation",
    fill="#000000",
    font=("Inter", 24 * -1)
)

username_label_login_image_2 = PhotoImage(
    file=relative_to_assets("username_label_login.png"))
username_label_login = canvas.create_image(
    840.0,
    187.00000000000003,
    image=username_label_login_image_2
)

password_label_login_image = PhotoImage(
    file=relative_to_assets("password_label_login.png"))
password_label_login = canvas.create_image(
    840.0,
    261.0,
    image=password_label_login_image
)
#-------------------------------------------------------------------------------------------------------
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name == '':
        user.insert(0,"Username")
user = Entry(login_window, width=25, fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=720.0,y=175.0,)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
#-------------------------------------------------------------------------------------------------------
def on_enter(e):
    password.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name == '':
        password.insert(0,"password")
password = Entry(login_window, width=25, fg='black',show="*",border=0,bg='white',font=('Microsoft YaHei UI Light',11))
password.place(x=720.0,y=250.0,)
password.insert(0,'Password')
password.bind('<FocusIn>',on_enter)
password.bind('<FocusOut>',on_leave)

def show_password():
    if password.cget('show') == '*':
        password.config(show='')
    else:
        password.config(show='*')
        
log_in_show_pass_btn_image = PhotoImage(
    file=relative_to_assets("log_in_show_pass_btn.png"))
log_in_show_pass_btn = Button(
    image=log_in_show_pass_btn_image,
    borderwidth=0,
    highlightthickness=0,
    command=show_password,
    relief="flat"
)
log_in_show_pass_btn.place(
    x=979.0,
    y=254.00000000000003,
    width=22.0,
    height=19.0
)
#-------------------------------------------------------------------------------------------------------

create_new_account_btn_image_1 = PhotoImage(
    file=relative_to_assets("create_new_account_btn.png"))
create_new_account_btn_1 = Button(
    image=create_new_account_btn_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=create_account,
    relief="flat"
)
create_new_account_btn_1.place(
    x=690.0,
    y=412.0,
    width=300.0,
    height=50.0
)

log_in_btn_image_2 = PhotoImage(
    file=relative_to_assets("log_in_btn.png"))
log_in_btn_2 = Button(
    image=log_in_btn_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
log_in_btn_2.place(
    x=665.0,
    y=316.0,
    width=350.0,
    height=50.0
)
login_window.resizable(False, False)
login_window.mainloop()
