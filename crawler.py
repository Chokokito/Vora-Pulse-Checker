import requests as req
import requests.exceptions as req_exceptions
from bs4 import BeautifulSoup 
from typing import List, Dict, Any
websites = [
        'https://g1.globo.com'
    ]

def crawler (websites: List[str]) -> List[Dict[str, Any]]:
    

    sucessful_requests = []


    for site in websites:
        try:
            response = req.get(site)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            print(f"Successfully accessed {site} with status code {response.status_code}")
            soup = BeautifulSoup(response.text, 'html.parser')

            



            website_data = {
                'url': site,
                'status_code': response.status_code,
                'title': soup.title.string if soup.title else 'No title found',
                'content_length': len(response.content)

            }
            
            for link in soup.find_all('a', href=True):
                website_data.setdefault('links', []).append(link['href'])
            # Initialize links if not present

            # Store the data in the list
            sucessful_requests.append(website_data)
            print(f"Title of {site}: {soup.title.string if soup.title else 'No title found'}")
            
        except req_exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred for {site}: {conn_err}")
        except req_exceptions.HTTPError as http_err:
            print(f"HTTP error occurred for {site}: {http_err}")
        except Exception as err:
            print(f"An error occurred for {site}: {err}")


    # Print the collected data
    print("\nCollected data from successful requests:")
    for data in sucessful_requests:
        print(data) 
    return sucessful_requests      # Print the links found on the page        website_data.setdefault('links', [])  # Ensure 'links' is initialized
            
crawler(websites)