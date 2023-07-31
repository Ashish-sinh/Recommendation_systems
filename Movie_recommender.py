#import streamlit lib :

import streamlit as st 
import pandas as pd 

# make title of movie :
st.title('Movie Recommeder System')
import pickle  


# load data from the pickle file : 
similarity_fector = pickle.load(open('sf.pkl','rb')) 
df = pickle.load(open('df.pkl','rb'))
img_id = df['imdbId'].values


# design according to you 
def recomendation ( movie_name ):
    movie_index = df[df['title'] == movie_name].index[0] 
    similer_movie_index = sorted(enumerate(similarity_fector[movie_index]),reverse=True, key = lambda x : x[1])[1:6]
    movie_list = [] 
    
    for i in similer_movie_index : 
        movie_list.append(df.iloc[i[0],1])
    return movie_list


Selected_Movie = st.selectbox('Select Movie',df['title'].values)

if st.button('Suggest Movie') :
    for i in recomendation(Selected_Movie):
        st.write(i)
        