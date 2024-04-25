# --------------- IMPORT ART --------------- #
from logo import logo

# --------------- CREATE MORSE CODE DICTIONARY --------------- #
with open("morse.csv", mode="r") as file:
    contents = file.read()

morse_code_list = [item for item in contents.replace("\n", ",").split(",")]
morse_code_dict = dict([(key, value) for key, value in zip(morse_code_list[::2], morse_code_list[1::2])])

# --------------- ADD SYMBOLS TO MORSE CODE DICTIONARY --------------- #
symbol_morse_code = {
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    '"': ".-..-.",
    "$": "...-..-",
    "@": ".--.-.",
    " ": "/",
}

for key in symbol_morse_code:
    morse_code_dict[key] = symbol_morse_code[key]

symbols_list = [key for key in symbol_morse_code]


# --------------- FUNCTIONS --------------- #
def convert_text(text):
    text_chars = list(text)
    output_list = [morse_code_dict[char] for char in text_chars]
    output = " ".join(output_list)
    return output


# --------------- USER INPUT --------------- #
app_on = True

print(logo)
print("Welcome to the Morse Code Converter!")


while app_on:
    user_text = input("Type the text to be converted below! Press <ENTER> when completed.\n").upper()

    try:
        translated_text = convert_text(user_text)
        print(f"\nThe translated text is: {translated_text}")

    except KeyError:
        print(f"\nSorry! You typed a character that cannot be converted to Morse Code. Please use only letters, "
              f"numbers, and the following characters: {' '.join(symbols_list)}")

    finally:
        start_again = input("Would you like to convert something else? Type Y to continue: ").upper()

        if start_again != "Y":
            print("\nThank you! The Morse Code Converter is closed.")
            app_on = False
