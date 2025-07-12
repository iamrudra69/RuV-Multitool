import os 
import requests
import pathlib

from functions import interface, inputColor, outputColor, errorColor, outputLine

menuOptions = "[1] Rename Files 📂\n[2] Download File 📥\n[3] Search Files 🔍"

def renameFiles():
    try:
        print(outputColor("This feature renames the files ✏️"))
        outputLine()
        path = input(inputColor("Enter the directory path to rename files (default: current directory) 📁 : ")).strip() or os.getcwd()

        if not os.path.isdir(path):
            print(errorColor(f"❌ Invalid directory: {path} 🚫"))
            return

        os.chdir(path)
        files = [f for f in os.listdir() if os.path.isfile(f)]

        if not files:
            print(errorColor("⚠️ No files found in the directory. 📭"))
            return

        oldNames = input(inputColor("Enter old file names (comma-separated, leave empty for all files) 📝 : ")).strip().split(',')
        oldNames = [name.strip() for name in oldNames if name.strip()]

        newNames = input(inputColor("Enter new file names (comma-separated, leave empty for auto-indexing) 🔠 : ")).strip().split(',')
        newNames = [name.strip() for name in newNames if name.strip()]
        outputLine()

        if not oldNames:
            oldNames = files

        oldNames = [name for name in oldNames if name in files]

        if not oldNames:
            print(errorColor("⚠️ No matching files found to rename. ❗"))
            return

        if newNames:
            if len(newNames) != len(oldNames):
                print(errorColor("❌ Mismatch in the number of old and new names. Please ensure both lists match in length. ⚖️"))
                return

            print(outputColor("🔧 Renaming with custom names... ✂️"))
            for old, new in zip(oldNames, newNames):
                try:
                    os.rename(old, new)
                    print(outputColor(f"{old} → {new} ✔️"))
                except Exception as e:
                    print(errorColor(f"❌ Failed: {old} → {new}: {e} 💥"))

        elif not newNames and oldNames:
            print(outputColor("🔁 Auto-generating indexed names... 🔢"))
            width = max(2, len(str(len(oldNames))))
            for idx, old in enumerate(oldNames):
                new_name = f"{str(idx).zfill(width)}{os.path.splitext(old)[1]}"
                try:
                    os.rename(old, new_name)
                    print(outputColor(f"{old} → {new_name} ✔️"))
                except Exception as e:
                    print(errorColor(f"❌ Failed: {old} → {new_name}: {e} 💥"))

        else:
            print(outputColor("🔄 Renaming all files with basic counting... 🔁"))
            width = len(str(len(files)))
            for idx, old in enumerate(files, 1):
                new_name = f"{str(idx).zfill(width)}{os.path.splitext(old)[1]}"
                try:
                    os.rename(old, new_name)
                    print(outputColor(f"{old} → {new_name} ✔️"))
                except Exception as e:
                    print(errorColor(f"❌ Failed: {old} → {new_name}: {e} 💥"))

    except KeyboardInterrupt:
        print("\n")
        outputLine()
        print(errorColor("⛔ Operation cancelled by user. 🛑"))

    except Exception as e:
        print("\n")
        outputLine()
        print(errorColor(f"❌ Unexpected error occurred: {e} 🚨"))

def downloadFile():
    try:
        print(outputColor("This feature downloads the file or the HTML of the given URL 🌐"))
        outputLine()

        url      = input(inputColor("Enter the URL of the file to download 🌍 : ")).strip()
        filename = input(inputColor("Enter the filename to save as (with extension) 💾 : ")).strip()
        folder   = input(inputColor("Enter the folder path to save the file (leave empty for Downloads) 📂 : ")).strip()
        outputLine()

        if not url.startswith("http://") and not url.startswith("https://"):
            print(errorColor("Invalid URL. Please provide a valid HTTP or HTTPS URL ❗🌐"))
            return

        if not filename:
            print(errorColor("Filename cannot be empty ❗📛"))
            return

        if not folder:
            folder = os.path.join(os.path.expanduser("~"), "Downloads")
            print(outputColor(f"📁 No folder given. Using default Downloads folder: {folder} 📥"))

        os.makedirs(folder, exist_ok=True)
        full_path = os.path.join(folder, filename)

        if os.path.exists(full_path):
            print(outputColor(f"⚠️ File '{full_path}' already exists. Overwriting... ✍️"))
        else:
            print(outputColor(f"📄 Saving file as {full_path}... 💾"))

        print(outputColor(f"⬇️ Downloading file from {url}... 🔽"))

        try:
            response = requests.get(url)
            response.raise_for_status()
            with open(full_path, "wb") as file:
                file.write(response.content)
            print(outputColor(f"✅ File downloaded successfully: {full_path} 🎉"))

        except requests.exceptions.RequestException as e:
            print(errorColor(f"❌ Error downloading file: {e} ⚠️"))

    except KeyboardInterrupt:
        print("\n")
        outputLine()
        print(errorColor("⛔ Operation cancelled by user. 🛑"))

    except Exception as e:
        print("\n")
        outputLine()
        print(errorColor(f"❌ Unexpected error occurred: {e} 🚨"))

def searchFiles():
    try:
        inputPath = input(inputColor("Enter the folder path 🔍 : "))
        folderPath = pathlib.Path(inputPath)
        filePaths = []

        for file in folderPath.rglob('*'):
            if file.is_file():
                filePaths.append(str(file))

        formatted_output = '[\n' + ',\n'.join(f'  "{path}"' for path in filePaths) + '\n]'
        print(outputColor("📁 Files Found: " + formatted_output))

        fileExtensions = []
        for file in folderPath.rglob('*'):
            if file.is_file():
                ext = file.suffix.lower()
                if ext and ext not in fileExtensions:
                    fileExtensions.append(ext)

        formattedd_output = '[\n' + ',\n'.join(f'  "{ext}"' for ext in fileExtensions) + '\n]'
        print(outputColor("📦 Unique File Extensions: " + formattedd_output))

    except KeyboardInterrupt:
        print("\n")
        outputLine()
        print(errorColor("⛔ Operation cancelled by user. 🛑"))

    except Exception as e:
        print("\n")
        outputLine()
        print(errorColor(f"❌ Unexpected error occurred: {e} 🚨"))


def fileMenu():
    interface("Files", menuOptions, renameFiles, downloadFile, searchFiles)
