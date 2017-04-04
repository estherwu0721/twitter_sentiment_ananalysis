import sys
import json
from pprint import pprint

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)

    scores = {}
    for line in sent_file:
        tweet, score = line.split("\t")
        scores[tweet] = int(score)
    
    for line in tweet_file:
        temp = json.loads(line)
        # print data
        score = 0
        if "text" in temp:
            twe = temp["text"]
            twe = twe.encode('ascii', 'ignore')

            twe_words = twe.split(" ")

            for word in twe_words:
                #print word
                if word in scores:
                    score = score + scores.get(word)

            for word in twe_words:
                if word not in scores:
                    print word + " " + str(score)


if __name__ == '__main__':
    main()
