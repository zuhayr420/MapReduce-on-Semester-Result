# Description:
This project implements a MapReduce pipeline on university examination data using Python. The MapReduce framework is used to extract student grades from text files and calculate the total number of students in each grade category (S, A, B, C, D, E, and F).  

# Technologies used:
- Python
- Map Reduce

# Features:
Reads unstructured examination text files
Filters valid student records using registration numbers
Finds and extracts the final grades
Generates intermediate key-value pairs (Mapping)
Calculates the aggregated count of each grade (Reducing)
Dataset: The project uses text files containing end-semester examination results with details like registration numbers, internal marks, university marks, totals, and final grades.  

# How to Run:
* Clone the repository
* Place the grade sheet text files in the data directory
* Make the python and bash scripts executable
* Run the bash script or terminal pipe command

# Output:
The program displays:
* Valid grade categories
* Total student counts for each grade
# Result:
MapReduce was successfully implemented using Python to process and aggregate the distribution of grades across multiple university examination records.
