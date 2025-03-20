import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import Toplevel, Label
import time
from tkinter import *
from PIL import Image,ImageTk




# Splash screen design
w = Tk()
width_of_window = 430
height_of_window = 380
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width / 2) - (width_of_window / 2)
y_coordinate = (screen_height / 2) - (height_of_window / 2)
w.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))
w.overrideredirect(1)

Frame(w, width=width_of_window, height=height_of_window, bg='#272727').place(x=0, y=0)

label1 = Label(w, text='Virtual Real Estate Agent', fg='white', bg='#272727', font=("Game Of Squids", 20, "bold"))
label1.place(x=50, y=45)

# Use absolute path to load the image
import os
script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir, 'c1.png')
image_original = Image.open(image_path)
new_size = (image_original.width // 6, image_original.height // 6)
image_resized = image_original.resize(new_size)
image_a = ImageTk.PhotoImage(image_resized)

image_x_coordinate = (width_of_window // 2) - (image_a.width() // 2)

for i in range(5):  # Animation loop
    l1 = Label(w, image=image_a, border=0, relief=SUNKEN)
    l1.place(x=image_x_coordinate, y=85)
    w.update_idletasks()
    time.sleep(0.5)

    loading_label = Label(w, text='Loading...', fg='white', bg='#272727', font=("Arial", 12))
    loading_label.place(x=image_x_coordinate, y=250)
    w.update_idletasks()

w.destroy()


# Load the dataset
data = pd.read_csv('House Price India.csv')

# Check for missing values and handle them
data = data.ffill()

# Handle categorical data
data['mainroad'] = data['mainroad'].map({'yes': 1, 'no': 0})
data['guestroom'] = data['guestroom'].map({'yes': 1, 'no': 0})
data['basement'] = data['basement'].map({'yes': 1, 'no': 0})
data['hotwaterheating'] = data['hotwaterheating'].map({'yes': 1, 'no': 0})
data['airconditioning'] = data['airconditioning'].map({'yes': 1, 'no': 0})
data['prefarea'] = data['prefarea'].map({'yes': 1, 'no': 0})
data['furnishingstatus'] = data['furnishingstatus'].map({'furnished': 2, 'semi-furnished': 1, 'unfurnished': 0})

# Define features and target
X = data.drop('price', axis=1)
y = data['price']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the feature data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a Linear Regression model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Evaluate the model
y_pred = model.predict(X_test_scaled)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error on Test Set:", mse)

# Create the main application window
app = tk.Tk()
app.title("House Price Prediction")

# Make the window full screen
app.attributes('-fullscreen', True)

# Change background color
app.configure(bg='#272727')

# Function to switch frames
def show_frame(frame):
    frame.tkraise()

# Create frames for input parameters
frame_area = tk.Frame(app, bg='#272727')
frame_bed_bath = tk.Frame(app, bg='#272727')
frame_yes_no = tk.Frame(app, bg='#272727')
frame_other = tk.Frame(app, bg='#272727')

for frame in (frame_area, frame_bed_bath, frame_yes_no, frame_other):
    frame.grid(row=0, column=0, sticky='news')

from PIL import Image, ImageTk

# Load and resize the image using Pillow
image = Image.open('area.png')
resized_image = image.resize((700, 800))  # Adjust the width and height as needed
area_image = ImageTk.PhotoImage(resized_image)

# Display the resized image
image_label = tk.Label(frame_area, image=area_image, bg='#272727')
image_label.grid(row=0, column=5, rowspan=2, sticky='ns', padx=(700, 450))

# Frame for Area input
# Label for Area input
area_label = tk.Label(frame_area, text="Area (in sq ft):", fg="white", font=('Helvetica', 20), bg='#272727')
area_label.place(x=50, y=300)  # Adjust x and y as needed

# Entry for Area input
area_entry = tk.Entry(frame_area, font=('Helvetica', 20))
area_entry.place(x=250, y=300)  # Adjust x and y as needed

# Next button for Area frame
next_button_area = tk.Button(frame_area, text="Next", command=lambda: show_frame(frame_bed_bath), font=('Helvetica', 20))
next_button_area.place(x=300, y=500)  # Adjust x and y as needed

# Load and resize the image using Pillow
image1 = Image.open('bedroom.png')
resized_image1 = image1.resize((700, 900))  # Adjust the width and height as needed
area_image1 = ImageTk.PhotoImage(resized_image1)

# Display the resized image using x and y coordinates
image_label1 = tk.Label(frame_bed_bath, image=area_image1, bg='#272727')
image_label1.place(x=1, y=1)  # Adjust x and y as needed

# Frame for Bedrooms and Bathrooms input
tk.Label(frame_bed_bath, text="Bedrooms:", fg="white", font=('Helvetica', 20), bg='#272727').place(x=780, y=292)
bedrooms_entry = tk.Entry(frame_bed_bath, font=('Helvetica', 16))
bedrooms_entry.place(x=930, y=300)

tk.Label(frame_bed_bath, text="Bathrooms:", fg="white", font=('Helvetica', 20), bg='#272727').place(x=780, y=346)
bathrooms_entry = tk.Entry(frame_bed_bath, font=('Helvetica', 16))
bathrooms_entry.place(x=930, y=350)

# Next button for Bed & Bath frame
next_button_bed_bath = tk.Button(frame_bed_bath, text="Next", command=lambda: show_frame(frame_yes_no), font=('Helvetica', 20))
next_button_bed_bath.place(x=950, y=550)

image2 = Image.open('amen.jpeg')
resized_image2 = image2.resize((700, 700))  # Adjust the width and height as needed
area_image2 = ImageTk.PhotoImage(resized_image2)

# Display the resized image using x and y coordinates
image_label2 = tk.Label(frame_yes_no, image=area_image2, bg='#272727')
image_label2.place(x=600, y=1)  # Adjust x and y as needed
# Frame for Yes/No parameters input
tk.Label(frame_yes_no, text="Main Road (Yes/No):", fg="white", font=('Helvetica', 16), bg='#272727').place(x=50, y=100)
mainroad_entry = tk.Entry(frame_yes_no, font=('Helvetica', 16))
mainroad_entry.place(x=300, y=100)

tk.Label(frame_yes_no, text="Guestroom (Yes/No):", fg="white", font=('Helvetica', 16), bg='#272727').place(x=50, y=170)
guestroom_entry = tk.Entry(frame_yes_no, font=('Helvetica', 16))
guestroom_entry.place(x=300, y=170)

tk.Label(frame_yes_no, text="Basement (Yes/No):", fg="white", font=('Helvetica', 16), bg='#272727').place(x=50, y=240)
basement_entry = tk.Entry(frame_yes_no, font=('Helvetica', 16))
basement_entry.place(x=300, y=240)

tk.Label(frame_yes_no, text="Hot Water Heating (Yes/No):", fg="white", font=('Helvetica', 16), bg='#272727').place(x=20, y=310)
hotwaterheating_entry = tk.Entry(frame_yes_no, font=('Helvetica', 16))
hotwaterheating_entry.place(x=300, y=310)

tk.Label(frame_yes_no, text="Air Conditioning (Yes/No):", fg="white", font=('Helvetica', 16), bg='#272727').place(x=50, y=380)
airconditioning_entry = tk.Entry(frame_yes_no, font=('Helvetica', 16))
airconditioning_entry.place(x=300, y=380)

tk.Label(frame_yes_no, text="Preferred Area (Yes/No):", fg="white", font=('Helvetica', 16), bg='#272727').place(x=50, y=450)
prefarea_entry = tk.Entry(frame_yes_no, font=('Helvetica', 16))
prefarea_entry.place(x=300, y=450)

# Next button for Yes/No frame
next_button_yes_no = tk.Button(frame_yes_no, text="Next", command=lambda: show_frame(frame_other), font=('Helvetica', 20))
next_button_yes_no.place(x=250, y=605)
#other 
image3 = Image.open('park.png')
resized_image3 = image3.resize((900, 800))  # Adjust the width and height as needed
area_image3 = ImageTk.PhotoImage(resized_image3)

# Display the resized image using x and y coordinates
image_label3= tk.Label(frame_other, image=area_image3, bg='#272727')
image_label3.place(x=700, y=-10) 


def exit_application():
    app.destroy()
def start_again():
    area_entry.delete(0, tk.END)
    bedrooms_entry.delete(0, tk.END)
    bathrooms_entry.delete(0, tk.END)
    mainroad_entry.delete(0, tk.END)
    guestroom_entry.delete(0, tk.END)
    basement_entry.delete(0, tk.END)
    hotwaterheating_entry.delete(0, tk.END)
    airconditioning_entry.delete(0, tk.END)
    prefarea_entry.delete(0, tk.END)
    stories_entry.delete(0, tk.END)
    parking_entry.delete(0, tk.END)
    furnishing_status.current(0)
    pincode_entry.delete(0, tk.END)
    show_frame(frame_area)  # Reset to the first frame


# Stories label and entry
tk.Label(frame_other, text="Stories:", font=('Helvetica', 20), fg="white", bg='#272727').place(x=125, y=200)  # Increased font size
stories_entry = tk.Entry(frame_other, font=('Helvetica', 20))
stories_entry.place(x=225, y=200)  # Reduced x

# Parking label and entry
tk.Label(frame_other, text="Parking:", font=('Helvetica', 20), fg="white", bg='#272727').place(x=118, y=260)  # Increased font size
parking_entry = tk.Entry(frame_other, font=('Helvetica', 20))
parking_entry.place(x=225, y=260)  # Reduced x

# Dropdown for furnishing status
furnishing_status_label = tk.Label(frame_other, text="Furnishing Status:", fg="white", font=('Helvetica', 18), bg='#272727')  # Increased font size
furnishing_status_label.place(x=20, y=320)  # Reduced x

furnishing_status = ttk.Combobox(frame_other, font=('Helvetica', 20), state="readonly")  # Increased font size
furnishing_status['values'] = ("Semi-furnished", "Furnished", "Unfurnished")
furnishing_status.place(x=225, y=320)  # Reduced x
furnishing_status.current(0)

# Postal Code label and entry
tk.Label(frame_other, text="Postal Code:", font=('Helvetica', 20), fg="white", bg='#272727').place(x=60, y=380)  # Increased font size
pincode_entry = tk.Entry(frame_other, font=('Helvetica', 20))
pincode_entry.place(x=225, y=380)  # Reduced x
# Start Again button
start_again_button = tk.Button(frame_other, text="Start Again", command=start_again, font=('Helvetica', 20))
start_again_button.place(x=400, y=500)  # Adjust position as needed

# Exit butto2
exit_button = tk.Button(frame_other, text="Exit", command=exit_application, font=('Helvetica', 20))
exit_button.place(x=320, y=600)  # Adjust position as needed

# Predict price button
predict_button = tk.Button(frame_other, text="Predict Price", command=lambda: predict_price(), font=('Helvetica', 20))  # Increased font size
predict_button.place(x=200, y=500)








def predict_price():
    # Gather inputs from the entries
    area = float(area_entry.get())
    bedrooms = int(bedrooms_entry.get())
    bathrooms = int(bathrooms_entry.get())
    mainroad = 1 if mainroad_entry.get().strip().lower() == 'yes' else 0
    guestroom = 1 if guestroom_entry.get().strip().lower() == 'yes' else 0
    basement = 1 if basement_entry.get().strip().lower() == 'yes' else 0
    hotwaterheating = 1 if hotwaterheating_entry.get().strip().lower() == 'yes' else 0
    airconditioning = 1 if airconditioning_entry.get().strip().lower() == 'yes' else 0
    prefarea = 1 if prefarea_entry.get().strip().lower() == 'yes' else 0
    stories = int(stories_entry.get())
    parking = int(parking_entry.get())

    # Retrieve the value from the dropdown and map it
    furnishingstatus = {'Furnished': 2, 'Semi-furnished': 1, 'Unfurnished': 0}[furnishing_status.get()]

    # Process postal code
    pincode = pincode_entry.get().strip()

    # Postal code adjustment rates
    pincode_rate_adjustments = {
    '400001': 8.0,  # Mumbai Fort
    '400002': 4.20,  # Mumbai Dhobi Talao
    '400003': 5.18,  # Mumbai Kalbadevi
    '400004': 4.22,  # Mumbai Girgaon
    '400070': 5.7,
    '400612': 3.5,
    '400058': 6.9,
    '411001': 1.15,  # Pune Shivajinagar
    '411002': 1.10,  # Pune Ganeshkhind
    '440001': 1.12,  # Nagpur
    '431116': 1.05,
    '423701': 1.02,
    '431133': 1.08,
    '413207': 1.03,
    '431523': 1.07,
    '431517': 1.06,
    '414203': 1.04,
    '431518': 1.08,
    '431122': 1.06,
    '431126': 1.04,
    '431128': 1.07,
    '431127': 1.05,
    '431519': 1.09,
    '431143': 1.03,
    '414202': 1.04,
    '414208': 1.06,
    '431123': 1.05,
    '431142': 1.06,
    '431124': 1.07,
    '431131': 1.08,
    '431125': 1.07,
    '431515': 1.05,
    '431520': 1.09,
    '414204': 1.02,
    '413229': 1.04,
    '414205': 1.05,
    '413249': 1.06,
    '431129': 1.06,
    '431130': 1.07,
    '431530': 1.05,
    '431701': 1.06,
    '431705': 1.08,
    '431703': 1.06,
    '431513': 1.07,
    '431702': 1.05,
    '431117': 1.08,
    '431204': 1.07,
    '431212': 1.06,
    '431202': 1.04,
    '431150': 1.09,
    '431113': 1.06,
    '431114': 1.08,
    '431209': 1.05,
    '431206': 1.07,
    '431203': 1.04,
    '431213': 1.05,
    '431211': 1.06,
    '431118': 1.07,
    '431207': 1.05,
    '431132': 1.04,
    '431112': 1.07,
    '431135': 1.06,
    '431120': 1.05,
    '431208': 1.07,
    '431205': 1.06,
    '413515': 1.08,
    '413522': 1.04,
    '413520': 1.06,
    '413511': 1.05,
    '413513': 1.07,
    '413521': 1.09,
    '413532': 1.06,
    '413607': 1.07,
    '413516': 1.08,
    '413523': 1.05,
    '413527': 1.07,
    '413512': 1.05,
    '413510': 1.06,
    '413524': 1.04,
    '413521': 1.09,
    '413530': 1.07,
    '431522': 1.05,
    '413527': 1.08,
    '413544': 1.06,
    '413514': 1.07,
    '413531': 1.06,
    '413517': 1.05,
    '413518': 1.07,
    '413529': 1.09,
    '431704': 1.06,
    '431801': 1.07,
    '431710': 1.08,
    '431603': 1.07,
    '431717': 1.09,
    '431809': 1.05,
    '431712': 1.07,
    '431802': 1.05,
    '410206':1.10,
    '431604': 1.06,
    '431714': 1.07,
    '431804': 1.06,
    '431708': 1.07,
    '431721': 1.08,
    '431806': 1.07,
    '431815': 1.05,
    '431709': 1.07,
    '431601': 1.06,
    '431602': 1.05,
    '431606': 1.07,
    '431605': 1.05,
    '431512': 1.06,
    '431508': 1.07,
    '431521': 1.09,
    '431514': 1.06,
    '431509': 1.08,
    '431505': 1.07,
    '431402': 1.06,
    '431720': 1.05,
    '431401': 1.07,
    '431506': 1.05,
    '431537': 1.07,
    '431511': 1.05,
    '431541': 1.07,
    '431536': 1.06,
    '431503': 1.07,
    '431542': 1.08,
    '431516': 1.09,
    '431510': 1.05,
    '431540': 1.08,
    '442705': 1.06,
    '442703': 1.07,
    '442914': 1.08,
    '441208': 1.05,
    '442707': 1.06,
    '444917': 1.07,
    '442403': 1.06,
    '442901': 1.09,
    '442707': 1.06,
    '441226': 1.07,
    '442902': 1.06,
    '441206': 1.05,
    '442502': 1.07,
    '442603': 1.06,
    '442402': 1.05,
    '442501': 1.08,
    '442404': 1.07,
    '442908': 1.06,
    '442903': 1.09,
    '441207': 1.06,
    '442606': 1.07,
    '442704': 1.06,
    '442604': 1.08,
    '442505': 1.07,
    '442702': 1.06,
    '442507': 1.09,
    '442709': 1.06,
    '441209': 1.08,
    '442910': 1.05,
    '442406': 1.06,
    '441224': 1.07,
    '441205': 1.05,
    '442912': 1.08,
    '441223': 1.06,
    '442904': 1.07,
    '441215': 1.08,
    '442506': 1.07,
    '441212': 1.09,
    '442905': 1.06,
    '441225': 1.07,
    '442706': 1.08,
    '442906': 1.06,
    '442503': 1.08,
    '441222': 1.05,
    '442504': 1.06,
    '441217': 1.07,
    '442916': 1.06,
    '441227': 1.05,
    '442907': 1.07,
    '425101': 1.05,
    '425102': 1.06,
    '425115': 1.08,
    '425001': 1.06,
    '425003': 1.07,
    '425002': 1.08,
    '425116': 1.07,
    '425115': 1.06,
    '425103': 1.08,
    '425104': 1.07,
    '425420': 1.06,
    '425401': 1.08,
    '410208':1.05,
    '425402': 1.05,
    '425303': 1.07,
    '425108': 1.06,
    '425304': 1.08,
    '425201': 1.05,
    '425203': 1.06,
    '425310': 1.07,
    '410208': 1.10
}


    adjustment_rate = pincode_rate_adjustments.get(pincode, 1.0)

    # Create a DataFrame for the input
    input_data = pd.DataFrame([[area, bedrooms, bathrooms, mainroad, guestroom, basement, 
                                 hotwaterheating, airconditioning, prefarea, stories, 
                                 parking, furnishingstatus]], 
                               columns=X.columns)

    # Scale the input data
    input_scaled = scaler.transform(input_data)

    # Predict the price
    predicted_price = model.predict(input_scaled)[0]

    # Apply adjustment rate based on the postal code
    adjusted_price = predicted_price * adjustment_rate

  
    prediction_window = Toplevel()
    prediction_window.title("Predicted Price")
    prediction_window.geometry("400x300")

    # Center the window on the screen
    screen_width = prediction_window.winfo_screenwidth()
    screen_height = prediction_window.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (400 / 2))
    y_coordinate = int((screen_height / 2) - (300 / 2))
    prediction_window.geometry(f"400x300+{x_coordinate}+{y_coordinate}")

    prediction_window.configure(bg='#272727')

    # Add a title label
    title_label = Label(prediction_window, text="Predicted Price", font=('Helvetica', 24), fg="white", bg='#272727')
    title_label.pack(pady=20)

    # Display the adjusted price
    price_label = Label(prediction_window, text=f"The predicted price is: ₹{adjusted_price:.2f}", font=('Helvetica', 16), fg="white", bg='#272727')
    price_label.pack(pady=10)

    # Add a close button
    close_button = tk.Button(prediction_window, text="Close", command=prediction_window.destroy, font=('Helvetica', 16))
    close_button.pack(pady=20)



# Start the application by showing the first frame
show_frame(frame_area)
app.mainloop()
