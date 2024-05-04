# MACHINE-LEARNING-BASED-VEHICLE-PERFORMANCE-ANALYZER


## 1. Introduction
The Vehicle Mileage Analyzer is a software application designed to predict the mileage of a vehicle in kilometers per liter (km/l) based on various vehicle parameters. It utilizes a linear regression model trained with features like engine size, horsepower, torque, and weight to estimate mileage. The application, built with Streamlit, offers an interactive user interface for users to input vehicle characteristics and receive real-time mileage predictions. Additionally, the application calculates the fuel efficiency required to travel 1 kilometer and provides an assessment of whether the predicted values are within expected thresholds.

## 2. Technology Stack
The following technologies are used to build the Vehicle Mileage Analyzer:
- **Python**: Primary programming language for data processing and model training.
- **Streamlit**: Framework for creating interactive web applications.
- **Scikit-Learn**: Library for machine learning, including linear regression and evaluation metrics.
- **Joblib**: Library for model serialization and deserialization.
- **Pandas**: Library for data manipulation and analysis.

## 3. Installation
To run the Vehicle Mileage Analyzer, ensure Python and required libraries are installed. You can install the necessary dependencies with the following command:

```bash
pip install streamlit pandas scikit-learn joblib
```

## 4. Data and Model Training
The data used to train the model consists of vehicle parameters like engine size, horsepower, torque, and weight, along with the target variable, mileage per liter. The data is split into training and testing sets, with a linear regression model trained on the training set to predict mileage. After training, the model is evaluated using metrics like mean squared error (MSE) and R2 score to gauge accuracy. Once validated, the trained model is saved for later use in the Streamlit application.

## 5. Streamlit Application
The Streamlit application provides an interactive user interface, allowing users to input vehicle parameters and get predictions for mileage per liter. It also calculates the fuel efficiency for 1 kilometer by taking the reciprocal of the predicted mileage. The application includes a sidebar for user input and a main section for displaying predictions and results.

### 5.1. User Input
The sidebar in the Streamlit app allows users to input vehicle characteristics like engine size, horsepower, torque, and weight. The user inputs are then used to predict mileage per liter using the trained model.

### 5.2. Prediction and Display
The application predicts mileage per liter based on the given parameters. It also calculates the fuel efficiency required to travel 1 kilometer. This information is displayed in a user-friendly format in the Streamlit app.

### 5.3. Performance Evaluation
The application evaluates whether the predicted mileage and fuel efficiency are good or bad based on defined thresholds. If the mileage and fuel efficiency meet or exceed the thresholds, they are considered "good"; otherwise, they are "bad." This provides feedback on whether the vehicle's configuration is efficient.

### 5.4. Running the Streamlit App
To run the Streamlit application, use the following command in your terminal:

```bash
streamlit run app.py
```

Replace `app.py` with the name of your Streamlit script. This command will launch the Streamlit application in a browser window where you can interact with the user interface and test the predictions.

## 6. Customizations
To improve the user experience, the Streamlit application uses custom CSS to hide the default Streamlit header and footer, providing a clean and focused interface.

## 7. Conclusion
The Vehicle Mileage Analyzer is an interactive tool for predicting vehicle mileage and assessing fuel efficiency based on linear regression. It offers real-time predictions and evaluates whether the predicted values meet expected thresholds. This documentation covers the technology stack, model training, Streamlit application, and steps to run the application, providing a comprehensive guide for developers and users.
