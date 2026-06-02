import os
import shutil
import logging

logging.basicConfig(
    filename="operations_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Music": [".mp3", ".wav", ".aac"],
    "Code": [".py", ".js", ".html", ".css", ".java"],
    "Others": []
}

def get_folder_name(extension):
    for folder, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return folder
    return "Others"

def sort_files(directory):
    print(f"\nSorting files in: {directory}")
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isdir(file_path):
            continue
        _, ext = os.path.splitext(filename)
        folder_name = get_folder_name(ext)
        target_folder = os.path.join(directory, folder_name)
        os.makedirs(target_folder, exist_ok=True)
        try:
            shutil.move(file_path, os.path.join(target_folder, filename))
            print(f"Moved: {filename} -> {folder_name}")
            logging.info(f"Moved: {filename} -> {folder_name}")
        except Exception as e:
            print(f"Error moving {filename}: {e}")
            logging.error(f"Error moving {filename}: {e}")

def rename_files(directory):
    print(f"\nRenaming files in: {directory}")
    prefix = input("Enter prefix name (e.g. 'photo'): ")
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    for i, filename in enumerate(files):
        ext = os.path.splitext(filename)[1]
        new_name = f"{prefix}_{i+1}{ext}"
        try:
            os.rename(
                os.path.join(directory, filename),
                os.path.join(directory, new_name)
            )
            print(f"Renamed: {filename} -> {new_name}")
            logging.info(f"Renamed: {filename} -> {new_name}")
        except Exception as e:
            print(f"Error renaming {filename}: {e}")

def delete_empty_folders(directory):
    print(f"\nCleaning empty folders in: {directory}")
    for folder in os.listdir(directory):
        folder_path = os.path.join(directory, folder)
        if os.path.isdir(folder_path) and not os.listdir(folder_path):
            try:
                os.rmdir(folder_path)
                print(f"Deleted empty folder: {folder}")
                logging.info(f"Deleted empty folder: {folder}")
            except Exception as e:
                print(f"Error deleting {folder}: {e}")

def main():
    print("=== File Automation Tool ===")
    directory = input("\nEnter the folder path to work on: ")
    if not os.path.exists(directory):
        print("That folder does not exist!")
        return
    print("\nWhat do you want to do?")
    print("1. Sort files by type")
    print("2. Rename files")
    print("3. Delete empty folders")
    print("4. Do all")
    choice = input("\nEnter choice (1/2/3/4): ")
    if choice == "1":
        sort_files(directory)
    elif choice == "2":
        rename_files(directory)
    elif choice == "3":
        delete_empty_folders(directory)
    elif choice == "4":
        sort_files(directory)
        rename_files(directory)
        delete_empty_folders(directory)
    else:
        print("Invalid choice!")
    print("\nDone! Check operations_log.txt for details.")

if __name__ == "__main__":
    main()