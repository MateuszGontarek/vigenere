def vigenere(text, key, want):
    result, letterCount = '', 0

    for i in text:
        if i.isalpha():
            keyLetter = ord(key[letterCount % len(key)]) - ord('A') \
                        if key[letterCount % len(key)].isupper() \
                        else ord(key[letterCount % len(key)]) - ord('a')
            keyLetter = keyLetter if want == "encrypt" else - keyLetter
            toAdd = ord('A') if i.isupper() else ord('a')
            result += chr((ord(i) + keyLetter - toAdd) % 26 + toAdd)
            letterCount += 1
        else:
            result += i
    return result
