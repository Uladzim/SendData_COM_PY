import tkinter as tk
import serial
import struct


def run(DATA):
    ser = serial.Serial("COM7", 115200)
    ser.write(bytes.fromhex(DATA))
    ser.close()

def fun_001():
    run('7E FF 06 0D 00 00 00 FE EE EF')

def fun_002():
    run('7E FF 06 0E 00 00 00 FE ED EF')
    
def fun_003():
    run('7E FF 06 01 00 00 00 FE FA EF')
    
def fun_004():
    run('7E FF 06 02 00 00 00 FE F9 EF')
    
def fun_005():
    run('7E FF 06 16 00 00 00 FE E5 EF')

def fun_006():
    run('7E FF 06 0C 00 00 00 FE EF EF')

def fun_007():
    run('7E FF 06 19 00 00 00 EF')

def fun_008():
    run('7E FF 06 04 00 00 00 FE F7 EF')

def fun_009():
    run('7E FF 06 05 00 00 00 FE F6 EF')

def fun_00a():
    run('7E FF 06 08 00 00 01 FE F2 EF')#

def fun_00b():
    run('7E FF 06 08 00 00 02 FE F1 EF')#
    
def fun_00c():
    run('7E FF 06 08 00 00 05 FE F1 EF')#

def fun_00d():
    run('7E FF 06 08 00 00 0A FE E9 EF')#
##############################################################################
root = tk.Tk()

button_001   = tk.Button(root, text="001", command=fun_001, padx=10, pady=5, width=15, wraplength=100)
button_002   = tk.Button(root, text="002", command=fun_002, padx=10, pady=5, width=15, wraplength=100)
button_005   = tk.Button(root, text="003", command=fun_003, padx=10, pady=5, width=15, wraplength=100)
button_010   = tk.Button(root, text="004", command=fun_004, padx=10, pady=5, width=15, wraplength=100)
button_PLAY  = tk.Button(root, text="005", command=fun_005, padx=10, pady=5, width=15, wraplength=100)
button_PAUSE = tk.Button(root, text="006", command=fun_006, padx=10, pady=5, width=15, wraplength=100)
button_NEXT  = tk.Button(root, text="007", command=fun_007, padx=10, pady=5, width=15, wraplength=100)
button_PREV  = tk.Button(root, text="008", command=fun_008, padx=10, pady=5, width=15, wraplength=100)
button_STOP  = tk.Button(root, text="009", command=fun_009, padx=10, pady=5, width=15, wraplength=100)
button_RESET = tk.Button(root, text="00a", command=fun_00a, padx=10, pady=5, width=15, wraplength=100)
button_LOOP  = tk.Button(root, text="00b", command=fun_00b, padx=10, pady=5, width=15, wraplength=100)
button_UP    = tk.Button(root, text="00c", command=fun_00c, padx=10, pady=5, width=15, wraplength=100)
button_DOWN  = tk.Button(root, text="00d", command=fun_00d, padx=10, pady=5, width=15, wraplength=100)


button_001.pack (padx= 0, pady= 0)
button_002.pack (padx= 0, pady= 0)
button_003.pack (padx= 0, pady= 0)
button_004.pack (padx= 0, pady= 0)
button_005.pack (padx= 0, pady= 0)
button_006.pack (padx= 0, pady= 0)
button_007.pack (padx= 0, pady= 0)
button_008.pack (padx= 0, pady= 0)
button_009.pack (padx= 0, pady= 0)
button_00a.pack (padx= 0, pady= 0)
button_00b.pack (padx= 0, pady= 0)
button_00c.pack (padx= 0, pady= 0)
button_00d.pack (padx= 0, pady= 0)

root.mainloop()
