import sys
import itertools
from collections import defaultdict

# find frequent pairs (local chunk)
def apriori(data):
    items_count = defaultdict(lambda: 0)
    N = 0
    for line in data:
        N += 1
        words = line.split()
        for w in words:
            items_count[w] += 1

    s = 0.005
    frequentItems = set()
    for item, count in sorted(items_count.items(), key=lambda item: item[1], reverse=True):
        if count >= s*N:
            frequentItems.add(item)
        else:
            break

    pairs_count = defaultdict(lambda: 0)
    for line in data:
        words = line.split()
        for pair in itertools.combinations(set(words).intersection(frequentItems), 2):
            pairs_count[tuple(sorted(pair))] += 1

    frequentPairs = {}  # dict(pair: count)
    for pair, count in sorted(pairs_count.items(), key=lambda item: item[1], reverse=True):
        if count >= s*N:
            frequentPairs[pair] = count
        else:
            break

    return frequentPairs


data = sys.stdin.readlines() # for the 2 passes in A-priori
frequentPairs = apriori(data)
# emit all candidate frequent pairs
for pair in frequentPairs:
    print('%s,%s\t%d' % (pair[0], pair[1], frequentPairs[pair]))

