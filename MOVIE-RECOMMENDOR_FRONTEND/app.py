import streamlit as st
import pandas as pd
import pickle
#to hit on an api we need an libarary called as requests
import requests



import os

# Get the directory where app.py is located
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "movies_dict.pkl")

with open(file_path, "rb") as f:

#ffor the similarity matrix
#opening the file 
with open("similarity.pkl","rb") as f:
    similarity=pickle.load(f)


#this is basically ghuma ke kaan pakda because the other way i was  getting an error 
#remeber that we will use / this for the writting of paths in the code and \ this  in the terminal 
#makign a dataframe back
movies=pd.DataFrame(movies_list)


#making a heading for our streamlit app
st.title("Movie Recommendor System")

#dropdown for the movies
selected_movie =st.selectbox("Select The movie",movies["title"].values)

# a button for selectoing the movie
#FUNCTION FOR FETCHING THE MOVOE
def fecth_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=52334d1951a349eba03ca79f42713e0c&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data["poster_path"]
#making the recommneder functionn
def recommend(movie):
    movie_index=movies[movies["title"]==movie].index[0]
    distance=similarity[movie_index]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies_poster=[]
    recommended_movies=[]
    for i in movies_list:
        
        movie_id=movies.iloc[i[0]].movie_id
        #so our task is to fetch the poster and the poster will be fetched from where
        
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fecth_poster(movie_id))
    return recommended_movies,recommended_movies_poster

if st.button("Recommend"):
 
    names,poster=recommend(selected_movie)
    
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])

#now we just want the poster of the movie
#i.e is basically doen with the help of id of movie 

#now our recommendation sytstem is complteed by we will devleoped it in herouku