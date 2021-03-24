def decrypt(string, key):
    def new_character(char, key, start):
        new_char = (((ord(char) - key) - start) % 26) + start
        return chr(new_char)

    new_string = ""
    for character in string:
        if character.isalpha():
            if character.islower():
                character = new_character(character, key, 97)
            else:
                character = new_character(character, key, 65)
        new_string += character
    return new_string


def main():
    print("This is Caesar Cipher, for decoding only.")
    key = int(input("Please type the key: "))
    print("You can enter as many lines as you like. Please enter a blank line after you're done.")
    inputString = input("Please type the message:\n")
    text = []
    while inputString != "":
        text.append(inputString)
        inputString = input()
    for line in text:
        secretText = decrypt(line, key)
        print(secretText)


main()
