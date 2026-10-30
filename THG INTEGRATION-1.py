# Melissa García
# This program is a small quiz about one of my favorite sagas, The Hunger Games!
# 09/13/2026
# Thanks to my dad for clarifying the if and else statements and making everything so much easier!

def salute(name): #This function salutes the player after they finish the quiz
        print("\nI'm glad to see you made it through the arena " + name + "!")
name=input("What is your name? ")

#"end=" controls what get printed RIGHT AFTER the print statement!
print("\nHello, " + name, end=" ")
print("and welcome to the arena. Good luck, and may the odds be ever in your favor.\n")
print("You may begin in...\n")
# "range()" makes a countdown from 5 to 1
for number in range (5,0,-1):
      print(number)
print("\nGO!")

total_score=0

print("\n── ⋆⋅𖤓⋅⋆ ──Question 1── ⋆⋅𖤓⋅⋆ ──\n")
question_1=input("What is the name of the country where The Hunger Games takes place?"
                "\nA. Archadia\nB. Panem\nC. Ravka\nD. Parem\nEnter your answer: ").upper()
while question_1 not in ["A", "B", "C", "D"]:
   question_1 = input("⚠︎Invalid option. \n──Please try again: ").upper()
if question_1=='B':
    #"*50" prints the "!" 50 times when running the program!
        print("────Correct","!"*50)
        total_score +=1
else:
    #"sep=" indicates that what you put in there will be in between the earlier statements!
        print("────Boo", "incorrect!", sep=" :c ")
        if question_1 !="B":
                print("The correct answer was B.")

print("\n── ⋆⋅𖤓⋅⋆ ──Question 2── ⋆⋅𖤓⋅⋆ ──\n")
question_2=input("How many districts are required to participate in The Hunger Games?"
                    "\nA. 10\nB. 15\nC. 14\nD. 12\nEnter your answer: ").upper()
while question_2 not in ["A", "B", "C", "D"]:
   question_2 = input("⚠︎Invalid option. \n──Please try again: ").upper()
if question_2=='D':
        print("────Correct","!"*50)
        total_score +=1
else:
        print("────Boo", "incorrect!", sep=" :c ")
        if question_2 !="D":
                print("The correct answer was D.")
                
print("\n── ⋆⋅𖤓⋅⋆ ──Question 3── ⋆⋅𖤓⋅⋆ ──\n")
question_3=input("How many tributes are chosen each year to participate in the games?"
                    "\nA. 24\nB. 12\nC. 30\nD. 20\nEnter your answer: ").upper()
while question_3 not in ["A", "B", "C", "D"]:
   question_3 = input("⚠︎Invalid option. \n──Please try again: ").upper()
if question_3=='A':
        print("────Correct","!"*50)
        total_score +=1
else:
        print("────Boo", "incorrect!", sep=" :c ")
        if question_3 !="A":
                print("The correct answer was A.")

print("\n── ⋆⋅𖤓⋅⋆ ──Question 4── ⋆⋅𖤓⋅⋆ ──\n")
question_4=input("A quarter quell occurs every ___ years"
                    "\nA. 25\nB. 35\nC. 5\nD. 40\nEnter your answer: ").upper()
while question_4 not in ["A", "B", "C", "D"]:
   question_4 = input("⚠︎Invalid option. \n──Please try again: ").upper()
if question_4=='A':
        print("────Correct","!"*50)
        total_score +=1
else:
        print("────Boo", "incorrect!", sep=" :c ")
        if question_4 !="A":
                print("The correct answer was A.")
                    
print("\n── ⋆⋅𖤓⋅⋆ ──Question 5── ⋆⋅𖤓⋅⋆ ──\n")
question_5=input("Which Hunger Games did Katniss and Peeta win?"
                    "\nA. 70th\nB. 72nd\nC. 74th\nD. 73rd\nEnter your answer: ").upper()
while question_5 not in ["A", "B", "C", "D"]:
   question_5 = input("⚠︎Invalid option. \n──Please try again: ").upper()
if question_5=='C':
        print("────Correct","!"*50)
        total_score +=1
else:
    print("────Boo", "incorrect!", sep=" :c ")
    if question_5 !="C":
                print("The correct answer was C.")
    
print("\n── ⋆⋅𖤓⋅⋆ ──Question 6── ⋆⋅𖤓⋅⋆ ──\n")
question_6=input("'The Hunger Games' reflects a ____ government"
                    "\nA. Communist\nB. Totalitarian\nC. Socialist\nD. Democratic\nEnter your answer: ").upper()
while question_6 not in ["A", "B", "C", "D"]:
   question_6 = input("⚠︎Invalid option. \n──Please try again: ").upper()
if question_6=='B':
        print("────Correct","!"*50)
        total_score +=1
else:
    print("────Boo", "incorrect!", sep=" :c ")
    if question_6 !="B":
                print("The correct answer was B.")
                           

print("\n⋆˚࿔⭑.ᐟGood Job. Now, Let's see if you are ready to enter the battle.")

print("\n· · ─ ·✶· ─ · ·Question 1· · ─ ·✶· ─ · ·")
question1=input("\nThere are 24 tributes in the arena and only 6 bows available, if you want to arm yourself with one, what are your chances?"
                     "\nA. 20%\nB. 25%\nC. 40%\nD. 30%\nEnter your answer: ").upper()
