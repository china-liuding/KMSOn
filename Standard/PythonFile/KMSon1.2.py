import tkinter.ttk
import os

Window = tkinter.Tk()
Window.title("KMSon")
Window.geometry("450x250")

KMS_Office_Var = tkinter.StringVar()
KMS_Office_Version_Var = tkinter.StringVar()
KMS_Windows_Var = tkinter.StringVar()


def Windows_Active():
    os.system("slmgr /skms kms.luody.info")
    os.system("slmgr /ato")
    

def K_O_Bu_Clicked():
    if KMS_Office_Var.get() == "64位" and KMS_Office_Version_Var.get() == "Microsoft 365(Office 365)":
        os.system("start MondoVL.bat")
    elif KMS_Office_Var.get() == "32位" and KMS_Office_Version_Var.get() == "Microsoft 365(Office 365)":
        os.system("start MondoVL86.bat")
    elif KMS_Office_Var.get() == "64位" and KMS_Office_Version_Var.get() == "Office 2019":
        os.system("start ProPlus2019.bat")
    elif KMS_Office_Var.get() == "32位" and KMS_Office_Version_Var.get() == "Office 2019":
        os.system("start ProPlus2019x86.bat")


K_Office = tkinter.Label(Window, text="*****激活Office*****")
K_Office.grid(column=0, row=0)

K_Windows = tkinter.Label(Window, text="*****激活Windows*****")
K_Windows.grid(column=0, row=4)

K_Windows_Active = tkinter.Button(Window, text="点此直接激活Windows", command=Windows_Active)
K_Windows_Active.grid()

K_reader = tkinter.Label(Window, text="请选择Office版本: ")
K_reader.grid(column=0, row=1)

K_O_b = tkinter.ttk.Combobox(Window, textvariable=KMS_Office_Version_Var)
K_O_b['value'] = ("Microsoft 365(Office 365)",
                  "Office 2019",
                  "Office 2016",)
K_O_b.grid(column=1, row=1)

K_O_Br = tkinter.Label(Window, text="请选择您的Office的位数: ")
K_O_Br.grid(column=0, row=2)

K_O_Bu = tkinter.Button(Window, text="激活", command=K_O_Bu_Clicked)
K_O_Bu.grid(column=4, row=1)

K_O_Bit = tkinter.ttk.Combobox(Window, textvariable=KMS_Office_Var)
K_O_Bit['value'] = ("32位",
                    "64位")
K_O_Bit.grid(column=1, row=2)


Window.mainloop()
