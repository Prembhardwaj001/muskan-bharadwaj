try:
    # Open the file in read mode
    file = open("sample.txt", "r")

    # Read and print the file line by line
    for line in file:
        print(line.strip())

    # Close the file
    file.close()

except FileNotFoundError:
    # Handle the error if file does not exist
    print("Error: The file 'sample.txt' does not exist.")
    

Error: The file 'sample.txt' does not exist.

Process finished with exit code 0
