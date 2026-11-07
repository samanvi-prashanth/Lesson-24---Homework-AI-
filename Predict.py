# NEXT WORD NOTEBOOK
# ---------- SETUP (given to you) ----------
TEXT = "the cat sat on the mat and the cat ate the fish and the dog sat on the rug"
WORDS = TEXT.split()

TEST_WORDS = [
    ("the", "cat"),
    ("sat", "on"),
    ("and", "the"),
    ("dog", "sat"),
    ("pizza", "the"),
    ("cat", "ate"),
]

# ---------- PART 1: count what follows what ----------
def build_bigrams(words):
    model = {}
    for current, following in zip(words, words[1:]) :
        if current not in model :
            model[current] = {}
        model[current][following] = model[current].get(following, 0) + 1
    return model

BIGRAMS = build_bigrams(WORDS)
print("PART 1: Bigrams")
print(BIGRAMS.get("the"), BIGRAMS.get("pizza", "not found"))

# ---------- PART 2: turn counts into probabilities ----------
def probabilities(word):
    result = {}
    # YOUR CODE HERE
    # counts = BIGRAMS.get(word, {}) gives what followed the word ({} if it was never seen).
    # For each following word and count, store count divided by the sum of all the counts in result.
    return result

print("\nPART 2: Probabilities")
print({w: round(p, 2) for w, p in probabilities("the").items()})

# ---------- PART 3: predict the next word ----------
def predict(word):
    chances = probabilities(word)
    if not chances :
        return "the"
    return max(chances, key=chances.get)

print("\nPART 3: Predict")
print(predict("the"), "|", predict("pizza"))

# ---------- PART 4: check every test word ----------
print("\nPART 4: Test all words")
mistakes = 0
for word, wanted in TEST_WORDS :
    answer = predict(word)
    if answer != wanted :
        mistakes += 1
    print(word,"-",answer)
print("Mistakes:", mistakes,"out of", len(TEST_WORDS))