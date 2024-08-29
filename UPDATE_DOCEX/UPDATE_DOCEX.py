from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\63947\Documents\College\DBMS PROJECT\UPDATE_DOCEX\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def exit_update():
    update_window.destroy()

update_window = Tk()

update_window.geometry("500x550")
update_window.configure(bg = "#DBDBDB")


canvas = Canvas(
    update_window,
    bg = "#DBDBDB",
    height = 550,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
update_logo_image = PhotoImage(
    file=relative_to_assets("update_logo.png"))
update_logo = canvas.create_image(
    207.0,
    338.00000000000006,
    image=update_logo_image
)

canvas.create_text(
    20.00000000000003,
    11.000000000000057,
    anchor="nw",
    text="Update Document",
    fill="#4C0C7E",
    font=("Inter SemiBold", 35 * -1)
)

canvas.create_text(
    21.00000000000003,
    50.00000000000006,
    anchor="nw",
    text="It’s quick and easy",
    fill="#000000",
    font=("Inter Regular", 14 * -1)
)

canvas.create_rectangle(
    -1.0,
    84.00000000000006,
    500.0,
    85.00000000000006,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    -1.0,
    74.00000000000006,
    500.0,
    75.00000000000006,
    fill="#000000",
    outline="")

canvas.create_text(
    21.00000000000003,
    429.00000000000006,
    anchor="nw",
    text="*In compliance with the Republic Act 10173 or the Data Privacy Act of 2012, DocEx can",
    fill="#000000",
    font=("Inter Regular", 10 * -1)
)

canvas.create_text(
    25.00000000000003,
    440.00000000000006,
    anchor="nw",
    text="guarantee that your personal information and files are safely kept on our server.",
    fill="#000000",
    font=("Inter Regular", 10 * -1)
)

canvas.create_text(
    21.00000000000003,
    400.00000000000006,
    anchor="nw",
    text="Copy the link of your uploaded file",
    fill="#000000",
    font=("Inter Regular", 10 * -1)
)

canvas.create_text(
    21.00000000000003,
    386.00000000000006,
    anchor="nw",
    text="Upload your file on your Google Drive",
    fill="#000000",
    font=("Inter Regular", 10 * -1)
)

canvas.create_text(
    21.00000000000003,
    373.00000000000006,
    anchor="nw",
    text="Make sure you have a Google Drive",
    fill="#000000",
    font=("Inter Regular", 10 * -1)
)

canvas.create_text(
    21.00000000000003,
    357.00000000000006,
    anchor="nw",
    text="To upload your Document Image Link:",
    fill="#000000",
    font=("Inter Regular", 10 * -1)
)

canvas.create_text(
    25.00000000000003,
    100.00000000000006,
    anchor="nw",
    text="Document Type: \n(e.g. Birth Cert., License, Docs., etc. )",
    fill="#000000",
    font=("Inter Regular", 14 * -1)
)

canvas.create_text(
    25.00000000000003,
    186.00000000000006,
    anchor="nw",
    text="Document Expiration:\n(N.A. if None)",
    fill="#000000",
    font=("Inter Regular", 14 * -1)
)

canvas.create_text(
    25.00000000000003,
    271.00000000000006,
    anchor="nw",
    text="Document Image link: \n(Link of file from Google Drive)",
    fill="#000000",
    font=("Inter Regular", 14 * -1)
)

update_ext_btn_image = PhotoImage(
    file=relative_to_assets("update_ext_btn.png"))
update_ext_btn = Button(
    image=update_ext_btn_image,
    borderwidth=0,
    highlightthickness=0,
    command=exit_update,
    relief="flat"
)
update_ext_btn.place(
    x=460.0,
    y=11.000000000000057,
    width=29.0,
    height=29.0
)

update_btn_image = PhotoImage(
    file=relative_to_assets("update_btn.png"))
update_btn = Button(
    image=update_btn_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
update_btn.place(
    x=165.00000000000003,
    y=496.00000000000006,
    width=170.0,
    height=40.0
)

update_box_image = PhotoImage(
    file=relative_to_assets("update_box.png"))
update_box = canvas.create_image(
    248.00000000000003,
    240.00000000000006,
    image=update_box_image
)
#--------------------------------------------------------------------------------------------------------------------
#Doc Type
def on_enter(e):
    doc_type.delete(0,'end')
def on_leave(e):
    name=doc_type.get()
    if name == '':
        doc_type.insert(0,"Document Type")
doc_type = Entry(update_window, width=25, fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
doc_type.place(x=30.0,y=143.0,)
doc_type.insert(0,'Document Type')
doc_type.bind('<FocusIn>',on_enter)
doc_type.bind('<FocusOut>',on_leave)
#--------------------------------------------------------------------------------------------------------------------
#Doc Expiration
def on_enter(e):
    doc_expiration.delete(0,'end')
def on_leave(e):
    name=doc_expiration.get()
    if name == '':
        doc_expiration.insert(0,"MM/DD/YY")
doc_expiration = Entry(update_window, width=25, fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
doc_expiration.place(x=30.0,y=229.0,)
doc_expiration.insert(0,'MM/DD/YY')
doc_expiration.bind('<FocusIn>',on_enter)
doc_expiration.bind('<FocusOut>',on_leave)
#--------------------------------------------------------------------------------------------------------------------
#Doc Image Link
def on_enter(e):
    doc_image.delete(0,'end')
def on_leave(e):
    name=doc_image.get()
    if name == '':
        doc_image.insert(0,"Image Link")
doc_image = Entry(update_window, width=25, fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
doc_image.place(x=30.0,y=315.0,)
doc_image.insert(0,'Image Link')
doc_image.bind('<FocusIn>',on_enter)
doc_image.bind('<FocusOut>',on_leave)
#--------------------------------------------------------------------------------------------------------------------

update_window.resizable(False, False)
update_window.mainloop()
