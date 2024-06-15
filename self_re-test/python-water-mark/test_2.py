from cairosvg import svg2png

def read_file(file_path):
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read the contents of the file and store it in a variable
        contents = file.read()

    # Return the contents of the file
    return contents

# Call the function with the path to your file
file_contents = read_file('me679.svg')

# Print the contents stored in the variable
# print(file_contents)

svg2png(bytestring=file_contents, write_to='mark.png')