import time


print("#################################################\n"
      "You are born into a loving family in the UK and you\n"
      "     are just finishing primary school.\n"
      "#################################################")
time.sleep(1)
print("Your parents are discussing whether it would be best\n"
      "to move to the other side of the UK for a private school\n"
      "and leave all your friends, or attend the nearby public\n"
      "      school where all your friends are going.\n")

choice1=input("Where are you going?\n"
              "A)Private School\n"
              "B)Public School\n"
              ">>>")

if choice1 in ("a"):
    private_job=input("You've decided to join a private school and you did very\n"
            "good in your exams. Do you want to be a:\n"
            "A)Software Engineer\n"
            "B)Doctor\n"
            "C)Join the Army instead\n"
            ">>>")
    if private_job in ("a"):
        software_uni=input("You decided to take a course in Software Engineering.\n"
            "   which university do you have to enrol in?\n"
            "A)University College London\n"
            "B)University of Edinburgh\n"
            ">>>")
        if software_uni in ("a"):
            print("You are going to london")
        elif software_uni in ("b"):
            print("You are going to Edinburgh")

    elif private_job in ("b"):
        doctor_uni=input("You decided to become a doctor but you need to\n"
            "choose which university to apply for. Are you going\n"
            "for:\n"
            "A)Cambridge University\n"
            "B)Oxford Unitversity\n"
            ">>>")
        if doctor_uni in ("a"):
            print("You are going to Cambridge")
        elif doctor_uni in ("b"):
            print("You are going to oxford")



    elif private_job in ("c"):
        army_type=input("You decided to join the army.\n"
                        "Do you want to join as an:\n"
                        "A)Officer\n"
                        "B)Private\n"
                        ">>>")
        if army_type in ("a"):
            print("you are joining as an officer")
        elif army_type in ("b"):
            print("You are joining as a private")






elif choice1 in ("b"):
    dilemma=input("So you've decided to stay close to home and\n"
                  "keep the friends you have at the local public school.\n"
                  "It's been a few years and your final exam is coming up\n"
                  "and your friends are convincing you to skip revision\n"
                  "and hang out.\n"
                  "Will you:\n"
                  "A)Ditch class to hang out with friends\n"
                  "B)Stay and revise for exam\n"
                  ">>>")
    if dilemma in ("a"):
        after_fail=input("What were you thinking? because you ditched the\n"
                      "revision session, you didn't get the grades you wanted\n"
                      "for the course you wanted to do. Your next choice is to\n"
                      "either:\n"
                      "A)Get a job at Mcdonalds\n"
                      "B)Re-sit your exams\n"
                      ">>>")
        if after_fail in ("a"):
            print("You decided to work at Mcdonalds")
        elif after_fail in ("b"):
            print("You've decided to re-sit your exams")

    elif dilemma in ("b"):
        public_job=input("YAY!, you've aced the exams and got the grades you\n"
                         "needed and can be either a:\n"
                         "A)Psycologist\n"
                         "B)Criminal Scientist\n"
                         ">>>")
        if public_job in ("a"):
            print("You are going to be a Psycologist")
        elif public_job in ("b"):
            print("You are going to be a Criminal Scientist")








