# Anime Recommendation System

This project provides a recommendation system for anime based on content similarity. It includes a FastAPI backend for serving recommendations and a script to train the recommendation model.

## Getting Started

Follow these steps to set up and run the project:

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/UjjTiw/anime_reccomender.git
cd anime_reccomender
```

### 2. Install Requirements

Create a virtual environment and install the required dependencies. If you don’t have `virtualenv`, you can install it using `pip`:

```bash
pip install virtualenv
```

Create and activate the virtual environment:

```bash
virtualenv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the Training Script

To train the recommendation model and save it, run the `train.py` script:

```bash
python train.py
```

This will process the data, train the model, and save the necessary files (`indices.pkl`, `sig.pkl`, `anime_csv.pkl`) for recommendations.

### 4. Run the FastAPI Application

Start the FastAPI application using `uvicorn`:

```bash
uvicorn app:app --reload
```

Replace `app:app` with the appropriate module path if your `app.py` file is located elsewhere.

### 5. Access the Application

Once the server is running, open your web browser and go to:

```
http://127.0.0.1:8000
```

You should see the anime recommender frontend where you can enter an anime name to get recommendations.

## Project Structure

- `artifact/`: Folder containing the data.
- `app.py`: StreamLit application that serves recommendations.
- `train.py`: Script to train the recommendation model and save it.
- `requirements.txt`: List of project dependencies.

## Dependencies

- `streamlit`
- `matplotlib`
- `scikit-learn`
- `pandas`
- `pickle` (part of Python Standard Library)

