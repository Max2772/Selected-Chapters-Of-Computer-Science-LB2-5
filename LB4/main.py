"""
A collection of tasks for Lab work №4.

Subject: IGI
Lab Work: 4
Variant: 3
Version: 1.0
Author: Bibikau M.A.
Date: 20.04.2025
"""

import sys

import LB4.Task1.task1 as task1
import LB4.Task2.task2 as task2
import LB4.Task3.task3 as task3
import LB4.Task4.task4 as task4
import LB4.Task5.task5 as task5
import LB4.ui as ui
from LB4.Task6 import task6


def task_exit():
    """
    Task to exit the program
    """

    sys.exit(0)


TASK_DESCRIPTIONS = [
    "Exit",
    "Task 1 – Library catalog (search by author, CSV / Pickle)",
    "Task 2 – Text analysis (emails, regex, sentence stats)",
    "Task 3 – Series expansion of ln(1+x) with stats and plot   ",
    "Task 4 – Isosceles trapezoid (draw, fill, save)",
    "Task 5 – NumPy matrix analysis (min row sum, even/odd index correlation).",
    "Task 6 – Pandas analysis of the Boston Housing dataset",
]

tasks = [
    task_exit,
    task1.run,
    task2.run,
    task3.run,
    task4.run,
    task5.run,
    task6.run,
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
