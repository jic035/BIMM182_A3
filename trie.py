import sys
import argparse
import math

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, text):
        results = {}
        for i in range(len(text)):
            node = self.root
            j = i
            while j < len(text) and text[j] in node.children:
                node = node.children[text[j]]
                if node.is_end_of_word:
                    word = text[i:j+1]
                    if word not in results:
                        results[word] = 0
                    results[word] += 1
                j += 1
        return results

def load_dna_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    # Skip the header line and remove newline characters
    dna_sequence = ''.join(line.strip() for line in lines[1:])
    return dna_sequence

def load_queries_file(filename):
    with open(filename, 'r') as file:
        return file.read().strip().split('\n')

def calculate_e_value(length_of_keyword, length_of_database):
    return (length_of_database - length_of_keyword + 1) * (0.25 ** length_of_keyword)

def write_results_to_file(filename, data):
    with open(filename, 'w') as file:
        for line in data:
            file.write(f"{line[0]}, {line[1]}, {line[2]:.8f}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Search DNA sequences for keywords and calculate their E-values.')
    parser.add_argument('dna_file', type=str, help='Filename of the DNA data')
    parser.add_argument('queries_file', type=str, help='Filename of the query keywords')
    parser.add_argument('-o', '--output', type=str, default='output.txt', help='Output file name')
    
    args = parser.parse_args()

    # Load data
    database_sequence = load_dna_file(args.dna_file)
    queries = load_queries_file(args.queries_file)

    # Initialize Trie
    trie = Trie()

    for query in queries:
        trie.insert(query)

    # Search database sequence
    matches = trie.search(database_sequence)

    # Calculate and output E-values for queries
    length_of_database = len(database_sequence)
    results = []

    for query in queries:
        e_value = calculate_e_value(len(query), length_of_database)
        match_count = matches.get(query, 0)
        results.append((query, match_count, e_value))

    # Write results to file
    write_results_to_file(args.output, results)
