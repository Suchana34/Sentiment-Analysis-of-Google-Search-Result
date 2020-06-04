from textblob import TextBlob
import requests
from bs4 import BeautifulSoup

class Analysis:
    def __init__(self,term):
        self.term = term
        self.subjectivity = 0
        self.sentiment = 0
        self.url = "https://www.google.com/search?q={0}&source=lnms&tbm=nws".format(self.term)


    def scrape(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        page = soup.find_all('div', class_ = "med")
        for p in page:
            blob = TextBlob(p.text)
            self.sentiment += blob.sentiment.polarity/len(page)
            self.subjectivity += blob.sentiment.subjectivity/len(page)
            

a = Analysis('bitcoin')
a.scrape()
print(a.term, 'Subjectivity: ', a.subjectivity, 'Sentiment: ', a.sentiment)

