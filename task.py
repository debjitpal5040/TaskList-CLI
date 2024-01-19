"""This is a command line tool for managing your TODOs."""
import re
import sys


def help():
    """help"""
    sa = """Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics"""
    sys.stdout.buffer.write(sa.encode("utf8"))


def add(p, task):
    """
    Adds a new task to the task list.

    Args:
        priority (int): The priority of the task.
        task (str): The description of the task.

    Returns:
        None
    """
    with open("task.txt", "a", encoding="utf-8") as file:
        file.write(str(p))
        file.write(" ")
        file.write(task)
        file.write("\n")
    task = '"' + task + '"'
    print(f"Added task: {task} with priority {p}")


def nec():
    """nec"""
    try:
        f = open("task.txt", "r", encoding="utf-8")
        for line in f:
            line = line.strip("\n")
            x = re.search(r"\d+", line)
            if x is None:
                raise ValueError
            x = x.group()
            priority.append(int(x))
            line = line.lstrip("0123456789 ")
            line = f"{line} [{x}]"
            d.update({int(x): line})
    except OSError:
        sys.stdout.buffer.write("There are no pending tasks!".encode("utf8"))


def ls():
    """Prints the list of tasks in ascending order of priority"""
    try:
        nec()
        k = 1
        for i in sorted(priority):
            sys.stdout.buffer.write(f"{k}. {d[i]}".encode("utf8"))
            sys.stdout.buffer.write("\n".encode("utf8"))
            k = k + 1
    except Exception as e1:
        raise e1


def done(no):
    """Marks the task with the given index as done"""
    try:
        nec()
        no = int(no)
        f = open("completed.txt", "a", encoding="utf-8")
        if no == 0:
            raise ValueError
        x = sorted(priority)[no - 1]
        st = d[x]
        st = st.rstrip("0123456789[] ")
        f.write(st)
        f.write("\n")
        f.close()
        print("Marked item as done.")
        with open("task.txt", "r+", encoding="utf-8") as f:
            lines = f.readlines()
            f.seek(0)
            for i in lines:
                if i.strip("\n") != f"{x} {st}":
                    f.write(i)
            f.truncate()
    except ValueError:
        print(f"Error: no incomplete item with index #{no} exists.")


def deL(no):
    """Deletes the task with the given index"""
    try:
        nec()
        no = int(no)
        if no == 0:
            raise ValueError
        x = sorted(priority)[no - 1]
        st = d[x]
        st = st.rstrip("0123456789[] ")
        with open("task.txt", "r+", encoding="utf-8") as f:
            lines = f.readlines()
            f.seek(0)
            for i in lines:
                if i.strip("\n") != f"{x} {st}":
                    f.write(i)
            f.truncate()
        print(f"Deleted task #{no}")
    except (IndexError, ValueError):
        print(f"Error: task with index #{no} does not exist. Nothing deleted.")


def report():
    """Prints the number of pending and completed tasks"""
    try:
        f = open("task.txt", "r", encoding="utf-8")
        d = f.readlines()
        up = f"Pending : {len(d)}"
        sys.stdout.buffer.write(up.encode("utf8"))
        sys.stdout.buffer.write("\n".encode("utf8"))
        ls()
        sys.stdout.buffer.write("\n".encode("utf8"))
        nf = open("completed.txt", "r", encoding="utf-8")
        don = nf.readlines()
        p = 1
        print(f"Completed : {len(don)}")
        for lines in don:
            lines = lines.strip("\n")
            print(f"{p}. {lines}")
            p = p + 1
    except OSError:
        print("error")


if __name__ == "__main__":
    try:
        d = {}
        priority = []
        args = sys.argv
        if args[1] == "del":
            args[1] = "deL"
        if args[1] == "add" and len(args[2:]) == 0:
            sys.stdout.buffer.write(
                "Error: Missing tasks string. Nothing added!".encode("utf8")
            )
        elif args[1] == "done" and len(args[2:]) == 0:
            sys.stdout.buffer.write(
                "Error: Missing NUMBER for marking tasks as done.".encode("utf8")
            )
        elif args[1] == "deL" and len(args[2:]) == 0:
            sys.stdout.buffer.write(
                "Error: Missing NUMBER for deleting tasks.".encode("utf8")
            )
        else:
            globals()[args[1]](*args[2:])
    except IndexError:
        S = """Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics"""
        sys.stdout.buffer.write(S.encode("utf8"))
