import time
import requests

years = [year for year in range(1991, 2023)]


def make_http_req(url):
    """
    Make a GET request to the given URL with retries.

    :param url: The URL to send the GET request to.
    :return: Response object if successful.
    :raises InvalidURL: If the URL is unknown.
    :raises TooManyRedirects: If max retries are reached due to too many
    redirects.
    :raises RequestException: For unknown request errors.
    """
    retry_count = 3
    # Send a GET request to the URL
    while retry_count > 0:
        response = requests.get(url)
        if response.status_code in (400, 404):  # Indicates a bad request
            raise requests.exceptions.InvalidURL(f"{url} is an unknown URL")
        elif response.status_code == 429:  # Indicates too many requests
            retry_count -= 1
            # Sleep for 10 seconds before making a new request
            time.sleep(10)
        elif response.status_code != 200:  # Indicates some unknown error
            raise requests.exceptions.RequestException(
                f"Error with status code {response.status_code}encountered"
            )
        else:  # If we are here, we made a successful request
            return response
    # If we are here, we ran out of retries
    raise requests.exceptions.TooManyRedirects(
        f"Reached maximum retries for url {url}."
    )
