import rotatescreen as rs
import keyboard
import random
import pygame
import os
import time
import msvcrt

from Functions import interface

menuOptions = "[1] Rotate Screen 🔄\n[2] Play Random Sound 🔊\n[3] Keyboard Prank ⌨️\n[4] CMD Overload 💻"


def rotateScreen():
    print(f"\033[1;31mThis prank will suddenly rotate screen at different angles.\033[0m")
    print(f"\033[1;31mThis could even result for system to be unresponsive or crash !!!\033[0m")
    while True:
        try:
            screen = rs.get_primary_display()
            angle = random.choice([0, 90, 180, 270])
            screen.rotate_to(angle)
            print(f"\033[96mScreen rotated to {angle} degrees.\033[0m")  
            time.sleep(0.5)
            continue
        except Exception as e:
            print(f"\033[91mAn error occurred while rotating the screen: {e}\033[0m") 


def playSound():
    print(f"\033[1;31mThis prank will play different sounds to disturb the people.\033[0m")
    try:
        pygame.mixer.init()
        sound_folder = "sounds"

        if not os.path.isdir(sound_folder):
            print(f"\033[91m❌ Sound folder '{sound_folder}' not found.\033[0m")
            return

        sound_files = [f for f in os.listdir(sound_folder) if f.endswith(('.mp3', '.wav'))]

        if not sound_files:
            print("\033[93m⚠️ No sound files found in the specified folder.\033[0m")
            return

        while True:
            try:
                sound = random.choice(sound_files)
                full_path = os.path.join(sound_folder, sound)
                pygame.mixer.music.load(full_path)
                pygame.mixer.music.play()

                print(f"\033[96m🔊 Playing: {sound}\033[0m")

                # Wait while sound plays or a fixed delay
                while pygame.mixer.music.get_busy():
                    time.sleep(1)

                # Optional: random wait before playing next
                time.sleep(random.randint(1, 5))

            except Exception as e:
                print(f"\033[91m❌ Error playing sound: {e}\033[0m")
                time.sleep(2)

    except KeyboardInterrupt:
        print("\n\033[91m⛔ Sound playback interrupted by user (Ctrl+C).\033[0m")
        pygame.mixer.music.stop()
        time.sleep(1)
    except Exception as e:
        print(f"\033[91m❌ Initialization failed: {e}\033[0m")


def keyboardPrank():
    print(f"\033[1;31mThis prank will suddenly type any key from the keyboard when you press a key.\033[0m")
    letters = list("abcdefghijklmnoprqstuvwxyz1234567890-=[]\\;',./`~!@#$%^&*()_+{}|:\"<>?")
    print(f"\033[96mYou can start typing now! ⌨️\033[0m")
    while True:
        for letter in letters:
            if keyboard.is_pressed(letter):
                print(f"\033[1;33m=========================\033[0m")
                print(f"\033[92mYou Pressed: {keyboard.read_key()}\033[0m")
                random_char = random.choice(letters)
                keyboard.write(random_char)
                print(f"\033[92mTyped: {random_char}\033[0m")
                time.sleep(0.1)  # Add a small delay to avoid flooding


def CMDoverload():


    print(f"\033[1;31mThis prank will create a batch file that opens multiple command prompts.\033[0m")
    print(f"\033[1;31mThis could even result for system to be unresponsive or crash !!!\033[0m")
    print(f"\033[1;31mAre you sure ?? \033[0m")
    print(f"\033[1;31mPress 'y' to continue or any other key to cancel.\033[0m")
    
    choice = msvcrt.getch()
    
    if choice.lower() == b"y":
        print(f"\033[38;5mCreating bat file ...\033[0m")
        
        time.sleep(1)
    
        fileContent = ":loop\nstart cmd\ngoto loop"
    
        try:
            with open("sysmain.bat", "w+") as file:
                file.write(fileContent)
            
            print(f"\033[38;5;45mPrank file created successfully!\033[0m")
            print(f"\033[1;31mPress y to run to run the file\033[0m")
            run_choice = msvcrt.getch()
            if run_choice.lower() == b"y":
                print(f"\033[38;5;27mRunning the prank file...\033[0m")
                os.system("sysmain.bat")  
            else:
                print("\033[1;31mPrank file not executed.\033[0m")  

        except Exception as e:
            print(f"\033[38;5;196mError creating prank file: {e}\033[0m")
        return False
    
    else:
        print("\033[1;31mOperation cancelled.\033[0m")
        return False


def prankMenu():
    interface("Pranks", menuOptions, rotateScreen, playSound, keyboardPrank, CMDoverload)