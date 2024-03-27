# 1er Mini Proyecto - Pr. Integrador Gestión TI

This is a Python project for web scraping and ETL (Extract, Transform, Load) processes. It utilizes Python 3.11 along with Jupyter Notebook for scraping data and performing ETL operations. 

## Requirements
* Python 3.11
* Dependencies from `requirements.txt`.
* Pycharm, Notebook anaconda o Jupyterlab

## Setup and Usage

Follow these steps to configure the virtual environment and run the scraping and ETL processes:

### Step 1: Set up Virtual Environment

```bash
# Clone the repository
git clone https://github.com/Dizkm8/pigti-pr-pt1.git
cd pigti-pr-pt1

# Create virtual environment
python3.11 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

Step 2: Install Dependencies
```bash
# Install dependencies
pip install -r requirements.txt
```
Step 3: Scraping
Open scrapping.ipynb using Jupyter Notebook.
Run the notebook cells to perform web scraping.
After execution, the scraped data will be saved in country_data.xlsx.

Step 4: ETL
Open etl.ipynb using Jupyter Notebook.
Run the notebook cells to execute the ETL process.
After execution, the transformed data will be saved in transformed_data.xlsx.

## Output Files
country_data.xlsx: Output file from the scraping process.

transformed_data.xlsx: Output file from the ETL process.
Contributing
Contributions are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Development files
Ensure to ignore any development files such as Jose.py while running or working on the project.
Files like **Jose.py** are for each develop to work isolated