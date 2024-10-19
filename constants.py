TITLE = "🧐 Impostor Syndrome Comparison Map 🧐"
SUBTITLE_MAIN = "Calculating your Impostor Syndrome metric:"
SUBTITLE_SIDE = "Required details about you:"
QUESTIONS_FILE = "questions.txt"
QUESTION_AGE = "How old are you?"
QUESTION_EXP = "How many years of experience?"
QUESTION_IS = "Based on the question on the right, your IS metric is:"
AGE_MIN_MAX_DEFAULT = 15, 80, 25
EXP_MIN_MAX_DEFAULT = 0, 30, 1
IS_MIN_MAX = 0.0, 8.0
OPTIONS_WEIGHT = [("Disagree", 0.0), ("Mostly Disagree", 0.25), ("Neutral", 0.5), ("Mostly Agree", 0.75), ("Agree", 1.0)]
PLOT_TITLE_3D = "Impostor Syndrome Comparison Map"
PLOT_TITLE_2D_AGE = "Comparison Map - Age"
PLOT_TITLE_2D_EXP = "Comparison Map - Experience"
CSV_FILE = "data/dataset.csv"
KMEANS_LABEL = "KMeans"
MEANSHIFT_LABEL = "MeanShift"
SUBTITLE_SIDE_2 = "Select a Clustering Algorithm:"
COMPARE_BTN_LABEL = 'Compare Myself!'
UPLOAD_BTN_LABEL = 'Upload Results!'
IS_METRIC_LABEL = "My Impostor Syndrome metric is:"
CLUSTER_A_LABEL = 'Cluster A'
CLUSTER_B_LABEL = 'Cluster B'
USER_LABEL = 'You'
PLOT_AXIS_X = "Age"
PLOT_AXIS_Y = "Years of Experience"
PLOT_AXIS_Z = "Impostor Syndrome Metric"
LAYOUT2D_AXIS_AGE = 0
LAYOUT2D_AXIS_EXP = 1
UPLOAD_SUCCESS = "Your results were uploaded successfully!"
UPLOAD_FAILED = "Sorry, there was a problem uploading your results, try later!"
JS_SCROLLDOWN = '''
    <script>
        window.parent.document.querySelector(".main").scrollTop = 1550;
    </script>
    '''
SLEEPING_TIME = 1.25
