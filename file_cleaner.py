import os
import shutil

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

def get_files_in_directory(directory):
    
    #Returns a list of file paths in the given directory.

    all_files = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            all_files.append(item_path)
    return all_files

#Organizes files in the source directory by their extensions.
def organize_by_extension(source_directory):
    
    
    #Get the list of files from the source directory
    files = get_files_in_directory(source_directory)
    
    for file_path in files:
        #Extract the file extension
        _, ext = os.path.splitext(file_path)
        ext = ext.lower() #Standardizes to lowercase
        
        #Decide on folder name based on extension
        folder_name = EXTENSION_MAP.get(ext, 'Others')
       
        #Construct the full path of the target folder
        target_folder = os.path.join(source_directory, folder_name)
        
        #Creates the target folder if it doesn't exist
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        
        #Constructs the full path for the new file location
        file_name = os.path.basename(file_path)
        new_path = os.path.join(target_folder, file_name)
       
        #Moves the file from the source directory to the target folder
        shutil.move(file_path, new_path)
        
        #Prints a message to show what happened
        print(f"Moved {file_name} to {folder_name}")
        pass
def main():
    
    #Main function 
    
    source_directory = input("Enter the directory to clean (ex. /Users/You/Desktop): ")
    
    # Prints out the files to check that it's working
    files = get_files_in_directory(source_directory)
    print("Found the following files:")
    for f in files:
        print(f)
    
    # Calls the organizer function
    organize_by_extension(source_directory)
    print("Organization complete!")

if __name__ == "__main__":
    main()
