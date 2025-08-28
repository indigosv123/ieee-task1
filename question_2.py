def find_palindromes(sentence):
    import string

    # Remove punctuation
    for char in string.punctuation:
        sentence = sentence.replace(char, "")

    
    palindrome_list = []
    words = sentence.split()

    for word in words:
        word = word.lower()
        if word == word[::-1]:
            palindrome_list.append(word)
    
    return palindrome_list


    return palindromes if palindromes else [0]

# Input
sentence = input("Enter a sentence: ")
print(find_palindromes(sentence))




