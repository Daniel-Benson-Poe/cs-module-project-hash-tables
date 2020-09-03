import random

def markov():
    # Read in all the words in one go
    with open("input.txt") as f:
        words = f.read()

    # TODO: analyze which words can follow other words
    # Your code here
    words = words.split()
    word_dict = {}

    for i in range(len(words)):
        if i + 1 > len(words) - 1:
            continue
        else:
            if words[i] in word_dict.keys():
                word_dict[words[i]].append(words[i + 1])
            else:

                word_dict[words[i]] = [words[i + 1]]

    return word_dict

# TODO: construct 5 random sentences
# Your code here
if __name__ == "__main__":
    word_dict = markov()
    starting_words = ["Alice", "She", "And", "I", "Well", "Just", "Here"]
    for i in range(6):
        choice = random.choice(starting_words)
        new_sentence = [choice]
        for _ in range(10):
            choice = random.choice(word_dict[choice])
            new_sentence.append(choice)

        for word in new_sentence:
            print(word, end=" ")
