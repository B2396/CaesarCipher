import string

alphabet = list(string.ascii_lowercase)


def encode(text, encode_key):
    encoded_text = ""
    for letter in text:
        if letter != " ":
            lindex = alphabet.index(letter)
            x = encode_key
            while x > 0:
                if lindex + 1 > len(alphabet) - 1:
                    lindex = 0
                else:
                    lindex += 1
                x -= 1
            encoded_text += alphabet[lindex]
        else:
            encoded_text += " "
    print(encoded_text)


def decode(text, encode_key):
    decoded_text = ""
    for letter in text:
        if letter == " ":
            decoded_text += " "
        else:
            x = encode_key
            lindex = alphabet.index(letter)
            while x > 0:
                if lindex - 1 < 0:
                    lindex = len(alphabet) - 1
                else:
                    lindex -= 1
                x -= 1
            decoded_text += alphabet[lindex]
    print(decoded_text)


method = input("What would you like to do (encode / decode)?:   ")
text = input("What is the word you would like to encode?:   ")
encode_key = int(input("What is the encoding key?:  "))

if method == "encode":
    encode(text, encode_key)
elif method == "decode":
    decode(text, encode_key)
else:
    print("You typed that wrong!")
