import argparse
import os

parser = argparse.ArgumentParser(description="Check if you have solved a specific kattis problem")

parser.add_argument("name", type=str, help="The problem name")
parser.add_argument("--lang", type=str, help="The extension of the file", choices=["cpp", "py"], default="cpp")
parser.add_argument("--path", type=str, help="The path to the problem", default="solutions/")

args = parser.parse_args()

#check path for 
file_path = os.path.join(args.path, f"{args.name}.{args.lang}")

if os.path.isfile(file_path):
    print(f"Found the file: {file_path}")
else:
    print(f"The file '{args.name}.{args.lang}' does not exist in '{args.path}'")