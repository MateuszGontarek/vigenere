def vigenere(text, key, want):
    result = ''

    for i in range(len(text)):
        if text[i].isalpha():
            toAdd = ord("A") if text[i].isupper() else ord("a")
            keyLetter = ord(key[i % len(key)]) if want == "encrypt" else - ord(key[i % len(key)])
            result += chr((ord(text[i]) + keyLetter - toAdd) % 26 + toAdd)
        else:
            result += text[i]

    return result