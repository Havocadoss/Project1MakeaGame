character_name = input("Choose Your Character Name: ")
print(f"Welcome, {character_name}!")
skills = input("Choose Your Skill Set: ")
if skills.lower() == "hacking":
  print("You have chosen the skill set 'hacking'")
  
elif skills.lower() == "combat":
  print("You have chosen the skill set 'combat'")
  
elif skills.lower() == "diplomacy":
  print("You have chosen the skill set 'diplomacy'")
  
else:
  print("Invalid skill set. Please choose a valid skill set.")
mysterious_figure = input("You encounter a mysterious figure. Do you accept their offer? (yes/no): ")
if mysterious_figure.lower() == "yes":
  print("You accept the offer.")
  join_criminal_world = input("Do you want to join the criminal world or work with a secret government agency? (criminal/agency): ")
  if join_criminal_world.lower() == "criminal":
    print("You choose to work with the drug cartel.")
    
  elif join_criminal_world.lower() == "agency":
    print("You choose to work with the secret government agency.")
    
  else:
    print("Invalid choice. Please choose a valid option.")
elif mysterious_figure.lower() == "no":
  print("You decline the offer and return to your ordinary life.")
else:
  print("Invalid choice. Please choose a valid option.")
portal = input("You encounter a portal to the Upside Down. Do you enter the portal? (yes/no): ")
if portal.lower() == "yes":
  print("You enter the portal.")
  discover_lair = input("Do you want to discover the Demogorgon's lair? (yes/no): ")
  if discover_lair.lower() == "yes":
    print("You discover the Demogorgon's lair.")
    fight_demogorgon = input("Do you want to fight the Demogorgon (yes/no): ")
    if fight_demogorgon.lower() == "yes":
      print("You choose to fight the Demogorgon.")
    elif fight_demogorgon.lower() == "no":
      print("You choose not to fight the Demogorgon.")
    else:
      print("Invalid choice. Please choose a valid option.")
  elif discover_lair.lower() == "no":
    print("You choose not to discover the Demogorgon's lair and continue your journey.")
  else:
    print("Invalid choice. Please choose a valid option.")
elif portal.lower() == "no":
  print("You ignore the portal and continue your journey in the normal world.")
else:
  print("Invalid choice. Please choose a valid option.")
  print("Game Over")