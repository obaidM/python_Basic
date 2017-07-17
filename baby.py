questions=["Why is sky blue?:","why do boys stand up to pee?:", "Where do babies come from?:",
           "Where do we go when we die?:","Why are muslims so angry?:","Why do people have different colors?:"]

# list have total of 6 questions so starting from 0 to 5

import random

answer = ""

while answer != "just because":
      ques=random.randint(0,5)
      print("{}".format(questions[ques]))
      answer = input("answer:").strip().lower()
