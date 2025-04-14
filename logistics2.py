import os
import shutil

n=int(input("How many folders you want to split into:?"))

# Define the path to the folder containing the PDFs
folder_path = "path/to/your/folder"
# Define the path where you want to create the subfolders
output_base_path = "path/to/your/output/folders"

# Ensure the output base path exists
if not os.path.exists(output_base_path):
    os.makedirs(output_base_path)

# List all PDF files in the folder
pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

# Calculate the number of files per folder
num_files = len(pdf_files)
files_per_folder = num_files // n
remainder = num_files % n
#n is basically the number of folders you want to split into
# Create and populate the folders
start_index = 0
for i in range(n):
    folder_name = f"folder_{i+1}"
    folder_output_path = os.path.join(output_base_path, folder_name)
    os.makedirs(folder_output_path, exist_ok=True)

    # Determine the end index for this batch of files
    end_index = start_index + files_per_folder
    if i < remainder:
        end_index += 1

    # Move the files to the new folder
    for j in range(start_index, end_index):
        source_path = os.path.join(folder_path, pdf_files[j])
        destination_path = os.path.join(folder_output_path, pdf_files[j])
        shutil.move(source_path, destination_path)

    # Update the start index for the next batch
    start_index = end_index

print("PDF files have been successfully divided into n folders.")