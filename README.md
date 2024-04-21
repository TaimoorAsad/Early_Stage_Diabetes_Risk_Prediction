# Diabetes Prediction UI

This project provides a user interface (UI) for predicting diabetes risk based on a pre-trained machine learning model.

## Features

- Predicts diabetes risk based on user input.
- Utilizes a Logistic Regression model.
- Employs a graphical user interface (GUI) for user interaction.

## Dependencies

- Python 3.x
- tkinter
- pandas
- scikit-learn

## Instructions

1. Download the required libraries:

    pip install tkinter pandas scikit-learn


2. Download the diabetes dataset from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/529/early+stage+diabetes+risk+prediction+dataset).
3. Save the dataset as `data.csv` in the same directory as this code.
4. Run the script:



## User Interface

The UI presents text boxes and checkboxes corresponding to various diabetes risk factors. Users can enter their age and select symptoms like weight loss, excessive thirst, and others. Clicking the "Predict" button will display the predicted diabetes risk category based on the model's output.

## Disclaimer

This is a basic prediction tool and should not be used for medical diagnosis. Please consult a healthcare professional for any health concerns.

## Note

This code utilizes the `tkinter` library for the GUI, which is a built-in library in most Python installations.

## Further Improvements

- Enhance the UI design for better user experience.
- Implement user input validation for data types.
- Integrate the model training process within the application.
- Display additional information about the prediction or diabetes risk factors.

## Dataset Source

The diabetes dataset used in this project is from the [UCI Machine Learning Repository]([http](<https://archive.ics.uci.edu/dataset/529/early+stage+diabetes+risk+prediction+dataset).>)