# ❤️ Heart Disease Predictor

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.26-orange)
![License](https://img.shields.io/badge/License-MIT-green)

A **Streamlit-based web app** that predicts the risk of heart disease using multiple machine learning models.  
Users can input patient data individually or in bulk (via CSV) and get predictions from **Decision Tree, Random Forest, Logistic Regression, and SVM** models.  

---

## 🌟 Features

- **Single Patient Prediction** – Enter patient details manually and get risk predictions from multiple models.
- **Bulk Prediction** – Upload a CSV with multiple patients and download predictions.
- **Interactive Model Dashboard** – View model accuracies, feature importance, and dataset outcome distribution.
- **Dark & Modern UI** – Gradient headers, glassmorphism cards, animated buttons.
- **Download Results** – Save predictions as CSV for further analysis.
- **Responsive Design** – Works well on both desktop and mobile.

---

## 📸 Screenshots

### App Header & Input Form
![App Header](screenshots/header.png)

### Bulk CSV Prediction
![Bulk Prediction](screenshots/bulk_prediction.png)

### Model Dashboard
![Dashboard](screenshots/dashboard.png)

> Replace the screenshots with your own images in the `screenshots/` folder.

---

## 🚀 Live Demo

Check out the app live on **[Streamlit Community Cloud](https://share.streamlit.io/<your-username>/<your-repo>/main/app.py)**  

> Replace `<your-username>` and `<your-repo>` with your GitHub username and repository name.

---

## 🛠️ Tech Stack

- Python 3.10+  
- Streamlit  
- Pandas  
- Plotly  
- Scikit-learn (for ML models)  

---

## ⚡ Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

```
2. **Create and activate virtual environment (venv):**

   ```bash
   # Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python -m venv venv
source venv/bin/activate

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4.**Run the app locally**
```bash
streamlit run app.py
```
> The app should open automatically in your default browser at http://localhost:8501.

## 📂 Project Structure

```graphql
HearDiseasePredictor/
│
├─ app.py                   # Main Streamlit app
├─ requirements.txt         # Python dependencies
├─ heart_image.png          # Header image
├─ models/                  # Folder containing trained ML models
│   ├─ heart_disease_ct.pkl
│   ├─ heart_disease_RF.pkl
│   ├─ heart_disease.pkl
│   └─ heart_disease_svm.pkl
├─ screenshots/             # Folder for app screenshots
└─ README.md
```
## 📑 CSV Format for Bulk Predictions
**Required columns (numeric values only):**

| Column Name    | Description / Example Values                                                    |
| -------------- | ------------------------------------------------------------------------------- |
| Age            | Patient age, e.g., 45                                                           |
| Sex            | 1 = Male, 0 = Female                                                            |
| ChestPainType  | 0 = Typical Angina, 1 = Atypical Angina, 2 = Non-anginal Pain, 3 = Asymptomatic |
| RestingBP      | Resting blood pressure, e.g., 120                                               |
| Cholesterol    | Serum cholesterol, e.g., 230                                                    |
| FastingBS      | 1 if >120 mg/dl, 0 if <120 mg/dl                                                |
| RestingECG     | 0 = Normal, 1 = ST-T Abnormality, 2 = Left Ventricular Hypertrophy              |
| MaxHR          | Maximum heart rate, e.g., 150                                                   |
| ExerciseAngina | 1 = Yes, 0 = No                                                                 |
| Oldpeak        | ST depression induced by exercise, e.g., 1.5                                    |
| ST_Slope       | 0 = Upsloping, 1 = Flat, 2 = Downsloping                                        |

## Example CSV:

```csv
Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope
45,1,0,120,230,0,1,150,1,1.5,0
50,0,2,140,250,1,0,160,0,2.3,1
60,1,1,130,200,0,2,145,1,0.5,2
```
> Make sure column names match exactly and numeric values are used where required.

## 📢 Notes
- Ensure all model files are present in the models/ folder.

- Bulk CSV columns must match exactly; otherwise, the app will show an error.

- Works best with Python >= 3.10 and a virtual environment.

## ❤️ Author

**Ishini Vidanapathirana**
> IT Undergraduate | Aspiring Full Stack Developer 

   

                   
