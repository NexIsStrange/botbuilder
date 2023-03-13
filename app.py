import customtkinter as ctk
import json

window = ctk.CTk()
window.geometry("700x500")
window.resizable(False,False)
ver = 0.01
window.title(f"[{ver}] Discord Bot Builder")
frame = ctk.CTkFrame(master=window,width=650,height=450)
frame.place(x=25,y=25)

def Create_Command():
    print("Pressed")
    
def Setting():
    window = ctk.CTk()
    window.geometry("700x500")
    window.resizable(False,False)
    
    frame = ctk.CTkFrame(master=window,width=650,height=450)
    frame.place(x=25,y=25)
    
    def save_token():
        with open("data.json","r") as f:
            data = json.load(f)
        token_ = token.get()
        data["TOKEN"] = token_
    
    with open("data.json","r") as f:
        data = json.load(f)
        
    token_placeholder = data.get("TOKEN","None")
    
    token = ctk.CTkEntry(master=frame,placeholder_text=token_placeholder,width=200,height=50)
    token.place(x=25,y=25)

    save = ctk.CTkButton(master=frame,text="Save",width=75,height=50,command=save_token)
    save.place(x=250,y=25)
    
    window.mainloop()

create_command = ctk.CTkButton(master=frame,text="Create Command",command=Create_Command,width=200,height=75,font=("Helvetica",24))
create_command.place(x=27,y=30)

settings = ctk.CTkButton(master=frame,text="Settings",command=Setting,width=200,height=75,font=("Helvetica",24))
settings.place(x=27,y=130)
window.mainloop()