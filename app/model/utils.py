import time
import joblib
import pandas as pd
from config import model_path,scaler_path





# Load the model
model = joblib.load(model_path)

# Load Scaler
scaler = joblib.load(scaler_path)


def get_bmi(weight, height):
    return weight / (height ** 2)


def get_risk_score(glucose,bmi,age):
    risk_score = (glucose*bmi) / age
    return risk_score

def get_bmi_category(bmi):
    if bmi < 18.5:
        return 0
    elif bmi < 25:
        return 1
    elif bmi < 30:
        return 2
    elif bmi > 30:
        return 3
    
def run_prediction(user_data):
    
   
    start = time.time()
    
     # Column order (same as used in training)
    column_order = ['age','gender','pulse_rate','systolic_bp','diastolic_bp'
                    ,'glucose','height','weight','bmi',
                    'family_diabetes','hypertensive',
                    'family_hypertension','cardiovascular_disease',
                    'stroke','BMI_Category','Risk_Score']
            
    

    # Example new input (list format, same order as training)
    data = pd.DataFrame([user_data], columns=column_order)

    # Scale the input using the loaded scaler
    data_scaled = scaler.transform(data)

    # Predict using the loaded model
    prediction = model.predict(data_scaled)

    print("Prediction:", "Diabetic" if prediction[0] == 1 else "Not Diabetic")  
    
    print("⏱️ Prediction took", round(time.time() - start, 3), "seconds")
    



