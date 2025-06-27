import tkinter as tk
import math
from PIL import Image, ImageTk
from tkinter import messagebox, simpledialog

image_path = "bg.png"
img = Image.open(image_path)

# Create the main window
root = tk.Tk()
root.title("DLSU Food Map")
root.geometry("800x600")
root.resizable(False, False)
# Resize the image to match the window size
img = img.resize((800, 600))  
bg_image = ImageTk.PhotoImage(img)

background_label = tk.Label(root, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)

start_point = None
end_point = None
selection_stage = ["start"]

# Track default nodes that cannot be removed
DEFAULT_NODES = set(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"])

# Track custom nodes and their buttons
custom_nodes = {}
custom_buttons = {}

# Current mode: 'select' or 'add_node'
current_mode = "select"

def toggle_selection(value):
    global start_point, end_point

    if current_mode != "select":
        return

    if selection_stage[0] == "start":
        start_point = value
        selection_stage[0] = "end"
    else:
        end_point = value
        selection_stage[0] = "done"

    entry.delete(0, tk.END)
    entry.insert(0, f"Start: {start_point or 'None'} | Destination: {end_point or 'None'}")

def on_canvas_click(event):
    """Handle canvas clicks for adding nodes"""
    if current_mode == "add_node":
        # Get next available node label
        used_labels = set(coordinates.keys())
        available_labels = []
        
        # Generate labels: AA, AB, AC, ... BA, BB, BC, etc.
        for first in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            for second in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                label = first + second
                if label not in used_labels and label not in DEFAULT_NODES:
                    available_labels.append(label)
        
        if not available_labels:
            messagebox.showerror("Error", "No more node labels available!")
            return
        
        new_label = available_labels[0]
        
        # Get restaurant name from user
        restaurant_name = simpledialog.askstring("Restaurant Name", f"Enter name for node {new_label}:")
        if not restaurant_name:
            return
        
        # Get rating (optional)
        rating_str = simpledialog.askstring("Rating", "Enter rating (1.0-5.0, press Enter for 4.0):")
        try:
            rating = float(rating_str) if rating_str else 4.0
            rating = max(1.0, min(5.0, rating))  # Clamp between 1.0 and 5.0
        except ValueError:
            rating = 4.0
        
        # Get review count (optional)
        reviews_str = simpledialog.askstring("Reviews", "Enter number of reviews (press Enter for 50):")
        try:
            reviews = int(reviews_str) if reviews_str else 50
            reviews = max(1, reviews)  # Minimum 1 review
        except ValueError:
            reviews = 50
        
        coordinates[new_label] = (event.x, event.y)
        restaurant_data[new_label] = {
            "name": restaurant_name,
            "rating": rating,
            "reviews": reviews
        }
        
        # Add to graph (initially no connections)
        graph[new_label] = {}
        
        # Create button
        button = tk.Button(root, text=new_label, bg="lightgray", 
                          command=lambda l=new_label: toggle_selection(l))
        button.place(x=event.x, y=event.y)
        
        # Store custom node info
        custom_nodes[new_label] = {"name": restaurant_name, "rating": rating, "reviews": reviews}
        custom_buttons[new_label] = button
        
        messagebox.showinfo("Node Added", f"Node {new_label} ({restaurant_name}) added successfully!")

# Bind canvas click
canvas.bind("<Button-1>", on_canvas_click)

entry = tk.Entry(root, width=40)
entry.place(x=210, y=50)
entry.insert(0, "Start: None | Destination: None")

# Create all default buttons
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

buttonV = tk.Button(root, text="V", command=lambda: toggle_selection("V"))
buttonV.place(x=160, y=500)

# Coordinates for each node (used for cost calculation)
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

# Database of Restaurants as Nodes
restaurant_data = {
    "A": {"name": "University Mall", "rating": 3.9, "reviews": 293},
    "B": {"name": "McDonalds", "rating": 4.2, "reviews": 1041},
    "C": {"name": "Pericos", "rating": 4.0, "reviews": 2},
    "D": {"name": "Bloemen Hall", "rating": 4.5, "reviews": 2},
    "E": {"name": "W.H. Taft Residence", "rating": 4.2, "reviews": 76},
    "F": {"name": "EGI Taft", "rating": 4.7, "reviews": 88},
    "G": {"name": "Castro Street", "rating": 4.5, "reviews": 11},
    "H": {"name": "Agno Food Court", "rating": 4.3, "reviews": 34},
    "I": {"name": "One Archers", "rating": 3.9, "reviews": 31},
    "J": {"name": "La Casita Br. Andrew Gonzales Hall", "rating": 4.2, "reviews": 105},
    "K": {"name": "Green Mall", "rating": 4.1, "reviews": 30},
    "L": {"name": "Green Court", "rating": 4.4, "reviews": 176},
    "M": {"name": "Sherwood", "rating": 4.1, "reviews": 178},
    "N": {"name": "Jollibee", "rating": 3.7, "reviews": 230},
    "O": {"name": "Dagonoy St.", "rating": 4.8, "reviews": 78},
    "P": {"name": "Burgundy", "rating": 4.2, "reviews": 607},
    "Q": {"name": "Estrada St.", "rating": 3.5, "reviews": 181},
    "R": {"name": "D' Student's Place", "rating": 4.5, "reviews": 265},
    "S": {"name": "Leon Guinto St.", "rating": 4.6, "reviews": 310},
    "T": {"name": "P. Ocampo St.", "rating": 4.1, "reviews": 1079},
    "U": {"name": "Fidel A, Reyes St.", "rating": 4.2, "reviews": 105},
    "V": {"name": "La Casita Enrique Razon Hall", "rating": 4.2, "reviews": 105},
    "X": {"name": "Pedestrian Crossing", "rating": 5.0, "reviews": 9999},
    "Y": {"name": "Pedestrian Crossing", "rating": 5.0, "reviews": 9999},
    "Z": {"name": "Pedestrian Crossing", "rating": 5.0, "reviews": 9999}
}

def calculate_review_score(node):
    """Calculate a score based on restaurant reviews and ratings"""
    data = restaurant_data.get(node, {"rating": 3.0, "reviews": 100})
    rating = data["rating"]
    reviews = data["reviews"]
    
    # Normalize rating (0-5 scale) and review count
    rating_score = rating / 5.0  # Convert to 0-1 scale
    review_weight = min(reviews / 1000.0, 1.0)  # Cap at 1000 reviews for weight
    
    # Combined score: higher rating + more reviews = better score
    combined_score = (rating_score * 0.7) + (review_weight * 0.3)
    return combined_score

# Heuristic function for A* (combines distance and review quality)
def heuristic(node1, node2):
    """Calculate heuristic based on Euclidean distance and destination quality"""
    # Calculate Euclidean distance
    x1, y1 = coordinates[node1]
    x2, y2 = coordinates[node2]
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # Get review-based quality score for destination
    destination_quality = calculate_review_score(node2)
    
    # Adjust heuristic: better restaurants have lower heuristic values
    # This encourages the algorithm to prefer paths to highly-rated places
    quality_modifier = 1.0 - (destination_quality * 0.3)  # Reduce heuristic by up to 30%
    
    return distance * quality_modifier

# Alternative: Pure review-based heuristic
def review_heuristic(node1, node2):
    """Pure review-based heuristic - prefers highly rated destinations"""
    destination_score = calculate_review_score(node2)
    # Lower score for better restaurants (A* minimizes heuristic)
    return 100 * (1.0 - destination_score)

# A* Algorithm Function with heuristic choice
def astar(start, end, heuristic_type="review"):
    import heapq
    
    # Priority queue: (f_score, g_score, current_node, path)
    open_set = [(0, 0, start, [start])]
    closed_set = set()
    g_scores = {start: 0}
    
    while open_set:
        f_score, g_score, current, path = heapq.heappop(open_set)
        
        if current == end:
            return path, g_score
        
        if current in closed_set:
            continue
            
        closed_set.add(current)
        
        for neighbor in graph.get(current, {}):
            if neighbor in closed_set:
                continue
                
            tentative_g_score = g_score + graph[current][neighbor]
            
            if neighbor not in g_scores or tentative_g_score < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g_score
                
                # Choose heuristic type
                if heuristic_type == "review":
                    h_score = review_heuristic(neighbor, end)
                elif heuristic_type == "combined":
                    h_score = heuristic(neighbor, end)
                else:  # distance
                    x1, y1 = coordinates[neighbor]
                    x2, y2 = coordinates[end]
                    h_score = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                
                f_score = tentative_g_score + h_score
                new_path = path + [neighbor]
                heapq.heappush(open_set, (f_score, tentative_g_score, neighbor, new_path))
    
    return None, float('inf')

# Show restaurant info
def show_restaurant_info(node):
    if node in restaurant_data:
        data = restaurant_data[node]
        info = f"Restaurant: {data['name']}\nRating: {data['rating']}/5.0\nReviews: {data['reviews']}"
        messagebox.showinfo(f"Restaurant Info - {node}", info)

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
            # Add restaurant info for destination
            dest_info = ""
            if end_point in restaurant_data:
                data = restaurant_data[end_point]
                dest_info = f"\n\nDestination: {data['name']}\nRating: {data['rating']}/5 ({data['reviews']} reviews)"
            
            result = f"Path from {start_point} to {end_point}:\n\n{path_str}\n\nTravel Cost: {cost}{dest_info}"
            # Draw path
            for i in range(len(path) - 1):
                x1, y1 = coordinates[path[i]]
                x2, y2 = coordinates[path[i+1]]
                canvas.create_line(x1, y1, x2, y2, fill="red", width=5, tags="path")
        else:
            result = "No path found."

        result_window = tk.Toplevel(root)
        result_window.title("BFS Path Result")
        result_window.geometry("450x200")
        result_label = tk.Label(result_window, text=result, padx=10, pady=10, font=("Arial", 11))
        result_label.pack()
    elif algo == "A*":
        heuristic_type = heuristic_var.get()
        path, cost = astar(start_point, end_point, heuristic_type)
        if path:
            path_str = "-".join(path)
            # Add restaurant info for destination
            dest_info = ""
            if end_point in restaurant_data:
                data = restaurant_data[end_point]
                dest_info = f"\n\nDestination: {data['name']}\nRating: {data['rating']}/5 ({data['reviews']} reviews)"
            
            heuristic_info = f"\nHeuristic: {heuristic_type.title()}"
            result = f"Path from {start_point} to {end_point}:\n\n{path_str}\n\nTravel Cost: {cost}{heuristic_info}{dest_info}"

            for i in range(len(path) - 1):
                x1, y1 = coordinates[path[i]]
                x2, y2 = coordinates[path[i+1]]
                canvas.create_line(x1, y1, x2, y2, fill="red", width=5, tags="path")
        else:
            result = "No path found."

        result_window = tk.Toplevel(root)
        result_window.title("A* Path Result")
        result_window.geometry("450x220")
        result_label = tk.Label(result_window, text=result, padx=10, pady=10, font=("Arial", 11))
        result_label.pack()

# Node management functions
def toggle_add_node_mode():
    global current_mode
    if current_mode == "select":
        current_mode = "add_node"
        add_node_btn.config(text="Exit Add Mode", bg="red")
        canvas.config(cursor="cross")
        messagebox.showinfo("Add Node Mode", "Click anywhere on the map to add a new restaurant node.")
    else:
        current_mode = "select"
        add_node_btn.config(text="Add Node", bg="lightgray")
        canvas.config(cursor="")

def remove_custom_node():
    if not custom_nodes:
        messagebox.showinfo("No Custom Nodes", "No custom nodes to remove.")
        return
    
    remove_window = tk.Toplevel(root)
    remove_window.title("Remove Custom Node")
    remove_window.geometry("300x400")
    
    tk.Label(remove_window, text="Select node to remove:", font=("Arial", 12)).pack(pady=10)
    
    listbox = tk.Listbox(remove_window, width=40, height=15)
    listbox.pack(pady=10)
    
    # Populate listbox with custom nodes
    for node_id, node_info in custom_nodes.items():
        listbox.insert(tk.END, f"{node_id}: {node_info['name']}")
    
    def confirm_remove():
        selection = listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a node to remove.")
            return
        
        # Get selected node ID
        selected_text = listbox.get(selection[0])
        node_id = selected_text.split(":")[0]
        
        # Confirm removal
        if messagebox.askyesno("Confirm Removal", f"Are you sure you want to remove node {node_id}?"):
            # Remove from all data structures
            if node_id in coordinates:
                del coordinates[node_id]
            if node_id in restaurant_data:
                del restaurant_data[node_id]
            if node_id in graph:
                del graph[node_id]
            
            # Remove references from other nodes' adjacency lists
            for other_node in graph:
                if node_id in graph[other_node]:
                    del graph[other_node][node_id]
            
            # Remove button
            if node_id in custom_buttons:
                custom_buttons[node_id].destroy()
                del custom_buttons[node_id]
            
            # Remove from custom nodes tracking
            if node_id in custom_nodes:
                del custom_nodes[node_id]
            
            # Reset selection if this node was selected
            global start_point, end_point
            if start_point == node_id:
                start_point = None
            if end_point == node_id:
                end_point = None
            
            entry.delete(0, tk.END)
            entry.insert(0, f"Start: {start_point or 'None'} | Destination: {end_point or 'None'}")
            
            messagebox.showinfo("Node Removed", f"Node {node_id} has been removed.")
            remove_window.destroy()
    
    tk.Button(remove_window, text="Remove Selected", command=confirm_remove, bg="lightgray", fg="white").pack(pady=10)
    tk.Button(remove_window, text="Cancel", command=remove_window.destroy).pack()

def manage_connections():
    """Manage connections between nodes"""
    if not coordinates:
        return
    
    conn_window = tk.Toplevel(root)
    conn_window.title("Manage Node Connections")
    conn_window.geometry("500x600")
    
    tk.Label(conn_window, text="Manage Node Connections", font=("Arial", 14, "bold")).pack(pady=10)
    
    # Node selection
    tk.Label(conn_window, text="Select Node:", font=("Arial", 12)).pack()
    node_var = tk.StringVar()
    node_dropdown = tk.OptionMenu(conn_window, node_var, *sorted(coordinates.keys()))
    node_dropdown.pack(pady=5)
    
    # Connection listbox
    tk.Label(conn_window, text="Current Connections:", font=("Arial", 12)).pack(pady=(20,5))
    conn_listbox = tk.Listbox(conn_window, width=50, height=10)
    conn_listbox.pack(pady=5)
    
    def update_connections():
        conn_listbox.delete(0, tk.END)
        selected_node = node_var.get()
        if selected_node in graph:
            for neighbor, cost in graph[selected_node].items():
                conn_listbox.insert(tk.END, f"{selected_node} -> {neighbor} (cost: {cost})")
    
    def add_connection():
        selected_node = node_var.get()
        if not selected_node:
            messagebox.showwarning("No Selection", "Please select a node first.")
            return
        
        # Get target node
        target_node = simpledialog.askstring("Add Connection", "Enter target node ID:")
        if not target_node or target_node not in coordinates:
            messagebox.showwarning("Invalid Node", "Target node does not exist.")
            return
        
        # Get cost
        cost_str = simpledialog.askstring("Connection Cost", "Enter connection cost (default: 5):")
        try:
            cost = int(cost_str) if cost_str else 5
            cost = max(1, cost)  # Minimum cost of 1
        except ValueError:
            cost = 5
        
        # Add bidirectional connection
        if selected_node not in graph:
            graph[selected_node] = {}
        if target_node not in graph:
            graph[target_node] = {}
        
        graph[selected_node][target_node] = cost
        graph[target_node][selected_node] = cost
        
        update_connections()
        messagebox.showinfo("Connection Added", f"Added connection: {selected_node} <-> {target_node} (cost: {cost})")
    
    def remove_connection():
        selection = conn_listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a connection to remove.")
            return
        
        conn_text = conn_listbox.get(selection[0])
        # Parse connection text: "A -> B (cost: 5)"
        parts = conn_text.split(" -> ")
        if len(parts) != 2:
            return
        
        from_node = parts[0]
        to_node = parts[1].split(" (cost:")[0]
        
        # Remove bidirectional connection
        if from_node in graph and to_node in graph[from_node]:
            del graph[from_node][to_node]
        if to_node in graph and from_node in graph[to_node]:
            del graph[to_node][from_node]
        
        update_connections()
        messagebox.showinfo("Connection Removed", f"Removed connection: {from_node} <-> {to_node}")
    

    node_var.trace("w", lambda *args: update_connections())
    
    # Buttons
    button_frame = tk.Frame(conn_window)
    button_frame.pack(pady=20)
    
    tk.Button(button_frame, text="Add Connection", command=add_connection, bg="lightgray").pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Remove Connection", command=remove_connection, bg="lightgray").pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Close", command=conn_window.destroy).pack(side=tk.LEFT, padx=5)

