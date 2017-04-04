import sys
import json
import operator


def hw():
    print 'Hello, world!'


def lines(fp):
    print str(len(fp.readlines()))


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)

    scores = {}
    for line in sent_file:
        tweet, score = line.split("\t")
        scores[tweet] = int(score)
        #print scores.items()

    place_sent = {}
    for line in tweet_file:
        temp = json.loads(line)
        score = 0

        if "place" in temp:
            if (score == 0):
                place = temp["place"]

                if (place != None):
                    country = place["country_code"]
                    if (country == "US"):
                        place_name = place["full_name"]
                        place_name = place_name.split(", ")
                        state = place_name[1]

                    if "text" in temp:
                        twe = temp["text"]
                        twe = twe.encode('ascii', 'ignore')

                        twe_words = twe.split(" ")

                    for word in twe_words:
                        # print word
                        if word in scores:
                            score = score + scores.get(word)

                        if state in place_sent:
                                place_sent[state] = (float(place_sent[state]) + score) / 2
                        else:
                            place_sent.update({place_name: score})

    print max(place_sent.iteritems(), key=operator.itemgetter(1))[0]


if __name__ == '__main__':
    main()