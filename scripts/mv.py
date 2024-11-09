import os
import shutil

# Define the directories
source_dir = './'
extra_copy_dir = './extra_copy/'
done_dir = './done/'

# Remove all files in the extra_copy directory
for file in os.listdir(extra_copy_dir):
    os.remove(os.path.join(extra_copy_dir, file))

# Process each .cpp file in the source directory
for file in os.listdir(source_dir):
    if file.endswith(".cpp"):
        file_name = os.path.splitext(file)[0]
        url_line = f"// https://open.kattis.com/problems/{file_name}\n"
        
        # Read the source file content
        with open(os.path.join(source_dir, file), 'r') as f:
            content = f.read()
        
        # Write to a new file with the URL comment prepended
        new_file_name = f"{file_name}1.cpp"
        with open(new_file_name, 'w') as f:
            f.write(url_line + content)
        
        # Copy the new file to the extra_copy directory
        shutil.copy(new_file_name, os.path.join(extra_copy_dir, file))
        
        # Move the new file to the done directory
        shutil.move(new_file_name, os.path.join(done_dir, file))
        
        # remove the old file from the source directory
        os.remove(os.path.join(source_dir, file))

# Remove all .out files
for file in os.listdir(source_dir):
    if file.endswith(".out"):
        os.remove(os.path.join(source_dir, file))


print(len(os.listdir(extra_copy_dir)))