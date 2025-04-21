📋 Program: Add Three Copies to a List
This is a simple Python program that demonstrates how to modify a list inside a function by adding multiple copies of a user-input message.

🧠 What It Does
Takes a message from the user.

Creates an empty list.

Adds 3 copies of the entered message to the list using a function.

Prints the list before and after the modification to show the changes.

💻 Code Breakdown
add_three_copies(my_list, data)
A helper function that receives a list and a data item.

It adds the same data three times to the list using a for loop and the append() method.

main()
Asks the user to enter a message.

Creates an empty list my_list.

Prints the list before modification.

Calls add_three_copies() to add the message 3 times.

Prints the updated list.

📦 Example Output
pgsql
Copy
Edit
Enter a message to copy: Hello
List before: []
List after: ['Hello', 'Hello', 'Hello']
🔧 How to Run
Make sure you have Python installed (version 3.x).

Save the code in a file named something like copy_message.py.

Run the program using the terminal or command prompt:

bash
Copy
Edit
python copy_message.py
📚 Concepts Used
Functions

Lists (mutable data structures)

Loops (for)

User input (input() function)

✨ Author
Made by Tahira – learning Python one step at a time! 🚀