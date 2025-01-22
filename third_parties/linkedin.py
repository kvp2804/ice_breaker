import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url:str, mock: bool = False) :
    """scrape information from linkedIn profiles,
    Manually scrape the information from the linkedIn profile"""

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/kvp2804/5f266663f3e8684f1b158633e01a77e6/raw/e76d602d5dbc753a232cac0fe5eeb021b4795c7a/lang-chain-kp.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response = requests.get(api_endpoint,
                                params={'url': linkedin_profile_url},
                                headers=header_dic,
                                timeout=10)
    data = response.json()

    data = {
            k: v
            for k, v in data.items()
            if v not in ([], "", "", None)
            and k not in ["people_also_viewed", "certifications"]
        }

    if data.get("groups"):
            for group_dict in data.get("groups"):
                group_dict.pop("profile_pic_url")

    return data

if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="www.linkedin.com/in/kaushal-patankar-28ba604/",mock=True
        )

    )