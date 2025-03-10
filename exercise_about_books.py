import requests

# URLs of the two books in plain text format (replace with actual URLs)
book1_url = "https://www.gutenberg.org/cache/epub/1513/pg1513.txt"
#The Adventures of Ferdinand Count Fathom
book2_url = "https://www.gutenberg.org/cache/epub/75570/pg75570.txt"
#Psychology of stock market
# Function to count unique words in a book
def count_unique_words(url):
    punctuation = ",.?!';\":-=(){}"
    response = requests.get(url)
    text = response.text

    unique_words = set()  # Set to store unique words
    lines = text.splitlines()

    for line in lines:
        for p in punctuation:
            line = line.replace(p, " ")
        words = line.split()
        for word in words:
            word = word.lower()
            unique_words.add(word)  # Add word to the set

    return len(unique_words)

# Count unique words in both books
book1_unique_count = count_unique_words(book1_url)
book2_unique_count = count_unique_words(book2_url)

# Print results
print(f"Total unique words in Book 1: {book1_unique_count}")
print(f"Total unique words in Book 2: {book2_unique_count}")

# Determine which book has more unique words
if book1_unique_count > book2_unique_count:
    print("Book 1 has more unique words.")
elif book1_unique_count < book2_unique_count:
    print("Book 2 has more unique words.")
else:
    print("Both books have the same number of unique words.")