def words_count(text):
    words = text.split()
    return len(words)
def main():
    print("Hi! Welcome to word counter game.")
    input_user= input("Please enter a sentence or paragraph: ").strip()
    if not input_user:
        print("Error: You entered an empty string. Please provide valid text.")
    else:
        word_count = words_count(input_user)
        print(f"The number of words in the entered text is: {word_count}")
if __name__ == "__main__":
    main()
