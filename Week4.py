# Function to read, modify, and write the contents of a file
def modify_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as file:
            contents = file.read()

        # Modify the contents (For example, converting all text to uppercase)
        modified_contents = contents.upper()

        # Write the modified contents to the output file
        with open(output_filename, 'w') as file:
            file.write(modified_contents)

        print(f"File successfully modified and saved as {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")
    except IOError:
        print(f"Error: Could not read or write to the file {input_filename}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main program
def main():
    input_filename = input("Enter the filename to read from: ")
    output_filename = input("Enter the filename to save the modified content: ")
    
    # Call the modify_file function
    modify_file(input_filename, output_filename)

# Run the program
if __name__ == "__main__":
    main()
