import pandas as pd
import pickle
import streamlit as st
import warnings
warnings.filterwarnings('ignore')

#load dataset

data=pickle.load(open("movies_dict.pkl",mode="rb"))
data=pd.DataFrame(data)
#print(movies)

distance=pickle.load(open("distance_dict.pkl",mode="rb"))
#print(distance)

def recommend(movie):               #Recommend movies based on the input movie
    
    recommended_movies=[]
    
    movie_index=data[data["title"]==movie].index[0]
    movie_list=sorted(list(enumerate(distance[movie_index])),reverse=True,key=lambda x:x[1])[1:8]
    
    for i in movie_list:
        recommended_movies.append(data.iloc[i[0]]["title"])  # Print the recommended movie titles

    return recommended_movies

#print(recommend("Avatar"))

#streamlit web-app

st.title("Movie Recommendation System")

st.write("This is a simple movie recommendation system that recommends movies based on the input movie.")
selected_movie=st.selectbox("Search for movie",data["title"].values)
btn=st.button("Recommend")

if btn:
    recommended_movies=recommend(selected_movie)
    
    for movie in recommended_movies:
        st.write(movie)

