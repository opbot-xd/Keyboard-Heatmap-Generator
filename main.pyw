import tkinter as tk
import customtkinter as ctk
import time
from PIL import Image
import db
import app

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


def add_acc(p,u):
    print(type(p))
    db.add_login(u,p)
    sign_up.destroy()


def new_Acc():
    global sign_up
    sign_up = ctk.CTk()
    sign_up.title("Sign Up")
    sign_up.geometry("275x470")
    sign_up.resizable(False, False)
    label = ctk.CTkLabel(sign_up,text="\nWelcome to the family.",font=("serif" ,15 ,"bold"),corner_radius=20,text_color="lime green") 
    label.pack(pady=20) 
    
    
    frame3 = ctk.CTkFrame(master=sign_up) 
    frame3.pack(pady=20,padx=40,fill='both',expand=True) 
    
    label = ctk.CTkLabel(master=frame3,text='Craete your account.') 
    label.pack(pady=12,padx=10) 
    
    
    user_entry= ctk.CTkEntry(master=frame3,placeholder_text="Username") 
    user_entry.pack(pady=12,padx=10) 
    
    user_pass= ctk.CTkEntry(master=frame3,placeholder_text="Password",show="*") 
    user_pass.pack(pady=12,padx=10)
    user_pass4= ctk.CTkEntry(master=frame3,placeholder_text="Confirm Password",show="*") 
    user_pass4.pack(pady=12,padx=10)
    l_btn4 = ctk.CTkButton(frame3,text="Sign Up",font=("Ariel",15,"bold"),height=40,width=60,fg_color="#0085FF",cursor="hand2"
                    ,corner_radius=15,command=lambda: add_acc(user_pass.get(),user_entry.get()))
    l_btn4.pack(pady=24,padx=10)
    sign_up.mainloop()





def checking():
    user=usrname_entry.get()
    pasw=passwd_entry.get()
    if db.check_login(user,pasw):
        main.destroy()
        app.App(user)
    else:
        incorrect_label=ctk.CTkLabel(master=main, bg_color="#121212",corner_radius=25,text="Incorrect credentials\nTry again",font=("Terminal" ,20, "bold"),text_color="red",justify="left")
        incorrect_label.place(rely=.85,relx=0.81,anchor="s")


def new_start():
    global usrname_entry
    global passwd_entry
    global main
    global frame1
    main = ctk.CTk()
    main.title("Login Page")
    main.config(bg="#121212")
    main.resizable(False, False)
    bg_img = ctk.CTkImage(dark_image=Image.open("./imgs/bg12.jpg"), size=(700, 700))

    bg_lab = ctk.CTkLabel(main, image=bg_img, text="")
    bg_lab.grid(row=0, column=0)

    frame1 = ctk.CTkFrame(main,fg_color="#D9D9D9", bg_color="#121212", height=350, width=300,corner_radius=20)
    frame1.grid(row=0, column=1,padx=40)

    title = ctk.CTkLabel(frame1,text="Welcome Back! \nLogin to Account",text_color="#121212",font=("comic sans ms",35,"bold"))
    title.grid(row=0,column=0,sticky="nw",pady=30,padx=10)

    usrname_entry = ctk.CTkEntry(frame1,text_color="white", placeholder_text="Username", fg_color="#121212", placeholder_text_color="white",
                            font=("comic sans ms",16,"bold"), width=200, corner_radius=15, height=45)
    usrname_entry.grid(row=1,column=0,sticky="nwe",padx=30)

    passwd_entry = ctk.CTkEntry(frame1,text_color="white",placeholder_text="Password",fg_color="#121212",placeholder_text_color="white",
                            font=("comic sans ms",16,"bold"), width=200,corner_radius=15, height=45, show="*")
    passwd_entry.grid(row=2,column=0,sticky="nwe",padx=30,pady=20)

    cr_acc = ctk.CTkButton(frame1,text="Sign Up",font=("comic sans ms",15,"bold"),height=40,width=60,fg_color="#0085FF",cursor="hand2",
                    corner_radius=15,command=new_Acc)
    cr_acc.grid(row=3,column=0,sticky="w",pady=20,padx=40)

    l_btn = ctk.CTkButton(frame1,text="Login",font=("comic sans ms",15,"bold"),height=40,width=60,fg_color="#0085FF",cursor="hand2",command=checking
                    ,corner_radius=15)
    l_btn.grid(row=3,column=0,sticky="ne",pady=20, padx=35)

    main.mainloop()


def button_event():
    switch_1.place_forget()
    label_intro.place_forget()
    button.place_forget()
    root.destroy()
    new_start()

def switch_event():
    if switch_var.get() == 'on':
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")
    else:
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("KeyKing")
root.geometry("800x450")
bg_img1 = ctk.CTkImage(dark_image=Image.open("./imgs/bg1.jpg"), size=(1500, 1500))
bg_lab1 = ctk.CTkLabel(root, image=bg_img1, text="")
bg_lab1.place(rely=0.5,relx=0.5,anchor="center")
switch_var = ctk.StringVar(value="off")
switch_1 = ctk.CTkSwitch(master=root, text="Dark Mode", command=switch_event,font = ("Terminal", 15, "bold"),
                                   variable=switch_var, onvalue="off", offvalue="on",height=15)
switch_1.place(relx=0.99, rely=0.02, anchor = "e")


label_intro = ctk.CTkLabel(master=root,text="Welcome to Keyboard King...",font=("Terminal" ,25, "bold"),text_color="lime green")
label_intro.place(relx=0.5, rely=0.44, anchor=tk.CENTER)
button = ctk.CTkButton(master=root, text="Start", command=button_event,height = 50,width=30,font=("Terminal" ,20, "bold"))
button.place(relx=0.5, rely=0.57,anchor=tk.CENTER)

root.mainloop()