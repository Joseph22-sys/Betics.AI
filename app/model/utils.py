import joblib

def get_bmi(weight, height):
    return weight / ((height / 100) ** 2)


def get_risk_score(glucose,bmi,age):
    risk_score = (glucose*bmi) / age
    return risk_score.floordiv(1)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return 0
    elif bmi < 25:
        return 1
    elif bmi < 30:
        return 2
    elif bmi > 30:
        return 3
    
def run 
