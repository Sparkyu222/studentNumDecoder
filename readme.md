# Student ID Decoder

### Overview

This Python utility offers a simple, yet powerful tool to convert anonymized student IDs in a PDF document back to identifiable names. Originally crafted out of boredom, it serves an essential function in the academic context where student grades are published without names, preserving privacy yet maintaining individual recognizability for those with access to the corresponding student records.

The script simply works by taking a PDF file containing anonymized student IDs and a CSV file with names mapped to those IDs, and it outputs the full names associated with each ID in the terminal.

At this moment, this script will only print out the first table that it found.

### Prerequisites

Before you get started with using this Python script, ensure you have the following dependencies installed:

• `tabula`: A library for extracting tables from PDF files.

• `pandas`: A powerful data manipulation library. (While tabula may install pandas as a dependency, ensure it is available in your environment.)

### Installation of Dependencies

To install the required dependencies, run the following commands in your terminal:

```bash
pip3 install tabula-py
pip3 install pandas
```

Note: Ensure that you have Python3 and pip already installed on your system.

### Usage

To use this script, follow the syntax below:

```bash
python3 decoder.py <csv_file> <pdf_file>
```
CSV File Format

Ensure that your CSV file adheres to the following structure:

```csv
student id, last name, firstname
12345678, Doe, John
```

Each line should contain a student ID followed by the last name and first name of a student, separated by commas.

### Running the Script

To run the script, provide the path to the CSV file containing student IDs alongside their corresponding last names and first names, as well as the path to the PDF file that contains the grades with anonymized student IDs.

Example:

```bash
python3 decoder.py students.csv grades.pdf
```

### Customization

If necessary, you can alter the regular expression used to match the student ID within the script to fit a different ID format. The default is set to match an 8-digit string.

Happy decoding!
