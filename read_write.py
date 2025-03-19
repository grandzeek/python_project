def modify_file(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, "r") as infile:
            content = infile.read()

        # Modify content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ Successfully written to '{output_filename}'!")

    except FileNotFoundError:
        print(f"❌ Error: File '{input_filename}' not found!")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Ask user for filenames
input_file = input("Enter the filename to read: ")
output_file = input("Enter the new filename to write to: ")

modify_file(input_file, output_file)
