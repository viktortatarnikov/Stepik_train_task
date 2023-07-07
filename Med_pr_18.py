with open('words.txt', 'r', encoding='utf-8') as file:
    words = file.read().strip().split()
    for word in words:
        if len(word) == len(max(words, key=len)):
            print(word)
