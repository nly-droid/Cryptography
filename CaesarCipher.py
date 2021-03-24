def caesar(string, key, process):
    new_string = ""

    def new_character(char, key, start):
        if process == 'e':
            new_char = (((ord(char) + key) - start) % 26) + start
        if process == 'd':
            new_char = (((ord(char) - key) - start) % 26) + start
        return chr(new_char)

    for character in string:
        if character.isalpha():
            if character.islower():
                character = new_character(character, key, 97)
            else:
                character = new_character(character, key, 65)
        new_string += character
    return new_string


def main():
    print("This is Caesar Cipher.")
    process = input("Do you want to encrypt or decrypt the text? Enter 'e' or encrypt and 'd' for decrypt.\n")
    while process != 'e' and process != 'd':
        process = input("Enter 'e' for encrypt, 'd' for decrypt or a blank line to stop the program.\n")
        if process == '':
            return
    key = int(input("Please type the key: "))
    print("You can enter as many lines as you like. Please enter a blank line after you're done.")
    inputString = input("Please type the message:\n")
    text = []
    while inputString != "":
        text.append(inputString)
        inputString = input()
    for line in text:
        secretText = caesar(line, key, process)
        print(secretText)


main()
