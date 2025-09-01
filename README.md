<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ErnieSumoso/impostor-syndrome-comparison-map">
    <img src="readme-files/project-icon.jpg" alt="Icon" width="120">
  </a>

<h2 align="center">Impostor Syndrome Comparison Map</h2>
<b>### Final version - no additional updates planned ###</b> <br><br>

  Impostor syndrome, defined by self-perceived fraudulence, achievement pressure, and negative emotions, creates doubts in one's capacity. This project is a comprehensive evaluating and visualization tool which uses the Young Impostor Syndrome (YIS) scale in a web application to identify symptoms through Likert-scale responses. Users provide personal info, expanding our initial dataset of medical students. We analyze this data using clustering algorithms and present it in 2D/3D scatter plots, highlighting relationships between impostor syndrome traits and demographics. This tool enhances understanding and awareness of impostor syndrome through advanced data analytics and visualizations.
  <p align="center">
    <br />
    <a href="https://github.com/ErnieSumoso/impostor-syndrome-comparison-map/pulls">Pull Requests</a>
    ·
    <a href="https://github.com/ErnieSumoso/impostor-syndrome-comparison-map/issues">Issues</a>
  </p>
</div>


## About The Project

<div align="center">
  <img src="readme-files/project-showcase.jpg" alt="Showcase" width="650">
</div>
This project was initially created as part of the 2024 National Inter-University Big Data & AI Challenge by the STEM Fellowship. We aimed to enhance the understanding and awareness of the impostor syndrome psychological phenomenon through advanced 2D and 3D visualizations and clustering algorithms based on real world data. The initial dataset comes from medical students who are encouraged to provide information such as age and years of experience in the field, enabling users to attribute their accomplishments to their own ability. Furthermore, the data is processed as the basis for our analysis and then expanded through online user responses to the Young Impostor Syndrome questions, using a cloud solution to store their inputs. Visualizations help to better understand the frequency and the variability of this mental health phenomenon among demographic groups, in addition to quantifying it. Users can see where their inputs fit inside the identified clusters.
<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

* [![Python][python-badge]][python-url]
* [![Streamlit][streamlit-badge]][streamlit-url]
* [![JupyterLab][jupyter-badge]][jupyter-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Getting Started

<!-- TODO -->

### Prerequisites

To run the code you need Python 3 installed and optionally JupyterLab (or Notebook) for visualization and file editing.
* [Python 3+](https://www.python.org/downloads/)
* [JupyterLab 4.0+](https://jupyter.org/install) or Jupyer Notebook

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/ErnieSumoso/impostor-syndrome-comparison-map.git
   ```
2. Navigate to the project directory:
   ```sh
   cd impostor-syndrome-comparison-map
   ```
3. (Recommended) Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate        # On macOS/Linux
   .\venv\Scripts\activate         # On Windows
   ```
4. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
5. (Optional) Run JupyterLab or Jupyter Notebook to explore the notebook:
   ```sh
   jupyter lab
   ```
6. Launch the Streamlit web app:
   ```sh
   streamlit run app.py
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Roadmap

- [X] Built 2D & 3D visualizations as part of the front-end using Streamlit.
- [X] Add 2 clustering algorithms: K-Means and MeanShift algorithms to process the data and visualize results.
- [X] Enhance and complete the front-end using Streamlit as the final project update.

I am always open to suggestions and solving issues. Please, add them [here](https://github.com/ErnieSumoso/impostor-syndrome-comparison-map/issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[python-badge]: https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff
[python-url]: https://www.python.org/
[jupyter-badge]: https://img.shields.io/badge/jupyter-book-orange?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAZCAMAAAAVHr4VAAAAXVBMVEX////v7+/zdybv7+/zdybv7+/zdybv7+/zdybv7+/zdybv7+/zdybv7+/zdybv7+/zdybv7+/zdybv7+/v7+/zdybv7+/zdybv7+/v7+/zdybv7+/zdybv7+/zdyaSmqV2AAAAHXRSTlMAEBAgIDAwQEBQUGBgcHCAgJCQoLCwwMDQ4ODw8MDkUIUAAADJSURBVHjaddAFkgNBCAXQP+7uAvc/5tLFVseYF8crUB0560r/5gwvjYYm8gq8QJoyIJNwlnUH0WEnART6YSezV6c5tjOTaoKdfGXtnclFlEBEXVd8JzG4pa/LDql9Jff/ZCC/h2zSqF5bzf4vqkgNwEzeClUd8uMadLE6OnhBFsES5niQh2BOYUqZsfGdmrmbN+TMvPROHUOkde8sEs6Bnr0tDDf2Roj6fmVfubuGyttejCeLc+xFm+NLuLnJeFAyl3gS932MF/wBoukfUcwI05kAAAAASUVORK5CYII=
[jupyter-url]: https://jupyter.org/
[streamlit-badge]: https://img.shields.io/badge/-Streamlit-61DAFB?style=plastic&logo=streamlit
[streamlit-url]: https://docs.streamlit.io/
