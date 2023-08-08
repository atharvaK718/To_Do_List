from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

def add_task():
    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Field is Empty.')
    else:
        tasks.append(task_string)
        the_cursor.execute('INSERT INTO tasks VALUES (?)', (task_string,))
        list_update()
        task_field.delete(0, 'end')

def list_update():
    clear_list()
    for index, task in enumerate(tasks, start=1):
        task_listbox.insert('end', f"{index}. {task}")

def delete_task():
    try:
        selected_index = task_listbox.curselection()
        if selected_index:
            the_value = task_listbox.get(selected_index)
            task_index = int(the_value.split('.')[0]) - 1
            if task_index < len(tasks):
                tasks.pop(task_index)
                list_update()
                the_cursor.execute('DELETE FROM tasks WHERE title = ?', (the_value,))
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

def delete_all_tasks():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')
    if message_box:
        tasks.clear()
        the_cursor.execute('DELETE FROM tasks')
        list_update()

def clear_list():
    task_listbox.delete(0, 'end')

def close():
    print(tasks)
    guiWindow.destroy()

def retrieve_database():
    tasks.clear()
    for row in the_cursor.execute('SELECT title FROM tasks'):
        tasks.append(row[0])

if __name__ == "__main__":
    guiWindow = Tk()
    guiWindow.title("To-Do List")
    guiWindow.geometry("650x500")
    guiWindow.configure(bg="#F9E5D8")

    the_connection = sql.connect('listOfTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('CREATE TABLE IF NOT EXISTS tasks (title TEXT)')

    tasks = []

    frame = Frame(guiWindow, bg="#F29544")
    frame.pack(fill="both")

    task_label = Label(frame, text="To-Do List", font=("Times New Roman", 24), bg="#F29544", fg="white")
    task_label.pack(pady=15)

    name_label = Label(frame, text="Atharva Khadse", font=("Times New Roman", 8), bg="#F29544", fg="Black")
    name_label.place(relx=1, y=0, anchor="ne")

    task_field = Entry(frame, font=("Times New Roman", 12), bg="white")
    task_field.pack(padx=20, pady=10, fill="x")

    button_frame = Frame(frame, bg="#F29544")
    button_frame.pack(pady=10)

    add_button = Button(button_frame, text="Add Task", bg="#F2C94C", font=("Times New Roman", 12), command=add_task)
    del_button = Button(button_frame, text="Delete Task", bg="#F2C94C", font=("Times New Roman", 12), command=delete_task)
    del_all_button = Button(button_frame, text="Delete All", bg="#F2C94C", font=("Times New Roman", 12), command=delete_all_tasks)
    exit_button = Button(button_frame, text="Exit", bg="#F2C94C", font=("Times New Roman", 12), command=close)

    add_button.pack(side="left", padx=10)
    del_button.pack(side="left", padx=10)
    del_all_button.pack(side="left", padx=10)
    exit_button.pack(side="left", padx=10)

    task_listbox = Listbox(guiWindow, width=60, height=12, font=("Times New Roman", 14), bg="#F9E5D8", selectmode='SINGLE',
                           selectbackground="#F29544", selectforeground="white")
    task_listbox.pack(padx=20, pady=20)

    retrieve_database()
    list_update()

    guiWindow.mainloop()
    the_connection.commit()
    the_cursor.close()
    the_connection.close()
