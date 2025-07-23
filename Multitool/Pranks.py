import rotatescreen as rs
import keyboard
import random
import pygame
import os
import time
import msvcrt
import sys
import shutil

from functions import interface, outputColor, errorColor, line

menuOptions = "[1] Rotate Screen 🔄\n[2] Play Random Sound 🔊\n[3] Keyboard Prank ⌨️\n[4] CMD Overload 💻"

def rotateScreen():
    try:
        print(errorColor("This prank will suddenly rotate screen at different angles. 😵"))
        print(errorColor("This could even result for system to be unresponsive or crash !!! ⚠️"))
        line()

        while True:
            try:
                screen = rs.get_primary_display()
                angle = random.choice([0, 90, 180, 270])
                screen.rotate_to(angle)
                print(outputColor(f"Screen rotated to {angle} degrees 🔃"))
                time.sleep(0.5)

            except Exception as e:
                print(errorColor(f"❌ An error occurred while rotating the screen: {e} 💥"))
                break

            except KeyboardInterrupt:
                line()
                print(errorColor("⛔ Keyboard interrupted by user (Ctrl+C). 🛑"))
                break

    except KeyboardInterrupt:
        print("\n")
        line()
        print(errorColor("⛔ Operation cancelled by user. 🛑"))

    except Exception as e:
        print("\n")
        line()
        print(errorColor(f"❌ Unexpected error occurred: {e} 🚨"))

def resource_path(relative_path):
    # Works whether it's a script or a bundled .exe
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)

def playSound():
    try:
        print(errorColor("This prank will play different sounds to disturb the people. 🎧"))
        line()

        pygame.mixer.init()
        assets = resource_path("assets")

        if not os.path.isdir(assets):
            print(errorColor(f"❌ Asset folder '{assets}' not found. 📁"))
            line()
            return

        sound_files = [f for f in os.listdir(assets) if f.endswith((".mp3", ".wav"))]

        if not sound_files:
            print(errorColor("⚠️ No sound files found in the specified folder. 📭"))
            line()
            return

        # Optional: Extract all sounds to working directory for debug or reuse
        extract_dir = os.path.join(os.getcwd(), "extracted_sounds")
        os.makedirs(extract_dir, exist_ok=True)
        for f in sound_files:
            shutil.copyfile(os.path.join(assets, f), os.path.join(extract_dir, f))

        while True:
            try:
                sound = random.choice(sound_files)
                full_path = os.path.join(assets, sound)
                pygame.mixer.music.load(full_path)
                pygame.mixer.music.play()

                print(outputColor(f"🔊 Playing: {sound} 🎶"))

                while pygame.mixer.music.get_busy():
                    time.sleep(1)

                time.sleep(random.randint(1, 5))

            except Exception as e:
                print(errorColor(f"❌ Error playing sound: {e} 💥"))
                line()
                time.sleep(2)

    except KeyboardInterrupt:
        print("\n")
        line()
        print(errorColor("⛔ Sound playback interrupted by user (Ctrl+C). 🛑"))
        pygame.mixer.music.stop()
        time.sleep(1)

    except Exception as e:
        print("\n")
        line()
        print(errorColor(f"❌ Initialization failed: {e} 🚨"))

def keyboardPrank():
    try:
        print(errorColor("This prank will suddenly type any key from the keyboard when you press a key. 🤖"))
        print(outputColor("You can start typing now! ⌨️"))
        letters = list("abcdefghijklmnoprqstuvwxyz1234567890-=[]\\;',./`~!@#$%^&*()_+{}|:\"<>?")

        while True:
            for letter in letters:
                if keyboard.is_pressed(letter):
                    line()
                    pressed = keyboard.read_key()
                    random_char = random.choice(letters)
                    print(outputColor(f"You Pressed: {pressed} 🔘"))
                    keyboard.write(random_char)
                    print(outputColor(f"Typed: {random_char} 📝"))
                    time.sleep(0.1)

    except KeyboardInterrupt:
        print("\n")
        line()
        print(errorColor("⛔ Keyboard prank interrupted by user. 🛑"))

    except Exception as e:
        print("\n")
        line()
        print(errorColor(f"❌ Error during keyboard prank: {e} ⚠️"))

def CMDoverload():
    try:
        print(errorColor("This prank will create a batch file that opens multiple command prompts. 💣"))
        print(errorColor("This could even result for system to be unresponsive or crash !!! ⚠️"))
        print(errorColor("Are you sure ?? 🤔"))
        print(errorColor("Press 'y' to continue or any other key to cancel. ❓"))
        line()

        choice = msvcrt.getch()

        if choice.lower() == b"y":
            print(outputColor("Creating bat file ... 🛠️"))
            time.sleep(1)

            fileContent = ":loop\nstart cmd\ngoto loop"

            try:
                with open("sysmain.bat", "w+") as file:
                    file.write(fileContent)

                print(outputColor("✅ Prank file created successfully! 📄"))
                print(errorColor("Press y to run the file ▶️"))
                run_choice = msvcrt.getch()
                if run_choice.lower() == b"y":
                    print(outputColor("⚡ Running the prank file... 💻"))
                    line()
                    os.system("sysmain.bat")
                else:
                    line()
                    print(errorColor("Prank file not executed. ❌"))

            except Exception as e:
                line()
                print(errorColor(f"❌ Error creating prank file: {e} 💥"))
                return False

        else:
            line()
            print(errorColor("Operation cancelled. 🚫"))
            return False

    except KeyboardInterrupt:
        print("\n")
        line()
        print(errorColor("⛔ Operation interrupted by user. 🛑"))

    except Exception as e:
        print("\n")
        line()
        print(errorColor(f"❌ Unexpected error occurred: {e} 🚨"))

def prankMenu():
    interface("Pranks", menuOptions, rotateScreen, playSound, keyboardPrank, CMDoverload)