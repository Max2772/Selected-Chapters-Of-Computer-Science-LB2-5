"""
Toolbox containing various tasks that operate on strings and numbers.

Subject: IGI
Lab Work: 3
Variant: 3
Version: 1.0
Author: Bibikau M.A.
Date: 27.03.2025
"""

import sys

import LB3.task1 as task1
import LB3.task2 as task2
import LB3.task3 as task3
import LB3.task4 as task4
import LB3.task5 as task5
import LB3.ui as ui


def task_exit():
    """
    Task to exit the program
    """

    sys.exit(0)


TASK_DESCRIPTIONS = [
    "Exit",
    "Task 1 – Series expansion of ln(1+x), x in (-1, 1]",
    "Task 2 – Count positive numbers (stop at 10)",
    "Task 3 – Check if string is a hexadecimal number",
    "Task 4 – Sentence analysis",
    "Task 5 – Max-abs element; sum before last positive",
]

tasks = [
    task_exit,
    task1.run,
    task2.run,
    task3.run,
    task4.run,
    task5.run,
]


def menu():
    """
    Display the task menu and launch the selected task.

    Lists all available tasks with short descriptions, reads a valid
    integer choice from the user, and delegates to the corresponding
    runner function.
    """

    print("\n======================")
    for i, desc in enumerate(TASK_DESCRIPTIONS):
        print(f"  {i}. {desc}")

    res = ui.read_int(
        f"Enter task number (1-{len(tasks) - 1}) or 0 to exit: ",
        min=0,
        max=len(tasks) - 1,
    )
    tasks[res]()


if __name__ == "__main__":
    while True:
        menu()
