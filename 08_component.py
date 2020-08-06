import random

# Number checking function goes here
def intcheck(question, low=None, high=None):
    # sets up error messages
    if low is not None and high is not None:
            error = "Please enter an integer between {} and {} " \
                    "(inclusive)".format(low, high)
    elif low is not None and high is None:
        error = "Please enter an integer that is more than is more than or " \
                "equal to {}".format(low)
    elif low is None and high is not None:
        error = "Please enter an integer that is less than or " \
                "equal to {}".format(high)
    else:
        error = "Please enter an integer"

    while True:

        try:
            response = int(input(question))

            # Checks response is not too low
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        except ValueError:
            print(error)
            continue

# game history list
won = 0
lost = 0

game_history = []


#  Statement Generator
def hl_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print

 # asks how many rounds
rounds = intcheck("How many rounds? ")    

def creat_list(n):
  global list1
  list1 = [n+1 for i in n]
  print(list1)


# loop
for x in range(rounds ):
  rounds_statement = "Rounds {}".format(x+1)
  hl_statement(rounds_statement, "#")
 
 

  # generates 2 random numbers
  num_1 = random.randint(0,50)
  num_2 = random.randint(0,50)

 # generates question
  question = input("fill in the missing sign {} _ {}: ".format(num_1, num_2))

 # checks if input is correct or wrong
  if num_1 > num_2 and question == '>':
    feedback = "correct"
    hl_statement (feedback, "#")
  elif num_2 > num_1 and question == '<':
    feedback = "correct"
    won += 1
    hl_statement(feedback, "#")
  elif num_1 == num_2 and question == "=":
    feedback = "correct"
    won += 1
    hl_statement(feedback, "#")
    won += 1

  else:
    feedback = "wrong"
    hl_statement(feedback,"#")
    lost += 1
    
 # game history

  D = x+1
  round_result = "Rounds {}: {}".format(D, feedback)
  game_history.append(round_result)


# prints game history results
print()
print("**** Results ****")

for D in game_history:
    print(D) 

