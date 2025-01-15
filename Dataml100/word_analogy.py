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


def find_closest_words(input_vector, W, ivocab, top_2=2):
    # Function to find the closest words by Euclidean distance
    distances = []
    for i in range(W.shape[0]):
        distance = eulidean_distance(input_vector, W[i, :])
        distances.append((i, distance))
    # Sort by similiarity and get top 2
    sorted_distances = sorted(distances, key=lambda x: x[1])
    closest_indices = [index for index, _ in sorted_distances[:top_2]]
    closest_words = [ivocab[index] for index in closest_indices]

    return closest_words


# Main loop for analogy
while True:
    words = []
    for i in range(0, 3):
        input_term = input("\nEnter word (EXIT to break): ")
        if input_term == "EXIT":
            exit()
        words.append(input_term)
    x_term = words[0]
    y_term = words[1]
    z_term = words[2]
    if x_term not in vocab or y_term not in vocab or z_term not in vocab:
        print("Some of the words are not in vocab")
        continue
    else:
        analogy_vector = W[vocab[z_term], :] + (
            W[vocab[y_term], :] - W[vocab[x_term], :]
        )  # Get vector for the analogy
        result_words = find_closest_words(analogy_vector, W, ivocab, top_2=2)  # 2 closest words
        print(*result_words, sep = "\n")
