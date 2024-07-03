import pickle
import streamlit as st #building interactive web applications with Python UI
import requests #fetch data from external API

#fetch poster img using movie_id from movies API
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id) # fetch based on spesific moive id
    data = requests.get(url) #reterive info about that poster
    data = data.json() #convert to json
    poster_path = data['poster_path'] #takes only the img path from json file
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path #add the img path to this path
    return full_path


# recommend movies similer to the input, return both title and poster
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie detailes (id, poster , title)
        movie_id = movies.iloc[i[0]].movie_id #fetch movie id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


#header displied with text
st.header('Top 5 Movies Recommender!')
#loading files
movies = pickle.load(open('C:\\Users\\ghaid\\OneDrive\\سطح المكتب\\mmmmm\\pklfiles\\movie_list.pkl','rb'))
similarity = pickle.load(open('C:\\Users\\ghaid\\OneDrive\\سطح المكتب\\mmmmm\\pklfiles\\similarity.pkl','rb'))

#select bar to select moives on certain values
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or Select a Movie you Liked!",
    movie_list
)

# Button to trigger recommendations
if st.button('Show Recommendations'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
