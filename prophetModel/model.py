import math
import pickle
from datetime import datetime
import pandas as pd
import os

TEA_TYPES = ['Ceylon Black', 'Green Tea', 'Herbal Tea']


def find_model(user_tea_type):
    filename = f"model_{user_tea_type.replace(' ', '_')}.pkl"
    file_path = os.path.join(os.path.dirname(__file__), "..", "models", filename)
    file_path = os.path.abspath(file_path)
    with open(file_path, 'rb') as f:
        model = pickle.load(f)
    return model


def model(user_tea_type, picked_date):
    if user_tea_type not in TEA_TYPES:
        print("Enter correct tea type")
        return

    picked_model = find_model(user_tea_type)

    if picked_date.strip() == "":
        date = datetime.now().date()
    else:
        date = pd.to_datetime(picked_date).date()

    future = pd.DataFrame({"ds": [date]})
    forecast = picked_model.predict(future)
    predicted_price = forecast['yhat'].values[0]

    return math.floor(predicted_price)


# if __name__ == "__main__":
#     input_tea_type = input("Enter type of tea : ")
#     input_date = input("Enter date you want to predict if not you will get today date price:")
#
#     model(input_tea_type, input_date)
