#!/usr/bin/env python

########################################################################
# Filename    : Morse.py
# Description : Make an led blinking.
# auther      : www,my-pi.xyz
# modification: 2017/02/27
########################################################################

from gpiozero import LED
import subprocess as sp

# -----------------------------------------------------------------------
# Module variables
blueLight = LED(17)
yellowLight = LED(18)


# -----------------------------------------------------------------------
# Control the lights
def dash():
    yellowLight.blink(2, 0.5, 1, False)


def dot():
    yellowLight.blink(1, 0.5, 1, False)


def new_output():
    blueLight.blink(0.5, 0.5, 3, False)


# -----------------------------------------------------------------------
# Letters to Morse
def to_morse_code(message):
    morse_code_map = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": ".--",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--.."}

    result = ""
    first_char = True

    for c in message:
        new_char = morse_code_map.get(c, "")
        if new_char == "":
            continue

        if not first_char:
            result += '#'
        else:
            first_char = False

        result += new_char

    return result


def send_morse_code(message):
    for c in message:
        if c == '#':
            new_output()
        if c == '-':
            dash()
        if c == '.':
            dot()


# -----------------------------------------------------------------------
# Program clean up
def destroy():
    blueLight.off()
    yellowLight.off()


# -----------------------------------------------------------------------
# Program main loop
def loop():
    while True:
        sp.call("clear", shell=True)
        # Get user input
        new_word = raw_input("Enter a word (Q to quit): ")
        new_word = new_word.strip().upper()

        if new_word == "":
            continue

        # Wanta cancel?
        if new_word == "Q":
            break

        # send the code baby!
        print "\nSending morse code... eyes on the lights!"
        send_morse_code(to_morse_code(new_word))

        # Pause to let the dog see the rabbit
        raw_input("\nPress enter to continue...")

    destroy()


# -----------------------------------------------------------------------
# Program Start
if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        # When 'Ctrl+C' is pressed we need to clean up and exit.
        destroy()
