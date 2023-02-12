from art import logo2

print(logo2)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

def caesar(text, shift, direction):
    end = ''
    if direction == "decode":
        shift *= -1

    for x in text:
        if x in alphabet:
            position = alphabet.index(x)
            new_position = position + shift
            new_position %= 26
            end += alphabet[new_position]
        else:
            end += x
    print(f"Here's the {direction}d result: {end}")

stop = False
while not stop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)

    choice = input("Do you want to continue? Yes(Y) or No(N)").lower()
    if choice == 'n':
        stop = True

