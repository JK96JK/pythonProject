import random
import numpy as np

vocabulary_file = "word_embeddings.txt"

# Read words
print("Read words...")
with open(vocabulary_file, "r", encoding="utf-8") as f:
    words = [x.rstrip().split(" ")[0] for x in f.readlines()]

# Read word vectors
print("Read word vectors...")
with open(vocabulary_file, "r", encoding="utf-8") as f:
    vectors = {}
    for line in f:
        vals = line.rstrip().split(" ")
        vectors[vals[0]] = [float(x) for x in vals[1:]]

vocab_size = len(words)
vocab = {w: idx for idx, w in enumerate(words)}
ivocab = {idx: w for idx, w in enumerate(words)}

# Vocabulary and inverse vocabulary (dict objects)
print("Vocabulary size")
print(len(vocab))
print(vocab["man"])
print(len(ivocab))
print(ivocab[10])

# W contains vectors for
print("Vocabulary word vectors")
vector_dim = len(vectors[ivocab[0]])
W = np.zeros((vocab_size, vector_dim))
for word, v in vectors.items():
    if word == "<unk>":
        continue
    W[vocab[word], :] = v
print(W.shape)


def eulidean_distance(vec_1, vec_2):
    # Function to calculate Euclidean distance, aka distance between two points.
    return np.linalg.norm(vec_1 - vec_2)


def find_closest_words(input_vector, W, ivocab, top_3=3):
    # Function to find the closest words by Euclidean distance
    distances = []
    for i in range(W.shape[0]):
        distance = eulidean_distance(input_vector, W[i, :])
        distances.append((i, distance))
    # Sort by similiarity and get top 3
    closest = sorted(distances, key=lambda x: x[1])[:top_3]
    return [(ivocab[idx], dist) for idx, dist in closest]


# Main loop for analogy
while True:
    input_term = input("\nEnter word (EXIT to break): ")
    if input_term == "EXIT":
        break
    else:
        input_vector = W[vocab[input_term], :]  # Get vector for the input word
        top_3 = find_closest_words(input_vector, W, ivocab, top_3=3)
        print("\n                               Word       Distance\n")
        print("---------------------------------------------------------\n")
        for word, distance in top_3:
            print("%35s\t\t%f\n" % (word, distance))
