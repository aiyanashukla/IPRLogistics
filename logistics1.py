import pandas as pd
import requests
import os

# Function to download a PDF from a URL and save it
def download_pdf(url, save_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        print(f"Downloaded: {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")

csv_file_path = "enter the file path to your csv"
df = pd.read_csv(csv_file_path)

# Debug: Print the column names to check for discrepancies
print("Column names in the CSV:", df.columns.tolist())
df.columns = df.columns.str.strip()

# Ensure the column names are correct (optional)
roll_number_col = 'Name'
file_url_col = 'URL'

# Specify the target directory where the downloaded files will be saved
target_directory = "folder path"

# Create the target directory if it doesn't exist
if not os.path.exists(target_directory):
    os.makedirs(target_directory)

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    try:
        roll_number = row[roll_number_col]
        file_url = row[file_url_col]
        file_path = os.path.join(target_directory, f"{roll_number}.pdf")
        download_pdf(file_url, file_path)
    except KeyError as e:
        print(f"Column not found: {e}")
    except Exception as e:
        print(f"Error processing row {index}: {e}")

print("All files have been processed.")