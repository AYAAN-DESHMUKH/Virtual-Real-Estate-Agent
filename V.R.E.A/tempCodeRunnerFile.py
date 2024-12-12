import tkinter as tk
from tkinter import ttk

# Function to show the next frame
def show_frame(frame):
    frame.tkraise()

# Function to start the form sequence
def start_app():
    show_frame(area_frame)

# Function to submit each slide's data
def submit_area():
    user_data["area"] = area_scale.get()
    show_frame(bed_bath_frame)

def submit_bed_bath():
    user_data["bedrooms"] = bedrooms_scale.get()
    user_data["bathrooms"] = bathrooms_scale.get()
    show_frame(stories_frame)

def submit_stories():
    user_data["stories"] = stories_spinner.get()
    show_frame(mainroad_frame)

def submit_mainroad():
    user_data["mainroad"] = mainroad_var.get()
    user_data["guestroom"] = guestroom_var.get()
    user_data["basement"] = basement_var.get()
    user_data["hotwaterheating"] = hotwater_var.get()
    user_data["airconditioning"] = airconditioning_var.get()
    user_data["prefarea"] = prefarea_var.get()
    show_frame(parking_frame)

def submit_parking():
    user_data["parking"] = parking_scale.get()
    show_frame(furnish_frame)

def submit_furnish():
    user_data["furnishingstatus"] = furnish_var.get()
    # After all inputs are submitted, print the data
    print("User Data Submitted:", user_data)
    root.quit()  # Close the window after final submission

# Initialize main window
root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(bg="black")

# Dictionary to store user inputs
user_data = {}

# Create frames for each slide
welcome_frame = tk.Frame(root, bg="black")
area_frame = tk.Frame(root, bg="black")
bed_bath_frame = tk.Frame(root, bg="black")
stories_frame = tk.Frame(root, bg="black")
mainroad_frame = tk.Frame(root, bg="green")
parking_frame = tk.Frame(root, bg="black")
furnish_frame = tk.Frame(root, bg="black")

# Put all frames on the same stack
for frame in (welcome_frame, area_frame, bed_bath_frame, stories_frame, mainroad_frame, parking_frame, furnish_frame):
    frame.grid(row=0, column=1, sticky='nsew')

### Welcome Screen
welcome_label = tk.Label(welcome_frame, text="Virtual Real Estate Agent", font=("Helvetica", 36), fg="white", bg="black")
welcome_label.pack(pady=100)

start_btn = tk.Button(welcome_frame, text="Start", font=("Helvetica", 24), command=start_app, bg="white")
start_btn.pack(pady=50)

### Slide 1: Area
area_label = tk.Label(area_frame, text="Enter the area of your house (sqft):", font=("Helvetica", 24), fg="white", bg="black")
area_label.pack(pady=50)

area_scale = tk.Scale(area_frame, from_=100, to=10000, orient='horizontal', length=300, font=("Helvetica", 16), bg="black", fg="white")
area_scale.pack(pady=50)

area_submit_btn = tk.Button(area_frame, text="Submit", font=("Helvetica", 24), command=submit_area, bg="white")
area_submit_btn.pack(pady=50)

### Slide 2: Bedrooms and Bathrooms
bedrooms_label = tk.Label(bed_bath_frame, text="Enter number of bedrooms:", font=("Helvetica", 24), fg="white", bg="black")
bedrooms_label.pack(pady=50)

bedrooms_scale = tk.Scale(bed_bath_frame, from_=1, to=5, orient='horizontal', length=300, font=("Helvetica", 16), bg="black", fg="white")
bedrooms_scale.pack(pady=50)

bathrooms_label = tk.Label(bed_bath_frame, text="Enter number of bathrooms:", font=("Helvetica", 24), fg="white", bg="black")
bathrooms_label.pack(pady=50)

bathrooms_scale = tk.Scale(bed_bath_frame, from_=1, to=3, orient='horizontal', length=300, font=("Helvetica", 16), bg="black", fg="white")
bathrooms_scale.pack(pady=50)

bed_bath_submit_btn = tk.Button(bed_bath_frame, text="Submit", font=("Helvetica", 24), command=submit_bed_bath, bg="white")
bed_bath_submit_btn.pack(pady=50)

