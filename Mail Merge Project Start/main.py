#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# \Users\susha\PycharmProjects\Mail Merge Project Start\Input\Letters

with open("/Users/susha/PycharmProjects/Mail Merge Project Start/Input/Letters/starting_letter.txt", "r") as letter:
    letter_content = letter.read()

with open("/Users/susha/PycharmProjects/Mail Merge Project Start/Input/Names/invited_names.txt", "r") as sender:
    name_lines = sender.readlines()

for lines in name_lines :
    temp_content = letter_content
    temp_content=temp_content.replace("[name]",lines,1)
    print(temp_content)



