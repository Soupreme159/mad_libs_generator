def mad_libs_generator():
    noun = input("Enter a noun")
    occ = input("Enter an occupation")
    verb = input("Enter a verb")
    place = input("Enter a place")
    verb_ed = input("Enter a verb ending with -ed")
    verb_ing = input("Enter a verb ending with -ing")
    plu_noun = input("Enter a plural noun")
    emotion = input("Enter an emotion")

    print("It was during the battle of " + noun + " when I was running through a " + noun + " when a " + noun \
+ " went off right next to my . Our " + occ + " yelled for us to " + verb + " to the nearest " + place + \
 " we could find. When we got to " + place + ", we " + verb_ed \
+ " to start a fire. As we were starting the fire, the enemy saw the " + \
noun + " from the fire and started " + verb_ing \
+ plu_noun + " at us. We all quickly ducked behind the " + noun + " at the " + place \
+ " and returned fire. We quickly eliminated the enemy and were " + emotion + " that we had won the battle.")
    


mad_libs_generator()
