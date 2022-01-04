import itertools
from collections import defaultdict

items_count = defaultdict(lambda: 0)
hashpairs_count = defaultdict(lambda: 0)
N = 0
f = open("shakespeare_basket1", "r")
for line in f:
    N += 1
    words = line.split()
    # count items
    for w in words:
        items_count[w] += 1
    # hash pairs
    for pair in itertools.combinations(words, 2):
        w1, w2 = sorted(pair)[0], sorted(pair)[1]
        hashpairs_count[hash(w1 + w2) % 100000] += 1
f.close()
f = open("shakespeare_basket2", "r")
for line in f:
    N += 1
    words = line.split()
    # count items
    for w in words:
        items_count[w] += 1
    # hash pairs
    for pair in itertools.combinations(words, 2):
        w1, w2 = sorted(pair)[0], sorted(pair)[1]
        hashpairs_count[hash(w1 + w2) % 100000] += 1
f.close()

s = 0.005
frequentItems = set()
for item, count in sorted(items_count.items(), key=lambda item: item[1], reverse=True):
    if count >= s*N:
        frequentItems.add(item)
    else:
        break

pairs_count = defaultdict(lambda: 0)
f = open("shakespeare_basket1", "r")
for line in f:
    words = line.split()
    for pair in itertools.combinations(set(words).intersection(frequentItems), 2):
        # check frequent bucket
        w1, w2 = sorted(pair)[0], sorted(pair)[1]
        if hashpairs_count[hash(w1 + w2) % 100000] >= s*N:
            pairs_count[(w1, w2)] += 1
f.close()
f = open("shakespeare_basket2", "r")
for line in f:
    words = line.split()
    for pair in itertools.combinations(set(words).intersection(frequentItems), 2):
        # check frequent bucket
        w1, w2 = sorted(pair)[0], sorted(pair)[1]
        if hashpairs_count[hash(w1 + w2) % 100000] >= s*N:
            pairs_count[(w1, w2)] += 1
f.close()

frequentPairs = {}
for pair, count in sorted(pairs_count.items(), key=lambda item: item[1], reverse=True):
    if count >= s*N:
        frequentPairs[pair] = count
    else:
        break

topFrequent = dict(itertools.islice(frequentPairs.items(), 40))
for pair in topFrequent:
    print ('{}: {}'.format(pair, topFrequent[pair]))
