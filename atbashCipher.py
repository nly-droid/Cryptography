# This is the comment section. Written on 14/11/2019. I am in the library. This is the worst reading week ever.
# Seems like I overuse functions. Dunno why.
# This is a comment on August 20th, 2020. I am in Vietnam now.
# I am about to exploded since I'm not allowed to turn on the light.
# I was excited to live with other girls, but I soon realized that it is a disaster.


def atbash(string):
    # The function that translates a coded line.
    new_string = ""

    def new_character(char, first, last):  # The function that translates a coded character.
        new_char = chr((first - ord(char)) + last)  # Turn the character into its reverse version. Works both way.
        return new_char

    for character in string:
        if character.isalpha():  # Only translates characters in the alphabet.
            if character.islower():
                # Translate capital and lower-case letters require different first and last numbers.
                new_string += new_character(character, 97, 122)
            else:
                new_string += new_character(character, 65, 90)
        else:
            new_string += character
    return new_string


# Main body.
def main():
    print("Atbash cipher")
    print("You can enter as many lines as you like. Please enter a blank line after you're done.")
    inputString = input("Please type the message:\n")
    text = []
    # Type and translate multiple lines. While not a blank line, keep adding line to a list.
    while inputString != "":
        text.append(inputString)
        inputString = input()
    for line in text:
        atbashLine = atbash(line)
        print(atbashLine)


main()
