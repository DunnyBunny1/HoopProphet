# main.py

# Import functionalities from your src directory
from src import data_management, mvp_predictor


#  A list of years (integers) for which MVP data needs to be  scraped.
years = [year for year in range(1991, 2023)]

def main():
    # Example: Call functions from your modules in src directory
    # scraper.scrape_basketball_reference(years)
    processed_data = data_management.create_yearly_mvp_csv(years)
    predicted_mvp = mvp_predictor.predict_mvp(processed_data)

    # Display or use the predicted MVP
    print(f"The predicted MVP is: {predicted_mvp}")


if __name__ == "__main__":
    main()
