import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel
import pickle
import os

# Load the dataset
def load_data(filepath):
    return pd.read_csv(filepath)

# Process the dataset
def process_data(anime_csv):
    content_anime = anime_csv[['anime_id', 'Name', 'Producers', 'Licensors', 'Synopsis', 'Type', 'Source', 'Studios', 'Genres', 'Rating']]
    
    def convert(obj):
        return obj.split(",")
    
    def convert_syno(obj):
        return obj.split(" ")

    cols = ['Producers', 'Licensors', 'Type', 'Source', 'Studios', 'Genres', 'Rating']

    for col in cols:
        content_anime[col].replace({'UNKNOWN': ""}, inplace=True)

    content_anime['Synopsis'].replace({'No description available for this anime.': ""}, inplace=True)

    for col in cols:
        content_anime[col] = content_anime[col].apply(convert)
        content_anime[col] = content_anime[col].apply(lambda x: [i.replace(" ", "").lower() for i in x])

    content_anime['Synopsis'] = content_anime['Synopsis'].apply(convert_syno)
    content_anime['Synopsis'] = content_anime['Synopsis'].apply(lambda x: [i.lower() for i in x])

    content_anime['tag'] = (content_anime['Producers'] + content_anime['Licensors'] + 
                            content_anime['Type'] + content_anime['Rating'] + 
                            content_anime['Source'] + content_anime['Studios'] + 
                            content_anime['Genres'] + content_anime['Synopsis'])
    new_df = content_anime[['anime_id', 'Name', 'tag']]
    new_df['tag'] = new_df['tag'].apply(lambda x: " ".join(x))

    return new_df

# Train the model and save it
def train_and_save_model(new_df):
    tfv = TfidfVectorizer(min_df=3, max_features=None,
                         strip_accents='unicode', analyzer='word', ngram_range=(1, 3),
                         stop_words='english')
    tag_str = new_df['tag'].astype(str)
    tfv_matrix = tfv.fit_transform(tag_str)

    sig = sigmoid_kernel(tfv_matrix, tfv_matrix)

    indices = pd.Series(new_df.index, index=new_df['Name']).drop_duplicates()

    # Save models
    with open('indices.pkl', 'wb') as f:
        pickle.dump(indices, f)
    with open('sig.pkl', 'wb') as f:
        pickle.dump(sig, f)
    with open('anime_csv.pkl', 'wb') as f:
        pickle.dump(anime_csv, f)

    print("Model trained and saved successfully!")

# Main function to run the script
if __name__ == "__main__":
    data_filepath = 'artifacts/data/data.csv'
    anime_csv = load_data(data_filepath)
    new_df = process_data(anime_csv)
    train_and_save_model(new_df)
