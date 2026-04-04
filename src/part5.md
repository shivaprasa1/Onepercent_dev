# Python_Learning

## The Python Interactive Shell (REPL)

This is the REPL — Read, Evaluate, Print, Loop.

Read — Python reads what you type
Evaluate — Python executes it
Print — Python shows the result
Loop — Python waits for the next input

## print() — Sending Output to the Screen

print() is the most basic way to send data from your program to the screen.
>print("hello")
>print(object, sep="" , end="" , file="" , flush=true)

## input() — Receiving Data from the User

input() pauses the program and waits for the user to type something.
the text inside input() called prompt
>name = input("Enter your name: ")
>print("Hello,", name)
---
>a = int(input("Enter first number: "))
>b = int(input("Enter second number: "))
>print("Sum:", a + b)
>print("Difference:", a - b)
>print("Product:", a * b)

## f-strings — Clean Output Formatting

Python provides a clean way to embed values inside strings using f-strings (formatted string literals).
>name = "Shyam"
>age = 28
>print(f"My name is {name} and I am {age} years old")

## Comments - Comments are lines that Python ignores. They are notes for humans reading the code.

This calculates the user's age  -----> comments
>birth_year = int(input("Enter your birth year: "))
>current_year = 2026
>age = current_year - birth_year
>print(f"You are {age} years old")

## Where This Applies in Real Work

* print() —    used daily for quick debugging in development. When a variable has an unexpected value, print() is the fastest way to check.

* input() —    the concept of receiving external data applies to APIs (receiving HTTP requests), reading files, and accepting command-line arguments.

* f-strings —    used everywhere: log messages, API responses, error messages, database queries, email templates.

Input → Process → Output — this is the architecture of every backend service, every data pipeline, and every AI system.

## The Fundamental Program Model

Every program — from a simple calculator to a complex AI system — follows the same core model:

Input → Process → Output

| Step    | What Happens                         | Example             |
| ------- | ------------------------------------ | ------------------- |
| Input   | Data comes in                        | User types a number |
| Process | Program does something with the data | Calculate the sum   |
| Output  | Result goes out                      | Print the answer    |

This model applies everywhere:

* A web API receives a request (input), processes it, and returns a response (output)
* An AI model receives text (input), processes it through the model, and generates a response (output)
* A data pipeline reads raw data (input), cleans and transforms it (process), and stores the result (output)

Every system you will ever build follows this pattern. Understanding it now creates a mental framework for everything ahead.

## ASSIGNMENT

Asks for the user's name

Asks for their birth year

Calculates their age (use 2026 as the current year)

Prints a formatted message using an f-string:
