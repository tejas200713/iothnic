def text_to_emoji_converter(sentence):
    # Dictionary mapping words to emojis
    emoji_dict = {
        "love": "❤",
        "pizza": "🍕",
        "cats": "🐱",
        "happy": "😊",
        "sad": "😢"
    }

    # Validate sentence length (between 1 and 500 characters)
    if 1 <= len(sentence) <= 500:
        words = sentence.split()  # Split sentence into words
        # Replace words with corresponding emojis if found
        converted_sentence = ' '.join(emoji_dict.get(word.lower(), word) for word in words)
        return converted_sentence
    else:
        return "Invalid sentence length. Please enter a sentence between 1 and 500 characters."

# Example Usage
sentence = input("Enter a sentence: ").strip()  # Strip leading/trailing spaces
print(text_to_emoji_converter(sentence))
