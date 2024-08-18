import streamlit as st
import pickle
import pandas as pd


def reccomend(anime):
    # Get the index corresponding to original_title
    idx = indices[anime]

    # Get the pairwsie similarity scores
    sig_scores = list(enumerate(sig[idx]))

    # Sort the movies
    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)

    # Scores of the 10 most similar movies
    sig_scores = sig_scores[1:11]

    # Movie indices
    anime_indices = [i[0] for i in sig_scores]

    # Top 10 most similar movies
    return {'Anime Name': anime_csv["Name"].iloc[anime_indices].values,
                         'Rating': anime_csv['Rating Score'].iloc[anime_indices].values,
                         'Synopsis': anime_csv["Synopsis"].iloc[anime_indices].values}


anime_csv = pickle.load(open('anime_csv.pkl', 'rb'))
indices = pickle.load(open('indices.pkl', 'rb'))
sig = pickle.load(open('sig.pkl', 'rb'))

st.title('Anime Recommender System')

selected_movie_name = st.selectbox(
    'For which anime you want recommendation?',
    anime_csv['Name'].values
)

if st.button('Reccomend'):
    recommendation = reccomend(selected_movie_name)
    for i in range(10):
        st.write('<H3>{}</H3>'.format(recommendation['Anime Name'][i]),unsafe_allow_html=True)
        st.write('<p>{}</p>'.format(recommendation['Synopsis'][i]),unsafe_allow_html=True)
