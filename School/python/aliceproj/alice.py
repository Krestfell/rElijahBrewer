import pickle
import string
from collections import Counter


def main():
    # Step 1: Open the text file
    with open(r"C:\Users\heyit\Desktop\Projects\GitHub\rElijahBrewer\School\python\aliceproj\AliceInWonderland.txt", encoding='utf-8-sig') as file:
        # Step 2: Count individual words and their frequency
        words = file.read().split()
        words = [word.translate(str.maketrans(
            "", "", string.punctuation)).upper() for word in words]
        word_counts = Counter(words)

    # Step 3: Save the words and their frequency to a text file
    with open(r"C:\Users\heyit\Desktop\Projects\GitHub\rElijahBrewer\School\python\aliceproj\word_counts.txt", "w", encoding='utf-8') as out_file:
        for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True):
            out_file.write(f"{word}: {count}\n")

    # Step 4: Pickle the data structure
    with open(r"C:\Users\heyit\Desktop\Projects\GitHub\rElijahBrewer\School\python\aliceproj\word_counts.pickle", "wb") as file:
        pickle.dump(word_counts, file)

    # Step 5: Unpickle and print the data structure
    with open(r"C:\Users\heyit\Desktop\Projects\GitHub\rElijahBrewer\School\python\aliceproj\word_counts.pickle", "rb") as file:
        unpickled_counts = pickle.load(file)
        print(unpickled_counts)


if __name__ == "__main__":
    main()
