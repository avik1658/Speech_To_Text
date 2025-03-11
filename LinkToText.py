import requests
from bs4 import BeautifulSoup

def extract_text_from_webpage(url):
    """Extract visible text from a webpage."""
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")
        return ""

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract visible text from paragraphs
    text = "\n".join([p.get_text() for p in soup.find_all("p")])
    
    return text

# Webpage URL
webpage_link = "https://www.freecodecamp.org/news/best-practices-for-react/"

# Extract text
text = extract_text_from_webpage(webpage_link)

# Print extracted text
print(text)

