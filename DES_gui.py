"""    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """
    
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import DES_lib as des

Tr2Eng  = str.maketrans("çÇğĞıİöÖşŞüÜ", "cCgGiIoOsSuU")
form    = tk.Tk()

form.geometry('540x320+475+300')
form.resizable(False,False)
form.title('DES Encryption (ECB Mode)')
  
key_var     = tk.StringVar() 
text_var    = tk.StringVar() 

title1      = tk.Label(form, text='Omer Faruk KOCADAYI', fg='Blue', font='Times 15').pack()
title2      = tk.Label(form, text='DES Encryption/Decryption (ECB)', fg='Red', font='Times 13').pack()
      
keyLabel    = tk.Label(form, text='Key : ', fg='Red', font='Times 13').place(x=10, y=65)
keyLabel    = tk.Label(form, text='*If your key length < 8, space will be added to the end', fg='Black', font='Times 9 bold').place(x=10, y=90)
keyEntry    = tk.Entry(form, textvariable=key_var, fg='Black', bg='Gray', font='Times 13').place(x=70, y=65)
     
textLabel   = tk.Label(form, text='Text :', fg='Red', font='Times 13').place(x=10, y=140)
textEntry   = tk.Entry(form, textvariable=text_var , fg='Black', bg='Gray', font='Times 13').place(x=70, y=140)

keyLabel        = tk.Label(form, text='Your Key\t\t: ', fg='Blue', font='Times 13 bold').place(x=10, y=200)
cipherLabel     = tk.Label(form, text='Cipher Text\t: ', fg='Blue', font='Times 13 bold').place(x=10, y=240)
decipherLabel   = tk.Label(form, text='Decipher Text\t: ', fg='Blue', font='Times 13 bold').place(x=10, y=280)

def clear():
    a=100 * ' '
    keyLabel2       = tk.Label(form, text=a, fg='Red', font='Times 15 bold').place(x=165, y=198)
    cipherLabel2    = tk.Label(form, text=a, fg='Red', font='Times 15 bold').place(x=165, y=238)
    decipherLabel2  = tk.Label(form, text=a, fg='Red', font='Times 15 bold').place(x=165, y=278)

def compute(key,text):
    keyLen  = len(key)
    textLen = len(text)
    
    if  (keyLen == 0)       : key, keyLen = "SAUCyber", 8    
    elif(keyLen < 8)        : key += (8 - keyLen) * chr(keyLen)                 #padding -> pkcs5
    if  (textLen % 8 != 0)  : text += (8 - (textLen % 8)) * chr(textLen % 8)    #padding -> pkcs5
        
    ciphered    = des.run(key.translate(Tr2Eng), text.translate(Tr2Eng), 1)
    deciphered  = des.run(key.translate(Tr2Eng), ciphered, 0)
    ciphered    = ciphered[:textLen]       #remove padding
    deciphered  = deciphered[:textLen]   #remove padding
        
    return key,min(keyLen,8),text,ciphered,deciphered

def show_result():
    clear()
    if len(key_var.get()) == 0 : messagebox.showinfo("Warning !", "Key was empty. The key has been assigned as 'SAUCyber'")
    key,keyLen,text,ciphered,deciphered = compute(key_var.get().translate(Tr2Eng), text_var.get().translate(Tr2Eng))

    keyLabel2       = tk.Label(form, text=key[:keyLen].translate(Tr2Eng), fg='Red', font='Times 15 bold').place(x=165, y=198)
    cipherLabel2    = tk.Label(form, text="%r"% ciphered.translate(Tr2Eng), fg='Red', font='Times 15 bold').place(x=165, y=238)
    decipherLabel2  = tk.Label(form, text=deciphered.translate(Tr2Eng), fg='Red', font='Times 15 bold').place(x=165, y=278)
   
def txt_output():
    path        = filedialog.askopenfilename(initialdir="/", filetypes=(("Text Files", "*.txt"), ))
    decrFile    = open(path, 'r', encoding="utf-8")
    path        = path[0:len(path)-4] + '_CRYPTED' + path[len(path)-4:]
    crFile      = open(path, 'w', encoding="utf-8")
    path        = path[path[:path.rindex('/')].rindex('/'):]
        
    if len(key_var.get()) == 0 : messagebox.showinfo("Warning !", "Key was empty. The key has been assigned as 'SAUCyber'")
    for row in decrFile:
        key,keyLen,text,ciphered,deciphered = compute(key_var.get().translate(Tr2Eng), row.translate(Tr2Eng))
        crFile.write(""+str(ciphered)+"\n")
        
    messagebox.showinfo("Successful !", "YOUR ENCRYPTED DATA IS SAVED IN : ..."+path)   
    decrFile.close()
    crFile.close()    

run_button = tk.Button(form,text='RUN', fg='White', bg='Red', font='Times 19 bold', command=show_result).place(x=310, y=85)
txt_button = tk.Button(form,text='RUN with\nTXT UPLOAD', fg='White', bg='Blue', font='Times 13 bold', command=txt_output).place(x=400, y=85)

form.mainloop()