# CLIMADE Africa dashboard
Repository contains code and files to interactive genomics Africa Dashboard

## How to install:
1. `conda env create -f requirements.yml`
2. `conda (or source) activate climade-dashboard`

## Data

### Using metadata
Create your metadata based on [data/template_metadata.csv](data/template_metadata.csv) and save as `./data/<pathogen>/metadata.csv`
For example, if you are working with Dengue, save your metadata on data/dengue/metadata.csv

### Using API

~~~
Do the editions you need to fit your data if they differ from ours in [data_process.py](data_process.py)

## Running the app
Once your environment is set, run the following commands to generate the files and run the app:
1. `python data_process.py`
2. `streamlit run Home.py`