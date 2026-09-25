#!/usr/bin/env python3
import sys

current_grade = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    
    try:
        grade, count = line.split('\t', 1)
        count = int(count)
    except ValueError:
        continue
        
    if current_grade == grade:
        current_count += count
    else:
        if current_grade:
            print(f"{current_grade}\t{current_count}")
        current_grade = grade
        current_count = count

# Output the final grade count
if current_grade == grade:
    print(f"{current_grade}\t{current_count}")
