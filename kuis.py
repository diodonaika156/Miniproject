import streamlit as st
from collections import defaultdict

st.set_page_config(page_title="Kuis Minat Teknologi", layout="centered")
st.title("🧠 Kuis Minat Teknologi")

# Data pertanyaan, pilihan, dan mapping skor
questions = [
    {
        "question": "1. Kamu paling suka ngapain?",
        "options": {
            "a. Ngoding sampai lupa waktu": "Developer",
            "b. Bikin layout & warna yang estetik": "Desainer",
            "c. Main data dan analisa tren": "Data Analyst"
        }
    },
    {
        "question": "2. Kamu lebih suka alat yang mana?",
        "options": {
            "a. VS Code": "Developer",
            "b. Figma": "Desainer",
            "c. Google Colab": "Data Analyst"
        }
    },
    {
        "question": "3. Motto kamu?",
        "options": {
            "a. Keep calm and debug the code": "Developer",
            "b. Design is thinking made visual": "Desainer",
            "c. In data we trust": "Data Analyst"
        }
    }
]

# Jawaban & skor kategori
answers = {}
score = defaultdict(int)

# Loop pertanyaan
for i, q in enumerate(questions):
    st.subheader(q["question"])
    selected = st.radio("Pilih satu:", list(q["options"].keys()), key=f"q{i}")
    answers[q["question"]] = selected
    role = q["options"][selected]
    score[role] += 1

# Tombol submit
if st.button("Submit Jawaban"):
    st.markdown("---")
    st.success("✅ Jawaban Kamu:")
    for question, answer in answers.items():
        st.write(f"**{question}**")
        st.write(f"👉 {answer}")
    
    st.markdown("---")
    st.subheader("🧩 Hasil Analisis Minat Kamu:")

    # Tentukan role dengan skor tertinggi
    result = max(score, key=score.get)
    st.write(f"🎓 **Kamu paling cocok jadi: {result}**")

    # Opsional: tampilkan semua skor
    st.write("📊 Skor Kategori:")
    for role, val in score.items():
        st.write(f"- {role}: {val}")