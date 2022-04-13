#functions with outputs
#Will take a first and last name and change it to title case i.e. sam lorimer = Sam Lorimer

# def format_name():
#   name = " "
#   f_name = input("What is your first name? \n")
#   l_name = input("What is your last name? \n")
#   name = (f_name + " " + l_name).title()
#   return name
    
# name = format_name()
# print(name)

def format_name(f_name, l_name):
    name = ""
    first = f_name.title()
    last = l_name.title()
    name = (first + " " + last)
    return name

title_name = format_name("sAm", "LoRIMEr")
print(title_name)