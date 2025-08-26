#!/usr/bin/env python3
"""
MuMu Emulator Instance Manager GUI

A graphical user interface for managing MuMu emulator instances.

Author: Instance Management Software
Version: 1.0.0
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
from typing import List, Optional
from instance_manager import MuMuInstanceManager, EmulatorInfo


class EmulatorManagerGUI:
    """GUI for MuMu Emulator Instance Manager"""
    
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("MuMu Emulator Instance Manager")
        self.root.geometry("800x600")
        
        # Initialize the manager
        self.manager = MuMuInstanceManager()
        
        # Create GUI elements
        self.setup_ui()
        
        # Load emulator information on startup
        self.refresh_emulators()
    
    def setup_ui(self):
        """Setup the user interface"""
        # Create main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="MuMu Emulator Instance Manager", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))
        
        # Emulator list frame
        list_frame = ttk.LabelFrame(main_frame, text="Emulator Instances", padding="5")
        list_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)
        
        # Treeview for emulator list
        columns = ("Index", "Name", "State", "Android Started", "ADB Port")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=10)
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        
        # Scrollbar for treeview
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Control buttons frame
        control_frame = ttk.LabelFrame(main_frame, text="Instance Control", padding="5")
        control_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Buttons row 1
        button_frame1 = ttk.Frame(control_frame)
        button_frame1.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 5))
        
        ttk.Button(button_frame1, text="Refresh", command=self.refresh_emulators).grid(row=0, column=0, padx=(0, 5))
        ttk.Button(button_frame1, text="Create", command=self.create_emulator_dialog).grid(row=0, column=1, padx=(0, 5))
        ttk.Button(button_frame1, text="Clone", command=self.clone_emulator_dialog).grid(row=0, column=2, padx=(0, 5))
        ttk.Button(button_frame1, text="Delete", command=self.delete_selected).grid(row=0, column=3, padx=(0, 5))
        ttk.Button(button_frame1, text="Rename", command=self.rename_emulator_dialog).grid(row=0, column=4, padx=(0, 5))
        
        # Buttons row 2
        button_frame2 = ttk.Frame(control_frame)
        button_frame2.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        ttk.Button(button_frame2, text="Launch", command=self.launch_selected).grid(row=0, column=0, padx=(0, 5))
        ttk.Button(button_frame2, text="Shutdown", command=self.shutdown_selected).grid(row=0, column=1, padx=(0, 5))
        ttk.Button(button_frame2, text="Restart", command=self.restart_selected).grid(row=0, column=2, padx=(0, 5))
        ttk.Button(button_frame2, text="Install APK", command=self.install_apk_dialog).grid(row=0, column=3, padx=(0, 5))
        ttk.Button(button_frame2, text="Backup", command=self.backup_emulator_dialog).grid(row=0, column=4, padx=(0, 5))
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E))
    
    def get_selected_emulator_index(self) -> Optional[str]:
        """Get the index of the currently selected emulator"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select an emulator from the list.")
            return None
        
        item = self.tree.item(selection[0])
        return item["values"][0]  # Index is the first column
    
    def refresh_emulators(self):
        """Refresh the emulator list"""
        def _refresh():
            try:
                self.status_var.set("Refreshing emulator list...")
                
                # Clear existing items
                for item in self.tree.get_children():
                    self.tree.delete(item)
                
                # Get emulator information
                emulators = self.manager.get_emulator_info("all")
                
                # Populate treeview
                for emu in emulators:
                    values = (
                        emu.index,
                        emu.name,
                        emu.player_state or "Unknown",
                        "Yes" if emu.is_android_started else "No",
                        emu.adb_port or "N/A"
                    )
                    self.tree.insert("", tk.END, values=values)
                
                self.status_var.set(f"Loaded {len(emulators)} emulator(s)")
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to refresh emulator list: {e}")
                self.status_var.set("Error refreshing emulator list")
        
        # Run in background thread to avoid freezing UI
        threading.Thread(target=_refresh, daemon=True).start()
    
    def create_emulator_dialog(self):
        """Show dialog for creating new emulator"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Create Emulator")
        dialog.geometry("300x150")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Center the dialog
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (dialog.winfo_width() // 2)
        y = (dialog.winfo_screenheight() // 2) - (dialog.winfo_height() // 2)
        dialog.geometry(f"+{x}+{y}")
        
        frame = ttk.Frame(dialog, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Index entry
        ttk.Label(frame, text="Index (optional):").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        index_var = tk.StringVar()
        ttk.Entry(frame, textvariable=index_var, width=20).grid(row=0, column=1, pady=(0, 5))
        
        # Count entry
        ttk.Label(frame, text="Count:").grid(row=1, column=0, sticky=tk.W, pady=(0, 10))
        count_var = tk.StringVar(value="1")
        ttk.Entry(frame, textvariable=count_var, width=20).grid(row=1, column=1, pady=(0, 10))
        
        # Buttons
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=(10, 0))
        
        def create():
            try:
                index = index_var.get().strip() or None
                count = int(count_var.get())
                
                self.status_var.set("Creating emulator(s)...")
                self.manager.create_emulator(index, count)
                
                dialog.destroy()
                self.refresh_emulators()
                messagebox.showinfo("Success", f"Successfully created {count} emulator(s)")
                
            except ValueError:
                messagebox.showerror("Error", "Count must be a valid number")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to create emulator: {e}")
                self.status_var.set("Error creating emulator")
        
        ttk.Button(button_frame, text="Create", command=create).grid(row=0, column=0, padx=(0, 5))
        ttk.Button(button_frame, text="Cancel", command=dialog.destroy).grid(row=0, column=1)
    
    def clone_emulator_dialog(self):
        """Show dialog for cloning emulator"""
        selected_index = self.get_selected_emulator_index()
        if not selected_index:
            return
        
        dialog = tk.Toplevel(self.root)
        dialog.title("Clone Emulator")
        dialog.geometry("300x120")
        dialog.transient(self.root)
        dialog.grab_set()
        
        frame = ttk.Frame(dialog, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        ttk.Label(frame, text=f"Clone emulator {selected_index}").grid(row=0, column=0, columnspan=2, pady=(0, 10))
        
        # Count entry
        ttk.Label(frame, text="Count:").grid(row=1, column=0, sticky=tk.W, pady=(0, 10))
        count_var = tk.StringVar(value="1")
        ttk.Entry(frame, textvariable=count_var, width=20).grid(row=1, column=1, pady=(0, 10))
        
        # Buttons
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=(10, 0))
        
        def clone():
            try:
                count = int(count_var.get())
                self.status_var.set(f"Cloning emulator {selected_index}...")
                self.manager.clone_emulator(selected_index, count)
                
                dialog.destroy()
                self.refresh_emulators()
                messagebox.showinfo("Success", f"Successfully cloned emulator {selected_index} {count} time(s)")
                
            except ValueError:
                messagebox.showerror("Error", "Count must be a valid number")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to clone emulator: {e}")
                self.status_var.set("Error cloning emulator")
        
        ttk.Button(button_frame, text="Clone", command=clone).grid(row=0, column=0, padx=(0, 5))
        ttk.Button(button_frame, text="Cancel", command=dialog.destroy).grid(row=0, column=1)
    
    def delete_selected(self):
        """Delete the selected emulator"""
        selected_index = self.get_selected_emulator_index()
        if not selected_index:
            return
        
        # Confirm deletion
        if not messagebox.askyesno("Confirm Deletion", 
                                  f"Are you sure you want to delete emulator {selected_index}?"):
            return
        
        try:
            self.status_var.set(f"Deleting emulator {selected_index}...")
            self.manager.delete_emulator(selected_index)
            
            self.refresh_emulators()
            messagebox.showinfo("Success", f"Successfully deleted emulator {selected_index}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete emulator: {e}")
            self.status_var.set("Error deleting emulator")
    
    def rename_emulator_dialog(self):
        """Show dialog for renaming emulator"""
        selected_index = self.get_selected_emulator_index()
        if not selected_index:
            return
        
        new_name = tk.simpledialog.askstring("Rename Emulator", 
                                           f"Enter new name for emulator {selected_index}:")
        if not new_name:
            return
        
        try:
            self.status_var.set(f"Renaming emulator {selected_index}...")
            self.manager.rename_emulator(selected_index, new_name)
            
            self.refresh_emulators()
            messagebox.showinfo("Success", f"Successfully renamed emulator {selected_index}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to rename emulator: {e}")
            self.status_var.set("Error renaming emulator")
    
    def launch_selected(self):
        """Launch the selected emulator"""
        selected_index = self.get_selected_emulator_index()
        if not selected_index:
            return
        
        try:
            self.status_var.set(f"Launching emulator {selected_index}...")
            self.manager.launch_emulator(selected_index)
            
            messagebox.showinfo("Success", f"Successfully launched emulator {selected_index}")
            self.refresh_emulators()
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch emulator: {e}")
            self.status_var.set("Error launching emulator")
    
    def shutdown_selected(self):
        """Shutdown the selected emulator"""
        selected_index = self.get_selected_emulator_index()
        if not selected_index:
            return
        
        try:
            self.status_var.set(f"Shutting down emulator {selected_index}...")
            self.manager.shutdown_emulator(selected_index)
            
            messagebox.showinfo("Success", f"Successfully shutdown emulator {selected_index}")
            self.refresh_emulators()
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to shutdown emulator: {e}")
            self.status_var.set("Error shutting down emulator")
    
    def restart_selected(self):
        """Restart the selected emulator"""
        selected_index = self.get_selected_emulator_index()
        if not selected_index:
            return
        
        try:
            self.status_var.set(f"Restarting emulator {selected_index}...")
            self.manager.restart_emulator(selected_index)
            
            messagebox.showinfo("Success", f"Successfully restarted emulator {selected_index}")
            self.refresh_emulators()
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to restart emulator: {e}")
            self.status_var.set("Error restarting emulator")
    
    def install_apk_dialog(self):
        """Show dialog for installing APK"""
        selected_index = self.get_selected_emulator_index()
        if not selected_index:
            return
        
        apk_path = filedialog.askopenfilename(
            title="Select APK file",
            filetypes=[("APK files", "*.apk"), ("XAPK files", "*.xapk"), ("APKS files", "*.apks")]
        )
        
        if not apk_path:
            return
        
        try:
            self.status_var.set(f"Installing APK to emulator {selected_index}...")
            self.manager.install_app(selected_index, apk_path)
            
            messagebox.showinfo("Success", f"Successfully installed APK to emulator {selected_index}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to install APK: {e}")
            self.status_var.set("Error installing APK")
    
    def backup_emulator_dialog(self):
        """Show dialog for backing up emulator"""
        selected_index = self.get_selected_emulator_index()
        if not selected_index:
            return
        
        dialog = tk.Toplevel(self.root)
        dialog.title("Backup Emulator")
        dialog.geometry("400x200")
        dialog.transient(self.root)
        dialog.grab_set()
        
        frame = ttk.Frame(dialog, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        ttk.Label(frame, text=f"Backup emulator {selected_index}").grid(row=0, column=0, columnspan=3, pady=(0, 10))
        
        # Directory selection
        ttk.Label(frame, text="Backup Directory:").grid(row=1, column=0, sticky=tk.W, pady=(0, 5))
        dir_var = tk.StringVar()
        ttk.Entry(frame, textvariable=dir_var, width=30).grid(row=1, column=1, pady=(0, 5))
        
        def browse_dir():
            directory = filedialog.askdirectory()
            if directory:
                dir_var.set(directory)
        
        ttk.Button(frame, text="Browse", command=browse_dir).grid(row=1, column=2, padx=(5, 0), pady=(0, 5))
        
        # Name entry
        ttk.Label(frame, text="Backup Name:").grid(row=2, column=0, sticky=tk.W, pady=(0, 5))
        name_var = tk.StringVar(value=f"emulator_{selected_index}_backup")
        ttk.Entry(frame, textvariable=name_var, width=30).grid(row=2, column=1, pady=(0, 5))
        
        # Compression checkbox
        compress_var = tk.BooleanVar()
        ttk.Checkbutton(frame, text="Compress backup", variable=compress_var).grid(row=3, column=0, columnspan=2, sticky=tk.W, pady=(5, 10))
        
        # Buttons
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=4, column=0, columnspan=3, pady=(10, 0))
        
        def backup():
            backup_dir = dir_var.get()
            name = name_var.get()
            
            if not backup_dir or not name:
                messagebox.showerror("Error", "Please specify backup directory and name")
                return
            
            try:
                self.status_var.set(f"Backing up emulator {selected_index}...")
                self.manager.backup_emulator(selected_index, backup_dir, name, compress_var.get())
                
                dialog.destroy()
                messagebox.showinfo("Success", f"Successfully backed up emulator {selected_index}")
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to backup emulator: {e}")
                self.status_var.set("Error backing up emulator")
        
        ttk.Button(button_frame, text="Backup", command=backup).grid(row=0, column=0, padx=(0, 5))
        ttk.Button(button_frame, text="Cancel", command=dialog.destroy).grid(row=0, column=1)


def main():
    """Main function for GUI application"""
    # Import simpledialog here to avoid importing tkinter at module level
    import tkinter.simpledialog
    tk.simpledialog = tkinter.simpledialog
    
    root = tk.Tk()
    app = EmulatorManagerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()