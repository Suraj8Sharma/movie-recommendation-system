# 🎬 Movie Recommendation System

A machine learning–powered movie recommendation application that suggests movies based on **content similarity**.  
The project features a **Streamlit frontend** for user interaction and a **backend pipeline** for data preprocessing and model generation.

---

## 📂 Project Structure

movie-recommendation-system/
│
├── MOVIE-RECOMMENDOR_FRONTEND/
│ ├── app.py # Streamlit application (UI)
│ ├── movies_dict.pkl # Processed movie metadata
│ ├── similarity.pkl # Cosine similarity matrix
│ ├── requirements.txt # Required Python libraries
│ └── Dockerfile # Docker configuration
│
├── MOVIE-RECOMMENDOR-BACKEND/
│ ├── data_preprocessing.ipynb # Data cleaning & model training
│ ├── tmdb_5000_movies.csv # TMDB movies dataset
│ ├── tmdb_5000_credits.csv # TMDB credits dataset
│ └── project_flow.txt # Backend logic flow
│
└── README.md

yaml
Copy code

---

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
2️⃣ Set Up Virtual Environment
Using a virtual environment is recommended.

bash
Copy code
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on Mac/Linux
# source venv/bin/activate
3️⃣ Install Required Libraries
bash
Copy code
pip install -r MOVIE-RECOMMENDOR_FRONTEND/requirements.txt
4️⃣ Run the Application
bash
Copy code
cd MOVIE-RECOMMENDOR_FRONTEND
streamlit run app.py
The application will open automatically in your default browser.

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

bash
Copy code
git lfs install
👨‍💻 Developer
Suraj Sharma
CSE (AI & ML) Student
JNGEC Sundernagar