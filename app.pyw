import customtkinter as ctk
import os
class App:
    def __init__(self,user):
        global win
        win = ctk.CTk()
        win.geometry("950x500")
        win.resizable(False,False)
        win.title("Instruction for noobs...")
        win.config(bg="#121212")
        label = ctk.CTkLabel(master=win,text=f"\n\nHi {user},\nWelcome to Keyboard Heatmap Generator.\nPress Start.,\nDo not close the terminl window.\nTo get your output press left-shift+esc.\nKeylogger would be closed after that,\nTo restart it run the app again and login\nHappy typing!!!\n",font=("Terminal" ,25, "bold"),text_color="lime green",bg_color="#121212")
        label.pack()
        button=ctk.CTkButton(master=win,height=60,width=120,text="START",bg_color="#121212",fg_color="lime green",text_color="black",font=("Terminal" ,25, "bold"),corner_radius=20,border_width=5,hover_color="#dddddd",border_color="#ffffff",command=self.go)
        button.pack()
        win.mainloop()
    
    def go(self):
        win.destroy()
        os.system('py heatmap2.pyw')
        
        
        







if __name__=="__main__":
    App("testing directly")




