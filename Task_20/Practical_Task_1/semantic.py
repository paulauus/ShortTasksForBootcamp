import spacy

nlp = spacy.load('en_core_web_md')

# Calculate the similarity between the three words.
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
# Cat and money are the most similar - they are both animals.
# Monkey and banana have second highest similarity, because although the are an animal and a fruit, we know monkeys eat bananas.
# Cat and banana have the lowest similarity - cats and bananas don't have a clear connection.
print("\n")

# Compare a series of words with one another.
tokens = nlp("cat apple monkey banana tree")
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
# Tree and apple have the highest similarity - apples grow on trees. Banana is second, monkey third, and cat has the lowest similarity.
print("\n")

# Calculate similarity between longer phrases.
sentence_to_compare = "Why is my cat on the car"
sentences = ["Where did my dog go",
"Hello, there is my car",
"I've lost my car in my car",
"I'd like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - " + str(similarity))