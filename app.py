import streamlit as st
import pandas as pd
from sklearn import cluster
from plotly import express as px
import constants as c
from helpers import set_layout_3D, set_layout_2D, scroll_down, upload_message


st.set_page_config(
    page_title="Impostor Syndrome Map",
    page_icon="🧐",
    layout="wide",
    initial_sidebar_state="expanded",
)

# return the labels of the clustering features based on the algorithm selected
def get_labels(algo, features):
    # KMeans algorithm selected: find 2 clusters within the data
    if algo == c.KMEANS_LABEL:
        return cluster.KMeans(n_clusters = 2).fit(features).labels_
    
    # MeanShift algorithm: default parameters, room for improvement
    elif algo == c.MEANSHIFT_LABEL:
        return cluster.MeanShift().fit(features).labels_
    
    # TODO: room for improvement, experiment with more algorithms
    else:
        pass
    
# concatenate the user input into the existing dataframe
def update_dataframe(df, user_input):
    # turn the user input into a single-row dataframe
    new_row = pd.DataFrame([user_input])

    # concatenate both dataframes: current user input and current submissions dataset
    new_df = pd.concat([df, new_row], axis = 0, ignore_index=True)

    # return new merged dataset
    return new_df

# plot the scatterplots in both 2D and 3D using plotly express
def plot_figure(df, labels):
    # transform the labels into a Python list
    labels = labels.tolist()

    # transform the cluster labels (integers) into strings for better visualization
    labels = list(map(lambda x : c.CLUSTER_A_LABEL if x == 0 else c.CLUSTER_B_LABEL, labels))

    # change the user input label into a "single point cluster" using a different label
    labels[-1] = c.USER_LABEL

    # map the colors using a dictionary
    color_map = {c.CLUSTER_A_LABEL: "blue", c.CLUSTER_B_LABEL: "white", c.USER_LABEL:"red"}  

    # return the plots (3D or 2D based on the dataframe number of columns)
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

# button on-click function called to visualize the plots (comparison maps)
def compare_user(btn_compare, user_input, algo_selected):
    # trigger the functionality if the button was pressed or the user input was submitted to the cloud
    if btn_compare or st.session_state.uploaded == 1:
        
        # retrieve the dataframe from the cloud and update locally with user's input (row)
        df = get_dataframe()
        df = update_dataframe(df, user_input)

        # set the other 2 dataframes for 2D age and years-of-experience plots
        df_age = df.drop([1], axis=1)
        df_exp = df.drop([0], axis=1)

        # get the labels by applying the selected clustering algorithm
        labels = get_labels(algo_selected, df.values)
        
        # plot the 3D Impostor Syndrome comparison map
        st.header(c.PLOT_TITLE_3D)
        fig_3d = plot_figure(df.values, labels)
        set_layout_3D(fig_3d)
        st.plotly_chart(fig_3d)

        # plot the 2D Impostor Syndrome comparison map (Age vs IS metric)
        st.header(c.PLOT_TITLE_2D_AGE)
        fig_age = plot_figure(df_age.values, labels)
        set_layout_2D(fig_age, c.LAYOUT2D_AXIS_AGE)
        st.plotly_chart(fig_age)

        # plot the 2D Impostor Syndrome comparison map (Years-of-Experience vs IS metric)
        st.header(c.PLOT_TITLE_2D_EXP)
        fig_exp = plot_figure(df_exp.values, labels)
        set_layout_2D(fig_exp, c.LAYOUT2D_AXIS_EXP)
        st.plotly_chart(fig_exp)

        # scroll down to show plots
        scroll_down()

# TODO: retrieve the current dataframe containing all user submissions (and original dataset) from the cloud
def get_dataframe():
    # temporarily: using a local CSV file
    df = pd.read_csv(c.CSV_FILE, header=None)
    return df

