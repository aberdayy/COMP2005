from cryptography.fernet import Fernet
import tkinter as tk
master = tk.Tk()
master.title("TextBox Input")
master.geometry('600x250')




def Encrypt():
    inp = inputtxt.get(1.0, "end-1c")
    if(inp):
        key = Fernet.generate_key()
        fernet = Fernet(key)
        encMessage = fernet.encrypt(inp.encode())
        lbl.config(text="Original: " + inp + f"\n Encrypted : {encMessage}")
        f = open("demo.txt", "a")
        f.write(f"Your Master Key : {key.decode('utf-8')} \n{encMessage.decode('utf-8')}\n\n")
        f.close()
    else:
        lbl.config(text="Please provide a data!")

def Decrypt():
    inp = inputtxt.get(1.0, "end-1c")
    key = keyInput.get(1.0,"end-1c")
    if (inp and key):
        fernet = Fernet(key)
        decMessage = fernet.decrypt(inp).decode()
        lbl.config(text=f"Decrypted : {decMessage}")
    else:
        lbl.config(text="Please provide a data!")

# Label Creation
lbl = tk.Label(master, text="Data:")
lbl.pack()
# TextBox Creation
inputtxt = tk.Text(master,height=5, width=20)
inputtxt.pack()
# Label Creation
lbl = tk.Label(master, text="Master Key:")
lbl.pack()
# TextBox Creation
keyInput = tk.Text(master,height=2, width=25)
keyInput.pack()

# Button Creation
EncryptButton = tk.Button(master,text="Encrypt Data",command=Encrypt)
EncryptButton.pack()

DecryptButton = tk.Button(master,text="Decrypt Data",command=Decrypt)
DecryptButton.pack()


master.mainloop()