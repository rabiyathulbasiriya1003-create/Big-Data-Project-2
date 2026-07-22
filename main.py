import subprocess

input_file = "food.txt"

# Mapper
with open(input_file, "r") as infile, open("mapped.txt", "w") as outfile:
    subprocess.run(["python", "mapper.py"], stdin=infile, stdout=outfile)

# Sort
with open("mapped.txt", "r") as infile:
    lines = sorted(infile.readlines())

with open("sorted.txt", "w") as outfile:
    outfile.writelines(lines)

# Partitioner
with open("sorted.txt", "r") as infile, open("partitioned.txt", "w") as outfile:
    subprocess.run(["python", "partitioner.py"], stdin=infile, stdout=outfile)

# Reducer
with open("partitioned.txt", "r") as infile:
    subprocess.run(["python", "reducer.py"], stdin=infile)