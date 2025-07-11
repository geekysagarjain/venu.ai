import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """
    Manuallly scrape information abot a linkedin profile
    """
    if mock:

        linkedin_profile_url = "https://gist.githubusercontent.com/geekysagarjain/b5d6d5d8207e2b740eba176be9b8515b/raw/7446bff1da5ccfe4b1da26acb698069377142fdb/sagar-jain-scraping.json"

        response = requests.get(
            linkedin_profile_url, timeout = 10
        ).json()

        print("printing from hardcoded URL\n")
        return response
        
    else:

        api_endpoint = "https://api.scrapin.io/v1/enrichment/profile"
        params={
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": linkedin_profile_url
        }

        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10
        )
        
        data = response.json().get("person")

        print("printing from scrapin API method\n")
        return data

if __name__ == '__main__':
    print(
        scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/mrsagarjain/", mock=True)
    )