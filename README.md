* Description
This project implements a MapReduce pipeline using Python to parse, process, and analyze end-semester examination grade sheets. It reads through multiple unstructured or semi-structured text files containing student records, extracts the final grades, and aggregates the total count for each valid grade category (S, A, B, C, D, E, and F). The project is designed to simulate a distributed data processing environment and can be run locally using Unix pipes or deployed to a Hadoop cluster via Hadoop Streaming.

* Technologies Used
* **Python 3:** Core programming language used for the Mapper and Reducer logic.
* **Bash / Unix Shell:** Used for scripting the local execution pipeline (`cat`, `sort`, `|`).
* **MapReduce Paradigm:** The underlying distributed computing framework concept used for mapping data pairs and reducing them into aggregated results.
* **Hadoop Streaming (Optional):** The scripts are fully compatible with Hadoop for distributed processing on large clusters.

* Features
* **Intelligent Data Filtering:** Automatically sanitizes input by ignoring file headers, footers, statistical metadata, and empty lines. It isolates valid student records by validating numeric Registration Numbers (REGNO).
* **Flexible Parsing:** Seamlessly handles inconsistent spacing, tabs, and formatting across different source files.
* **Zero Dependencies:** Built entirely using Python's standard library (`sys`), requiring no third-party packages like `pandas` or `mrjob`.
* **Highly Scalable:** The decoupled Mapper and Reducer architecture allows the pipeline to scale from analyzing a few megabytes of text locally to terabytes of data on a distributed cluster.
  
* How to Run

**Step 1: Prepare the Environment**
Ensure you have Python 3 installed on your machine and are using a Unix-like terminal (Linux, macOS, or WSL). 

**Step 2: Grant Execution Permissions**
Make the Python scripts and the bash execution script executable:
```bash
chmod +x src/mapper.py src/reducer.py run_job.sh
