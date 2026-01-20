# 🎬 Movie Recommendation System

A machine learning–powered movie recommendation application that suggests movies based on **content similarity**.  
The project features a **Streamlit frontend** for user interaction and a **backend pipeline** for data preprocessing and model generation.

---

## 📂 Project Structure

# Movie Recommendation System 🎬

A machine learning-powered application that suggests movies based on content similarity. This system uses a **Streamlit** frontend for the user interface and a dedicated **Backend** for data processing.

## 📂 Project Structure

* **`MOVIE-RECOMMENDOR_FRONTEND/`**: 
    * `app.py`: The main application file for the UI.
    * `movies_dict.pkl` & `similarity.pkl`: Precomputed model files.
    * `requirements.txt`: Required Python libraries.
    * `Dockerfile`: Container configuration.
* **`MOVIE-RECOMMENDOR-BACKEND/`**: 
    * `data_preprocessing.ipynb`: Notebook for data cleaning and model training.
    * `tmdb_5000_movies.csv` & `tmdb_5000_credits.csv`: TMDB datasets.
    * `project_flow.txt`: Logic of the backend process.



## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Machine Learning:** Scikit-learn, Pandas, NLTK  
- **Frontend Framework:** Streamlit  
- **Dataset:** TMDB 5000 Movies & Credits  
- **Large File Handling:** Git LFS  

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Suraj8Sharma/movie-recommendation-system.git
cd movie-recommendation-system
```

2️⃣ Set Up Virtual Environment
Using a virtual environment is recommended.
```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on Mac/Linux
# source venv/bin/activate
```

3️⃣ Install Required Libraries
```bash
pip install -r MOVIE-RECOMMENDOR_FRONTEND/requirements.txt
```
4️⃣ Run the Application
```bash
cd MOVIE-RECOMMENDOR_FRONTEND
streamlit run app.py
```
🧠 Methodology

This system uses Content-Based Filtering:

Text Processing: Movie metadata (genres, keywords, cast, crew) is combined into tags.

Vectorization: Tags are converted into vectors using CountVectorizer.

Similarity Measure: Cosine Similarity is used to find movies with similar content.

Recommendation: Top similar movies are suggested based on the selected movie.

⚠️ Important Information

The file similarity.pkl is approximately 176 MB.

This repository uses Git LFS to manage large files.

Ensure Git LFS is installed before cloning:
```bash
git lfs install
```
👨‍💻 Developed By:

Suraj Sharma
CSE (AI & ML) Student
JNGEC Sundernagar
