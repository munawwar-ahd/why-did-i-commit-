# reflect.py
# A simple daily reflection tool
# Beginner-friendly and easy to extend

from datetime import date
import os

# Get today's date in YYYY-MM-DD format
today = date.today().isoformat()

# Make sure the "entries" folder exists
if not os.path.exists("entries"):
    os.makedirs("entries")

# File path for today's reflection
file_path = f"entries/{today}.md"

# Ask reflection questions
worked_on = input("What did you work on today?\n> ")
reason = input("\nWhy did you commit today?\n> ")
feeling = input("\nHow did it feel?\n> ")

# Write answers to Markdown file
with open(file_path, "w", encoding="utf-8") as file:
    file.write(f"# {today}\n\n")
    file.write("## What did I work on today?\n")
    file.write(f"{worked_on}\n\n")
    file.write("## Why did I commit today?\n")
    file.write(f"{reason}\n\n")
    file.write("## How did it feel?\n")
    file.write(f"{feeling}\n")

print(f"\nReflection saved to {file_path}")
