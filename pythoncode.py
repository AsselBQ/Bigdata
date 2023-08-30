import csv
import argparse

def csv_reader(file_name):
    with open(file_name, "r") as file:
        csv_reader = csv.reader(file)
        for row_ind, row in enumerate(csv_reader, start=1):
            for col_ind, cell_value in enumerate(row, start=1):
                yield cell_value, row_ind, col_ind

def create_color_count(data, error_condition=None):
    color_count = {}
    error_cells = set()

    for cell_value, row_ind, col_ind in data:
        if cell_value in color_count:
            color_count[cell_value] += 1
        else:
            color_count[cell_value] = 1

        if error_condition and error_condition(cell_value):
            error_cells.add((row_ind, col_ind))

    return color_count, error_cells

def main():
    parser = argparse.ArgumentParser(description="Count color occurrences in a CSV file.")
    parser.add_argument("-error", dest="error_color", help="Color to trigger an error condition")
    args = parser.parse_args()

    error_condition = lambda color_value: color_value == args.error_color if args.error_color else False

    file_path = "Colors.csv"
    data_generator = csv_reader(file_path)
    color_count, error_cells = create_color_count(data_generator, error_condition)

    print("Reading CSV file\n")
    for row_ind, col_ind in error_cells:
        print(f"Found a broken {args.error_color} cell at row {row_ind}, column {col_ind}")

    print("\nDone reading CSV file\n")

    for color, count in color_count.items():
        print(f"{count} {color} cells")

if __name__ == "__main__":
    main()
