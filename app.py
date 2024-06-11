import streamlit as st
import pandas as pd
import numpy as np
from numpy.random import randint
from plotly import express as px
import time


st.set_page_config(
    page_title="Impostor Syndrome Map",
    page_icon="🧐",
    layout="wide",
    initial_sidebar_state="expanded",
)

TITLE = "🧐 Impostor Syndrome Comparison Map 🧐"
SUBTITLE_MAIN = "Calculating your Impostor Syndrome metric:"
SUBTITLE_SIDE = "Required details about you:"
QUESTIONS_FILE = "questions.txt"
QUESTION_AGE = "How old are you?"
QUESTION_EXP = "How many years of experience / dedication?"
QUESTION_IS = "Based on the question on the right, your IS metric is:"
AGE_MIN_MAX_DEFAULT = 15, 80, 25
EXP_MIN_MAX_DEFAULT = 0, 30, 1
IS_MIN_MAX = 0.0, 8.0
OPTIONS_WEIGHT = [("Disagree", 0.0), ("Mostly Disagree", 0.25), ("Neutral", 0.5), ("Mostly Agree", 0.75), ("Agree", 1.0)]
JS_SCROLLDOWN = '''
    <script>
        window.parent.document.querySelector(".main").scrollTop = 5000;
    </script>
    '''
PLOT_TITLE_3D = "Impostor Syndrome Comparison Map - 3D"
PLOT_TITLE_2D_AGE = "Comparison Map - Age Only"
PLOT_TITLE_2D_EXP = "Comparison Map - Experience Only"
PLOT_AXIS_X = "Age"
PLOT_AXIS_Y = "Years of Experience"
PLOT_AXIS_Z = "Impostor Syndrome Metric"

def scroll_down():
    # added javascript for scrolling down feature
    temp_container = st.empty()
    with temp_container:
        st.components.v1.html(JS_SCROLLDOWN)
        time.sleep(.25)
    temp_container.empty()

def get_dataframe():
    # retrieving the dataframe (from a CSV file for now)
    df = pd.read_csv('test.csv', header=None)
    return df

def update_dataframe(df, user_input):
    # concat user input into the existing dataframe
    new_row = pd.DataFrame([user_input])
    new_df = pd.concat([df, new_row], axis = 0, ignore_index=True)

    # udpate the CSV file adding the new user input
    new_df.to_csv('test.csv', header=False, index=False)
    return new_df


def plot_figure(df):
    # use a scatter 3D to plot the user inputs
    labels = ['Others' for _ in range(df.shape[0])]
    labels[-1] = 'You'
    color_map = {"Others": "blue", "You": "red"}  
    if df.shape[1] == 3:
        return px.scatter_3d(x = df[:,0],
                             y = df[:,1],
                             z = df[:,2],
                             color = labels,
                             color_discrete_map = color_map)
    elif df.shape[1] == 2:
        return px.scatter(x = df[:,0],
                          y = df[:,1],
                          color = labels,
                          color_discrete_map = color_map)

def set_layout_3D(fig):
    # setting the plot layout, axis labels, title, and size
    fig.update_layout(
        scene=dict(
            xaxis_title=PLOT_AXIS_X,
            yaxis_title=PLOT_AXIS_Y,
            zaxis_title=PLOT_AXIS_Z,
        )
    )

def set_layout_2D(fig, axis):
    # setting the plot layout, axis labels, title, and size
    if axis == "age":
        fig.update_layout(
            xaxis_title=PLOT_AXIS_X,
            yaxis_title=PLOT_AXIS_Z
        )
    elif axis == "exp":
        fig.update_layout(
            xaxis_title=PLOT_AXIS_Y,
            yaxis_title=PLOT_AXIS_Z
        )


def compare_user(btn_compare, user_input):
    if btn_compare:
        # update user input database (test csv file for now)
        df = get_dataframe()
        df = update_dataframe(df, user_input)

        # set other dataframes for age and experience only
        df_age = df.drop([1], axis=1)
        df_exp = df.drop([0], axis=1)

        # plot updated 3D scatterplot and 2D plots
        st.header(PLOT_TITLE_3D)
        fig_3d = plot_figure(df.values)
        set_layout_3D(fig_3d)
        st.plotly_chart(fig_3d)

        st.header(PLOT_TITLE_2D_AGE)
        fig_age = plot_figure(df_age.values)
        set_layout_2D(fig_age, "age")
        st.plotly_chart(fig_age)

        st.header(PLOT_TITLE_2D_EXP)
        fig_exp = plot_figure(df_exp.values)
        set_layout_2D(fig_exp, "exp")
        st.plotly_chart(fig_exp)


        # scroll down to show plot
        scroll_down()

def main():
    # setting the titles
    st.title(TITLE)
    st.subheader(SUBTITLE_MAIN)

    # reading questions from txt file
    file_questions = open(QUESTIONS_FILE, "r")
    questions = [line.strip() for line in file_questions]

    # setting user options and their scale
    options_text = [option[0] for option in OPTIONS_WEIGHT]
    options_scale = [option[1] for option in OPTIONS_WEIGHT]

    # setting radio buttons and calculating IS metric
    answers = []
    for i, question in enumerate(questions):
        text = str(i+1) + "\. " + question
        answer = st.radio(text, options_text, index=0)
        answer_index = options_text.index(answer)
        answers.append(options_scale[answer_index])
    is_metric = sum(answers)

    # building the side bar for more user input
    with st.sidebar:
        st.title(TITLE)
        st.subheader(SUBTITLE_SIDE)

        age = st.slider(QUESTION_AGE, *AGE_MIN_MAX_DEFAULT)
        st.write("I'm ", age, "years old.")
        
        exp = st.slider(QUESTION_EXP, *EXP_MIN_MAX_DEFAULT)
        st.write("I have", exp, "year" + (exp != 1)*"s" + " of experience.")

        st.slider(QUESTION_IS, *IS_MIN_MAX, is_metric, disabled=True)
        st.write("My Impostor Syndrome metric is:", is_metric)

        btn_compare = st.button('Compare Me!', type="primary")
    
    compare_user(btn_compare, user_input = [age, exp, is_metric])

if __name__ == "__main__":
    main()
