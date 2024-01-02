import tkinter as tk
from tkinter import ttk
import math

# Function definitions for calculations
def calculate_2d_slope(x1, y1, x2, y2):
    try:
        return (y2 - y1) / (x2 - x1)
    except ZeroDivisionError:
        return float('inf')  # Infinite slope for vertical lines

def calculate_midpoint(x1, y1, x2, y2, is_3d=False, z1=0, z2=0):
    if is_3d:
        return ((x1 + x2) / 2, (y1 + y2) / 2, (z1 + z2) / 2)
    else:
        return ((x1 + x2) / 2, (y1 + y2) / 2)

def calculate_length(x1, y1, x2, y2, is_3d=False, z1=0, z2=0):
    if is_3d:
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    else:
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_other_endpoint(x1, y1, xm, ym, is_3d=False, z1=0, zm=0):
    if is_3d:
        return (2*xm - x1, 2*ym - y1, 2*zm - z1)
    else:
        return (2*xm - x1, 2*ym - y1)

# GUI Function to handle calculations and display results based on user inputs
def calculate_and_display():
    # Retrieve user inputs and perform calculations
    # Display results in the GUI
    # This part of the code needs to be completed with logic to retrieve inputs and display outputs

# Create the main window
root = tk.Tk()
root.title("Geometrical Line Segment Calculator")

# Create frames for input fields, output display, and action buttons
input_frame = ttk.Frame(root, padding="10")
input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))
output_frame = ttk.Frame(root, padding="10")
output_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))
action_frame = ttk.Frame(root, padding="10")
action_frame.grid(row=2, column=0, sticky=tk.E)

# Add input fields, labels, and buttons
# Example: Dimension selection, endpoint inputs, midpoint input, etc.
# This part of the code needs to be completed with GUI elements for input
# import tkinter as tk
# from tkinter import ttk
# import math

# ... [Include the calculation functions here, as previously defined] ...

# Function to update input fields based on dimension selection
def update_input_fields(event):
    dimension = dimension_var.get()
    if dimension == '2D':
        z1_entry.grid_remove()
        z2_entry.grid_remove()
        zm_entry.grid_remove()
    elif dimension == '3D':
        z1_entry.grid()
        z2_entry.grid()
        zm_entry.grid()

# Function to handle calculations and display results
def calculate_and_display():
    try:
        x1, y1 = float(x1_entry.get()), float(y1_entry.get())
        xm, ym = float(xm_entry.get()), float(ym_entry.get())
        is_3d = dimension_var.get() == '3D'
        z1 = float(z1_entry.get()) if is_3d else 0
        zm = float(zm_entry.get()) if is_3d else 0
        # Perform calculations
        if is_3d:
            x2, y2, z2 = calculate_other_endpoint(x1, y1, xm, ym, True, z1, zm)
        else:
            x2, y2 = calculate_other_endpoint(x1, y1, xm, ym)
            slope = calculate_2d_slope(x1, y1, x2, y2)
            output_text.set(f"Slope: {slope}")
        midpoint = calculate_midpoint(x1, y1, x2, y2, is_3d, z1, z2)
        length = calculate_length(x1, y1, x2, y2, is_3d, z1, z2)
        # Update output fields
        output_text.set(f"Other Endpoint: ({x2}, {y2}{', ' + str(z2) if is_3d else ''})\n"
                        f"Midpoint: {midpoint}\n"
                        f"Length: {length}")
    except ValueError:
        output_text.set("Invalid input. Please enter numeric values.")

# Create the main window
root = tk.Tk()
root.title("Geometrical Line Segment Calculator")

# Create frames for input fields, output display, and action buttons
input_frame = ttk.Frame(root, padding="10")
input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))
output_frame = ttk.Frame(root, padding="10")
output_frame.grid(row=2, column=0, sticky=(tk.W, tk.E))
action_frame = ttk.Frame(root, padding="10")
action_frame.grid(row=3, column=0, sticky=tk.E)

# Dimension selection
dimension_label = ttk.Label(input_frame, text="Select Dimension (2D/3D):")
dimension_label.grid(row=0, column=0, sticky=tk.W)
dimension_var = tk.StringVar()
dimension_combobox = ttk.Combobox(input_frame, textvariable=dimension_var, values=('2D', '3D'))
dimension_combobox.grid(row=0, column=1, sticky=(tk.W, tk.E))
dimension_combobox.bind('<<ComboboxSelected>>', update_input_fields)

# Endpoint and midpoint inputs
x1_label = ttk.Label(input_frame, text="x1:")
x1_label.grid(row=1, column=0, sticky=tk.W)
x1_entry = ttk.Entry(input_frame)
x1_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

y1_label = ttk.Label(input_frame, text="y1:")
y1_label.grid(row=2, column=0, sticky=tk.W)
y1_entry = ttk.Entry(input_frame)
y1_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

xm_label = ttk.Label(input_frame, text="xm:")
xm_label.grid(row=3, column=0, sticky=tk.W)
xm_entry = ttk.Entry(input_frame)
xm_entry.grid(row=3, column=1, sticky=(tk.W, tk.E))

ym_label = ttk.Label(input_frame, text="ym:")
ym_label.grid(row=4, column=0, sticky

# Run the application
root.mainloop()

