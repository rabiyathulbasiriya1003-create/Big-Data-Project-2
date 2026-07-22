# README - Hadoop MapReduce Word Count

## Project Name

**Hadoop MapReduce Word Count using Python**

## Description

This project implements the **Word Count** program using the Hadoop MapReduce concept in Python. It reads words from a text file, maps each word with a count of **1**, sorts the intermediate output, partitions the data, and finally reduces it to calculate the total occurrence of each word.

---

## Project Files

### 1. `main.py`

* Controls the complete execution of the MapReduce process.
* Executes the Mapper.
* Sorts the Mapper output.
* Executes the Partitioner.
* Executes the Reducer.
* Displays the final word count.

### 2. `mapper.py`

* Reads each line from the input text file.
* Splits the line into individual words.
* Outputs each word in the format:

  ```text
  word    1
  ```

### 3. `partitioner.py`

* Reads the sorted Mapper output.
* Passes the data to the Reducer.
* (In this project, it simply forwards the data.)

### 4. `reducer.py`

* Reads the partitioned data.
* Groups identical words.
* Adds their counts.
* Prints the final frequency of each word.

### 5. `food.txt`

Input file containing food names.

Example:

```text
rice dosa rice
idli pongal dosa
chapati rice
dosa biryani idli
pongal chapati rice
biryani biryani dosa
chapati idli pongal
rice dosa biryani
idli chapati rice
pongal pongal dosa
```

---

## Execution Flow

```text
food.txt
     │
     ▼
 mapper.py
     │
     ▼
 mapped.txt
     │
     ▼
 Sorting
     │
     ▼
 sorted.txt
     │
     ▼
 partitioner.py
     │
     ▼
 partitioned.txt
     │
     ▼
 reducer.py
     │
     ▼
 Final Output
```

---

## Expected Output

```text
biryani    4
chapati    4
dosa       6
idli       4
pongal     5
rice       6
```

---

## How to Run

Run the following command in the terminal:

```bash
python main.py
```

---

## Features

* Implements the Hadoop MapReduce concept.
* Counts the frequency of words.
* Uses separate Mapper, Partitioner, and Reducer programs.
* Easy to understand and modify.
* Suitable for learning Hadoop MapReduce fundamentals.

---

## Conclusion

This project demonstrates the working of the Hadoop MapReduce framework using Python scripts. It processes an input text file through the Mapper, Sort, Partitioner, and Reducer stages to generate the frequency of each word efficiently.
