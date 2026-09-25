import subprocess

def run_local_mapreduce():
    # Pipeline: Read file -> Mapper -> Shuffle & Sort -> Reducer
    command = "cat files.txt | python3 mapper.py | sort | python3 reducer.py"
    
    print("Starting MapReduce Job...\n")
    
    try:
        # Execute the shell command
        process = subprocess.run(
            command, 
            shell=True, 
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True
        )
        
        print("--- ANALYSIS RESULTS ---")
        print("GRADE\tCOUNT")
        print("-" * 15)
        print(process.stdout)
        
    except subprocess.CalledProcessError as e:
        print("An error occurred during MapReduce execution:")
        print(e.stderr)

if __name__ == "__main__":
    run_local_mapreduce()
