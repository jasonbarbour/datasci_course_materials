import sys
import json
import re
import pprint
from collections import defaultdict

def hw(sent_file, tweet_file):
    scores = build_sentiment_dictionary(sent_file)
    states = defaultdict(int)
    for line in tweet_file:
        tweet = json.loads(line)
        
        if ('lang' in tweet and tweet['lang'] == 'en') or ('lang' not in tweet):
            if 'text' in tweet:
                tweet['text'] = re.sub(u'[!?@#$.,#:\u2026]', '', tweet['text'])
                words = tweet['text'].split(' ')
                score = 0
                for word in words:
                    if word in scores:
                        score += scores[word]
                        
                if 'place' in tweet and tweet['place'] is not None:
                    place = tweet['place']
                    if 'full_name' in place:
                        full_name = place['full_name'].split(',')
                        if len(full_name) == 2:
                            match = re.search(r'\b[a-z]{2}\b', full_name[1], re.I)
                            if match is not None:
                                state = match.group(0).upper()
                                states[state] += score
                elif 'user' in tweet and tweet['user'] is not None:
                    user = tweet['user']
                    if 'location' in user and user['location'] is not None and len(user['location']) > 0:
                        match = re.search(r'\b[a-z]{2}\b', user['location'], re.I)
                        if match is not None:                        
                            state =  match.group(0).upper()
                            states[state] += score
                
    print max(states.items(), key=lambda x: x[1])[0]
    
def build_sentiment_dictionary(afinnfile):
    scores = {}
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    return scores

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)
    # lines(sent_file)
    # lines(tweet_file)

if __name__ == '__main__':
    main()
