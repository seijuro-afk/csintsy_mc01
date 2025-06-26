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

buttonI = tk.Button(root, text="I", command=lambda: print("Button clicked"))
buttonI.place(x=170, y=345)

buttonJ = tk.Button(root, text="J", command=lambda: print("Button clicked"))
buttonJ.place(x=112, y=375)

buttonK = tk.Button(root, text="K", command=lambda: print("Button clicked"))
buttonK.place(x=57, y=355)

buttonL = tk.Button(root, text="L", command=lambda: print("Button clicked"))
buttonL.place(x=213, y=485)

buttonM = tk.Button(root, text="M", command=lambda: print("Button clicked"))
buttonM.place(x=67, y=189)

buttonN = tk.Button(root, text="N", command=lambda: print("Button clicked"))
buttonN.place(x=137, y=189)

buttonO = tk.Button(root, text="O", command=lambda: print("Button clicked"))
buttonO.place(x=343, y=191)

buttonP = tk.Button(root, text="P", command=lambda: print("Button clicked"))
buttonP.place(x=484, y=201)

buttonQ = tk.Button(root, text="Q", command=lambda: print("Button clicked"))
buttonQ.place(x=524, y=201)

buttonR = tk.Button(root, text="R", command=lambda: print("Button clicked"))
buttonR.place(x=631, y=211)

buttonS = tk.Button(root, text="S", command=lambda: print("Button clicked"))
buttonS.place(x=481, y=150)

buttonT = tk.Button(root, text="T", command=lambda: print("Button clicked"))
buttonT.place(x=780, y=170)

buttonU = tk.Button(root, text="U", command=lambda: print("Button clicked"))
buttonU.place(x=10, y=420)


algo_frame = tk.LabelFrame(root, text="Choose Algorithm", padx=10, pady=10, bg="lightgray")
algo_frame.pack(padx=10, pady=10, anchor="nw")

algorithm_var = tk.StringVar(value="BFS")

bfs_radio = tk.Radiobutton(
    algo_frame,
    text="BFS (Breadth-First Search)",
    variable=algorithm_var,
    value="BFS",
    bg="lightgray"
)
bfs_radio.pack(anchor=tk.W)

astar_radio = tk.Radiobutton(
    algo_frame,
    text="A* (Heuristic Search)",
    variable=algorithm_var,
    value="A*",
    bg="lightgray"
)
astar_radio.pack(anchor=tk.W)

buttonU = tk.Button(root, text="Find Path", command=lambda: print("Button clicked"))
buttonU.place(x=210, y=12)


# Start the GUI loop
root.mainloop()