# TODO: button on-click function to upload the user input into the cloud dataframe
def upload_results(btn_upload, user_input, compare_user_params):
    # if the button was pressed
    if btn_upload:

        # retrieve the dataframe from the cloud and update locally with user's input (row)
        df_cloud = get_dataframe()
        df_cloud = update_dataframe(df_cloud, user_input)
        
        # TODO: upload the dataframe to cloud
        df_cloud.to_csv(c.CSV_FILE, header=False, index=False)
        st.session_state.uploaded = 1 # 0 failed

        # update the front-end to trigger the plots and success/fail message
        st.experimental_rerun()

# read the questions from a txt file and return them in a Python array
def get_survey_questions():
    # opening the text file in read mode
    file_questions = open(c.QUESTIONS_FILE, "r")

    # save the questions into a list
    questions = [line.strip() for line in file_questions]

    # closing the file and return the questions
    file_questions.close()
    return questions

# main app: contains frornt-end logic
def main():

    # front-end main section: setting the titles
    st.title(c.TITLE)
    st.subheader(c.SUBTITLE_MAIN)

    # session variable: uploaded - says if the user uploaded their results to the cloud
    if 'uploaded' not in st.session_state:
        st.session_state['uploaded'] = -1

    # questions - list that contains the impostor syndrome detection questions developed by Young
    questions = get_survey_questions()
    
    # options - lists containing both labels and weights for the user answers to each question
    options_text = [option[0] for option in c.OPTIONS_WEIGHT]
    options_scale = [option[1] for option in c.OPTIONS_WEIGHT]

    # front-end questions and answers section: using radio buttons for capturing the user's input to the questions
    answers = []
    for i, question in enumerate(questions):
        # set the question into a string
        text = str(i+1) + "\. " + question

        # set the radio button, setting the default as the 1st option
        answer = st.radio(text, options_text, index=0)

        # save the user answer to each question into a list
        answer_index = options_text.index(answer)
        answers.append(options_scale[answer_index])
    
    # calculate the user impostor syndrome metric using the sum of weigths
    is_metric = sum(answers)

    # front-end side bar section: getting age and years-of-experience from the user
    with st.sidebar:
        # setting the headers
        st.title(c.TITLE)
        st.subheader(c.SUBTITLE_SIDE)

        # 1st slider to capture the user's age
        age = st.slider(c.QUESTION_AGE, *c.AGE_MIN_MAX_DEFAULT)
        st.write("I'm ", age, "years old.")
        
        # 2nd slider to caputure the user's experience
        exp = st.slider(c.QUESTION_EXP, *c.EXP_MIN_MAX_DEFAULT)
        st.write("I have", exp, "year" + (exp != 1)*"s" + " of experience.")

        # 3rd slider (disabled) to show current impostor syndrome metric based on the questions-answers section
        st.slider(c.QUESTION_IS, *c.IS_MIN_MAX, is_metric, disabled=True)
        st.write(c.IS_METRIC_LABEL, is_metric)

        # selectbox to choose a clustering algorithm
        st.subheader(c.SUBTITLE_SIDE_2)
        algo_selected = st.selectbox("-", [c.KMEANS_LABEL, c.MEANSHIFT_LABEL], label_visibility ="collapsed")

        # 2 buttons: show the comparison maps, and submit the inputs to the cloud
        btn_compare = st.button(c.COMPARE_BTN_LABEL, type="primary")
        # btn_upload = st.button(c.UPLOAD_BTN_LABEL, type="primary", disabled= (st.session_state.uploaded != -1))

        # display a success/fail message only if the user submitted his inputs
        upload_message()
    
    # save user inputs into a list
    user_input = [age, exp, is_metric]

    # set the compare user function parameters
    compare_user_params = {'user_input':user_input, 'algo_selected':algo_selected}

    # 2 buttons on-click functions
    compare_user(btn_compare, **compare_user_params)
    upload_results(btn_upload, user_input, compare_user_params)

if __name__ == "__main__":
    main()
