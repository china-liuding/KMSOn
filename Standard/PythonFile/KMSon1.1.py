import tkinter
import tkinter.ttk
import os

Window = tkinter.Tk()
Window.title("KMSon")
Window.geometry("450x250")

KMS_Office_Var = tkinter.StringVar()

def K_O_Bu_Clicked():
    if KMS_Office_Var.get() == "64位":
        os.system("start MondoVL.bat")
    elif KMS_Office_Var.get() == "32位":
        os.system("start MondoVL86.bat")


K_Office = tkinter.Label(Window, text="*****激活Office*****")
K_Office.grid(column=0, row=0)

K_reader = tkinter.Label(Window, text="请选择Office版本: ")
K_reader.grid(column=0, row=1)

K_O_b = tkinter.ttk.Combobox(Window)
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