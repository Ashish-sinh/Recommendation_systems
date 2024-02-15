import streamlit as st 
from lang_chain_helper import name_and_menu_generator 

st.title('Resturant Name Generator Based On Cuisine')

cuisine = st.selectbox('select Cuisine' ,('Gujrati','Panjabi','South-Indian','Arebian','Chineese')) 

if cuisine : 
    output = name_and_menu_generator(cuisine) 
    resturant_name = output['resturant_name']
    menu = output['menu']

    st.header(resturant_name) 
    
    for name in menu : 
        st.write('•',name) 