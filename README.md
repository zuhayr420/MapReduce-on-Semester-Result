This repository contains a MapReduce pipeline written in Python that analyzes university grade sheets.The project processes multiple text files containing end-semester examination results and aggregates the total number of students in each valid grade category (S, A, B, C, D, E, and F).
The implementation uses standard standard input/output streams (⁠sys.stdin⁠ and ⁠sys.stdout⁠),making it compatible with Hadoop Streaming or local terminal execution.

Prerequisites:
 Python 3.x:Required to run the mapper and reducer scripts.
 Unix-like Environment:A Linux, macOS, or WSL (Windows Subsystem for Linux)terminal to execute the shell script and pipe commands.

Input Data Format:
The pipeline expects unstructured or semi-structured text files where student records are represented line-by-line.The mapper is designed to handle variable whitespace and tabs, automatically filtering out headers, footers, and statistical metadata by ensuring the row starts with a numeric Registration Number (⁠REGNO⁠).
A Valid row will look like this:
202400021	 35.70	   29	   65.00	B

Expected Output:
The script will output a sorted list of all valid grades alongside their total occurrences across all analyzed files.
A       134
B       160
C       209
D       212
E       64
F       74
S       33
