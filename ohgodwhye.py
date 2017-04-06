#! python3
# markovify - nice little library to make markov chains out of text files
# source of markovify https://github.com/jsvine/markovify
import markovify
import os

CORPUS_DIR = "corpus"

files = os.listdir(CORPUS_DIR)

# Holds markov models
models = []

# Get raw text as string.
for file in files:
    with open(os.path.join(CORPUS_DIR, file)) as f:
        text = f.read()
    models.append(markovify.Text(text))

model = markovify.combine(models=models)

# Print five randomly generated sentences
for i in range(5):
    print(model.make_sentence(tries=1000))


