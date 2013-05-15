import sys
import json
import re
from collections import defaultdict
import itertools

def hw(sent_file, tweet_file):
    scores = build_sentiment_dictionary(sent_file)
    
    unknown_scores = defaultdict(lambda: defaultdict(int))    
    
    for line in itertools.islice(tweet_file, 15):
        tweet = json.loads(line)
            
        if ('lang' in tweet and tweet['lang'] == 'en') or ('lang' not in tweet):
            if 'text' in tweet:
                tweet['text'] = re.sub(u'[!?@#$.,#:\u2026]', '', tweet['text'])
                words = tweet['text'].split(' ')
                score = 0
                unknown_words = []
                for word in words:
                    if word in scores:
                        score += scores[word]
                    else:
                        unknown_words.append(word)
                for word in unknown_words:
                    unknown_scores[word]['score'] += score
                    unknown_scores[word]['count'] += 1
                
    for k, v in unknown_scores.items():
        print k, float (v['score']) / v['count']

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
