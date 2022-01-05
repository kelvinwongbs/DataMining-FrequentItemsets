# Find frequent pairs using A-priori, PCY and SON algorithms

### Course: Web-scale Information Analytics

Dataset: Shakespeare text  
Data are preprocessed by applying sliding window, each window represents a basket

**Threshold of frequent pairs is defined as s=0.005**  

**A-priori**  
First pass:  
count frequency of each item, find all the frequent items

Candidate frequent pair iff it is formed by frequent items

Second pass:  
count frequency of each candidate frequent pair, find the true frequent pairs

**PCY**  
First pass:  
count frequency of each item, find all the frequent items  
hash all the pairs to buckets and keep a count for each bucket  
*Define hash function = hash(word1 + word2) % 100000*

Candidate frequent pair iff it is formed by frequent items AND hashed to a frequent bucket

Second pass:  
count frequency of each candidate frequent pair, find the true frequent pairs

**SON (using Hadoop streaming)**  
First MapReduce job:  
**aprioriMapper.py**: each mapper takes a subset of the dataset, finds all the frequent pairs in the subset using A-priori (can be replaced by PCY)  
**candidatePairReducer.py**: combine the frequent pairs of all subsets, output them as candidate frequent pairs

Candidate frequent pair iff it is a frequent pair of some subset of the dataset

Second MapReducer job:  
**countFrequencyMapper.py**: each mapper takes a subset of the dataset, count frequency of each candidate frequent pair in the subset  
**aggregateCountReducer.py**: aggregate the counts from all subsets, find the true frequent pairs
