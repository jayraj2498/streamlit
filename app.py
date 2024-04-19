# ## we crate stremlit app to hold front end  ML proj 


# import numpy as np
# import pickle
# import pandas as pd

# import streamlit as st 

# from PIL import Image



# pickle_in = open("classifier.pkl","rb")
# classifier=pickle.load(pickle_in)


# def welcome():
#     return "Welcome All"


# def predict_note_authentication(variance,skewness,curtosis,entropy):
    
#     """Let's Authenticate the Banks Note 
#     This is using docstrings for specifications.
#     ---
#     parameters:  
#       - name: variance
#         in: query
#         type: number
#         required: true
#       - name: skewness
#         in: query
#         type: number
#         required: true
#       - name: curtosis
#         in: query
#         type: number
#         required: true
#       - name: entropy
#         in: query
#         type: number
#         required: true
#     responses:
#         200:
#             description: The output values
        
#     """
   
#     prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
#     print(prediction)
#     return prediction



# def main():
#     st.title("Bank Authenticator Project stremlit ")
#     html_temp = """
#     <div style="background-color:tomato;padding:10px">
#     <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
#     </div>
#     """
#     st.markdown(html_temp,unsafe_allow_html=True)
#     variance = st.text_input("Variance")
#     skewness = st.text_input("skewness")
#     curtosis = st.text_input("curtosis")
#     entropy = st.text_input("entropy")
#     result=""
    
   
#     if st.button("Predict"):
#         prediction = predict_note_authentication(variance, skewness, curtosis, entropy)
#         if prediction == 1:
#             result = " genuine ..(Authentic)"
#         else:
#             result = "fake ..(Fraudulent)"      
#     st.success(f'The banknote is {result}')    
                      
#     if st.button("About"):
#         st.text("it's a machine learning application built with Streamlit that predicts whether \n a banknote is authentic or not based on its input.")
        

# if __name__ == '__main__':
#     main()
    
    
    
    
    
    
    
    
    
    
import numpy as np
import pickle
import streamlit as st

# Function to load the classifier model
def load_model():
    try:
        with open("classifier.pkl", "rb") as file:
            model = pickle.load(file)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Function to predict banknote authenticity
def predict_note_authentication(model, variance, skewness, curtosis, entropy):
    try:
        prediction = model.predict([[variance, skewness, curtosis, entropy]])
        return prediction
    except Exception as e:
        st.error(f"Error predicting authenticity: {e}")
        return None

def main():
    # Load the classifier model
    model = load_model()
    if model is None:
        return

    # Set up the Streamlit app UI
    st.title("Banknote Authenticator Project with Streamlit")
    html_temp = """
    <div style="background-color: tomato; padding: 10px;">
        <h2 style="color: white; text-align: center;">Streamlit Banknote Authenticator ML App</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Input fields for banknote features
    variance = st.text_input("Variance")
    skewness = st.text_input("Skewness")
    curtosis = st.text_input("Curtosis")
    entropy = st.text_input("Entropy")

    # Predict button
    if st.button("Predict"):
        prediction = predict_note_authentication(model, variance, skewness, curtosis, entropy)
        if prediction is not None:
            result = "Authentic" if prediction[0] == 1 else "Fraudulent"
            st.success(f"The banknote is {result}")

    # About section
    if st.button("About"):
        st.text("This is a machine learning application built with Streamlit.")
        st.text("It predicts the authenticity of banknotes based on their features.")

if __name__ == '__main__':
    main()
    