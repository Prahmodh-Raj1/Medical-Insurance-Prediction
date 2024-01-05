
import numpy as np
import pickle
import streamlit as st
loaded_model = pickle.load(open('C:/Users/prahm/Downloads/trained_model.sav','rb'))

def convert_input_data(input_data):
    # Convert Sex
    input_data[1] = 1 if input_data[1].lower() == 'male' else 0
    
    # Convert Smoker
    input_data[4] = 1 if input_data[4].lower() == 'yes' else 0
    
    # Convert Region
    region_mapping = {'southeast': 0, 'southwest': 1, 'northeast': 2, 'northwest': 3}
    input_data[5] = region_mapping.get(input_data[5].lower(), -1)
    
    
    return input_data

def insurance_prediction(input_data):
    # Assuming loaded_model is already defined
    input_data = np.array(input_data).reshape(1, -1)
    prediction = loaded_model.predict(input_data)
    print("Prediction: ", prediction)
    result = "Your Insurance cost is " + str(prediction[0])
    return result

def main():
    st.title("Medical Insurance Prediction WebApp")
    
    # Getting the input data
    Age = st.text_input('Age of Person')
    Sex = st.text_input("Sex of Person")
    Bmi = st.text_input("BMI of the person")
    Children = st.text_input("No. of Children")
    Smoker = st.text_input("Is the person a Smoker")
    Region = st.text_input("Region of the person")	
    
    # Convert input data to integers
    converted_input_data = convert_input_data([Age, Sex, Bmi, Children, Smoker, Region])
    
    # Prediction
    prediction_result = ''
    
    # Creating a button
    if st.button('Insurance Prediction result'):
        prediction_result = insurance_prediction(converted_input_data)
        
    st.success(prediction_result)

if __name__ == "__main__":
    main()
    