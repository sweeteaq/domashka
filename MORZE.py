morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---','K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
    'T': '-','U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..','0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',' ': '/'}
def encode_to_morse_code(text):
    text = text.upper()
    morse_code = []
    for ch in text:
        if ch in morse:
            morse_code.append(morse[ch])
        else:
            morse_code.append(ch)
    return ' '.join(morse_code)
inp_text = input("Введите строку для кодирования в азбуке Морзе: ")
en_text = encode_to_morse_code(inp_text)
print("Закодированная строка в азбуке Морзе:")
print(en_text)