while question1 not in ["A", "B", "C", "D"]:
   question1 = input("⚠︎Invalid option. \n──Please try again: ").upper()
    #"*" multiplies two numbers and "/" divides
answer=6*100/24
if question1=='A':
    choice=20
elif question1=='B':
    choice=25
elif question1=='C':
    choice=40
elif question1=='D':
    choice = 30
else:
    choice=0

if choice==answer:
    print("────Correct","!"*50)
    total_score +=1
else:
    print("────Boo", "incorrect!", sep=" :c ")
if question1 !="B":
                print("The correct answer was B.")


print("\n· · ─ ·✶· ─ · ·Question 2· · ─ ·✶· ─ · ·")
question2=input("\nAfter a while you got hungry and ate 10 berries out of your stash of 30. How many berries do you have left?"
                     "\nA. 10\nB. 21\nC. 20\nD. 15\nEnter your answer: ").upper()
while question2 not in ["A", "B", "C", "D"]:
   question2 = input("⚠︎Invalid option. \n──Please try again: ").upper()
    #"-" subtracts one number from another
answer=30-10
if question2=='A':
    choice=10
elif question2=='B':
    choice=21
elif question2=='C':
    choice=20
elif question2=='D':
    choice=15
else:
    choice=0
        
if choice==answer:
    print("────Correct","!"*50)
    total_score +=1
else:
    print("────Boo", "incorrect!", sep=" :c ")
if question2 !="C":
                print("The correct answer was C.")

print("\n· · ─ ·✶· ─ · ·Question 3· · ─ ·✶· ─ · ·")
question3=input("\nYou decide to gift your 20 leftover berries to your 3 teammates, how many berries do they each get?"
                    "\nA. 6\nB. 7\nC. 4\nD. 5\nEnter your answer: ").upper()
while question3 not in ["A", "B", "C", "D"]:
   question3 = input("⚠︎Invalid option. \n──Please try again: ").upper()
    #"//" divides two numbers and gives them a whole-number result
answer=20//3
if question3=='A':
    choice=6
elif question3=='B':
    choice=7
elif question3=='C':
    choice=4
elif question3=='D':
    choice=5
else:
    choice=0
        
if choice==answer:
    print("────Correct","!"*50)
    total_score +=1
else:
    print("────Boo", "incorrect!", sep=" :c ")
if question3 !="A":
                print("The correct answer was A.")
    
print("\n· · ─ ·✶· ─ · ·Question 4· · ─ ·✶· ─ · ·")
question4=input("\nAfter they equally split the berries, how many were left over?"
                    "\nA. 2\nB. 3\nC. 1\nD. 0\nEnter your answer: ").upper()
while question4 not in ["A", "B", "C", "D"]:
   question4 = input("⚠︎Invalid option. \n──Please try again: ").upper()
#"%" gives the remainder after division
answer=20%3
if question4=='A':
    choice=2
elif question4=='B':
    choice=3
elif question4=='C':
    choice=1
elif question4=='D':
    choice=0
else:
    choice=0
        
if choice==answer:
    print("────Correct","!"*50)
    total_score +=1
else:
    print("────Boo", "incorrect!", sep=" :c ")
if question4 !="A":
                print("The correct answer was A.")
                
print("\n· · ─ ·✶· ─ · ·Question 5· · ─ ·✶· ─ · ·")
question5=input("\nYou kept the 2 leftover berries for yourself, and walking around the deep forest you saw a package of 35 berries and took it with you. How many do you have now?"
                    "\nA. 35\nB. 38\nC. 37\nD. 39\nEnter your answer: ").upper()
while question5 not in ["A", "B", "C", "D"]:
   question5 = input("⚠︎Invalid option. \n──Please try again: ").upper()
answer=2+35
if question5=='A':
    choice=35
elif question5=='B':
    choice=38
elif question5=='C':
    choice=37
elif question5=='D':
    choice=39
else:
    choice=0
        
if choice==answer:
    print("────Correct","!"*50)
    total_score +=1
else:
    print("────Boo", "incorrect!", sep=" :c ")
if question5 !="C":
                print("The correct answer was C.")

print("\n· · ─ ·✶· ─ · ·Question 6· · ─ ·✶· ─ · ·")
question6=input("\nAn announcement was made. A sponsor sent you 3 boxes of supplies. Each box contains 3 smaller packages, and each package contains 3 arrows. How many arrows did the sponsor send?"
                    "\nA. 15\nB. 30\nC. 9\nD. 27\nEnter your answer: ").upper()
while question6 not in ["A", "B", "C", "D"]:
   question6 = input("⚠︎Invalid option. \n──Please try again: ").upper()
    #"**" raises a number to a power
answer=3**3
if question6=='A':
    choice=15
elif question6=='B':
    choice=30
elif question6=='C':
    choice=9
elif question6=='D':
    choice=27
else:
    choice=0 
        
if choice==answer:
    print("────Correct","!"*50)
    total_score +=1
else:
    print("────Boo", "incorrect!", sep=" :c ")
if question6 !="D":
                print("The correct answer was D.")

salute(name)       
print("\nCongrats " + name, "your total score is: " + str(total_score))
if total_score >= 8 and total_score <= 12:
        print("You would probably survive The Hunger Games!")
if not total_score >= 8:
        print("Maybe you should practice a little more before entering...")
if total_score == 0 or total_score == 1:
        print("It's time to pray your name is not picked...")
print("\nGoodbye, I hope you feel prepared to enter The Hunger Games. May the odds be ever in your favor.")
