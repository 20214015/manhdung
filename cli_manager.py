#!/usr/bin/env python3
"""
MuMu Emulator Instance Manager - CLI Only Version

A command-line only version that works in headless environments.
"""

from instance_manager import MuMuInstanceManager
import sys
import json
import os


def print_help():
    """Print help information"""
    print("MuMu Emulator Instance Manager - CLI Version")
    print("=" * 50)
    print("\nUsage: python cli_manager.py <command> [arguments]")
    print("\nAvailable commands:")
    print("  help                                    - Show this help")
    print("  info [vm_index]                         - Get emulator information")
    print("  list                                    - List all emulators")
    print("  create [vm_index] [count]               - Create new emulator(s)")
    print("  clone <vm_index> [count]                - Clone existing emulator(s)")
    print("  delete <vm_index>                       - Delete emulator(s)")
    print("  rename <vm_index> <name>                - Rename emulator(s)")
    print("  launch <vm_index> [package]             - Launch emulator(s)")
    print("  shutdown <vm_index>                     - Shutdown emulator(s)")
    print("  restart <vm_index>                      - Restart emulator(s)")
    print("  install <vm_index> <apk_path>           - Install app to emulator(s)")
    print("  backup <vm_index> <dir> <name> [--zip]  - Backup emulator(s)")
    print("  status                                  - Show system status")
    print("\nExamples:")
    print("  python cli_manager.py info              - Show all emulators")
    print("  python cli_manager.py create 2          - Create 2 emulators")
    print("  python cli_manager.py launch 0          - Launch emulator 0")
    print("  python cli_manager.py list              - List emulators in table format")


def print_emulator_list(emulators):
    """Print emulators in a nice table format"""
    if not emulators:
        print("No emulators found.")
        return
    
    # Header
    print("\n" + "=" * 80)
    print(f"{'Index':<8} {'Name':<20} {'State':<15} {'Android':<10} {'ADB Port':<10}")
    print("-" * 80)
    
    # Emulator rows
    for emu in emulators:
        index = emu.index
        name = (emu.name[:17] + "...") if len(emu.name) > 20 else emu.name
        state = emu.player_state or "Unknown"
        android = "Yes" if emu.is_android_started else "No"
        adb_port = str(emu.adb_port) if emu.adb_port else "N/A"
        
        print(f"{index:<8} {name:<20} {state:<15} {android:<10} {adb_port:<10}")
    
    print("=" * 80)
    print(f"Total: {len(emulators)} emulator(s)")


def print_system_status():
    """Print system status information"""
    print("\nSystem Status")
    print("=" * 30)
    
    # Check Python version
    print(f"Python Version: {sys.version.split()[0]}")
    
    # Check if config exists
    config_exists = os.path.exists("config.json")
    print(f"Config File: {'Found' if config_exists else 'Not Found'}")
    
    # Try to initialize manager
    try:
        manager = MuMuInstanceManager()
        print("Instance Manager: ✓ Initialized")
        
        # Try to get emulator count
        try:
            emulators = manager.get_emulator_info("all")
            print(f"Emulators Found: {len(emulators)}")
        except Exception as e:
            print(f"Emulator Check: ✗ {e}")
            
    except Exception as e:
        print(f"Instance Manager: ✗ {e}")


