import tkinter as tk
from PIL import Image, ImageTk

# Load your image (replace 'your_image.jpg' with the actual file path)
image_path = "bg.png"
img = Image.open(image_path)

# Create the main window
root = tk.Tk()
root.title("DLSU Food Map")
root.geometry("800x600")
root.resizable(False, False)
# Resize the image to match the window size
img = img.resize((800, 600))  # You can adjust the size as needed
bg_image = ImageTk.PhotoImage(img)

# Create a label to display the background image
background_label = tk.Label(root, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


buttonA = tk.Button(root, text="A", command=lambda: print("Button clicked"))
buttonA.place(x=773, y=350)

buttonB = tk.Button(root, text="B", command=lambda: print("Button clicked"))
buttonB.place(x=745, y=350)

buttonC = tk.Button(root, text="C", command=lambda: print("Button clicked"))
buttonC.place(x=665, y=400)

buttonD = tk.Button(root, text="D", command=lambda: print("Button clicked"))
buttonD.place(x=413, y=495)

buttonE = tk.Button(root, text="E", command=lambda: print("Button clicked"))
buttonE.place(x=365, y=340)

buttonF = tk.Button(root, text="F", command=lambda: print("Button clicked"))
buttonF.place(x=326, y=340)

buttonG = tk.Button(root, text="G", command=lambda: print("Button clicked"))
buttonG.place(x=241, y=336)

buttonH = tk.Button(root, text="H", command=lambda: print("Button clicked"))
buttonH.place(x=285, y=520)

# Start the GUI loop
root.mainloop()