import streamlit as st
import pandas as pd
import numpy as np
from plotly import express as px


st.set_page_config(
    page_title="Impostor Syndrome Map",
    page_icon="🧐",
    layout="wide",
    initial_sidebar_state="expanded",
)

def plot_figure(cluster_features: np.ndarray, cluster_labels=None):

    if cluster_features.shape[1] == 3:
        return px.scatter_3d(x=cluster_features[:,0], y=cluster_features[:,1], z=cluster_features[:,2],
                             color=cluster_labels, color_continuous_scale=px.colors.diverging.Portland)
    else:
        return px.scatter(x=cluster_features[:,0], y=cluster_features[:,1], color=cluster_labels, template="plotly_dark",
                 color_continuous_scale=px.colors.diverging.Portland)

from numpy.random import randint
def update_plot(df):
    new_df = pd.DataFrame([list(randint(10, size=3))])
    st.write(new_df)
    df = pd.concat([df, new_df], axis=0, ignore_index=True)
    return df

def main():

    # reading questions from txt file
    file_questions = open("questions.txt", "r")
    questions = [line.strip() for line in file_questions]

    # setting user options and their scale
    options = [("Disagree", 0.0), ("Mostly Disagree", 0.25), ("Neutral", 0.5), ("Mostly Agree", 0.75), ("Agree", 1.0)]
    options_text = [option[0] for option in options]
    options_scale = [option[1] for option in options]

    # setting radio buttons and saving user answers into a list
    answers = []
    for i, question in enumerate(questions):
        text = str(i+1) + "\. " + question
        answer = st.radio(text, options_text, index=0)
        answer_index = options_text.index(answer)
        answers.append(options_scale[answer_index])

    # building the side bar for more user input
    with st.sidebar:
        st.title("🧐 Impostor Syndrome Comparison Map 🧐")

        age = st.slider("How old are you?", 15, 80, 25)
        st.write("I'm ", age, "years old")
        
        years_exp = st.slider("How many years of experience?", 0, 20, 1)
        st.write("I'm ", years_exp, "years old")

    st.write(answers)

    update_btn = st.button('Update')
    if update_btn:
        df = pd.read_csv('test.csv', header=None)
        df = update_plot(df)
        df.to_csv('test.csv',header=False, index=False)
        st.write(df)
        # st.write(cluster_features)
        fig = plot_figure(df.values)
        st.plotly_chart(fig)


if __name__ == "__main__":
    main()
