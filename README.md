# Basketball Reference MVP Predictor

This project predicts the MVP using data from Basketball Reference
## Src Organization 
```
HoopProphet-MVP-Predictor/
│
├── data/ # Holds data relevant to the project
│   ├── raw/                  # For storing raw data scraped from websites
│   ├── processed/            # For cleaned and merged CSVs ready for analysis
│   
├── notebooks/ # Holds jupyter notebooks for data analysis 
│   ├── mvp_data_processor.ipynb       # For scraping and cleaning player MVP voting data
│   ├── player_data_processor.ipynb    # For scraping and cleaning player stats 
│   ├── team_data_processor.ipynb      # For scraping and cleaning team W/L stats    
│   ├── 04_model_training.ipynb        # For feature extraction, fitting, and training models 
│   └── 05_model_evaluation.ipynb      # For evaluating the model's performance and backtesting
│
```