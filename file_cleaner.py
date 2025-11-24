from pathlib import Path
import shutil

# Maps file extensions to folders
EXTENSION_MAP = {
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
    '.pdf': 'Documents',
    '.doc': 'Documents',
    '.docx': 'Documents',
    '.txt': 'Documents',
    '.mp3': 'Music',
    '.wav': 'Music',
    '.pptx': 'Powerpoint'
}

def get_files_in_directory(directory: Path):
    """
    Return a list of file Paths in the given directory (non-recursive).
    """
    return [item for item in directory.iterdir() if item.is_file()]

def organize_by_extension(source_directory: Path):
    """
    Organize files into folders based on their extensions.
    """
    files = get_files_in_directory(source_directory)

    for file_path in files:
        ext = file_path.suffix.lower()
        folder_name = EXTENSION_MAP.get(ext, 'Others')
        target_folder = source_directory / folder_name
        target_folder.mkdir(exist_ok=True)

        new_path = target_folder / file_path.name

        try:
            shutil.move(str(file_path), str(new_path))
            print(f"Moved {file_path.name} to {folder_name}")
        except Exception as e:
            print(f"Error moving {file_path.name}: {e}")

def main():
    """
    Main function:
    - Asks user for the directory path
    - Lists files found
    - Asks for confirmation before moving files
    """
    # Prompt user to enter the path
    source_directory_input = input("Enter the directory to clean (e.g. /Users/You/Desktop): ")
    source_directory = Path(source_directory_input).expanduser().resolve()

    if not source_directory.is_dir():
        print(f"Error: {source_directory} is not a valid directory.")
        return

    files = get_files_in_directory(source_directory)
    if not files:
        print("No files found in the specified directory.")
        return

    print("\nFound the following files:")
    for f in files:
        print(f" - {f.name}")

    proceed = input("\nProceed with organizing these files? (y/n): ").strip().lower()
    if proceed == 'y':
        organize_by_extension(source_directory)
        print("Organization complete!")
    else:
        print("Operation cancelled.")

if __name__ == "__main__":
    main()
