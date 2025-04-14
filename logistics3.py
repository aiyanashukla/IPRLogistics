import pandas as pd
import os

# Load the CSV file into a pandas DataFrame
csv_file_path = "path_to_your_csv_file.csv"
df = pd.read_csv(csv_file_path)

# Clean column names by stripping any leading/trailing spaces
df.columns = df.columns.str.strip()

# Path to the directory containing the student files
folder = "C:/Users/aiyan/Downloads/appian-corporation-software-engineering-intern"

#write the number of files you have in the folder please do change the start and end values
start_iloc = -60
end_iloc = -490
step_value = -1

# Function to process files in the specified iloc range
def process_files(start_index, end_index):
    for index, row in df.iloc[start_index:end_index].iterrows():
        rollnumber = str(row['Roll Number']).strip()
        name = row['Student Name'].strip()
        
        oldname = os.path.join(folder, f"{rollnumber}.pdf")
        newname = os.path.join(folder, f"{name}.pdf")
        
        try:
            if os.path.exists(oldname):
                os.rename(oldname, newname)
                print(f"Renamed {oldname} to {newname}")
            else:
                print(f"File {oldname} does not exist")
        except Exception as e:
            print(f"Error renaming file {oldname}: {e}")

# Iterate through the DataFrame from start_iloc to end_iloc with step_value
for iloc in range(start_iloc, end_iloc - 1, step_value):
    # Determine the end index for the current step
    current_end_iloc = iloc - step_value
    if current_end_iloc < end_iloc:
        current_end_iloc = end_iloc  # Ensure we don't go out of bounds

    print(f"Processing rows from index {iloc} to {current_end_iloc}")
    process_files(iloc, current_end_iloc)

print("File renaming process completed for all specified ranges.")
