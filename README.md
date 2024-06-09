# Project Overview
- Leverages machine learning to predict the NBA MVP using data from over 30 NBA seasons from `BasketballReference`, a free sports statistics site. 
- Reverse-engineered the site's API to automate a web scraper using `BeautifulSoup` and `Selenium` to extract page content. 
- Preprocessed the raw data into a tabular format, using the `Pandas` and `Scikit-Learn` libraries for cleaning missing values, merging datasets, and scaling features 
- Trained and assessed multiple supervised regression machine learning models to predict the NBA MVP voting share % of each player in the 2023 NBA season, examining various error metrics for each model.
- Leveraged grid-search cross validation to tune model hyperparameters and implemented dimensionality reduction techniques such as PCA to optimize model performance and avoid overfitting.
## Source Organization 
This project is implemented using a modular approach, separating out high-level responsibilities into 2 key parts: 
1. **Data**->  Stores raw `HTML` data (to reduce server load from repeated web scrapes), as well as cleaned and merged `CSV` data ready for analysis.   
2. **Notebooks**-> Handles logic for scraping and extracting raw data, data processing, data analysis, model selection, and model evaluation. Houses various Jupyter Notebook files. 
```
HoopProphet-MVP-Predictor/
│
├── data/ 
│   ├── raw/                  # For storing raw data scraped from websites
│   ├── processed/            # For cleaned and merged CSVs ready for analysis
|
├── notebooks/  
│   ├── mvp_data_processor.ipynb       # For scraping and cleaning player MVP voting data
│   ├── player_data_processor.ipynb    # For scraping and cleaning player stats
│   ├── team_data_processor.ipynb      # For scraping and cleaning team W/L stats  
|   ├── data_cleaning.ipynb     # For combinining all our data and cleaning it for model use.
│   ├── model_training.ipynb        # For feature engineering and extraction, fitting/training models
│   └── model_evaluation.ipynb      # For evaluating the model's performance and model tuning
│   ├── scraping_utils.       # Contains shared logic HTTP response handling modules for web scraping
```
## Challenges & Edge Cases Encountered
- **Data merge conflicts - in particular from players whose names included non-traditional English characters**
	- For instance, when combining player statistics and team statistics, the CSV data contained separate data `Luka DonÄiÄ` vs. `Luka Dončić`, due to inconsistencies in the raw data's name strings.
	- This was resolved by using `utf-8` encoding when downloading and parsing scraped HTML.
- **Combining data from different datasets when there were duplicate player entries**
	- Players who were traded mid-season had multiple entries for different seasons.
	- This was an edge case that I had not considered when cleaning the data - in order to address this, if a player played for multiple teams in the same season, the cumulative individual performance data was used for player stats, and team W/L data of the players' most recent team was used for the player's team stats.
- **Dealing with `Nan` and missing values** 
	- One example is in many of the NBA seasons, there were some players, in particular centers, who never attempted 3-pointer shots over all 82 games, resulting in missing values for their `3PT%` features. 
	- This issue was handled by setting these players' `3PT%`s to 0 for that season. Although other techniques could be used for handling this missing value (such as mean imputation), in the context of this project, the design decision was made based on the heuristic that players who do not attempt any three-point shots are probably substandard three-point shooters and therefore less likely to win the NBA MVP (although Shaquille O'Neal did it in his MVP year).
	- The same logic was applied to the `FG%`, `FT%`, and `eFG%` features, for players who had not attempted any free throws or field goals in a given season. In the context of predicting the NBA MVP, it is okay to penalize players for not attempting free throws or field goals. It is virually impossible to win the MVP without a shot attempt or free throw attempt all year, since any MVP caliber player will attempt at least a handful of shots and free throws on pretty much any given game in a season. 
- **Converting raw data into a canonical format** 
	- There were several inconsistencies in the datasets even within the `basketball-reference` site, for instance some tables represented teams using abbreviations, (ex. BOS, NYK, etc.), while others used the full team name (ex. Boston Celtics, New York Knicks, etc.).
	- These errors were easy to fix once they were detected, however manually inspecting the dataset was impossible.  
	- With tens of thousands of columns in some CSV tables and the potential for human error, I relied on the aggregation functions of `Pandas` to query the dataset (selecting the columns, filtering the rows, etcl) in a way similar to `SQL` in order to ensure the data was cleaned and ready for machine learning.
- **Ethically scraping basketball-reference - complying with their crawl delay in their `robots.txt` file**
	- Initially, I encountered various `HTTP` errors while sending requests using the `requests` library, in particular `TooManyRedirects` and `TooManyRequests` status codes.
	- I examined the site's `robots.txt` file to learn the policy on web scraping bots, and implemented crawler delays as necessary to comply with them.
## Testing Overview
- Jupyter notebook display 
- Pandas aggregation functions, ex. `isna(), dtypes(), groupby(), apply()`
	- Checking for and handling null / missing values
	- Summary statistics 
	- Ensuring data is in the proper format 
- Firefox Browser 
	- Developer tools - used for reverse engineering basketball reference
	- HTML viewer - used to view the raw data that was scraped to ensure integrity
## Technologies & Resources Used 
- Python3, pip package manager 
- Version Control: Git & GitHub
- Obsidian.md - Markdown Editor for writing README
- Online documentation for Python standard library and data science frameworks 
- Libraries & Frameworks
	- Scikit-Learn 
	- Selenium & BeautifulSoup
	- Pandas
- Development Tools: VSCode (IDE), Jupyter Notebooks 
- https://basketball-reference.com
- DataQuest - YouTube - walked through how to interact with NBA datasets from basketball reference using the `pandas` library in Python
- *Python Machine Learning* - Book  

