import os
import pandas as pd

# Set the path to the folder containing the CSV files
folder_path = "C:\\Users\\msthu\\PycharmProjects\\pythonProject1\\semester5\\datascience\\data\\reviews"

# Get a list of all CSV files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Read the first CSV file to get column names and create an empty DataFrame
first_file_path = os.path.join(folder_path, csv_files[0])
df_combined = pd.read_csv(first_file_path)
i=0
# Iterate through the remaining CSV files and append them to the DataFrame
for csv_file in csv_files[1:]:
    file_path = os.path.join(folder_path, csv_file)
    df = pd.read_csv(file_path)
    i=i+1
    print(i)
    # Check if the columns of the current file match the columns of the combined DataFrame
    if list(df.columns) == list(df_combined.columns):
        df_combined = pd.concat([df_combined, df], ignore_index=True)
    else:
        print(f"Columns of {csv_file} do not match. Skipping.")

# Save the combined DataFrame to a new CSV file
combined_output_path = "C:\\Users\\msthu\\PycharmProjects\\pythonProject1\\semester5\\datascience\\data\\reviewsfile.csv"
df_combined.to_csv(combined_output_path, index=False)

print(f"Combined CSV file saved to {combined_output_path}")