### Slide 3: Stories (Spinner)
stories_label = tk.Label(stories_frame, text="Enter number of stories:", font=("Helvetica", 24), fg="white", bg="black")
stories_label.pack(pady=50)

stories_spinner = ttk.Spinbox(stories_frame, from_=1, to=10, width=5, font=("Helvetica", 16))
stories_spinner.pack(pady=50)

stories_submit_btn = tk.Button(stories_frame, text="Submit", font=("Helvetica", 24), command=submit_stories, bg="white")
stories_submit_btn.pack(pady=50)

### Slide 4: Main Road, Guestroom, Basement, etc.
mainroad_var = tk.StringVar(value="No")
guestroom_var = tk.StringVar(value="No")
basement_var = tk.StringVar(value="No")
hotwater_var = tk.StringVar(value="No")
airconditioning_var = tk.StringVar(value="No")
prefarea_var = tk.StringVar(value="No")

# Adding canvas for scrollbar functionality
canvas = tk.Canvas(mainroad_frame, bg="black")
scrollbar = ttk.Scrollbar(mainroad_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="black")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Main road section
mainroad_label = tk.Label(scrollable_frame, text="Is your property on the main road?", font=("Helvetica", 24), fg="white", bg="black")
mainroad_label.pack(pady=10)
tk.Radiobutton(scrollable_frame, text="Yes", variable=mainroad_var, value="Yes", font=("Helvetica", 18), bg="black", fg="white").pack()
tk.Radiobutton(scrollable_frame, text="No", variable=mainroad_var, value="No", font=("Helvetica", 18), bg="black", fg="white").pack()

# Additional options (guestroom, basement, etc.)
options = [
    ("Does your property have a guest room?", guestroom_var),
    ("Does your property have a basement?", basement_var),
    ("Does your property have hot water heating?", hotwater_var),
    ("Does your property have air conditioning?", airconditioning_var),
    ("Is your property in a preferred area?", prefarea_var)
]

for label_text, var in options:
    label = tk.Label(scrollable_frame, text=label_text, font=("Helvetica", 24), fg="white", bg="black")
    label.pack(pady=10)
    tk.Radiobutton(scrollable_frame, text="Yes", variable=var, value="Yes", font=("Helvetica", 18), bg="black", fg="white").pack()
    tk.Radiobutton(scrollable_frame, text="No", variable=var, value="No", font=("Helvetica", 18), bg="black", fg="white").pack()

mainroad_submit_btn = tk.Button(scrollable_frame, text="Next", font=("Helvetica", 24), command=submit_mainroad, bg="white")
mainroad_submit_btn.pack(pady=50)

# Adding scrollbar to the frame
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

### Slide 5: Parking
parking_label = tk.Label(parking_frame, text="Enter number of parking spaces:", font=("Helvetica", 24), fg="white", bg="black")
parking_label.pack(pady=50)

parking_scale = tk.Scale(parking_frame, from_=0, to=3, orient='horizontal', length=300, font=("Helvetica", 16), bg="black", fg="white")
parking_scale.pack(pady=50)

parking_submit_btn = tk.Button(parking_frame, text="Submit", font=("Helvetica", 24), command=submit_parking, bg="white")
parking_submit_btn.pack(pady=50)

### Slide 6: Furnishing Status
furnish_var = tk.StringVar(value="furnished")

furnish_label = tk.Label(furnish_frame, text="Is your home furnished?", font=("Helvetica", 24), fg="white", bg="black")
furnish_label.pack(pady=50)

tk.Radiobutton(furnish_frame, text="Furnished", variable=furnish_var, value="furnished", font=("Helvetica", 18), bg="black", fg="white").pack(pady=10)
tk.Radiobutton(furnish_frame, text="Semi-furnished", variable=furnish_var, value="semi-furnished", font=("Helvetica", 18), bg="black", fg="white").pack(pady=10)
tk.Radiobutton(furnish_frame, text="Not furnished", variable=furnish_var, value="not-furnished", font=("Helvetica", 18), bg="black", fg="white").pack(pady=10)

furnish_submit_btn = tk.Button(furnish_frame, text="Submit", font=("Helvetica", 24), command=submit_furnish, bg="white")
furnish_submit_btn.pack(pady=50)

# Start by showing the welcome frame
show_frame(welcome_frame)

# Start the Tkinter event loop
root.mainloop()