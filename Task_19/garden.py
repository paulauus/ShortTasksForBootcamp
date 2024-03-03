import spacy
nlp = spacy.load('en_core_web_sm')

# Create a list of garden path sentences.
gardenpathSentences = ["The sour drink from the ocean.", "The horse raced past the barn fell.", "Mary gave the child a Band-Aid.", "That Jill is never here hurts.", "The cotton clothing is made of grows in Mississippi."]
# Join the sentences in one string to make code shorter and more readable.
gardenpathSentences_joined = " ".join(gardenpathSentences)
print(gardenpathSentences_joined)

# Tokenise each sentence in the list.
doc = nlp(gardenpathSentences_joined)
for token in doc:
    print(token, token.orth_, token.orth)

# Perform named entity recognition.
for ent in doc.ents:
    print(ent.text, ent.label_)

# Look up and print the meaning of entities you dont understand.
entity_gpe = spacy.explain("GPE")
print(f"GPE:{entity_gpe}")

# Write a comment about two entities that you looked up. For each entity answer the following questions:
# What was the entity and its explanation that you looked up?
# - GPE is the label for locations: countries, cities and states. PERSON is the label for people, including fictional characters.
# Did the entity make sense in terms of the word associated with it?
# -  Mississippi was labelled correctly as a state. Mary and Jill were also labelled correctly as people. I was expecting Band-Aid to be identified by NER as a product or an organisation, but spaCy recognises it as a generic term for adhesive bandages instead of the brand.