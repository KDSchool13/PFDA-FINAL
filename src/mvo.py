
def rock_or_swim(): 
 answer = input(f"You are an adventurer! You've come across a pond in your journey, what will you do?\n""Tip: Answer with a or b\n""a. Skip a rock\n""b. Take a swim\n")
 if (answer == "a"):
    appease_or_refuse()
 elif (answer == "b"):
    mermaid_or_fish()

def appease_or_refuse():
   answer = input(f"You pick up a small rock and try your best to skip it across the water.\n""As the rock sinks below the surface, the ground beneath you starts to shake.\n"
          "A giant orange frog emerges out of the pond, it croaks in anger, it isn't pleased with your rock skipping!\n""You feel the strange urge to find something to appease it with.\n"
          "a. Appease the frog\n""b. Refuse to appease\n")
   if (answer == "a"):
       dance_or_decline()
   elif(answer == "b"):
       look_or_run()

def dance_or_decline():
   answer = input("You look around frantically for an offering, and see some water lilies in the pond.\n""You scoop one up and hold it out to the frog.\n"
            "It croaks in appreciation and starts to transform before your eyes.\nIt turns out that the frog was fae all along!\n"
            "The faery explains that shes looking for a dance partner, and you would be perfect!\n" "a. Accept the dance\n""b. Refuse the dance\n")
   if (answer == "a"):
      print("You accept the dance gleefully, in exchange, she takes your hand and you dance until your legs go numb and the world turns dark…")
   elif (answer == "b"):
      print("You're awfully shy about dancing with a stranger so you tell her youre good.\n""She makes an aggravated sound and blue dust surrounds you as you start to shrink.\n"
            "You feel your skin become slimy as the sides of your vision begins to blur.\n" 
            "You let out a croak and hop away, mind singled in on the flies around the pond.\n")
      
def look_or_run():
  answer = input("You cross your arms and stomp your foot into the ground, the frog is NOT pleased. It disappears in a blue burst of dust and you hear a strange garbled noise to your side.\n"
                 "a. Look twoards the noise\n""b. Run the other way\n")
  if (answer == "a"):
     print("You cant help it, curiosity gets the better of you as you turn your head to the noise.\n" "A figure with horns and many eyes reaches out to you.\n"
           "You turn to run too late as it grabs your arm and drags you into the forest depths.\n")
  elif (answer == "b"):
     print("After just seeing a giant frog before your eyes, you arent taking any chances!\n" 
           "You book it through the forest until your lungs feel like bursting and youve come to a clearing.\n" 
           "As you attempt to catch your breath, you look to the sky and are rewarded with a beautiful rainbow.\n""You get the warm feeling that you are safe.\n")
     
def mermaid_or_fish():
   answer = input("You channel your time served on the highschool swim team and do the biggest, baddest cannonball you can muster.\n""The pond is deeper than you thought, and the water around you is strangely blue. In front of you, you see a woman with…a fin instead of legs?\n"
         "Youre attempting to process this information when a beautiful serene noise erupts from her mouth and you get the overwhelming urge to follow her.\n"
         "As she does this a tropical fish nudges your side and appears to be gesturing the other way.\n"
         "You're not so sure if you're in a pond anymore…\n""a. Follow the mermaid\n""b. Follow the fish\n")
   if (answer == "a"):
       follow_or_swim_away()
   elif (answer == "b"):
       reef_or_air()

def follow_or_swim_away():
   answer = input("The fish woman leads you to a worn down shipwreck.\n""youre a bit confused and look to her for answers, but she just floats backwards further towards the wreck.\n"
         "You get the feeling that now might be a good time to come up for air...until she starts singing again and all thoughts of air dissolve from your brain.\n"
         "a. Follow her further\n""b. Resist and get air\n")
   if (answer == "a"):
      print("You cant resist her beautiful voice as you follow her into the wreckage.\n"
            "Upon looking around in the degraded ship youre startled to see a mirror that seems to have faint writing on it.\n" 
            "Next to the mirror is a skeleton that appears to be dressed like a pirate?\n" 
            "A well worn tag floats caught in-between its teeth, you turn over the tag to read it, but it just says “throw me.”\n"
            "you're not sure what to make of that so you redirect your attention to the mirror.\n"  
            "An overwhelming feeling of dread emerges when you make out that the words “run” are etched into the surface.\n""You turn a horrified look onto the woman behind you.\n" 
            "She starts to rush forward but you take the skeletons skull and chuck it at her.\n""It collides with her and you curl up into a ball as it explodes, rupturing the water around it.\n"
            "Relief overcomes you as the explosion pushes you to the surface and youre able to wade towards safety.\n") 
   elif (answer == "b"):
      print("You put all of your braincells into resisting her singing and push yourself to swim up.\n Your clothes drag you down as you do so, but you manage to break the surface.\n"
            "You're treated to the sight of a beautiful rainbow over the…ocean?\n"
            "Just as a sigh of relief leaves your mouth you feel fingers wrap around your ankle and you struggle as youre pulled into the depths once more.\n")

def reef_or_air():
   answer = input("You resist the urge to follow the aquatic lady and decide to follow the tropical fish instead.\n" "It leads you to a reef with a school of fish swimming around it.\n"
         "It nudges your hand and swims towards the reef, but youre starting to feel a little light headed.\n""a. Go towards the reef\nb. Come up for air\n")
   if (answer == "a"):
      print("You urge yourself to hold your breath a little longer and meet your fish friend at the reef.\n""The school of fish immediatly surround you in a ticklish fishy embrace.\n"
            "The ocean fades to darkness around you, floating with your little fish friends.\n""You lethargically blink crust out of your burning as a cough comes out of your burning throat.\n"
            "It takes you a moment to realize youre floating in the ocean, the waves moving you up and down\n"
            "The sky is strangley pink and as your vision comes to focus, you realize youre peering at a beautiful sunset.\n""You get the feeling that everything will be...okay.\n")
   elif (answer == "b"):
      print("You feel bad for abandoning your fish buddy but youre not keen on drowning.\nYou swim up and as you break the surface, you notice a boat circling around you.\n"
            "You call out for it and it stops in front of you.\n A ladder extends from it's deck and you climb on board.\nA friendly boatman is there to wrap you in a warm, cosy, towel!\n"
            "He looks at you with great concern as you describe ponds, mermaids, and fish.")
      
def main():
   rock_or_swim()

if __name__ == "__main__":
    main()