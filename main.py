import tkinter
import tkinter.filedialog
from PIL import Image,ImageGrab
import tkinter.colorchooser
root = tkinter.Tk()

selectedColor = "red"
currentWidth = 3
currentTool = "pen"

def promptChooseColor():
    global selectedColor
    selectedColor = tkinter.colorchooser.askcolor(selectedColor)[1]
    print(selectedColor)

def updateTool(new):
    global currentTool
    currentTool = new

def updateWidth(ev):
    global currentWidth
    currentWidth = thicknessPicker.get()

thicknessPicker = tkinter.Scale(root, from_=1, to_=8, orient=tkinter.HORIZONTAL, length=180, showvalue=0, command=updateWidth)
mainCanvas = tkinter.Canvas(root, width=650, height=600, bg="white")
mainCanvas.pack(side=tkinter.BOTTOM)

xe = 0
ye = 0

def onCanvasPressed(ev):
    global currentTool,currentWidth,selectedColor,xe,ye
    if currentTool == "brush":
        mainCanvas.create_line(xe,ye,ev.x,ev.y,width=currentWidth, fill=selectedColor, smooth=True, capstyle=tkinter.BUTT)
    elif currentTool == "pen":
        mainCanvas.create_line(xe,ye,ev.x,ev.y,width=currentWidth, fill=selectedColor, smooth=False, capstyle=tkinter.ROUND)
    elif currentTool == "eraser":
        mainCanvas.create_line(xe,ye,ev.x,ev.y,width=currentWidth, fill="white", smooth=False, capstyle=tkinter.ROUND)
    xe = ev.x
    ye = ev.y

def button1Pressed(ev):
    global xe,ye
    xe = ev.x
    ye = ev.y


mainCanvas.bind("<ButtonPress-1>", button1Pressed)
mainCanvas.bind("<B1-Motion>", onCanvasPressed)

introLabel = tkinter.Label(root, text="Paint App V1", font="Arial 15 bold")
introLabel.pack(padx=5, pady=4, side=tkinter.LEFT)

def save():
    x = mainCanvas.winfo_rootx()
    y = mainCanvas.winfo_rooty()
    x1 = x + mainCanvas.winfo_width()
    y1 = y + mainCanvas.winfo_height()
    ImageGrab.grab((x,y,x1,y1)).save(tkinter.filedialog.asksaveasfilename(filetypes=[("PNG Image", "*.png"), ("BMP Image", "*.bmp"), ("TIFF Image", "*.tiff"), ("JPEG Image", "*jpg")], defaultextension=".png"))

thicknessPicker.pack(padx=10, pady=0, side=tkinter.LEFT)

brushBtn = tkinter.Button(root, text="Brush", font="Arial 13", width=5, justify="center", anchor="center", command=lambda: updateTool("brush"))
brushBtn.pack(pady=4, padx=3, side=tkinter.RIGHT)

penBtn = tkinter.Button(root, text="Pen", font="Arial 13", width=5, justify="center", anchor="center", command=lambda: updateTool("pen"))
penBtn.pack(pady=4, padx=3, side=tkinter.RIGHT)

eraseBtn = tkinter.Button(root, text="Eraser", font="Arial 13", width=6, justify="center", anchor="center", command=lambda: updateTool("eraser"))
eraseBtn.pack(pady=4, padx=3, side=tkinter.RIGHT)

colorBtn = tkinter.Button(root, text="Color", font="Arial 13", width=5, justify="center", anchor="center", command=promptChooseColor)
colorBtn.pack(pady=4, padx=3, side=tkinter.RIGHT)

saveBtn = tkinter.Button(root, text="Save", font="Arial 13", width=8000000, justify="center", anchor="center", command=save)
saveBtn.pack(pady=4, padx=3, side=tkinter.RIGHT)

root.title("Paint App")
root.resizable(False, False)
root.geometry("650x650")

tkinter.mainloop()

pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
