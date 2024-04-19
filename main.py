import streamlit as st

st.title("Welcome to Streamlit page : ") 

# how you crete the website and live it 


name = st.text_input("Enter your name ") 
f_name = st.text_input("Enter your father name ") 
addres= st.text_area("Enter you full adress") 
class_data= st.selectbox("Enter your class :" , (1,2,3,4,5,6,7,8,9))


button = st.button("Done") 
if button :
    st.markdown(f""" name :{name} \n 
                    father_name : {f_name} \n 
                    address : {addres} \n 
                    Class: {class_data}""" )











## make the form by using stremlit :

# name = st.text_input("Enter your name ") 
# f_name = st.text_input("Enter your father name ") 
# addres= st.text_area("Enter you full adress") 
# class_data= st.selectbox("Enter your class :" , (1,2,3,4,5,6,7,8,9))


# button = st.button("Done") 
# if button :
#     st.markdown(f""" name :{name} \n 
#                     father_name : {f_name} \n 
#                     address : {addres} \n 
#                     Class: {class_data}""" )



# --- 


## add csv file or excel shit also 

# import pandas as pd 

# dataset = pd.read_csv("E:\\Python\\stremlit\\nba.csv")

# st.dataframe(dataset)


# Random code 

# st.code('''for i in range(1,30,1):
#                 print(hi)''')


# st.title("Welcome to Streamlit page  hi everyone from first page ") 
# st.header("Python") 
# st.subheader("Datascience") 
# st.markdown("Welcome to ML , DL , AI.... ")
