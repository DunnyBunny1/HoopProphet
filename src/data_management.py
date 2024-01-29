import pandas as pd


def load_yearly_mvp_data(year):
    """
    Load MVP data from an HTML file for a specific year.

    :param year: Year for data loading.
    :return a DataFrame formed by reading the scraped and downloaded HTML table
    corresponding to the given year
    :rtype pd.DataFrame
    :raises FileNotFoundError: If HTML file is not found.
    :raises ValueError: If no tables are in the HTML file.
    """
    file_path_template = 'src/yearly_mvp_data/{}.html'
    file_path = file_path_template.format(year)
    try:
        # Load the data from the html for each year into a pandas DataFrame
        # The mvp table is the 0th table in the html
        return pd.read_html(file_path)[0]
    except FileNotFoundError:
        raise FileNotFoundError(f"File for year {year} not found.")
    except ValueError:
        raise ValueError(f"No table found in file for year {year}.")


def create_yearly_mvp_csv(years):
    """
    Process and combine yearly MVP data from HTML files into a single DataFrame.
    Write the dataframe to a CSV

    :param years: A list of years for which the MVP data needs to be processed.
    :type years: list of int

    :return: A dataframe formed by concatenatinging each yearly MVP dataframe.
    Each yearly MVP dataframe is formed by reading the html table for the year
    :rtype pd.DataFrame

    :raises FileNotFoundError: If an HTML file for a specified year is not found.
    :raises ValueError: If the HTML file does not contain any tables.
    """
    dataframe_list = []  # Store a list to hold all of our dataframes
    for year in years:
        curr_df = load_yearly_mvp_data(year)
        # Add a year column to the current df
        curr_df['Year'] = year
        dataframe_list.append(curr_df)
    # Combine all yearly DataFrames into a single DataFrame
    mvp_df: pd.DataFrame = pd.concat(dataframe_list)
    # Now we have one data frame with all mvp voting from 1991 - 2022
    # Store the data in csv format
    mvp_df.to_csv('src/mvp_voting_1991-2022.csv')
    return mvp_df


def create_full_dataframe():
    pass
