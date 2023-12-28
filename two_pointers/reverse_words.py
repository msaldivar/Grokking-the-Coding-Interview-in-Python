def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])

def main():
    sentence = "We love Java "
    print(f"input sentence {sentence} - output: {reverse_words(sentence)}")


    sentence = "To be or not to be"
    print(f"input sentence {sentence} - output: {reverse_words(sentence)}")

    sentence = "You are amazing"
    print(f"input sentence {sentence} - output: {reverse_words(sentence)}")

    sentence = "Hello     World"
    print(f"input sentence {sentence} - output: {reverse_words(sentence)}")

    sentence = " Hey"
    print(f"input sentence {sentence} - output: {reverse_words(sentence)}")

if __name__ == "__main__":
    main()