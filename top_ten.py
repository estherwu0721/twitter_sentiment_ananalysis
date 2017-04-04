import sys
import json
import operator

def hw():
    print 'Hello, world!'


def lines(fp):
    print str(len(fp.readlines()))


def main():
    dic = {}
    count = 1
    tweet_file = open(sys.argv[1])
    for line in tweet_file:
        temp = json.loads(line)

        if "entities" in temp:
            entities = temp["entities"]

            hashtags = entities["hashtags"]

            for hashtag in hashtags:

                tag = hashtag["text"]
                tag = tag.encode('ascii', 'ignore')
                if tag in dic:
                    dic[tag] += 1
                else:
                    dic.update({tag: count})

    sorted_dic = sorted(dic.iteritems(), key=operator.itemgetter(1), reverse=True)

    i = 0
    for j in sorted_dic:
        i+=1
        while (i <= 10):
            print j[0] + "\t" + str(j[1])


if __name__ == '__main__':
    main()