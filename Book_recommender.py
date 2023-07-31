import streamlit as st 
import pickle 
import pandas as pd 
import numpy as np 



book = pickle.load(open('book_df.pkl','rb')) 
similarity_fector = pickle.load(open('sim_fec_book.pkl','rb'))

st.title('Book Recommendation System')

book_name = st.selectbox('Select Book',book['Book-Title'].values)

def recommendation(book_name):
    suggested_book_index= [] 
    book_index = book[book['Book-Title'] == book_name].index[0]
    similer_book_index = sorted(enumerate(similarity_fector[book_index]),reverse= True,key = lambda x:x[1])[1:6]
    
    for i in similer_book_index : 
        suggested_book_index.append(i[0])
    return suggested_book_index


def poster(index): 
    poster_url = [] 
    book_name = []
    for i in index: 
        poster_url.append( book['Image-URL-M'][i])
        book_name.append(book['Book-Title'][i])
    return pd.Series(poster_url , index = book_name)

book_indexs = recommendation(book_name) 

col_1,col_2,col_3,col_4,col_5 = st.columns(5)  

if st.button('Suggest Book For Me'):
    img_detail = poster(book_indexs)

    
    for col_index ,(name , img) in (zip([col_1,col_2,col_3,col_4,col_5],img_detail.items())) :
        with col_index : 
            st.image(img,caption=name) 