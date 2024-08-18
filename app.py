import streamlit as st
import pickle
import pandas as pd


def recommend(anime):
    # Get the index corresponding to original_title
    idx = indices[anime]

    # Get the pairwise similarity scores
    sig_scores = list(enumerate(sig[idx]))

    # Sort the animes
    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)

    # Scores of the 10 most similar animes
    sig_scores = sig_scores[1:21]

    # Anime indices
    anime_indices = [i[0] for i in sig_scores]

    # Top 10 most similar animes
    return {'Anime Name': anime_csv['Name'].iloc[anime_indices].values,
            'Score': anime_csv['Score'].iloc[anime_indices].values,
            'Rank': anime_csv['Rank'].iloc[anime_indices].values,
            'Synopsis': anime_csv["Synopsis"].iloc[anime_indices].values,
            'Image Link': anime_csv['Image URL'].iloc[anime_indices].values,
           }


anime_csv = pickle.load(open('anime_csv.pkl', 'rb'))
indices = pickle.load(open('indices.pkl', 'rb'))
sig = pickle.load(open('sig.pkl', 'rb'))

st.title('Anime Recommender System')

selected_movie_name = st.selectbox(
    'For which anime do you want a recommendation?',
    anime_csv['Name'].values
)

if st.button('Recommend'):
    recommendation = recommend(selected_movie_name)
    for i in range(20):
        # Create two columns: one for the image and one for the text
        col1, col2 = st.columns([1, 3])  # Adjust column ratio if needed

        with col1:
            st.image(recommendation['Image Link'][i], use_column_width=True)  # Display image in the left column
            st.write(f"<p style='font-size:14px;'><b>Score:</b> {recommendation['Score'][i]}</p>", unsafe_allow_html=True)
            st.write(f"<p style='font-size:14px;'><b>Rank:</b> {recommendation['Rank'][i]}</p>", unsafe_allow_html=True)

        with col2:
            st.write(f'<H3>{recommendation["Anime Name"][i]}</H3>', unsafe_allow_html=True)  # Display anime name
            st.write(f'<p>{recommendation["Synopsis"][i]}</p>', unsafe_allow_html=True)  # Display synopsis
