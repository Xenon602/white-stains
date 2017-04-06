#! python3
# markovify - nice little library to make markov chains out of text files
# source of markovify https://github.com/jsvine/markovify
import markovify

# Get raw text as string.
with open("corpus/hhgttg.txt") as f:
    hhgttg = f.read()

with open("corpus/bbf.txt") as f:
    bbf = f.read()

# Build the model

hhgttg_model = markovify.Text(hhgttg)

bbf_model = markovify.Text(bbf)

# Combuine the models
ohgodwhy_combo = markovify.combine([ bbf_model, hhgttg_model],[30,1])

# Print five randomly generated sentences
for i in range(5):
    print(ohgodwhy_combo.make_sentence(tries=9001))


