#! python3
# markovify - nice little library to make markov chains out of text files
# source of markovify https://github.com/jsvine/markovify
import markovify

# Get raw text as string.
with open("dedicace.txt") as f:
    text = f.read()

# Build the model
text_model = markovify.Text(text)

# Print five randomly generated sentences
for i in range(5):
    print(text_model.make_sentence(tries=9001))


