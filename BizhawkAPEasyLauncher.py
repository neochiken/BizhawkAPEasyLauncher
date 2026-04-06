import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

def create_batch_file():
    # Initialize tkinter and hide the main window
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    
    # popup instruction box
    messagebox.showinfo("Instructions", "Please follow the prompts at the top left of the following windows")


    # 1. Select ArchipelagoBizHawkClient.exe
    path_client = filedialog.askopenfilename(
        title="Select ArchipelagoBizHawkClient.exe from your Archipelago folder",
        filetypes=[("Executable files", "*.exe")]
    )
    if not path_client: return

    # 2. Select EmuHawk.exe
    path_emu = filedialog.askopenfilename(
        title="Select EmuHawk.exe from your Bizhawk folder",
        filetypes=[("Executable files", "*.exe")]
    )
    if not path_emu: return

    # 3. Select connector_bizhawk_generic.lua
    path_lua = filedialog.askopenfilename(
        title="Select connector_bizhawk_generic.lua from your Archipelago/Data/Lua folder",
        filetypes=[("LUA files", "*.lua")]
    )
    if not path_lua: return

    # 4. Construct the script content
    # We use double quotes around paths in case they contain spaces
    batch_content = (
        f"@echo off\n"
        f'start "" "{path_client}"\n'
        f'start "" "{path_emu}" --lua "{path_lua}"'
    )

    # 5. Save the final .bat file
    save_path = filedialog.asksaveasfilename(
        title="Save your new Batch file",
        defaultextension=".bat",
        filetypes=[("Batch files", "*.bat")]
    )

    if save_path:
        with open(save_path, "w") as f:
            f.write(batch_content)
        print(f"Success! Batch file created at: {save_path}")
    else:
        print("Operation cancelled.")

if __name__ == "__main__":
    create_batch_file()