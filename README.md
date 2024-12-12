# Virtual Real Estate Agent

## Overview
The Virtual Real Estate Agent is a Python-based application that predicts the price of a flat using basic parameters such as the number of bedrooms, bathrooms, stories, and additional features like parking, air conditioning, and furnishing status. The project leverages **Linear Regression** for predictive analysis and provides a user-friendly interface to estimate property prices.

---

## Key Features
- Predicts flat prices based on user-provided parameters.
- Considers multiple features including:
  - Number of bedrooms and bathrooms.
  - Total area of the flat.
  - Amenities like parking, air conditioning, and guestroom availability.
  - Location advantages such as proximity to the main road and preferred areas.
- Implements **Linear Regression** to create an accurate prediction model.

---

## Dataset
The model uses a structured dataset containing the following columns:
- **price**: Price of the flat (target variable).
- **area**: Total area of the flat in square feet.
- **bedrooms**: Number of bedrooms.
- **bathrooms**: Number of bathrooms.
- **stories**: Number of stories the flat has.
- **mainroad**: Whether the flat is near the main road (yes/no).
- **guestroom**: Availability of a guestroom (yes/no).
- **basement**: Whether the flat has a basement (yes/no).
- **hotwaterheating**: Presence of hot water heating (yes/no).
- **airconditioning**: Availability of air conditioning (yes/no).
- **parking**: Number of parking spaces.
- **prefarea**: If the flat is in a preferred area (yes/no).
- **furnishingstatus**: Furnishing status of the flat (furnished/semi-furnished/unfurnished).

---

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd virtual-real-estate-agent
   ```
3. Install required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage
1. Run the application:
   ```bash
   python main.py
   ```
2. Input the required parameters (e.g., number of bedrooms, bathrooms, area, etc.).
3. View the predicted price of the flat.

---

## Dependencies
- Python 3.x
- Libraries:
  - pandas
  - numpy
  - scikit-learn
  - matplotlib (optional, for visualization)

---

## How It Works
1. **Data Preprocessing**:
   - Encodes categorical variables.
   - Normalizes numerical features.
2. **Model Training**:
   - Fits a Linear Regression model using the dataset.
3. **Prediction**:
   - Accepts user input for parameters.
   - Uses the trained model to predict the flat's price.

---

## Future Enhancements
- Add support for additional machine learning algorithms like Decision Trees or Random Forests.
- Include more features such as neighborhood crime rates, nearby facilities, and public transportation access.
- Develop a web-based or mobile interface for better accessibility.

---

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your improvements or suggestions.

---

## License
This project is licensed under the MIT License.

---

## Acknowledgments
Special thanks to the open-source community and datasets available on **Kaggle** for enabling this project.

