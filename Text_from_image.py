import pytesseract
import cv2
import tkinter
import io
import os
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
from PIL import ImageGrab, ImageTk, Image
pytesseract.pytesseract.tesseract_cmd = r'D:\GIT\Text_from_image\Tesseract-OCR\\tesseract.exe'

main_win = tkinter.Tk()
main_win.geometry("1000x500")
scrollbar = tkinter.Scrollbar(main_win)
scrollbar.pack(side=tkinter.LEFT, fill=tkinter.Y)


def fromClipboard():
    text.delete("1.0", "end")
    img = ImageGrab.grabclipboard()
    img.save('paste.png', 'PNG')
    imgfc = 'paste.png'
    imgreaded2 = pytesseract.image_to_string(imgfc)
    print(imgreaded2)
    text.insert(END,imgreaded2)
    os.remove('paste.png')

def chooseFile():
    main_win.sourceFile = filedialog.askopenfilename(parent=main_win, initialdir= "/", title='Please select a file')
    img = cv2.imread(main_win.sourceFile)
    imgreaded = pytesseract.image_to_string(img)
    print(imgreaded)
    text.insert(END,imgreaded)

text = tkinter.Text(main_win, height=25, width=50) #okno z textem
text.place(x = 18,y = 0)
text.width = 1
text.config(yscrollcommand=scrollbar.set)
text.config(font=("Courier", 20))

b_chooseFile = tkinter.Button(main_win, text = "Chose File", width = 20, height = 3, command = chooseFile) #button
b_chooseFile.place(x = 830,y = 250)
b_chooseFile.width = 250

b_fc = tkinter.Button(main_win, text = "From clipboard", width = 20, height = 3, command = fromClipboard) #button
b_fc.place(x = 830,y = 100)
b_fc.width = 250

main_win.mainloop()

img = cv2.imread(main_win.sourceFile)
imgreaded = pytesseract.image_to_string(img)
print(imgreaded)

