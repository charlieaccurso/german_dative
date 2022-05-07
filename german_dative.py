"""
The program will ask the user for one of four German prepositions:
mit 'with', von 'from', zu 'to (someone's place)', or fur 'for'.

The program will then ask the user the person, number, and formality
(if applicable) of the desired possessive pronoun.

Lastly, the program will ask the user to choose one of four nouns,
representing masculine, feminine, neuter, and plural: Vater 'father',
Mutter 'mother', Haus 'house', and Freunde 'friends'.

"""

# The following is a dictionary containing key-value pairs of the form
# ('preposition','case'), where 'D' indicates dative and 'A' indicates
# accusative.
prepositions= {'mit':'D', 'von':'D', 'zu':'D', 'fur':'A'}

words= {'Vater':'m', 'Mutter':'f', 'Haus':'n', 'Freunde':'p'}

# Person 1, 2, 3, Number (sg or pl)
# key-value pairs of token : list of declensions (m/n, f, pl)
# M or N is index 0, F is index 1, PL is index 2
dative_persons=     {'1s':['meinem','meiner','meinen'],
                     '2si':['deinem','deiner','deinen'],
                     '3sm':['seinem','seiner','seinen'],
                     '3sf':['ihrem','ihrer','ihren'],
                     '2sf':['Ihrem','Ihrer','Ihren'],
                     '1p':['unsrem','unsrer','unsren'],
                     '2pi':['eurem','eurer','euren'],
                     '3p':['ihrem','ihrer','ihren'],
                     '2pf':['Ihrem','Ihrer','Ihren']}

# key-value pairs of token : list of declensions (m, f/pl, n)
# M is index 0, F or PL is index 1, N is index 2
accusative_persons= {'1s':['meinen','meine','mein'],
                     '2si':['deinen','deine','dein'],
                     '3sm':['seinen','seine','sein'],
                     '3sf':['ihren','ihre','ihr'],
                     '2sf':['Ihren','Ihre','Ihr'],
                     '1p':['unsren','unsere','unser'],
                     '2pi':['euren','eure','euer'],
                     '3p':['ihren','ihre','ihr'],
                     '2pf':['Ihren','Ihre','Ihr']}

def choose_preposition(prepositions):
    """
    Display the prepositions available by printing keys of prepositions
    dictionary.
    """
    
    
    # ask user to type the preposition they want
    preposition= input(("The following prepositions are available: %s\nEnter your choice here: " % ', '.join(prepositions)))
    # check to make sure the preposition is a key
    # if not, error.
    if preposition not in prepositions.keys():
        print("Error. Preposition not available.")
    # if so, proceed
    else:
        print("You selected the preposition '%s'." % (preposition))
        return preposition
    # return a string containing the preposition
    
    return preposition

def who():
    """
    Ask the user to provide the person, gender (if applicable), number, and formality (if applicable) of the possessive\
    Store each piece of information in a token of the form:
    person number gender formality -> pngf
    """
    token= ''
    person= str(input("Please enter 1 for first person (ich, wir),\n 2 for second person (du, ihr, Sie), or\n 3 for third person (er, sie 'she', sie 'they'): "))
    
    if person != '1' and person != '2' and person != '3':
        print("Error.")
    else:
        token+= person
    
    number= input("Please enter s for singular (ich, du, er, sie, Sie) or p for plural (wir, ihr, sie, Sie): ")
    if number != 's' and number != 'p':
        print("Error.")
    else:
        token+= number
    
    if token == '2s':
        formality= input("Please enter i for informal (du) or f for formal (Sie): ")
        if formality != 'i' and formality != 'f':
            print("Error.")
        else:
            token+= formality
    
    elif token == '3s':
        gender= input("Please enter m for masculine (er) or f for feminine (sie): ")
        if gender != 'm' and gender != 'f':
            print("Error.")
        else:
            token+= gender
    
    elif token == '2p':
        formality= input("Please enter i for informal (ihr) or f for formal (Sie) 'you plural formal': ")
        if formality != 'i' and formality != 'f':
            print("Error.")
        else:
            token+= formality
    
    return token

def choose_word(words):
    """
    Ask user to choose a word from the list words.
    """
    word= input(("The following words are available: %s \nEnter your choice here: ") % (', '.join(words)))
    
    # check if word is valid
    if word not in words.keys():
        print("Error. Word not available.")
    # if so, proceed
    else:
        print("You selected the word '%s'." % (word))
        return word
    
def collate(prepositions, words):
    preposition= choose_preposition(prepositions)
    token= who()
    word= choose_word(words)
    possessive= ''
    
    if prepositions[preposition] == 'D':
        if words[word] == 'm' or words[word] == 'n':
            possessive= dative_persons[token][0]
        elif words[word] == 'f':
            possessive= dative_persons[token][1]
        else: # for plural cases
            if word[-1] == 'e':
                word= word + 'n'
            possessive= dative_persons[token][2]
    
    elif prepositions[preposition] == 'A':
        if words[word] == 'm':
            possessive= accusative_persons[token][0]
        elif words[word] == 'f' or words[word] == 'p':
            possessive= accusative_persons[token][1]
        elif words[word] == 'n':
            possessive= accusative_persons[token][2]
            
    final_phrase= preposition + ' ' + possessive + ' ' + word
    print(final_phrase)
    return final_phrase

collate(prepositions, words)
        
    
    
    
    
    
    
    
    
    
