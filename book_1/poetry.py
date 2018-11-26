import random


def makePoem():
    noun = ['fossils', 'horse', 'chef']
    verbs = ['kicks', 'jingles', 'bounces']
    adverbs = ["curiously"]
    adjectives = ['furry', 'fragrant', 'glistening']
    prepositions = ['against', 'upon']

    adjective1 = random.choice(adjectives)

    adjective2 = random.choice(adjectives)
    while(adjective2 == adjective1):
        adjective2 = random.choice(adjectives)

    adjective3 = random.choice(adjectives)
    while(adjective1 == adjective3 or adjective2 == adjective3):
        adjective3 = random.choice(adjectives)

    noun1 = random.choice(noun)
    noun2 = random.choice(noun)
    while(noun1 == noun2):
        noun2 = random.choice(noun)
    noun3 = random.choice(noun)
    while(noun1 == noun3 or noun2 == noun3):
        noun3 = random.choice(noun)

    verb1 = random.choice(verbs)
    verb2 = random.choice(verbs)
    while(verb1 == verb2):
        verb2 = random.choice(verbs)
    verb3 = random.choice(verbs)
    while(verb1 == verb3 or verb2 == verb3):
        verb3 = random.choice(verbs)
    preposition1 = random.choice(prepositions)
    preposition2 = random.choice(prepositions)
    while(preposition1 == preposition2):
        preposition2 = random.choice(prepositions)


    vowels = ['a','e','i','o','u']

    if adjective1[0] in vowels:
        starter = 'An'
    else:
        starter = 'A'

    # poem = "{starter} {adjective1} {noun1}\n{starter} {adjective1} {noun1} {verb1} {preposition1} the {adjective2} {noun2} {adverbs}, the {noun1} {verb2} the {noun2} {verb3} {preposition2} a {adjective3} {noun3}".format(noun1,noun2,noun3, verb1,verb2,verb3, adjective1, adjective2, adjective3, adverbs, preposition1, preposition2, starter)

    title_poem = "{} {} {} ".format(starter, adjective1, noun1)

    body_poem = "{} {} {} {} {} the {} {} {}, the {} {} the {} {} {} a {} {}".format(starter, adjective1, noun1, verb1, preposition1, adjective2, noun2, adjective1, noun1, verb2, noun2, verb3, preposition2, adjective3, noun3)

    poem = title_poem + "\n\n" + body_poem

    return poem

print(makePoem())
