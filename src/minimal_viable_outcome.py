
def rock_or_swim(): 
 answer = input(f"You are an adventurer! You've come across a pond in your journey, what will you do?\n""Tip: Answer with a or b\n""a. Skip a rock\n""b. Take a swim\n")
 if (answer == "a"):
    print(f"You pick up a small rock and try your best to skip it across the water.\n""As the rock sinks below the surface, the ground beneath you starts to shake.\n"
          "A giant orange frog emerges out of the pond, it croaks in anger, it isn't pleased with your rock skipping!\n""You feel the strange urge to find something to appease it with.\n")
 elif (answer == "b"):
    print("You channel your time served on the highschool swim team and do the biggest, baddest cannonball you can muster.\n"
          "The pond is deeper than you thought, and the water around you is strangely blue. In front of you, you see a woman with … a fin instead of legs?\n"
          "Youre attempting to process this information when she extends her arm out towards you and a beautiful serene noise erupts from her mouth.\n"
          "You get the overwhelming urge to follow her. As she does this a tropical fish nudges your side and appears to be gesturing the other way.\n" 
          "You're not so sure if you're in a pond anymore…\n")


def appease_frog_or_refuse():
   answer = input("a. Appease the frog\n""b. Refuse to appease\n")
   if (answer == "a"):
      print(f"You look around frantically for an offering, and see some water lilies in the pond.\n""You scoop one up and hold it out to the frog.\n"
            "It croaks in appreciation and starts to transform before your eyes.\nIt turns out that the frog was fae all along!\n"
            "The fairy explains that shes looking for a dance partner, and you would be perfect!\n")
   elif (answer == "b"):
      print("You cross your arms and stomp your foot into the ground, the frog is NOT pleased. It disappears in a blue burst of dust and you hear a strange garbled noise to your side.\n")

      
def main():
   rock_or_swim()
   answer = input("a. Appease the frog\n""b. Refuse to appease\n")
   appease_frog_or_refuse()


if __name__ == "__main__":
    main()