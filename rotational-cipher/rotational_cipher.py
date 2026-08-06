def rotate(text, key):
    ciphered_text = ''

    for character in text:
        if character.isalpha():
            base = ord("A") if character.isupper() else ord("a")
            ciphered_text += chr((ord(character) - base + key) % 26 + base)
        else:
            ciphered_text += character
    return ciphered_text