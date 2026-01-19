# Step 1: Take user input and write it to the file
text = input("Enter text to write into the file: ")

with open("output.txt", "w") as file:
    file.write(text + "\n")

# Step 2: Take more input and append it to the same file
more_text = input("Enter text to append into the file: ")

with open("output.txt", "a") as file:
    file.write(more_text + "\n")

# Step 3: Read and display the final content of the file
print("\nFinal content of the file:")

with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
        

Enter text to write into the file: hello world,
Enter text to append into the file: we are learnig python programr. 

Final content of the file:
hello world.
we are learnig python programr.

Process finished with exit code 0
