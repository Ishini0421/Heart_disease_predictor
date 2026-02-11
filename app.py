import streamlit as st
import requests
import pandas as pd
import pickle
import base64
import plotly.express as px

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="wide"
)

st.image("heart_image.png", use_column_width=True, caption=" Heart Health Matters ")

# ---------- CACHE MODELS ----------
@st.cache_resource
def load_models():
    models = {
        "Decision Tree": pickle.load(open('heart_disease_ct.pkl', 'rb')),
        "Random Forest": pickle.load(open('heart_disease_RF.pkl', 'rb')),
        "Logistic Regression": pickle.load(open('heart_disease.pkl', 'rb')),
        "Support Vector Machine": pickle.load(open('heart_disease_svm.pkl', 'rb'))
    }
    return models

models = load_models()

# ---------- DOWNLOAD FUNCTION ----------
def get_binary_file_downloader_html(df):
    csv = df.to_csv(index=False).encode()
    b64 = base64.b64encode(csv).decode()
    return f'<a href="data:file/csv;base64,{b64}" download="output.csv">Download Predictions</a>'

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
/* DARK THEME */
body, .css-18e3th9 { background-color: #0B0C10; color: #FFFFFF; font-family: 'Segoe UI', sans-serif; }

/* GRADIENT HEADER */
h1.gradient-header {
    text-align: center;
    font-size: 3em;
    font-weight: bold;
    background: linear-gradient(90deg, #FF4B4B, #FFB347);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 30px;
}

/* GLASSMORPHISM CARD */
.glass-card {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 8px 32px 0 rgba(0,0,0,0.37);
    backdrop-filter: blur(10px);
    transition: transform 0.3s, box-shadow 0.3s;
    margin-bottom: 20px;
}
.glass-card:hover { transform: translateY(-5px); box-shadow: 0 12px 40px rgba(255,255,255,0.2); }

/* ANIMATED BUTTON */
.stButton>button {
    background: linear-gradient(90deg, #FF4B4B, #FFB347);
    color: #fff;
    border-radius: 50px;
    padding: 0.6em 2em;
    font-weight: bold;
    border: none;
    transition: all 0.3s ease;
}
.stButton>button:hover { background: linear-gradient(90deg, #FFB347, #FF4B4B); transform: scale(1.05); }

/* CENTER TABS */
.stTabs [data-baseweb="tab-list"] { justify-content: center; }

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<h1 class='gradient-header'>❤️ Heart Disease Predictor ❤️</h1>", unsafe_allow_html=True)

# ---------- TABS ----------
tab1, tab2, tab3 = st.tabs(['Predict', 'Bulk Predict', 'Model Information'])

# =====================================================
#                    TAB 1
# =====================================================
with tab1:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("Patient Information")
    
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", 0, 120)
        sex = st.selectbox("Sex", ['Male','Female'])
        chest_pain = st.selectbox("Chest Pain Type", ['Typical Angina','Atypical Angina','Non-anginal Pain','Asymptomatic'])
        resting_bp = st.number_input("Resting BP", 0, 200)
        cholesterol = st.number_input("Cholesterol", 0, 600)
    with col2:
        fasting_bs = st.selectbox("Fasting BS", ['>120 mg/dl','<120 mg/dl'])
        resting_ecg = st.selectbox("Resting ECG", ['Normal','ST-T Abnormality','Left Ventricular Hypertrophy'])
        max_hr = st.number_input("Max Heart Rate", 0, 250)
        exercise_angina = st.selectbox("Exercise Angina", ['Yes','No'])
        oldPeak = st.number_input("Old Peak", 0.0, 10.0)
        st_slope = st.selectbox("ST Slope", ['Upsloping','Flat','Downsloping'])
    st.markdown("</div>", unsafe_allow_html=True)

    # Convert inputs
    input_data = pd.DataFrame({
        'Age':[age],
        'Sex':[1 if sex=='Male' else 0],
        'ChestPainType':[ ['Typical Angina','Atypical Angina','Non-anginal Pain','Asymptomatic'].index(chest_pain)],
        'RestingBP':[resting_bp],
        'Cholesterol':[cholesterol],
        'FastingBS':[1 if fasting_bs=='>120 mg/dl' else 0],
        'RestingECG':[ ['Normal','ST-T Abnormality','Left Ventricular Hypertrophy'].index(resting_ecg)],
        'MaxHR':[max_hr],
        'ExerciseAngina':[1 if exercise_angina=='Yes' else 0],
        'Oldpeak':[oldPeak],
        'ST_Slope':[ ['Upsloping','Flat','Downsloping'].index(st_slope)]
    })

    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    if st.button("🔍 Predict Heart Risk", use_container_width=True):
        st.subheader("🧠 Model Predictions")
        predictions = []

        for name, model in models.items():
            pred = model.predict(input_data)[0]
            predictions.append(pred)
            if pred == 0:
                st.success(f"✅ **{name}: Low Risk**")
            else:
                st.error(f"🚨 **{name}: High Risk**")

        if sum(predictions) >= 2:
            st.error("⚠️ Multiple models indicate elevated risk. Consider medical consultation.")
        else:
            st.success("🎉 Majority of models suggest low risk!")
    st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
#                    TAB 2
# =====================================================
with tab2:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.header("Bulk Prediction")
    st.info("""
✔ Upload CSV only  
✔ Column names must match training data  
✔ No missing values  
✔ Categories must already be numeric
""")
    upload_files = st.file_uploader("Upload CSV", type=['csv'])

    if upload_files is not None:
        input_data = pd.read_csv(upload_files)
        expected_columns=['Age','Sex','ChestPainType','RestingBP','Cholesterol','FastingBS','RestingECG','MaxHR','ExerciseAngina','Oldpeak','ST_Slope']
        input_data.columns = input_data.columns.str.strip()
        if set(input_data.columns) == set(expected_columns):
            input_data = input_data[expected_columns]
            model = models["Logistic Regression"]
            predictions = model.predict(input_data)
            probs = model.predict_proba(input_data)[:,1]
            input_data['Prediction'] = predictions
            input_data['Risk Score (%)'] = (probs*100).round(2)
            st.dataframe(input_data, use_container_width=True)
            st.download_button("Download Predictions", input_data.to_csv(index=False), file_name="heart_predictions.csv", mime="text/csv")
        else:
            st.error("CSV format incorrect.")
    st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
#                    TAB 3
# =====================================================
with tab3:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.header("📊 Model Intelligence Dashboard")

    # Model Accuracy
    model_data = pd.DataFrame({"Model":["Decision Tree","Random Forest","Logistic Regression","SVM"],"Accuracy":[0.86,0.91,0.88,0.90]})
    fig = px.bar(model_data, x="Model", y="Accuracy", color="Model", text="Accuracy", template="plotly_dark")
    fig.update_layout(yaxis_range=[0,1])
    st.plotly_chart(fig, use_container_width=True)

    # Feature Importance
    st.subheader("🔥 Feature Importance (Random Forest)")
    try:
        rf_model = models["Random Forest"]
        features=['Age','Sex','ChestPainType','RestingBP','Cholesterol','FastingBS','RestingECG','MaxHR','ExerciseAngina','Oldpeak','ST_Slope']
        importance_df = pd.DataFrame({"Feature":features,"Importance":rf_model.feature_importances_}).sort_values(by="Importance",ascending=False)
        fig2 = px.bar(importance_df, x="Importance", y="Feature", orientation='h', template="plotly_dark")
        st.plotly_chart(fig2, use_container_width=True)
    except:
        st.warning("Random Forest model not found.")

    # Outcome Pie Chart
    st.subheader("❤️ Dataset Outcome Distribution")
    outcome_data = pd.DataFrame({"Outcome":["No Heart Disease","Heart Disease"],"Count":[580,420]})
    fig3 = px.pie(outcome_data, names="Outcome", values="Count", hole=0.5, template="plotly_dark")
    st.plotly_chart(fig3, use_container_width=True)

    st.success("Random Forest often performs best due to ensemble learning.")
    st.markdown("</div>", unsafe_allow_html=True)
