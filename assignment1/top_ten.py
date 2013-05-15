from collections import defaultdict
import itertools
import json
import re
import sys

def hw(tweet_file):
    terms = defaultdict(int) 
    global_count = 0
    
    hash_scores = defaultdict(int)
    
    for line in tweet_file:
        tweet = json.loads(line)
    
        if 'entities' in tweet and 'hashtags' in tweet['entities']:
            if  len(tweet['entities']['hashtags']) > 0:
                for hashtag in tweet['entities']['hashtags']:
                    hash_scores[hashtag['text']] += 1
    
    for k, v in sorted(hash_scores.items(), key = lambda x: x[1], reverse=True)[:10]:
        print k, v

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)
    # lines(sent_file)
    # lines(tweet_file)

if __name__ == '__main__':
    main()