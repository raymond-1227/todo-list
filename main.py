import json
import os

DATA_FILE = "todo.json"

# Load todos from the JSON file and return an empty list if missing or invalid
def load_todos():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

# Save the list of todos to the JSON file, overwriting existing data
def save_todos(todos):
    with open(DATA_FILE, "w") as f:
        json.dump(todos, f)

# Print all todo items with their ID and completion status
def list_todos(todos):
    if not todos:
        print("There are no items yet.")
    else:
        for item in todos:
            mark = "✓" if item["done"] else " "
            print(f"{item['id']}. [{mark}] {item['title']}")

# Prompt for a new todo title and append it to the list
def add_todo(todos):
    title = input("New item: ").strip()
    if title:
        next_id = todos[-1]["id"] + 1 if todos else 1
        todos.append({"id": next_id, "title": title, "done": False})
        save_todos(todos)
        print("Added item to list!")
    else:
        print("Title empty, skip.")

# Prompt for a todo ID, remove the matching item, and renumber remaining items
def remove_todo(todos):
    try:
        i = int(input("ID to remove: "))
        original_length = len(todos)
        todos = [t for t in todos if t["id"] != i]
        if len(todos) < original_length:
            for idx, t in enumerate(todos, start=1):
                t["id"] = idx
            save_todos(todos)
            print("Removed.")
        else:
            print(f"No item with ID {i}.")
    except:
        print("Invalid ID.")
    return todos

# Prompt for a todo ID and mark the matching item as done
def mark_todo(todos):
    try:
        i = int(input("ID to mark done: "))
        found = False
        for t in todos:
            if t["id"] == i:
                t["done"] = True
                found = True
                break
        if found:
            save_todos(todos)
            print(f"Marked task {i} as done.")
        else:
            print(f"No item with ID {i}.")
    except:
        print("Invalid ID.")
    return todos

# Prompt for a todo ID and mark the matching item as undone
def unmark_todo(todos):
    try:
        i = int(input("ID to unmark done: "))
        found = False
        for t in todos:
            if t["id"] == i:
                t["done"] = False
                found = True
                break
        if found:
            save_todos(todos)
            print(f"Marked task {i} as undone.")
        else:
            print(f"No item with ID {i}.")
    except:
        print("Invalid ID.")
    return todos

# Main loop: load todos and process user commands until exit
def main():
    todos = load_todos()
    while True:
        cmd = input("\nCommand (list/add/remove/mark/unmark/exit): ").strip().lower()
        if cmd == "help":   
            print("Available commands:")
            print("help   - Show this help message")
            print("list   - List all todo items with their status")
            print("add    - Add a new todo item")
            print("remove - Remove an item by its ID")
            print("mark   - Mark an item as done by its ID")
            print("unmark - Mark an item as undone by its ID")
            print("exit   - Exit the program")
        elif cmd == "list":
            list_todos(todos)
        elif cmd == "add":
            add_todo(todos)
        elif cmd == "remove":
            todos = remove_todo(todos)
        elif cmd == "mark":
            todos = mark_todo(todos)
        elif cmd == "unmark":
            todos = unmark_todo(todos)
        elif cmd == "exit":
            print("Bye!")
            break
        else:
            print("Unknown command. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()
