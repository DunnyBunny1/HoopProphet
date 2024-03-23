# Basketball Reference MVP Predictor

This project predicts the MVP using data from Basketball Reference
## Src Organization 
```
HoopProphet-MVP-Predictor/
│
├── data/ # Holds data relevant to the project
│   ├── raw/                  # For storing raw data scraped from websites
│   ├── processed/            # For cleaned and merged datasets ready for analysis
│   └── external/             # Any external data sources, e.g., manual entries, additional datasets
│
├── notebooks/ # Holds jupyter notebooks for data analysis 
│   ├── 01_data_collection.ipynb        # For web scraping with Selenium and BeautifulSoup
│   ├── 02_data_preprocessing.ipynb     # For data cleaning and preprocessing with pandas
│   ├── 03_feature_engineering.ipynb    # For feature selection and engineering
│   ├── 04_model_training.ipynb         # For training the random forest model with scikit-learn
│   └── 05_model_evaluation.ipynb       # For evaluating the model's performance and fine-tuning
│
```