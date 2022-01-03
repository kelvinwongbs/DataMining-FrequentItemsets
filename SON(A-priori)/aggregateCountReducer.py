import sys
from operator import itemgetter
from itertools import groupby
from collections import defaultdict


# generator for data input
def read_mapper_output(input):
    for line in input:
        yield line.rstrip().split('\t', 1)

data = read_mapper_output(sys.stdin)
pairs_count = defaultdict(lambda: 0)
N = 0
# reducer
# iterate keys
for key, key_value in groupby(data, itemgetter(0)):
    count = 0
    # iterate values
    for key, value in key_value:
        count += 1
        if key == 'N':
            N = count
        else:
            w = key.split(',')
            pairs_count[(w[0], w[1])] = count
# cleanup: find true frequent pairs
frequentPairs = {}
s = 0.005
for pair, count in sorted(pairs_count.items(), key=lambda item: item[1], reverse=True):
    if count >= s*N:
        frequentPairs[pair] = count
    else:
        break
for pair in frequentPairs:
    print('(%s, %s)\t%d' % (pair[0], pair[1], frequentPairs[pair]))