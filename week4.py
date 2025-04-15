def file_modifier():
    # Get input filename from user
    input_filename = input("Enter the name of the file to read: ")
    output_filename = input("Enter the name of the output file: ")
    
    try:
        # Try to open and read the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
            
            # Modify the content (example: convert to uppercase)
            modified_content = content.upper()
            
            # Try to write to the output file
            try:
                with open(output_filename, 'w') as output_file:
                    output_file.write(modified_content)
                print(f"Successfully wrote modified content to {output_filename}")
                
            except PermissionError:
                print(f"Error: Permission denied when trying to write to {output_filename}")
            except IOError as e:
                print(f"Error writing to file: {e}")
                
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{input_filename}'")
    except UnicodeDecodeError:
        print(f"Error: Could not decode the file '{input_filename}'. It might be a binary file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    file_modifier()