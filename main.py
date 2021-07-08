import string
import random

from Wdgraph.Wdgraph import Wdgraph

def clean_text(text):
    # turn into words
    words = text.split(" ")
    # remove puncutation
    # table = str.maketrans("", "", string.punctuation)
    # words = [word.translate(table) for word in words]
    # normalize case
    words = [word.lower() for word in words]

    return words

def increment_edge(graph, first, second):
    try:
        current = graph.get_edge(first, second)
        graph.set_edge(first, second, current + 1)
    except Exception:
        graph.set_edge(first, second, 1)


def main():
    graph = Wdgraph()

    with open("shakespeare.txt", "r") as file:
        text = file.read()

    amt = int(input("How many more words would you like? "))

    words = clean_text(text)

    # load into markov chain
    for first, second in zip(words, words[1:]):
        increment_edge(graph, first, second)

    # make cyclical so that the last word is guaranteed that have an outneighbor
    increment_edge(graph, words[-1], words[0])

    # generate markov chain
    graph.create_probability_graph()

    # randomly select first word
    current_word = graph.directmap[random.randint(0, len(graph) - 1)]
    output = [current_word]

    for _ in range(amt - 1):
        neighbor_data = graph.get_outneighbors(current_word)
        neighbors = [neighbor for neighbor, prob in neighbor_data]
        probs = [prob for neighbor, prob in neighbor_data]

        current_word = random.choices(population=neighbors, weights=probs)[0]

        output.append(current_word)

    output = " ".join(output)

    print(output)


if __name__ == "__main__":
    main()
