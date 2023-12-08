
print(f"Hi There! I  have an amazing story about an alien. I can't wait to tell it! ")
print(f"Before the story begins, I have a few questions I need you to answer.")
print(f"After typing your answer, be sure to press the enter key.")
input(f"\nPress the enter key to continue...")

color = input("\nWhat color is the alien?")
location = input("What is your favorite city and state?")
home = input("What planet was the alien from?")
restaurant = input("What is your favorite restaurant? ")
name  = input("What is your best friend's name?")

print (f"\nLETS GO!!!")
print (f"-"*10)        

print (f"\nOnce upon a time there was an Alien named {name}.")
print (f"{name} was a {color} Alien from the planet {home}.")
print (f"Unfortunately {name} had issues with their ship and crash landed in a place called {location}.")
 
#decision 1
materialsearch = input(f"Should {name} sneak into {restaurant} in search of materials that could power their space ship? Type yes or no.  ")
if materialsearch == "yes":
    print (f"\n{name} sneaks into {restaurant} in search of creatures or materials that can feul it's ship.")
    print (f"Immediately everyone in {restaurant} leaps from their seat and scrambles for the exit.")
    print (f"The manager of {restaurant} called the police and {name} walked into the kitchen in search of a familiar smell.")
    print (f"In search of silver, {name} found exactly what they needed before police arrived and escaped back into the madness.")
else:
    print(f"\n{name} decided sneaking into a public place was probably a bad idea.")
    print(f"Instead of going to {restaurant}, {name} decided he could find what he was looking for outside.")