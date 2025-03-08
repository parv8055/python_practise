from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Expanded training data
messages = [
    # Spam examples
    "Win a free iPhone now!",
    "Claim your prize today!",
    "Get rich quick with this trick!",
    "Free cash for you, click here!",
    "Congratulations, you’ve won $1,000!",
    "Limited time offer, act now!",
    "Earn money fast, no effort!",
    "Exclusive deal just for you!",
    "Download this to win big!",
    "You’re our lucky winner!",

    # Not spam examples
    "Hey, how are you today?",
    "Let’s meet up tomorrow.",
    "Did you see the new movie?",
    "I’m running late, sorry!",
    "Can you send me the notes?",
    "What’s for dinner tonight?",
    "Happy birthday, have a great day!",
    "The weather’s nice today.",
    "I’ll call you later, okay?",
    "Thanks for your help earlier!"
]
labels = ["spam"] * 10 + ["not spam"] * 10  # 10 spam, 10 not spam

# Convert text to numbers (vectorization)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

# Train the model
model = MultinomialNB()
model.fit(X, labels)

# Interactive testing loop
print("Spam Detector Ready! Type 'quit' to exit.")
while True:
    test_message = input("Enter a message to classify: ")
    if test_message.lower() == "quit":
        print("Goodbye!")
        break
    if not test_message.strip():  # Check for empty input
        print("Please enter something!")
        continue
    test_vector = vectorizer.transform([test_message])
    prediction = model.predict(test_vector)[0]
    print(f"Prediction: {prediction}")