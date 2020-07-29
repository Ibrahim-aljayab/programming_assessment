# asks question and compares with answer
import random
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
