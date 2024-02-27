# todo-list-python
 My To-Do-List Project which created using Python. Defined elements such as variables,lists,dictionaries and functions are described below according to their functionalities:

root: An object representing the main window of the Tkinter application, from the Tk class.

missions [ ]: A list that holds tasks. Each task is represented within a dictionary.

mission_entry: Text entry field where the user enters the task name.

start_label: Label providing information to enter the start date.

start_entry: Text entry field where the user enters the start date.

end_label: Label providing information to enter the end date.

end_entry: Text entry field where the user enters the end date.

mission_table: Tkinter Treeview widget that displays tasks in a table format.

mission_add ( ): Function used to add tasks.
    mission_text: String containing the task name entered by the user.
    start: String containing the start date entered by the user.
    end: String containing the end date entered by the user.

mission: Dictionary that holds user-entered name, start date, and end date data, defining the task completion status as False.

mission_done ( ): Function used to mark the status of the selected task as completed.
    selected_task_index: Tuple containing the index of the selected task.

task_index: Represents the index of the selected task in the task_table.

mission_delete ( ): Function used to delete the selected task.


mission_sort ( ): Function used to sort tasks in the table by end date.

entry_clean ( ): Function used to clear user entry fields.

table_revise ( ): Function used to update the table.

completed_text: Variable used to indicate the completion status of the task.

print_tasks ( ): Function created to write tasks from the tasks list to the tasks.txt file.

mission_write ( ): Function that reads data from the tasks.txt file and adds it to the tasks list.

parse_text_data ( ): Function that parses task data to create a dictionary.
    parts: Represents the parsed format of a String containing task information.

add_button: Variable representing the button pressed to add tasks.

sort_button: Variable representing the button pressed to sort tasks by end date.

done_button: Variable representing the button pressed to mark task status as completed.

delete_button: Variable representing the button pressed to delete tasks.
