import os

def create_web_page(name, description):
    # Create the file name with the user's name
    file_name = name.lower().replace(" ", "_") + ".html"
    
    # Open the file for writing
    try:
        with open(file_name, "w") as f:
            # Write the HTML tags and user input
            f.write("<HTML>\n")
            f.write("<HEAD>\n")
            f.write("<TITLE>{}</TITLE>\n".format(name))
            f.write("</HEAD>\n")
            f.write("<BODY>\n")
            f.write("<H1>{}</H1>\n".format(name))
            f.write("<HR />\n")
            f.write("{}\n".format(description))
            f.write("<HR />\n")
            f.write("</BODY>\n")
            f.write("</HTML>\n")
            
            print("File created: {}".format(file_name))
            
    except IOError:
        print("Error creating file.")

# Ask the user for their name and description
name = input("Enter your name: ")
description = input("Enter a sentence that describes yourself: ")

# Check if name was provided
if name.strip() == "":
    print("No name provided.")
else:
    # Create the web page
    create_web_page(name, description)