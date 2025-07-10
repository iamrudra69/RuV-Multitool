import os 
import requests

from Functions import interface

menuOptions = "[1] Rename Files 📂\n[2] Download File 📥"


def renameFiles():
    print("\033[0mThis feature renames the files")
    print(f"\033[1;33m=========================\033[0m")
    path = input(f"\033[1;36mEnter the directory path to rename files (default: current directory): \033[0m").strip() or os.getcwd()

    # Validate path
    if not os.path.isdir(path):
        print(f"\033[91m❌ Invalid directory: {path}\033[0m")
        return

    os.chdir(path)
    files = [f for f in os.listdir() if os.path.isfile(f)]

    if not files:
        print(f"\033[93m⚠️ No files found in the directory.\033[0m")
        return

    # Handle old file names input
    oldNames = input("\033[1;36mEnter old file names (comma-separated, leave empty for all files): \033[0m").strip().split(',')
    oldNames = [name.strip() for name in oldNames if name.strip()]

    # Handle new file names input
    newNames = input("\033[1;36mEnter new file names (comma-separated, leave empty for auto-indexing): \033[0m").strip().split(',')
    newNames = [name.strip() for name in newNames if name.strip()]
    print(f"\033[1;33m=========================\033[0m")

    # Use all files if oldNames is empty
    if not oldNames:
        oldNames = files

    # Filter oldNames to only match files in the directory
    oldNames = [name for name in oldNames if name in files]

    if not oldNames:
        print(f"\033[93m⚠️ No matching files found to rename.\033[0m")
        return

    # === Case 1: Rename with custom new names
    if newNames:
        if len(newNames) != len(oldNames):
            print(f"\033[91m❌ Mismatch in the number of old and new names. Please ensure both lists match in length.\033[0m")
            return

        print(f"\033[96m🔧 Renaming with custom names...\033[0m")
        for old, new in zip(oldNames, newNames):
            try:
                os.rename(old, new)
                print(f"\033[92m{old} → {new} ✔️\033[0m")
            except Exception as e:
                print(f"\033[91m❌ Failed: {old} → {new}: {e}\033[0m")

    # === Case 2: Auto-generate indexed names with extensions
    elif not newNames and oldNames:
        print(f"\033[96m🔁 Auto-generating indexed names...\033[0m")
        width = max(2, len(str(len(oldNames))))  # Use 2 digits as minimum width
        for idx, old in enumerate(oldNames):
            new_name = f"{str(idx).zfill(width)}{os.path.splitext(old)[1]}"  # Keep extension
            try:
                os.rename(old, new_name)
                print(f"\033[92m{old} → {new_name} ✔️\033[0m")
            except Exception as e:
                print(f"\033[91m❌ Failed: {old} → {new_name}: {e}\033[0m")

    # === Case 3: Default basic numbering (1, 2, 3...) when no inputs passed
    else:
        print(f"\033[96m🔄 Renaming all files with basic counting...\033[0m")
        width = len(str(len(files)))  # Length to pad numbers with
        for idx, old in enumerate(files, 1):
            new_name = f"{str(idx).zfill(width)}{os.path.splitext(old)[1]}"  # Keep extension
            try:
                os.rename(old, new_name)
                print(f"\033[92m{old} → {new_name} ✔️\033[0m")
            except Exception as e:
                print(f"\033[91m❌ Failed: {old} → {new_name}: {e}\033[0m")


def downloadFile():
    print("\033[0mThis feature downloads the file or the HTML of the given URL!")
    print(f"\033[1;33m=========================\033[0m")

    url = input("\033[1;36mEnter the URL of the file to download: \033[0m").strip()
    filename = input("\033[1;36mEnter the filename to save as (with extension): \033[0m").strip()
    folder = input("\033[1;36mEnter the folder path to save the file (leave empty for Downloads): \033[0m").strip()

    print(f"\033[1;33m=========================\033[0m")

    if not url.startswith("http://") and not url.startswith("https://"):
        print("\033[1;31mInvalid URL. Please provide a valid HTTP or HTTPS URL.\033[0m")
        return

    if not filename:
        print("\033[1;31mFilename cannot be empty.\033[0m")
        return

    if not folder:
        folder = os.path.join(os.path.expanduser("~"), "Downloads")
        print(f"\033[38;5;44mNo folder given. Using default Downloads folder: {folder}\033[0m")

    os.makedirs(folder, exist_ok=True)
    full_path = os.path.join(folder, filename)

    if os.path.exists(full_path):
        print(f"\033[1;33mFile '{full_path}' already exists. Overwriting...\033[0m")
    else:
        print(f"\033[38;5;27mSaving file as {full_path}...\033[0m")

    print(f"\033[38;5;27mDownloading file from {url}...\033[0m")

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        with open(full_path, "wb") as file:
            file.write(response.content)
        print(f"\033[38;5;45mFile downloaded successfully: {full_path}\033[0m")

    except requests.exceptions.RequestException as e:
        print(f"\033[1;31mError downloading file: {e}\033[0m")


def fileMenu():
    interface("Files", menuOptions, renameFiles, downloadFile)