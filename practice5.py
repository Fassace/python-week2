# Program 5: Create a new list with words that have an odd number of characters
def odd_length_words():
    words = ["apple", "banana", "grape", "kiwi", "strawberry"]
    odd_words = [word for word in words if len(word) % 2 != 0]
    return words, odd_words

# Program 5
words, odd_words = odd_length_words()
print("Original List of Words:", words)
print("Words with Odd Number of Characters:", odd_words)