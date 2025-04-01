try: 
    # ask the user to enter the filename to read 
    filename = input("Enter the filename to read: ")

    # open the file in read mode 
    with open(filename, "r") as file: 
        data = file.read()

    # create a new filename by adding "modified_" to the original filename 
    modified_filename = "modified_" + filename

    # open the new file in write mode and write the data on it 
    with open(modified_filename, "w") as new_file: 
        new_file.write(data)

# console this if file does not exist 
except FileNotFoundError: 
    print("Error: File does not exist.")

# console this if file cannot be read
except IOError:
    print("Error: File cannot be read.")