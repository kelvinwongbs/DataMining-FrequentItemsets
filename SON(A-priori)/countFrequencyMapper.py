import sys
import itertools

# mapper: read candidate pairs
candidatePairs = set()
for line in sys.stdin:
    pair, value = line.strip().split('\t', 1)
    w = pair.split(',')
    candidatePairs.add((w[0], w[1]))
# cleanup: count frequency of candidate pairs
N = 0
with open("shakespeare_basket1", "r") as f:
    for line in f:
        N += 1
        words = line.split()
        for pair in itertools.combinations(words, 2):
            sort_pair = tuple(sorted(pair))
            if  sort_pair in candidatePairs:
                print('%s,%s\t1' % (sort_pair[0], sort_pair[1]))
with open("shakespeare_basket2", "r") as f:
    for line in f:
        N += 1
        words = line.split()
        for pair in itertools.combinations(words, 2):
            sort_pair = tuple(sorted(pair))
            if sort_pair in candidatePairs:
                print('%s,%s\t1' % (sort_pair[0], sort_pair[1]))
print('N\t%d' % N)
