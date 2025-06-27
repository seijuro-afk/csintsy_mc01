import tkinter as tk
import math
from PIL import Image, ImageTk
from tkinter import messagebox

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

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)

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

buttonU = tk.Button(root, text="V", command=lambda: toggle_selection("V"))
buttonU.place(x=160, y=500)

# Coordinates for each node (to draw path)
coordinates = {
    "A": (773, 350), "B": (745, 350), "C": (665, 400), "D": (413, 495),
    "E": (365, 340), "F": (326, 340), "G": (241, 336), "H": (285, 520),
    "I": (170, 345), "J": (112, 375), "K": (57, 355), "L": (213, 485),
    "M": (67, 189), "N": (137, 189), "O": (343, 191), "P": (484, 201),
    "Q": (524, 201), "R": (631, 211), "S": (481, 150), "T": (780, 170),
    "U": (10, 420), "V": (160, 500), 
    "X": (190, 270), "Y": (400, 270), "Z": (740, 270)
}

# Adjacency list for each node with cost
graph = {
    "A": {"B": 1, "Z": 4},
    "B": {"A": 1, "C": 4, "Z": 3}, 
    "C": {"B": 4, "D": 12, "Y": 12}, 
    "D": {"C": 12, "E": 9, "H": 6},
    "E": {"D": 9, "F": 1, "Y": 4}, 
    "F": {"E": 1, "G": 3}, 
    "G": {"F": 3, "I": 4, "L": 7, "X": 4}, 
    "H": {"D": 6, "L": 4},
    "I": {"G": 4, "J": 2, "X": 4}, 
    "J": {"I": 2, "K": 2, "L": 6, "U": 5, "V": 7}, 
    "K": {"J": 2, "U": 4, "X": 7}, 
    "L": {"G": 7, "H": 4, "J": 6, "V": 3},
    "M": {"N": 2, "X": 6}, 
    "N": {"M": 2, "O": 9, "X": 5}, 
    "O": {"N": 9, "X": 8, "Y": 5}, 
    "P": {"S": 1, "Q": 1, "Y": 5},
    "Q": {"P": 1, "R": 5, "S": 2}, 
    "R": {"Q": 5, "T": 7, "Z": 6}, 
    "S": {"P": 1, "Q": 2}, 
    "T": {"R": 7, "Z": 5},
    "U": {"K": 4, "J": 5, "V": 9}, 
    "V": {"J": 7, "L": 3, "U": 9}, 
    "X": {"G": 4, "I": 4, "K": 7, "M": 6, "N": 5, "O": 8, "Y": 10}, 
    "Y": {"C": 12, "E": 4, "O": 5, "P": 5, "X": 10, "Z": 15}, 
    "Z": {"A": 4, "B": 3, "R": 6, "T": 5, "Y": 15}
}

# BFS Algorithm Function
def bfs(start, end):
    from collections import deque

    visited = set()
    queue = deque([(start, [start], 0)])

    while queue:
        current, path, cost = queue.popleft()

        if current == end:
            return path, cost

        visited.add(current)
        for neighbor in graph.get(current, {}):
            if neighbor not in visited:
                total_cost = cost + graph[current][neighbor]
                queue.append((neighbor, path + [neighbor], total_cost))

    return None, float('inf')

# Show Path of BFS / A*
def show_path():
    # Clear previous path
    for item in canvas.find_all():
        if "path" in canvas.gettags(item):
            canvas.delete(item)
    if not start_point or not end_point:
        messagebox.showwarning("Invalid Input", "Please select both start and destination nodes.")
        return

    algo = algorithm_var.get()
    if algo == "BFS":
        path, cost = bfs(start_point, end_point)
        if path:
            path_str = "-".join(path)
            result = f"Path from {start_point} to {end_point}:\n\n {path_str}\n\nCost: {cost}"
            # Draw path
            for i in range(len(path) - 1):
                x1, y1 = coordinates[path[i]]
                x2, y2 = coordinates[path[i+1]]
                canvas.create_line(x1, y1, x2, y2, fill="red", width=5, tags="path")
        else:
            result = "No path found."

        result_window = tk.Toplevel(root)
        result_window.title("BFS Path Result")
        result_window.geometry("400x150")
        result_label = tk.Label(result_window, text=result, padx=10, pady=10, font=("Arial", 12))
        result_label.pack()


algo_frame = tk.LabelFrame(root, text="Choose Algorithm", padx=10, pady=10, bg="lightgray")
algo_frame.place(x=10, y=10)

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

buttonFind = tk.Button(root, text="Find Path", command=show_path)
buttonFind.place(x=210, y=12)

buttonClear = tk.Button(root, text="Clear Path", command=lambda: toggle_clear())
buttonClear.place(x=280, y=12)

def toggle_clear():
    # Clear previous path
    for item in canvas.find_all():
        if "path" in canvas.gettags(item):
            canvas.delete(item)
    global start_point, end_point
    start_point = None
    end_point = None
    global selection_stage
    selection_stage = ["start"]
    entry.delete(0, tk.END)
    entry.insert(0, f"Start: {start_point or 'None'} | Destination: {end_point or 'None'}")

# Start the GUI loop
root.mainloop()
