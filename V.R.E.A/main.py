import os
import shutil
# Specify the directory path
path = r"C:\Users\Admin\AppData\Local\Temp"
path1= r"C:\Windows\Prefetch"

def clear_directory(directory_path):
    # Check if the directory exists
    if not os.path.exists(directory_path):
        print(f"The directory '{directory_path}' does not exist.")
        return

    # Loop through each item in the directory
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        try:
            # Check if it's a file or directory
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.remove(item_path)  # Remove file or symbolic link
                print(f"Deleted file: {item_path}")
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)  # Remove directory
                print(f"Deleted folder: {item_path}")
        except Exception as e:
            print(f"Failed to delete {item_path}. Reason: {e}")

    print(f"All contents in '{directory_path}' have been deleted.")

# Call the function
clear_directory(path)
clear_directory(path1)