def main():
    """Main CLI function"""
    if len(sys.argv) < 2:
        print_help()
        return
    
    command = sys.argv[1].lower()
    
    if command == "help":
        print_help()
        return
    
    if command == "status":
        print_system_status()
        return
    
    # Initialize manager for other commands
    try:
        manager = MuMuInstanceManager()
    except Exception as e:
        print(f"Error initializing manager: {e}")
        print("Make sure MuMuManager.exe is properly configured in config.json")
        return
    
    try:
        if command == "info":
            vm_index = sys.argv[2] if len(sys.argv) > 2 else "all"
            emulators = manager.get_emulator_info(vm_index)
            print_emulator_list(emulators)
        
        elif command == "list":
            emulators = manager.get_emulator_info("all")
            print_emulator_list(emulators)
        
        elif command == "create":
            vm_index = sys.argv[2] if len(sys.argv) > 2 else None
            count = int(sys.argv[3]) if len(sys.argv) > 3 else 1
            
            print(f"Creating {count} emulator(s)...")
            manager.create_emulator(vm_index, count)
            print(f"✓ Successfully created {count} emulator(s)")
        
        elif command == "clone":
            if len(sys.argv) < 3:
                print("Error: vm_index required for clone command")
                return
            vm_index = sys.argv[2]
            count = int(sys.argv[3]) if len(sys.argv) > 3 else 1
            
            print(f"Cloning emulator {vm_index} {count} time(s)...")
            manager.clone_emulator(vm_index, count)
            print(f"✓ Successfully cloned emulator(s) {count} time(s)")
        
        elif command == "delete":
            if len(sys.argv) < 3:
                print("Error: vm_index required for delete command")
                return
            vm_index = sys.argv[2]
            
            # Confirm deletion
            confirm = input(f"Are you sure you want to delete emulator {vm_index}? (y/N): ")
            if confirm.lower() != 'y':
                print("Deletion cancelled.")
                return
            
            print(f"Deleting emulator {vm_index}...")
            manager.delete_emulator(vm_index)
            print(f"✓ Successfully deleted emulator(s) {vm_index}")
        
        elif command == "rename":
            if len(sys.argv) < 4:
                print("Error: vm_index and name required for rename command")
                return
            vm_index = sys.argv[2]
            name = sys.argv[3]
            
            print(f"Renaming emulator {vm_index} to '{name}'...")
            manager.rename_emulator(vm_index, name)
            print(f"✓ Successfully renamed emulator(s) {vm_index} to '{name}'")
        
        elif command == "launch":
            if len(sys.argv) < 3:
                print("Error: vm_index required for launch command")
                return
            vm_index = sys.argv[2]
            package = sys.argv[3] if len(sys.argv) > 3 else None
            
            print(f"Launching emulator {vm_index}...")
            manager.launch_emulator(vm_index, package)
            print(f"✓ Successfully launched emulator(s) {vm_index}")
        
        elif command == "shutdown":
            if len(sys.argv) < 3:
                print("Error: vm_index required for shutdown command")
                return
            vm_index = sys.argv[2]
            
            print(f"Shutting down emulator {vm_index}...")
            manager.shutdown_emulator(vm_index)
            print(f"✓ Successfully shutdown emulator(s) {vm_index}")
        
        elif command == "restart":
            if len(sys.argv) < 3:
                print("Error: vm_index required for restart command")
                return
            vm_index = sys.argv[2]
            
            print(f"Restarting emulator {vm_index}...")
            manager.restart_emulator(vm_index)
            print(f"✓ Successfully restarted emulator(s) {vm_index}")
        
        elif command == "install":
            if len(sys.argv) < 4:
                print("Error: vm_index and apk_path required for install command")
                return
            vm_index = sys.argv[2]
            apk_path = sys.argv[3]
            
            if not os.path.exists(apk_path):
                print(f"Error: APK file not found: {apk_path}")
                return
            
            print(f"Installing {apk_path} to emulator {vm_index}...")
            manager.install_app(vm_index, apk_path)
            print(f"✓ Successfully installed app to emulator(s) {vm_index}")
        
        elif command == "backup":
            if len(sys.argv) < 5:
                print("Error: vm_index, directory, and name required for backup command")
                return
            vm_index = sys.argv[2]
            backup_dir = sys.argv[3]
            name = sys.argv[4]
            compressed = "--zip" in sys.argv
            
            print(f"Backing up emulator {vm_index} to {backup_dir}/{name}...")
            manager.backup_emulator(vm_index, backup_dir, name, compressed)
            print(f"✓ Successfully backed up emulator(s) {vm_index}")
        
        else:
            print(f"Unknown command: {command}")
            print("Use 'python cli_manager.py help' for available commands")
    
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()