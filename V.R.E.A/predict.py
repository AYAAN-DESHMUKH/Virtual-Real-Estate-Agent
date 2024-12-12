import tkinter as tk
from tkinter import ttk  # Import ttk for the combo box
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

class HousePricePredictor(tk.Tk):
    def __init__(self):
        super().__init__()

        # Fullscreen setup
        self.attributes('-fullscreen', True)
        self.bind("<Escape>", lambda e: self.quit())

        # Load the dataset and train the model
        self.data = pd.read_csv('House Price India.csv')
        self.preprocess_data()
        self.train_model()

        # Create the main frame
        self.frames = {}
        self.create_frames()
        self.create_widgets()

    def preprocess_data(self):
        self.data = self.data.ffill()
        # Mapping categorical data
        self.data['mainroad'] = self.data['mainroad'].map({'yes': 1, 'no': 0})
        self.data['guestroom'] = self.data['guestroom'].map({'yes': 1, 'no': 0})
        self.data['basement'] = self.data['basement'].map({'yes': 1, 'no': 0})
        self.data['hotwaterheating'] = self.data['hotwaterheating'].map({'yes': 1, 'no': 0})
        self.data['airconditioning'] = self.data['airconditioning'].map({'yes': 1, 'no': 0})
        self.data['prefarea'] = self.data['prefarea'].map({'yes': 1, 'no': 0})
        self.data['furnishingstatus'] = self.data['furnishingstatus'].map({'furnished': 2, 'semi-furnished': 1, 'unfurnished': 0})

        self.X = self.data.drop('price', axis=1)
        self.y = self.data['price']

        # Split data
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

        # Scale data
        self.scaler = StandardScaler()
        self.X_train_scaled = self.scaler.fit_transform(self.X_train)

    def train_model(self):
        self.model = LinearRegression()
        self.model.fit(self.X_train_scaled, self.y_train)
        print("Model training completed.")

    def create_frames(self):
        parameters = ['Area', 'Bedrooms', 'Bathrooms', 'Stories', 
                      'Main Road (yes/no)', 'Guest Room (yes/no)', 
                      'Basement (yes/no)', 'Hot Water Heating (yes/no)', 
                      'Air Conditioning (yes/no)', 'Parking', 
                      'Preferred Area (yes/no)', 'Furnishing Status']
        
        for param in parameters:
            frame = tk.Frame(self)
            frame.pack(pady=10)
            self.frames[param] = frame

    def create_widgets(self):
        self.entries = {}
        # Create labels and entry fields for each parameter
        labels = ['Area', 'Bedrooms', 'Bathrooms', 'Stories', 
                  'Main Road (yes/no)', 'Guest Room (yes/no)', 
                  'Basement (yes/no)', 'Hot Water Heating (yes/no)', 
                  'Air Conditioning (yes/no)', 'Parking', 
                  'Preferred Area (yes/no)']
        
        for label in labels:
            tk.Label(self.frames[label], text=label, font=("Arial", 20)).pack(side=tk.LEFT)
            entry = tk.Entry(self.frames[label], font=("Arial", 20))
            entry.pack(side=tk.RIGHT)
            self.entries[label] = entry

        # Create a combo box for Furnishing Status
        tk.Label(self.frames['Furnishing Status'], text='Furnishing Status', font=("Arial", 20)).pack(side=tk.LEFT)
        furnishing_options = ['furnished', 'semi-furnished', 'unfurnished']
        self.entries['Furnishing Status'] = ttk.Combobox(self.frames['Furnishing Status'], 
                                                          values=furnishing_options, 
                                                          font=("Arial", 20))
        self.entries['Furnishing Status'].pack(side=tk.RIGHT)
        self.entries['Furnishing Status'].current(0)  # Set default selection

        # Create button to predict price
        self.predict_button = tk.Button(self, text="Predict Price", command=self.predict_price, font=("Arial", 20))
        self.predict_button.pack(pady=20)

        # Create label to display the result
        self.result_label = tk.Label(self, text="", font=("Arial", 20))
        self.result_label.pack(pady=20)

    def predict_price(self):
        try:
            # Get values from the entries
            input_data = {}
            input_data['area'] = float(self.entries['Area'].get())
            input_data['bedrooms'] = int(self.entries['Bedrooms'].get())
            input_data['bathrooms'] = int(self.entries['Bathrooms'].get())
            input_data['stories'] = int(self.entries['Stories'].get())
            input_data['mainroad'] = int(self.entries['Main Road (yes/no)'].get())
            input_data['guestroom'] = int(self.entries['Guest Room (yes/no)'].get())
            input_data['basement'] = int(self.entries['Basement (yes/no)'].get())
            input_data['hotwaterheating'] = int(self.entries['Hot Water Heating (yes/no)'].get())
            input_data['airconditioning'] = int(self.entries['Air Conditioning (yes/no)'].get())
            input_data['parking'] = int(self.entries['Parking'].get())
            input_data['prefarea'] = int(self.entries['Preferred Area (yes/no)'].get())
            
            # Convert furnishing status to numerical value
            furnishing_status = self.entries['Furnishing Status'].get()
            input_data['furnishingstatus'] = {'furnished': 2, 'semi-furnished': 1, 'unfurnished': 0}[furnishing_status]

            # Convert input data to DataFrame
            input_df = pd.DataFrame([input_data])
            input_scaled = self.scaler.transform(input_df)

            # Predict price
            predicted_price = self.model.predict(input_scaled)[0]
            
            # Display the predicted price
            self.result_label.config(text=f"Predicted Price: ₹{predicted_price:.2f}")

        except ValueError as e:
            self.result_label.config(text="Invalid input. Please enter correct values.")
            print("Error:", e)  # Print the error to the console for debugging
        except Exception as e:
            self.result_label.config(text="An error occurred during prediction.")
            print("Error:", e)  # Print the error to the console for debugging

if __name__ == "__main__":
    app = HousePricePredictor()
    app.mainloop()
