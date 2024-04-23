import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = pd.read_csv("data.csv")

X = data.drop(columns=['class'])
y = data['class']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


model = LogisticRegression()
model.fit(X_train_scaled, y_train)


y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)


def predict():
    try:

        age_str = age_entry.get()
        if not age_str.isdigit():
            raise ValueError("Age must be an integer.")
        
        age = float(age_str)
        sudden_weight_loss = sudden_weight_loss_var.get()
        polyuria = polyuria_var.get()
        polydipsia = polydipsia_var.get()
        weakness = weakness_var.get()
        polyphagia = polyphagia_var.get()
        genital_thrush = genital_thrush_var.get()
        visual_blurring = visual_blurring_var.get()
        itching = itching_var.get()
        irritability = irritability_var.get()
        delayed_healing = delayed_healing_var.get()
        partial_paresis = partial_paresis_var.get()
        muscle_stiffness = muscle_stiffness_var.get()
        alopecia = alopecia_var.get()
        obesity = obesity_var.get()

        input_data = pd.DataFrame({
            'Age': [age],
            'Polyuria': [polyuria],
            'Polydipsia': [polydipsia],
            'sudden weight loss': [sudden_weight_loss],
            'weakness': [weakness],
            'Polyphagia': [polyphagia],
            'Genital thrush': [genital_thrush],
            'visual blurring': [visual_blurring],
            'Itching': [itching],
            'Irritability': [irritability],
            'delayed healing': [delayed_healing],
            'partial paresis': [partial_paresis],
            'muscle stiffness': [muscle_stiffness],
            'Alopecia': [alopecia],
            'Obesity': [obesity]
        })

        scaled_input = scaler.transform(input_data)

        prediction = model.predict(scaled_input)
        if(prediction[0] == 1):
            messagebox.showinfo("Prediction", "According to the predication you are diabetic")
        else:
            messagebox.showinfo("Prediction", "According to the predication you are not diabetic")
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")



root = tk.Tk()
root.title("Prediction UI")

tk.Label(root, text="Age:").grid(row=0, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=0, column=1)

tk.Label(root, text="Sudden Weight Loss:").grid(row=1, column=0)
sudden_weight_loss_var = tk.IntVar(root)
sudden_weight_loss_check = tk.Checkbutton(root, variable=sudden_weight_loss_var)
sudden_weight_loss_check.grid(row=1, column=1)

tk.Label(root, text="Polyuria:").grid(row=2, column=0)
polyuria_var = tk.IntVar(root)
polyuria_check = tk.Checkbutton(root, variable=polyuria_var)
polyuria_check.grid(row=2, column=1)

tk.Label(root, text="Polydipsia:").grid(row=3, column=0)
polydipsia_var = tk.IntVar(root)
polydipsia_check = tk.Checkbutton(root, variable=polydipsia_var)
polydipsia_check.grid(row=3, column=1)

tk.Label(root, text="Weakness:").grid(row=4, column=0)
weakness_var = tk.IntVar(root)
weakness_check = tk.Checkbutton(root, variable=weakness_var)
weakness_check.grid(row=4, column=1)

tk.Label(root, text="Polyphagia:").grid(row=5, column=0)
polyphagia_var = tk.IntVar(root)
polyphagia_check = tk.Checkbutton(root, variable=polyphagia_var)
polyphagia_check.grid(row=5, column=1)

tk.Label(root, text="Genital Thrush:").grid(row=6, column=0)
genital_thrush_var = tk.IntVar(root)
genital_thrush_check = tk.Checkbutton(root, variable=genital_thrush_var)
genital_thrush_check.grid(row=6, column=1)

tk.Label(root, text="Visual Blurring:").grid(row=7, column=0)
visual_blurring_var = tk.IntVar(root)
visual_blurring_check = tk.Checkbutton(root, variable=visual_blurring_var)
visual_blurring_check.grid(row=7, column=1)

tk.Label(root, text="Itching:").grid(row=8, column=0)
itching_var = tk.IntVar(root)
itching_check = tk.Checkbutton(root, variable=itching_var)
itching_check.grid(row=8, column=1)

tk.Label(root, text="Irritability:").grid(row=9, column=0)
irritability_var = tk.IntVar(root)
irritability_check = tk.Checkbutton(root, variable=irritability_var)
irritability_check.grid(row=9, column=1)

tk.Label(root, text="Delayed Healing:").grid(row=10, column=0)
delayed_healing_var = tk.IntVar(root)
delayed_healing_check = tk.Checkbutton(root, variable=delayed_healing_var)
delayed_healing_check.grid(row=10, column=1)

tk.Label(root, text="Partial Paresis:").grid(row=11, column=0)
partial_paresis_var = tk.IntVar(root)
partial_paresis_check = tk.Checkbutton(root, variable=partial_paresis_var)
partial_paresis_check.grid(row=11, column=1)

tk.Label(root, text="Muscle Stiffness:").grid(row=12, column=0)
muscle_stiffness_var = tk.IntVar(root)
muscle_stiffness_check = tk.Checkbutton(root, variable=muscle_stiffness_var)
muscle_stiffness_check.grid(row=12, column=1)

tk.Label(root, text="Alopecia:").grid(row=13, column=0)
alopecia_var = tk.IntVar(root)
alopecia_check = tk.Checkbutton(root, variable=alopecia_var)
alopecia_check.grid(row=13, column=1)

tk.Label(root, text="Obesity:").grid(row=14, column=0)
obesity_var = tk.IntVar(root)
obesity_check = tk.Checkbutton(root, variable=obesity_var)
obesity_check.grid(row=14, column=1)

predict_button = tk.Button(root, text="Predict", command=predict)
predict_button.grid(row=15, column=0, columnspan=2)

root.mainloop()