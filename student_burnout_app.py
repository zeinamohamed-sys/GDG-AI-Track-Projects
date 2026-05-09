import streamlit as st

st.title("Student Burnout Predictor")
st.write("Professional ML tool to assess burnout levels.")

study = st.slider("Study Hours", 1, 15, 6)
stress = st.slider("Stress Level", 1, 10, 5)
sleep = st.slider("Sleep Hours", 1, 12, 8)

if st.button("Predict"):
    score = (study * 2.5) + (stress * 6) - (sleep * 4)
    result = max(0, min(100, score + 35))
    st.success(f"Burnout Score: {result:.1f}%")
