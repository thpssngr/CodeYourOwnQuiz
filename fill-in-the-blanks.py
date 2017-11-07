# IPND Stage 2 Final Project: Fill in the blanks quiz

# The quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.

# below are three sets of blanks, answers and a matching quiz text for each difficulty level of the game

blanks_easy = ["___1___", "___2___", "___3___", "___4___"]
answers_easy = ['function', 'variables', 'nothing', 'lists']
text_easy = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

blanks_medium = ["___1___", "___2___", "___3___", "___4___", "___5___"]
answers_medium = ['computer', 'browser', 'Internet', 'servers', 'HTTP']
text_medium = '''Let's take a step back for a second and talk about the major pieces of the web.
The major pieces are you, your ___1___ running a web ___2___, the ___3___, and ___4___.
Your ___2___ makes requests via the Internet to ___4___. These requests are using a protocol called ___5___.
And the ___4___ respond with files that the ___2___ displays.
You're probably running one of those right this moment. These ___4___ are computers just like yours.
Except they are optimized for sitting in a closet and hosting files rather than sitting on your desk browsing these files.
And the protocol ___5___ is just a very simple protocol that your ___2___ uses to communicate with these ___4___.
We'll mostly be focusing on the ___2___ component in this section for rendering ___5___ files.'''

blanks_hard = ["___1___", "___2___", "___3___", "___4___", "___5___", "___6___"]
answers_hard = ["HTML", "Markup", "Language", "page", "client", "servers"]
text_hard = '''The web is composed largely of ___1___ documents.
___1___ stands for HyperText ___2___ ___3___ and is the ___3___ the browsers use to interpret a web ___4___.
The components of the web include the ___5___ (your computer and browser), the Internet, and ___6___.
The ___5___ and ___6___ interact through something called the Hypertext Transfer Protocol (HTTP).
___1___ elements are what we use to tell a web browser how to display content on a web ___4___.
Most ___1___ elements consist of an opening and a closing tag with some content between them.
Some elements accept additional values called attributes in their opening tags.
Attributes provide additional information to the browser.
For example, the anchor tag takes an attribute called href that defines a URL to link to.'''

def quiz_choice(difficulty):
    # the function takes the input for the variable "difficulty", and returns a suitable quiz text, a list of blanks, and a list of solutions
    if difficulty == "Easy":
        return blanks_easy, answers_easy, text_easy
    if difficulty == "Medium":
        return blanks_medium, answers_medium, text_medium
    if difficulty == "Hard":
        return blanks_hard, answers_hard, text_hard

def word_in_pos(word, blanks):
    # Checks if the word passed in contains a blank.
    for pos in blanks:
        if pos in word:
            return pos
    return None

def quiz_solution(blanks_remaining):
        if blanks_remaining != []:
            print "\nSORRY, YOU HAVE NOT SOLVED THE QUIZ:\n"
        else:
            print "\nCONGRATULATIONS, YOU HAVE SOLVED THE QUIZ:\n"

def play_game():
    # The function does not require any input (except the user prompts for difficulty and number of tries).
    # After a user has selected the defficulty level and number of tries,
    #the function will iterate through the text, look for blanks, and prompt the user to replace them with the correct answer.
    # It will return the quiz text with the blanks filled in.
    difficulty = raw_input("\nLET'S PLAY A QUIZ! PLEASE CHOOSE YOUR DIFFICULTY LEVEL! \n(Type in 'Easy', 'Medium' or 'Hard'): \n")
    tries = int(raw_input("HOW MANY TRIES DO YOU WANT TO HAVE FOR SOLVING THE QUIZ? \nType in a number between 1 and 5. \n"))
    blanks, answer, text = quiz_choice(difficulty)
    print '\nFILL THE BLANKS IN THE FOLLOWING TEXT:\n"' + text + '"'
    text = text.split()
    for word in text:
        replacement = word_in_pos(word, blanks)
        if replacement != None:
            while tries > 0:
                user_input = raw_input("\nWhat does " + word + " stand for? \n(TYPE IN YOUR ANSWER, YOU HAVE " + str(tries) + " TRIES LEFT):\n")
                if user_input not in answer:
                    if tries >1:
                        print '\nSORRY, "' + user_input + '" IS THE WRONG ANSWER! PLEASE TRY AGAIN!\n'
                    else:
                        print "You have used your maximum number of tries. GAME OVER!"
                    tries = (tries-1)
                else:
                    text = " ".join(text)
                    text = text.replace(word_in_pos(word, blanks), user_input)
                    text = text.split()
                    blanks.remove(replacement)
                    print '\nYOU ARE RIGHT, "' + user_input + '" IS THE CORRECT ANSWER!\n'
                break
    text = " ".join(text)
    quiz_solution(blanks)
    return '\n"'+ text + '"\n'

print play_game()
