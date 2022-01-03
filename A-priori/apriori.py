import itertools
from collections import defaultdict

# first pass: find frequent items
items_count = defaultdict(lambda: 0)
N = 0
f = open("shakespeare_basket1", "r")
for line in f:
    N += 1
    words = line.split()
    for w in words:
        items_count[w] += 1
f.close()
f = open("shakespeare_basket2", "r")
for line in f:
    N += 1
    words = line.split()
    for w in words:
        items_count[w] += 1
f.close()

s = 0.005
frequentItems = set()
for item, count in sorted(items_count.items(), key=lambda item: item[1], reverse=True):
    if count >= s*N:
        frequentItems.add(item)
    else:
        break

# second pass: find frequent pairs
pairs_count = defaultdict(lambda: 0)
f = open("shakespeare_basket1", "r")
for line in f:
    words = line.split()
    for pair in itertools.combinations(set(words).intersection(frequentItems), 2):
        pairs_count[tuple(sorted(pair))] += 1
f.close()
f = open("shakespeare_basket2", "r")
for line in f:
    words = line.split()
    for pair in itertools.combinations(set(words).intersection(frequentItems), 2):
        pairs_count[tuple(sorted(pair))] += 1
f.close()

frequentPairs = {}
for pair, count in sorted(pairs_count.items(), key=lambda item: item[1], reverse=True):
    if count >= s*N:
        frequentPairs[pair] = count
    else:
        break

# output the top 40 most frequent pairs
topFrequent = dict(itertools.islice(frequentPairs.items(), 40))
for pair in topFrequent:
    print ('{}: {}'.format(pair, topFrequent[pair]))
