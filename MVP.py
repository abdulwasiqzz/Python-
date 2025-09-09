import os       # to work with files/folders
import shutil   # to move files
from pathlib import Path 

# Set your folder path (change if needed)
TARGET_FOLDER = Path("D:/Semester 1")

# Dictionary: file extensions → folder name
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar"],
    "Code": [".py", ".java", ".cpp", ".html", ".js"]
}

def organize_folder(folder):
    for file in folder.iterdir():  # loop through all items in folder
        if file.is_file():  # only work on files, not folders
            moved = False
            for category, extensions in FILE_TYPES.items():
                if file.suffix.lower() in extensions:  # check extension
                    target_folder = folder / category
                    target_folder.mkdir(exist_ok=True)  # create if not exist
                    shutil.move(str(file), str(target_folder / file.name))
                    print(f"Moved {file.name} → {category}")
                    moved = True
                    break
            if not moved:
                # Files that don't match go to "Others"
                other_folder = folder / "Others"
                other_folder.mkdir(exist_ok=True)
                shutil.move(str(file), str(other_folder / file.name))
                print(f"Moved {file.name} → Others")

# ✅ This part must be at the bottom (not inside the function!)
if __name__ == "__main__":
    if TARGET_FOLDER.exists():
        organize_folder(TARGET_FOLDER)
        print("🎉 Done organizing your files!")
    else:
        print("❌ Folder path not found. Check your path.")
 
 