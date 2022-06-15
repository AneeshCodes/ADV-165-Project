from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


root = Tk()
root.title("Planet Encyclopedia")
root.geometry("500x500")
root.configure(bg="black")

label_image = Label(root,bg="black",highlightthickness=5)
label_image.place(relx=0.5,rely=0.5,anchor=CENTER)

img_path = ""

def OpenImage():
    global img_path
    img_path = filedialog.askopenfilename(title="Open Image File", filetypes=[("Image Files", "*.jpg *.gif *.png *.jpeg"),])
    print(img_path)
    im = Image.open(img_path)
    img = ImageTk.PhotoImage(im)
    label_image["image"] = img
    img.close()
    
def rotateImage():
    print("rotate")
    global img_path
    im = Image.open(img_path)
    img = ImageTk.PhotoImage(im.rotate(180))
    label_image["image"] = img
    img.close()
        
    
btn = Button(root,text="Open Image", bg="gray60", fg="gray97", command=OpenImage)
btn.place(relx=0.5,rely=0.25,anchor=CENTER)

btnRotate = Button(root,text="Rotate Image", bg="gray60", fg="gray97", command=rotateImage)
btnRotate.place(relx=0.5,rely=0.75,anchor=CENTER)

root.mainloop()