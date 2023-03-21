# CLIMADE Africa dashboard
Repository contains code and files to interactive genomics Africa Dashboard

## How to install:
1. Make sure you have Docker installed. For more information access: https://docs.docker.com/engine/install/
2. Build the image: `sudo docker build -t climade-dashboard .`
3. Run the Docker container: `sudo docker run -p 8501:8501 climade-dashboard .` 
4. You can view your Dashboard in your browser URL: http://0.0.0.0:8501

## Data

### Using metadata
Create your metadata based on [data/template_metadata.csv](data/template_metadata.csv) and save as `./data/<pathogen>/metadata.csv`
For example, if you are working with Dengue, save your metadata on data/dengue/metadata.csv
