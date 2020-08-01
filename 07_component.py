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

#  Statement Generator
def hl_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print

rounds = intcheck("How many rounds? ")    # asks how many rounds 
#rounds_played = 0

def creat_list(n):
  global list1
  list1 = [n+1 for i in n]
  print(list1)

k=0

for x in range(rounds):
  rounds_statement = "Rounds {}".format(x+1)
  hl_statement(rounds_statement, "#")
 
  # asks question and compares with answer
  num_1 = random.randint(0,50)
  num_2 = random.randint(0,50)
  #ran the postion of num_2 & num_1 in the format stam.
  question = input("fill in the missing sign {} _ {}: ".format(num_1, num_2))
  if num_1 > num_2 and question == '>':
    hl_statement ("correct", "#")
  elif num_2 > num_1 and question == '<':
    hl_statement("correct", "#")
  elif num_1 == num_2 and question == "=":
    hl_statement("correct", "#")

  else:
    hl_statement("wrong","#")
    k= k+1

print("")
print("you got ",x+1-k,"correct"," and you got ",k," wrong ")
  



