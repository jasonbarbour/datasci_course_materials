from collections import defaultdict
import itertools
import json
import re
import sys

def hw(tweet_file):
    terms = defaultdict(int) 
    global_count = 0
    
    for line in tweet_file:
        tweet = json.loads(line)
    
        if ('lang' in tweet and tweet['lang'] == 'en') or ('lang' not in tweet):
            if 'text' in tweet:
                # tweet['text'] = re.sub(u'[!?@#$.,#:\u2026]', '', tweet['text'])
                words = tweet['text'].split()
                for word in words:
                    word.strip()
                    if len(word):
                        terms[word] += 1
                        global_count += 1
    
    for k, v in terms.items():
        print k, float (v) / global_count

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)
    # lines(sent_file)
    # lines(tweet_file)

if __name__ == '__main__':
    main()