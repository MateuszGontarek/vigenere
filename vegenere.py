def encode_with_vigenere(text, key, want):
    result = ''

    for i in range(len(text)):
        if text[i].isalpha():

            toAdd = ord("A") if text[i].isupper() else ord("a")
        
            if want == 'encrypt':
                result += chr((ord(text[i]) + ord(key[i % len(key)]) - toAdd) % 26 + toAdd)
            else:
                result += chr((ord(text[i]) - ord(key[i % len(key)]) - toAdd) % 26 + toAdd)
        else:
            result += text[i]

    return result