#functions with outputs
#Will take a first and last name and change it to title case i.e. sam lorimer = Sam Lorimer

def format_name():
  name = " "
  f_name = input("What is your first name? \n")
  l_name = input("What is your last name? \n")
  name = (f_name + " " + l_name).title()
  return name
    
name = format_name()
print(name)