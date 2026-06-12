import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ==========================
# Chargement du modèle
# ==========================

try:
    model = joblib.load("best_model.joblib")
    model_loaded = True
except:
    model_loaded = False

# ==========================
# Interface
# ==========================

st.set_page_config(
    page_title="Prédiction No-Show Médical",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 Prédiction de No-Show Médical")

st.write("""
Cette application prédit la probabilité qu'un patient manque son rendez-vous médical.
""")

st.divider()

# ==========================
# Formulaire
# ==========================
col1, col2 = st.columns(2)
with col1:
    age = st.number_input(
        "Âge",
        min_value=0,
        max_value=120,
        value=30
    )

    gender = st.selectbox(
        "Sexe",
        ["F", "M"]
    )
    sms_received = st.selectbox(
        "SMS reçu",
        [0, 1]
    )

    waiting_days = st.number_input(
        "Nombre de jours d'attente avant le rendez-vous",
        min_value=0,
        max_value=365,
        value=7
    )
    
with col2:
    alcoholism = st.selectbox(
        "Alcoolisme",
        [0, 1]
    )

    scholarship = st.selectbox(
        "Bourse (Scholarship)",
        [0, 1]
    )

    
    hypertension = st.selectbox(
        "Hypertension",
        [0, 1]
    )

    diabetes = st.selectbox(
        "Diabète",
        [0, 1]
    )
# ==========================
# Prédiction
# ==========================

if st.button("Prédire le risque de No-Show"):

    if model_loaded:

        data = pd.DataFrame({
            "Age": [age],
            "Scholarship": [scholarship],
            "Hipertension": [hypertension],
            "Diabetes": [diabetes],
            "Alcoholism": [alcoholism],
            "SMS_received": [sms_received],
            "waiting_days": [waiting_days],
            "Gender_M": [1 if gender == "M" else 0]
        })

        prediction = model.predict(data)[0]

        if hasattr(model, "predict_proba"):
            probability = model.predict_proba(data)[0][1]
        else:
            probability = 0.0

        st.subheader("Résultat")

        st.metric(
            "Probabilité de No-Show",
            f"{probability*100:.1f}%"
        )

        if prediction == 1:
            st.error("⚠️ Risque élevé : le patient pourrait manquer son rendez-vous.")
        else:
            st.success("✅ Faible risque : le patient devrait se présenter.")

    else:

        st.warning(
            "Aucun modèle détecté (best_model.pkl). "
            "L'interface fonctionne mais le modèle n'est pas encore chargé."
        )