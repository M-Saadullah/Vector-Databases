import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=1003e825d9c358eae97f6ffa62e578e6'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend_movies(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity_vector[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

st.title('Movie Recommender System')
movies = pickle.load(open('movies.pkl', 'rb'))
movies_title_list = movies['title'].values



similarity_vector = pickle.load(open('similarity_vector.pkl', 'rb'))
selected_movie_name = st.selectbox(
    'Enter a Movie name',
    movies_title_list
)



if st.button('Recommend'):
    names, posters = recommend_movies(selected_movie_name)

    columns = st.columns(5)

    for i, col in enumerate(columns):
        with col:
            st.image(posters[i])
            st.write(names[i])



