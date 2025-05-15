# clean_attendance.py

input_file = "attendance.txt"

with open(input_file, "r") as infile:
    lines = infile.readlines()

with open(input_file, "w") as outfile:
    for line in lines:
        if " @ " in line and len(line.strip().split(" @ ")) == 2:
            outfile.write(line)
