import urllib
import json


def print_tweets(pages):
    for page in range(1,pages + 1):
        response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft&page=" + str(page))
        pyresponse = json.load(response)
        
        results = pyresponse['results']
        for result in results:
            print result['text']
            
if __name__ == "__main__":
    print_tweets(10)