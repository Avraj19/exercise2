#[04/02/20 16:54]


# Define the following variables
# name, last_name, species, eye_color, hair_color
# name = 'Lana'
# Prompt user for input and Re-assign these
# name = input('what new name would you like?')
# Print them back to the user as conversation
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.
# Section 2 - Calculate in what year was the person born? and responde back.
# print something like: 'You said you we're 28 hence you were born in 1991!'

# Define the following variables
name = input('Enter your First name: ').capitalize()
last_name = input('Enter your First name: ').capitalize()
species = input('Enter your what species you are: ').capitalize()
eye_color = input('What color is your eyes:').capitalize()
hair_color = input('What color is your hair:').capitalize()
age = int (input('What is your age:'))
age_in_years = 2020 - age


print(f"Hi {name +' '+ last_name}, welcome to Sparta Global,"
      f" you gender is {species}, ohh sorry species is {species}."
      f" Moving on so lets see, your eye color is {eye_color} and hair color is {hair_color}."
      f"Lastly your age is {age} and you were born in {age_in_years} ")
