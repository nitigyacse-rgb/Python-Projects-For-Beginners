import emoji

def convert_emoji_to_text(text):
    """
    Convert all emojis in the given text into readable text descriptions.

    Args:
        text (str): The input string that may contain emojis.

    Returns:
        str: The same text but with each emoji replaced by its text description.
    """
    return emoji.demojize(text)

def main():
    print("=" * 45)
    print("         EMOJI TO TEXT CONVERTER")
    print("=" * 45)
    print("Enter any text containing emojis and they will be\nconverted into words!\n")

    while True:
        # Get the user's input
        user_input = input("Enter text with emojis: ").strip()

        if not user_input:
            print("You entered an empty line. Please try again.\n")
            continue

        # Convert emojis to text
        converted = convert_emoji_to_text(user_input)

        print("\nConverted text:", converted)
        print()

        # Ask if the user wants to convert another line
        while True:
            again = input("Do you want to convert another line? (Y/N): ").lower()
            if again in ['y', 'n']:
                break
            print("Please enter Y or N.")

        if again == 'n':
            break

        print()

    print("\nThanks for using the Emoji to Text Converter!")

if __name__ == "__main__":
    main()
