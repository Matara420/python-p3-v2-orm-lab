#!/usr/bin/env python3

from __init__ import CONN, CURSOR
from department import Department
from employee import Employee
from review import Review

import ipdb

def reset_database():
    Department.drop_table()
    Employee.drop_table()
    Review.drop_table()
    
    Department.create_table()
    Employee.create_table()
    Review.create_table()

    # Create seed data
    engineering = Department.create("Engineering", "Building A, 3rd Floor")
    hr = Department.create("Human Resources", "Building C, 1st Floor")
    marketing = Department.create("Marketing", "Building B, 2nd Floor")

    alice = Employee.create("Alice Smith", "Software Engineer", engineering.id)
    bob = Employee.create("Bob Johnson", "HR Specialist", hr.id)
    charlie = Employee.create("Charlie Brown", "Marketing Manager", marketing.id)

    Review.create(2023, "Excellent performance, exceeded all expectations", alice.id)
    Review.create(2022, "Good work, met expectations", alice.id)
    Review.create(2023, "Outstanding leadership skills", bob.id)
    Review.create(2023, "Creative campaign strategies", charlie.id)

if __name__ == '__main__':
    reset_database()
    ipdb.set_trace()