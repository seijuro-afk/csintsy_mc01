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

start_point = None
end_point = None
selection_stage = ["start"]  # Mutable wrapper so it can update in toggle

def toggle_selection(value):
    global start_point, end_point

    if selection_stage[0] == "start":
        start_point = value
        selection_stage[0] = "end"
    else:
        end_point = value
        selection_stage[0] = "done"

    entry.delete(0, tk.END)
    entry.insert(0, f"Start: {start_point or 'None'} | Destination: {end_point or 'None'}")

entry = tk.Entry(root, width=40)
entry.place(x=210, y=50)
entry.insert(0, "Start: None | Destination: None")

buttonA = tk.Button(root, text="A", command=lambda: toggle_selection("A"))
buttonA.place(x=773, y=350)

buttonB = tk.Button(root, text="B", command=lambda: toggle_selection("B"))
buttonB.place(x=745, y=350)

buttonC = tk.Button(root, text="C", command=lambda: toggle_selection("C"))
buttonC.place(x=665, y=400)

buttonD = tk.Button(root, text="D", command=lambda: toggle_selection("D"))
buttonD.place(x=413, y=495)

buttonE = tk.Button(root, text="E", command=lambda: toggle_selection("E"))
buttonE.place(x=365, y=340)

buttonF = tk.Button(root, text="F", command=lambda: toggle_selection("F"))
buttonF.place(x=326, y=340)

buttonG = tk.Button(root, text="G", command=lambda: toggle_selection("G"))
buttonG.place(x=241, y=336)

buttonH = tk.Button(root, text="H", command=lambda: toggle_selection("H"))
buttonH.place(x=285, y=520)

buttonI = tk.Button(root, text="I", command=lambda: toggle_selection("I"))
buttonI.place(x=170, y=345)

buttonJ = tk.Button(root, text="J", command=lambda: toggle_selection("J"))
buttonJ.place(x=112, y=375)

buttonK = tk.Button(root, text="K", command=lambda: toggle_selection("K"))
buttonK.place(x=57, y=355)

buttonL = tk.Button(root, text="L", command=lambda: toggle_selection("L"))
buttonL.place(x=213, y=485)

buttonM = tk.Button(root, text="M", command=lambda: toggle_selection("M"))
buttonM.place(x=67, y=189)

buttonN = tk.Button(root, text="N", command=lambda: toggle_selection("N"))
buttonN.place(x=137, y=189)

buttonO = tk.Button(root, text="O", command=lambda: toggle_selection("O"))
buttonO.place(x=343, y=191)

buttonP = tk.Button(root, text="P", command=lambda: toggle_selection("P"))
buttonP.place(x=484, y=201)

buttonQ = tk.Button(root, text="Q", command=lambda: toggle_selection("Q"))
buttonQ.place(x=524, y=201)

buttonR = tk.Button(root, text="R", command=lambda: toggle_selection("R"))
buttonR.place(x=631, y=211)

buttonS = tk.Button(root, text="S", command=lambda: toggle_selection("S"))
buttonS.place(x=481, y=150)

buttonT = tk.Button(root, text="T", command=lambda: toggle_selection("T"))
buttonT.place(x=780, y=170)

buttonU = tk.Button(root, text="U", command=lambda: toggle_selection("U"))
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

buttonFind = tk.Button(root, text="Find Path", command=lambda: print("Button clicked"))
buttonFind.place(x=210, y=12)

buttonClear = tk.Button(root, text="Clear Path", command=lambda: toggle_clear())
buttonClear.place(x=280, y=12)

def toggle_clear():
    global start_point, end_point
    start_point = None
    end_point = None
    global selection_stage
    selection_stage = ["start"]
    entry.delete(0, tk.END)
    entry.insert(0, f"Start: {start_point or 'None'} | Destination: {end_point or 'None'}")

# Start the GUI loop
root.mainloop()