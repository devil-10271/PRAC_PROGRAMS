import os

def rename_txt_files(directory_path):
    # Check if the directory exists
    if not os.path.exists(directory_path):
        print(f"Directory '{directory_path}' doesn't exist.")
        return

    # Get a list of all '.txt' files  ______________main logic
    txt_files = [file for file in os.listdir(directory_path) if file.endswith(".txt")]

    # Check if there are any '.txt' files in the directory   
    if not txt_files:
        print(f"No '.txt' files found in '{directory_path}'.")
        return

    # Iterate through each '.txt' file and rename with natural numbers
    for index, file_name in enumerate(txt_files, start=1):
        old_path = os.path.join(directory_path, file_name)
        new_name = f"{index}.txt"
        new_path = os.path.join(directory_path, new_name)

        # Rename the file
        os.rename(old_path, new_path)

        # Print a message indicating the file has been renamed
        print(f"Renamed: {file_name} -> {new_name}")

if __name__ == "__main__":
    # Get the directory path from the user
    directory_path = input("Enter the directory path containing '.txt' files: ")

    # Call the function to rename '.txt' files in the specified directory
    rename_txt_files(directory_path)
 