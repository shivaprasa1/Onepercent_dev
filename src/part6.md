# Part 6 — How Python Actually Runs Your Code

## The Execution Pipeline

When you run a Python file, these steps happen in order:

┌─────────────────┐     ┌───────────────────┐       ┌─────────────────┐
│  Source Code    │────▶│  Lexing           │ ────▶│  Parsing        │
│  (.py file)     │      │  (Tokenization)   │      │  (AST)          │
└─────────────────┘     └───────────────────┘      └──────────────────┘
                                                           │
                        ┌───────────────────┐              │
                        │  Output           │              ▼
                        │  (Result)         │     ┌──────────────────┐
                        └───────────────────┘     │  Compilation     │
                                 ▲                │  (Bytecode)      │
                                 │                └──────────────────┘
                        ┌───────────────────┐              │
                        │  Python Virtual   │              │
                        │  Machine (PVM)    │◀─────────────┘
                        └───────────────────┘

### Step 1 — Python Reads Your Source Code

Python opens the .py file and reads the text you wrote. At this point, it is just text — characters in a file.

### Step 2 — Lexing (Tokenization)

Before Python can understand your code, it first breaks the raw text into small meaningful pieces called tokens. This step is called lexing (or tokenization).

When Python reads x = 10, it sees it as one long string of characters: x,  , =,  , 1, 0. Lexing splits it into individual tokens:

x    →  NAME (variable name)
=    →  OP (operator)
10   →  NUMBER (integer)
Each token is the smallest meaningful unit — a name, a symbol, a number. Think of it like breaking a sentence into individual words before you can understand the grammar.

You can see tokenization yourself using Python's built-in tokenize module:

>import tokenize
>import io
>tokens = tokenize.generate_tokens(io.StringIO("x = 10").readline)
>for tok in tokens:
   >print(tok)
You will see tokens for x (NAME), = (OP), 10 (NUMBER), and special tokens for newline and end-of-file.

### Step 3 — Parsing

Once Python has the tokens, it structures them into an Abstract Syntax Tree (AST) — a tree that represents the meaning of your code. Lexing gave Python the individual words. Parsing figures out the grammar — how those words relate to each other.

For x = 10, parsing understands: "this is an assignment, the left side is a variable name called x, the right side is the number 10."

Think of it like reading English. The sentence "Put the book on the table" — first you identify each word (lexing), then you understand the grammar: verb (put), object (book), location (table). Only then can you act. Python works the same way.

This step is also where syntax errors are caught. If you write x = = 10, Python catches it here — the structure does not make sense. It never reaches bytecode or execution.
The CPython parser — the actual code that does this parsing — is written in C

### Step 4 — Compilation to Bytecode

Python compiles the parsed structure into bytecode.

Bytecode is:

* A lower-level representation of your code
* Not machine code (not 0s and 1s)
* Not human readable
* An intermediate instruction set that the Python engine can execute
This compilation happens automatically. You do not run a separate compile step.

### Step 5 — Python Virtual Machine (PVM) Executes Bytecode

The Python Virtual Machine reads the bytecode instructions one by one and executes them.

What Is the PVM Really?
The name "Virtual Machine" sounds like something big — like VirtualBox or VMware, a whole computer running inside another computer. But the PVM is nothing like that.

The PVM is simply a loop inside the CPython program. When you installed Python, you got a C program (the interpreter). Inside that C program, there is a loop that does this:

* Pick up the next bytecode instruction
* Figure out what it means
* Do the operation
* Move to the next instruction
* Repeat until done
* That loop is the PVM. It is not a separate application. It is not a separate environment. It does not create a "space" or a "container." It is just a piece of C code running inside the Python interpreter.

It is called a "virtual machine" because it behaves like a computer — but in software. A real machine (your CPU) reads machine code instructions and executes them. The PVM reads bytecode instructions and executes them. It does the same job as a CPU, but it is implemented in software instead of hardware. That is why it is virtual.

The PVM also:

* Manages memory
* Handles function calls
* Tracks execution order.

### Why Python Is Called Interpreted — But It Is Not the Full Picture

Python is called interpreted because from the developer's perspective, that is what it looks like. You type `python main.py` and it runs. No separate compile step. No compiled file you run later. It feels interpreted.

But now you know the truth — Python **does** compile. It compiles to bytecode. Then the PVM interprets that bytecode. So Python is actually a hybrid — it compiles first, then interprets. The compilation just happens silently and automatically, so you never see it.

| Language | What Happens                             | Who Runs the Code          |
| -------- | ---------------------------------------- | -------------------------- |
| C        | Compiles to machine code (separate step) | CPU runs it directly       |
| Java     | Compiles to bytecode (separate step)     | JVM interprets/executes it |
| Python   | Compiles to bytecode (automatic, hidden) | PVM interprets/executes it |

## The Complete Picture

* When you run python main.py:
* The operating system loads the Python interpreter (CPython) into RAM
* CPython reads your .py file from disk
* It breaks the source code into tokens (lexing)
* It structures the tokens into an Abstract Syntax Tree (parsing)
* It compiles the AST into bytecode
* The Python Virtual Machine executes the bytecode
* Output is sent to the screen
* All of this happens in milliseconds for simple programs