# UI Layout
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

# Heuristic selection frame (only visible when A* is selected)
heuristic_frame = tk.LabelFrame(root, text="A* Heuristic Type", padx=5, pady=5, bg="lightblue")
heuristic_frame.place(x=600, y=10)

heuristic_var = tk.StringVar(value="distance")

distance_radio = tk.Radiobutton(
    heuristic_frame,
    text="Distance Only",
    variable=heuristic_var,
    value="distance",
    bg="lightblue"
)
distance_radio.pack(anchor=tk.W)

review_radio = tk.Radiobutton(
    heuristic_frame,
    text="Review-Based",
    variable=heuristic_var,
    value="review",
    bg="lightblue"
)
review_radio.pack(anchor=tk.W)

combined_radio = tk.Radiobutton(
    heuristic_frame,
    text="Distance + Reviews",
    variable=heuristic_var,
    value="combined",
    bg="lightblue"
)
combined_radio.pack(anchor=tk.W)

# Main control buttons
buttonFind = tk.Button(root, text="Find Path", command=show_path)
buttonFind.place(x=210, y=12)

buttonClear = tk.Button(root, text="Clear Path", command=lambda: toggle_clear())
buttonClear.place(x=280, y=12)

buttonInfo = tk.Button(root, text="Restaurant Info", command=lambda: show_restaurant_info(end_point) if end_point else messagebox.showwarning("No Selection", "Please select a destination first"))
buttonInfo.place(x=350, y=12)

# Node management buttons
node_mgmt_frame = tk.LabelFrame(root, text="Node Management", padx=5, pady=4, bg="lightgray")
node_mgmt_frame.place(x=640, y=470)

add_node_btn = tk.Button(node_mgmt_frame, text="Add Node", command=toggle_add_node_mode, bg="lightgray")
add_node_btn.pack(pady=2)

remove_node_btn = tk.Button(node_mgmt_frame, text="Remove Node", command=remove_custom_node, bg="lightgray")
remove_node_btn.pack(pady=2)

connections_btn = tk.Button(node_mgmt_frame, text="Manage Connections", command=manage_connections, bg="lightgray")
connections_btn.pack(pady=2)

def toggle_clear():
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