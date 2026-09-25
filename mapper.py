#!/usr/bin/env python3
import sys

# Define the target grade categories
TARGET_GRADES = {'S', 'A', 'B', 'C', 'D', 'E', 'F'}

for line in sys.stdin:
    line = line.strip()
    
    if not line:
        continue
        
    # Split by whitespace to handle irregular tabs and spaces
    parts = line.split()
    
    # Valid student record rows have at least 5 columns and start with a numeric REGNO
    if len(parts) >= 5 and parts[0].isdigit():
        grade = parts[-1].strip().upper()
        
        if grade in TARGET_GRADES:
            # Emit key-value pair separated by a tab
            print(f"{grade}\t1")
