# main.py

# Import functionalities from your src directory
from src import scraper, data_management, mvp_predictor


def main():
    # Example: Call functions from your modules in src directory
    data = scraper.scrape_basketball_reference()
    processed_data = data_management.process_data(data)
    predicted_mvp = mvp_predictor.predict_mvp(processed_data)

    # Display or use the predicted MVP
    print(f"The predicted MVP is: {predicted_mvp}")


if __name__ == "__main__":
    main()
