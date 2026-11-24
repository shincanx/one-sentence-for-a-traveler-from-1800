#!/usr/bin/env python3
"""One sentence explaining the modern internet to a traveler from 1800.

Prints the sentence and writes it to /output/entry.txt, as the bounty
requires. Every word in the sentence predates 1800: a letter, copper
wires, lightning, a parlour, books.
"""

import os

SENTENCE = "A letter that talks back, racing along copper wires swift as lightning, so the whole world may sit in your parlour, speak, and open its books to you."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    print(SENTENCE)

if __name__ == "__main__":
    main()
