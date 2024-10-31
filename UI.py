import pandas as pd  # Importing pandas for data manipulation
import pickle  # Importing pickle for serializing and deserializing objects
import streamlit as st  # Importing Streamlit for building the web app
import warnings  # Importing warnings to manage warning messages
import numpy as np  # Importing numpy for numerical operations

warnings.filterwarnings('ignore')  # Ignoring warning messages

# Load dataset
data = pickle.load(open("movies_dict.pkl", mode="rb"))
data = pd.DataFrame(data)  # Converting the loaded data to a DataFrame

# Load the precomputed distances from two files
distance_part1 = pickle.load(open("distance_part1.pkl", mode="rb"))
distance_part2 = pickle.load(open("distance_part2.pkl", mode="rb"))

# Combine the parts back into the full distance matrix
distance = np.vstack((distance_part1, distance_part2))

def recommend(movie):
    """
    Recommend movies based on the input movie
    Args:
    movie (str): The title of the movie to base the recommendations on

    Returns:
    list: List of recommended movie titles
    """
    recommended_movies = []  # List to store recommended movie titles
    movie_index = data[data["title"] == movie].index[0]  # Get the index of the input movie
    movie_list = sorted(list(enumerate(distance[movie_index])), 
                        reverse=True, key=lambda x: x[1])[1:8]  # Get similar movies based on distance
    
    for i in movie_list:
        recommended_movies.append(data.iloc[i[0]]["title"])  # Append the titles of recommended movies to the list
    
    return recommended_movies  # Return the list of recommended movies

# Uncomment the line below to test the recommendation function
# print(recommend("Avatar"))

# Streamlit web-app
st.title("Movie Recommendation System")  # Title of the web app
st.write("This is a simple movie recommendation system that recommends movies based on the input movie.")  # Description

# Dropdown menu for selecting a movie
selected_movie = st.selectbox("Search for a movie", data["title"].values)

# Button to trigger recommendation
btn = st.button("Recommend")

# Display the recommended movies when the button is clicked
if btn:
    recommended_movies = recommend(selected_movie)
    st.write("Here are some movies you might enjoy:")
    for movie in recommended_movies:
        st.write(movie)

# Additional Features for Better User Experience
# if st.checkbox("Show DataFrame"):
#     st.write(data.head())  # Display the first few rows of the DataFrame

st.sidebar.title("About")
st.sidebar.info("""
    This is a simple movie recommendation system built using **Streamlit** and **Machine Learning**.
    It recommends movies based on the input movie title.
    Feel free to select a movie and hit the "Recommend" button!
""")

# Footer with developer info
st.sidebar.markdown("""
    **Developed by**: Vinit Limkar  
    **Email**: limkarvinit@gmail.com  
    **GitHub**: [Vinit Limkar](https://github.com/Vvl1232)  
""")
