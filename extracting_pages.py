import requests
from bs4 import BeautifulSoup
import pandas as pd

urls = ["https://www.santander.co.uk/personal/current-accounts/santander-edge-up-current-account",
        "https://www.santander.co.uk/personal/current-accounts/santander-edge-current-account",
        "https://www.santander.co.uk/personal/current-accounts/everyday-current-account",
        "https://www.santander.co.uk/personal/current-accounts/santander-edge-student-current-account",
        "https://www.santander.co.uk/personal/current-accounts/123-mini-current-account",
        "https://www.santander.co.uk/personal/current-accounts/basic-current-account"]


def get_url_content(urls_list):
    text_content = {}
    for url in urls_list:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        text_content[url] = soup.get_text()
    return text_content


result = pd.DataFrame((get_url_content(urls)).items(), columns=['url','content'])
print(result)
result.to_csv("current_accounts.csv")
