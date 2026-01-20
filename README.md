# Movie Recommendation System 🎬

A machine learning-powered application that suggests movies based on content similarity. This system uses a **Streamlit** frontend to provide an interactive user interface and a dedicated **Backend** for data processing and model training.

## 📂 Project Structure

* **`MOVIE-RECOMMENDOR_FRONTEND/`**: 
    * `app.py`: The main application file to launch the user interface.
    * `movies_dict.pkl` & `similarity.pkl`: Precomputed data and similarity matrices.
    * `requirements.txt`: Required Python libraries for the application.
    * `Dockerfile`: Container configuration for the frontend.
* **`MOVIE-RECOMMENDOR-BACKEND/`**: 
    * `data_preprocessing.ipynb`: The notebook where data cleaning, stemming, and model training are performed.
    * `tmdb_5000_movies.csv` & `tmdb_5000_credits.csv`: Raw datasets used to build the model.
    * `project_flow.txt`: Step-by-step logic of the backend process.

## 🛠️ Tech Stack
* **Language:** Python
* **Machine Learning:** Scikit-learn, Pandas, count Vectorizer text to vectors
* **Frontend:** Streamlit
* **Large File Handling:** Git LFS

## 🚀 How to Run the Project

### 1. Clone the Repository
Open your terminal and run the following command to download the project:
```bash
git clone [https://github.com/Suraj8Sharma/movie-recommendation-system.git](https://github.com/Suraj8Sharma/movie-recommendation-system.git)
cd movie-recommendation-system

2. Set Up the Environment
It is highly recommended to use a virtual environment to keep your dependencies organized and prevent conflicts with system-wide installations:
# Create a virtual environment
python -m venv venv

# Activate the environment (Windows)
venv\Scripts\activate

# Activate the environment (Mac/Linux)
# source venv/bin/activate


3. Install Required Libraries
Once the virtual environment is active, install the necessary packages:
pip install -r MOVIE-RECOMMENDOR_FRONTEND/requirements.txt

4. Start the Application
Run this command to launch the Streamlit UI in your browser:
cd MOVIE-RECOMMENDOR_FRONTEND
streamlit run app.py