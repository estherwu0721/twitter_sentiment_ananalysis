import sys
import json


def hw():
    print 'Hello, world!'


def lines(fp):
    print str(len(fp.readlines()))


def main():
    tweet_file = open(sys.argv[1])
    total = 0
    term_count = {}
    for line in tweet_file:
        temp = json.loads(line)
        if "text" in temp:
            twe = temp["text"]
            twe = twe.encode('ascii', 'ignore')

            twe_words = twe.split(" ")
            count = 1
            for word in twe_words:
                if word in term_count:
                    term_count[word] += 1
                else:
                    term_count.update({word: count})
                total = total + 1

    for word, count in term_count.items():
        p = float(count) / total
        print str(word) + "  " + str(p)


if __name__ == '__main__':
    main()