Introduction to Programming – Week 5

Scripts and Modules – Lab Logbook Summary

Overview

This lab covered Python scripts and modules. It explained how programs are stored in files, executed from the terminal, and organised using modules. The lab also introduced command-line arguments, namespaces, and code reuse.

Python Scripts

Scripts are saved as .py files
Run from the terminal, not line-by-line
Output must be displayed using print()
Can be written in any text editor or IDE
Command-Line Arguments

Extra values can be passed to a script when it runs
sys.argv stores the script name and arguments
Allows programs to work differently based on user input
Modules and Imports

Modules group related code and functions
Can be imported fully or partially, with optional aliases
Using selective imports improves clarity
Avoid wildcard imports (*) to prevent conflicts
Name Management

Python uses symbol tables to track names and objects
dir() lists all names in a module
sys.path shows directories Python searches for modules
The __name__ Variable

__name__ is "__main__" when a file runs as a script
Changes to the module name when imported
Helps control which code executes
Conclusion

This lab taught how to create scripts, use command-line arguments, import modules, and manage namespaces. These skills are important for writing scalable, reusable, and well-structured Python programs.