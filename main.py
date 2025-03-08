import tkinter
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
mainCanvas = tkinter.Canvas(root, width=600, height=350, bg="white")
mainCanvas.pack(side=tkinter.BOTTOM)

xe = 0
ye = 0

def onCanvasPressed(ev):
    global currentTool,currentWidth,selectedColor,xe,ye
    if currentTool == "brush":
        xe = ev.x
        ye = ev.y
        mainCanvas.create_line(xe,ye,ev.x,ev.y,width=currentWidth, fill=selectedColor, smooth=True, capstyle=tkinter.ROUND, splinesteps=30)
    if currentTool == "pen":
        pass


mainCanvas.bind("<B1-Motion>", onCanvasPressed)

introLabel = tkinter.Label(root, text="Paint App V1", font="Arial 15 bold")
introLabel.pack(padx=5, pady=4, side=tkinter.LEFT)


thicknessPicker.pack(padx=10, pady=0, side=tkinter.LEFT)

brushBtn = tkinter.Button(root, text="Brush", font="Arial 13", width=5, justify="center", anchor="center", command=lambda: updateTool("brush"))
brushBtn.pack(pady=4, padx=3, side=tkinter.RIGHT)

penBtn = tkinter.Button(root, text="Pen", font="Arial 13", width=5, justify="center", anchor="center", command=lambda: updateTool("pen"))
penBtn.pack(pady=4, padx=3, side=tkinter.RIGHT)

eraseBtn = tkinter.Button(root, text="Eraser", font="Arial 13", width=6, justify="center", anchor="center", command=lambda: updateTool("eraser"))
eraseBtn.pack(pady=4, padx=3, side=tkinter.RIGHT)

colorBtn = tkinter.Button(root, text="Color", font="Arial 13", width=5, justify="center", anchor="center", command=promptChooseColor)
colorBtn.pack(pady=4, padx=3, side=tkinter.RIGHT)

root.title("Paint App")
root.resizable(False, False)
root.geometry("600x400")

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
