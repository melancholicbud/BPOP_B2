def intro_function(text, index):
    print(text[index])

if __name__ == "__main__":
    text_text = "Test"
    intro_function(text_text, 2)
    # IndexError:
    # intro_function(text_text, 10)
    # but
    try:
        intro_function(text_text, 10)
    except IndexError:
        print("Catching IndexError")
    print("Continuing...")