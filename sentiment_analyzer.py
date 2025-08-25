# 😊 Simple Sentiment Analyzer

print("Simple Sentiment Analyzer Bot")
print("Type 'quit' to exit.\n")

# Lists of positive and negative words
positive_words = ["happy", "love", "smile", "great", "joy", "nice", "good"]
negative_words = ["bad", "ugly", "hate", "sad", "awful", "hate", "stupid"]

while True:
    text = input("Enter a sentence: ").lower()
    if text == "quit":
        print("Goodbye!")
        break

    # Count positive and negative words
    pos_count = sum(word in text.split() for word in positive_words)
    neg_count = sum(word in text.split() for word in negative_words)

    # Determine sentiment
    if pos_count > neg_count:
        print("Positive Sentiment\n")
    elif neg_count > pos_count:
        print("Negative Sentiment\n")
    else:
        print("Neutral Sentiment\n")
