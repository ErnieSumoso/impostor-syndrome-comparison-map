import streamlit as st
import constants as c
import time

# set the 3D plot layout, specifically axis labels
def set_layout_3D(fig):
    fig.update_layout(
        scene=dict(
            xaxis_title=c.PLOT_AXIS_X,
            yaxis_title=c.PLOT_AXIS_Y,
            zaxis_title=c.PLOT_AXIS_Z,
        )
    )

# set the 2D plot layout, specifically axis labels
def set_layout_2D(fig, axis_variable):
    # set axis labels for the 2D plot: Age vs IS metric
    if axis_variable == c.LAYOUT2D_AXIS_AGE:
        fig.update_layout(
            xaxis_title=c.PLOT_AXIS_X,
            yaxis_title=c.PLOT_AXIS_Z
        )
    # set axis labels for the 2D plot: Years of Experience vs IS metric
    elif axis_variable == c.LAYOUT2D_AXIS_EXP:
        fig.update_layout(
            xaxis_title=c.PLOT_AXIS_Y,
            yaxis_title=c.PLOT_AXIS_Z
        )

# added scroll down functionality through javascript within Streamlit
def scroll_down():
    # use a temporary container
    temp_container = st.empty()

    # perform the scroll down funcionality
    with temp_container:
        st.components.v1.html(c.JS_SCROLLDOWN)
        time.sleep(c.SLEEPING_TIME)

    # get rid of the temporary container
    temp_container.empty()

# show a simple message to communicate the success/failure of uploading the user's input to the cloud
def upload_message():
    # state -1: the user hasn't uploaded his input yet
    if st.session_state.uploaded == -1:
        return
    # state 0: the submission failed
    elif st.session_state.uploaded == 0:
        st.write(c.UPLOAD_FAILED)
    # state 1: the submission was succesful
    elif st.session_state.uploaded == 1:
        st.write(c.UPLOAD_SUCCESS)
