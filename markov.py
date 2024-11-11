import random #import random to get random words
import argparse #import argparse to add command line input

text = "In Congress, July 4, 1776 The unanimous Declaration of the thirteen united States of America, When in the Course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation. We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.—That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed, —That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to institute new Government, laying its foundation on such principles and organizing its powers in such form, as to them shall seem most likely to effect their Safety and Happiness. Prudence, indeed, will dictate that Governments long established should not be changed for light and transient causes; and accordingly all experience hath shewn, that mankind are more disposed to suffer, while evils are sufferable, than to right themselves by abolishing the forms to which they are accustomed. But when a long train of abuses and usurpations, pursuing invariably the same Object evinces a design to reduce them under absolute Despotism, it is their right, it is their duty, to throw off such Government, and to provide new Guards for their future security.—Such has been the patient sufferance of these Colonies; and such is now the necessity which constrains them to alter their former Systems of Government. The history of the present King of Great Britain is a history of repeated injuries and usurpations, all having in direct object the establishment of an absolute Tyranny over these States. To prove this, let Facts be submitted to a candid world. [The Declaration proceeds with a list of grievances against King George III.] In every stage of these Oppressions We have Petitioned for Redress in the most humble terms: Our repeated Petitions have been answered only by repeated injury. A Prince whose character is thus marked by every act which may define a Tyrant, is unfit to be the ruler of a free people. Nor have We been wanting in attentions to our British brethren. We have warned them from time to time of attempts by their legislature to extend an unwarrantable jurisdiction over us. We have reminded them of the circumstances of our emigration and settlement here. We have appealed to their native justice and magnanimity, and we have conjured them by the ties of our common kindred to disavow these usurpations, which, would inevitably interrupt our connections and correspondence. They too have been deaf to the voice of justice and of consanguinity. We must, therefore, acquiesce in the necessity, which denounces our Separation, and hold them, as we hold the rest of mankind, Enemies in War, in Peace Friends. We, therefore, the Representatives of the united States of America, in General Congress, Assembled, appealing to the Supreme Judge of the world for the rectitude of our intentions, do, in the Name, and by Authority of the good People of these Colonies, solemnly publish and declare, That these United Colonies are, and of Right ought to be Free and Independent States; that they are Absolved from all Allegiance to the British Crown, and that all political connection between them and the State of Great Britain, is and ought to be totally dissolved; and that as Free and Independent States, they have full Power to levy War, conclude Peace, contract Alliances, establish Commerce, and to do all other Acts and Things which Independent States may of right do. And for the support of this Declaration, with a firm reliance on the protection of divine Providence, we mutually pledge to each other our Lives, our Fortunes and our sacred Honor."
#The declaration of Independance to train our markov chain 
transitions = {} #creates empty dictionary for our transitions
punctuation = {"!","?","."} #gives a dictionary with punctuation

words = text.split() #splits text at spaces, gets words
for i in range(len(words) - 1): #sets range to go over all the words
    current_word = words[i] #Gets the current word
    for char in current_word: #goes over every character in the current word
        if char in punctuation: #if that character is in our punctuation dictionary
            punctuation = current_word[-1] #grabs the punctuations
            word_wo_punctuation = current_word[:-1] #has the word cleaned of punctuation
            if word_wo_punctuation not in transitions: #adds clean word to our dictionary if its not already there
                transitions[word_wo_punctuation] = [] #adds word
            transitions[word_wo_punctuation].append(punctuation) #adds the punctuation behind the word it followed.

            continue #continues otherwise
        next_word = words[i + 1] #gets the word after the current word
        if current_word:
            if current_word not in transitions: #if current word isnt in dictionary already, add it
                transitions[current_word] = [] #adds the word
            transitions[current_word].append(next_word) #adds the next word to follow the current word


def generate_text(start_word, num_words): #defines our function and takes in arguments
    current_word = start_word #sets the first word to the start word
    result = [current_word] #adds it to our new text
    for _ in range(num_words - 1): #goes over all in range
        if current_word in transitions: #if current word is in transitions
            next_word = random.choice(transitions[current_word]) #randomizes the next word from the potential options
            result.append(next_word) #Adds the next word to the result
            current_word = next_word #goes to the next word
        else:
            break
    return " ".join(result) #joins all resulted words

parser = argparse.ArgumentParser(description="Generate text based on transitions.") #argparse description
parser.add_argument("start_word", type=str, help="The starting word for text generation") #help for starting words
parser.add_argument("num_words", type=int, help="The number of words to generate")# help for number of words

args = parser.parse_args() #args

# Generate and print the text
print(generate_text(args.start_word, args.num_words)) #prints our generate text function argument