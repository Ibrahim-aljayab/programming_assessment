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

rounds = intcheck("How many rounds? ", 1)    # asks how many rounds 
rounds_played = 0

while rounds_played < rounds:
  print("Round {}".format(rounds_played+1))
  rounds_played += 1

  # asks question and compares with answer

  num_1 = random.randint(0,50)
  import random
  num_2 = random.randint(0,50)
  question = input("fill in the missing sign {} _ {}: ".format(num_1, num_2))
  if num_1 > num_2 and question == '>':
    print ("correct")
  elif num_2 > num_1 and question == '<':
    print("correct")
  elif num_1 == num_2 and question == "=":
    print("Correct")

  else:
    print ("wrong")

