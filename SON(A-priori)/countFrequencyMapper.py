import sys
import itertools

# setup: read candidate pairs
candidatePairs = set()
with open("candidate_pairs", "r") as f:
    for line in f:
        pair, value = line.strip().split('\t', 1)
        w = pair.split(',')
        candidatePairs.add((w[0], w[1]))

# mapper
N = 0
for line in sys.stdin:
    N += 1
    words = line.split()
    for pair in itertools.combinations(words, 2):
        sort_pair = tuple(sorted(pair))
        if  sort_pair in candidatePairs:
            print('%s,%s\t1' % (sort_pair[0], sort_pair[1]))
print('N\t%d' % N)
