import sys
import json
import re

def hw(sent_file, tweet_file):
    scores = build_sentiment_dictionary(sent_file)
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
                print score

    
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
