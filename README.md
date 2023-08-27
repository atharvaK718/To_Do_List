# To_Do_List
To-Do List application with a graphical user interface using Tkinter. It uses SQLite for database storage, provides functions to add and manage tasks, and allows users to interact with the application through buttons and the GUI.

![To_Do_List](https://github.com/atharvaK718/To_Do_List/assets/126504513/ac9a74e2-60c9-4c0a-b0b5-ed498b80d0f8)

Components and Details:

Importing Libraries:
tkinter: Provides the GUI framework.
messagebox: Allows displaying message boxes for notifications.
sqlite3: Offers a simple way to work with SQLite databases.
Function Definitions:

add_task():
This function is called when the "Add Task" button is clicked. 
It retrieves the text entered in the entry field (task_field) and adds it to both the tasks list and the SQLite database. 
If the entry is empty, it displays an error message.

list_update():
This function updates the task list displayed in the GUI listbox (task_listbox). 
It first clears the existing list and then populates it with tasks from the tasks list, numbering them.

delete_task():
This function is triggered when the "Delete Task" button is clicked. 
It gets the index of the selected task from the listbox, deletes the task from both the tasks list and the SQLite database, and updates the list.

delete_all_tasks():
This function deletes all tasks from the tasks list and the SQLite database. 
It displays a confirmation message box before proceeding.

clear_list():
This function clears the listbox by deleting all items from it.

close():
This function is called when the "Exit" button is clicked. 
It prints the current tasks, closes the GUI window, and terminates the program.

retrieve_database():
This function retrieves tasks from the SQLite database and populates the tasks list with them.

Main Code:

The main part of the script sets up the GUI window and its components:

The GUI window is created (guiWindow = Tk()).
The SQLite database connection and cursor are established.
The tasks list is initialized.
The GUI components are created using various widgets (Label, Entry, Button, Listbox) and placed on the window using geometry managers like pack().

Styling and Layout:
The GUI components are styled with specific fonts, colors, and padding to create a visually appealing interface. The relx=1, y=0, anchor="ne" attribute in the name label (name_label) positions it in the top-right corner.

Database Setup:
The script creates an SQLite database named listOfTasks.db (if it doesn't exist) and a table tasks with a single column title.

Function Calls and Event Loop:
retrieve_database() is called to populate the tasks list with data from the database.
list_update() is called to update the listbox with the retrieved tasks.

The main event loop (guiWindow.mainloop()) starts, allowing the application to respond to user interactions. After the loop, changes are committed to the database, and the cursor and connection are closed.

User Interaction:
Users can interact with the GUI by adding tasks, deleting tasks, deleting all tasks, and exiting the application.
