import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Impostor Syndrome Map",
    page_icon="🧐",
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    st.title("🧐 Impostor Syndrome Comparison Map 🧐")
    file_questions = open("questions.txt", "r")
    questions = [line.strip() for line in file_questions]
    answers = []
    for i, question in enumerate(questions):
        answer = st.selectbox( str(i+1) + "- " + question, ("No", "Yes"))
        answers.append(answer)
    st.write(answers)



if __name__ == "__main__":
    main()
