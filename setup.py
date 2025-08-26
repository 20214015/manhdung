#!/usr/bin/env python3
"""
Setup and Installation Script for MuMu Emulator Instance Manager

This script helps users set up the instance manager software.
"""

import os
import sys
import json
import shutil
from pathlib import Path


def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("Error: Python 3.7 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    return True


def find_mumu_manager():
    """Try to find MuMuManager.exe automatically"""
    possible_paths = [
        "C:\\Program Files\\Netease\\MuMuPlayer-12.0\\shell\\MuMuManager.exe",
        "C:\\Program Files (x86)\\Netease\\MuMuPlayer-12.0\\shell\\MuMuManager.exe",
        "D:\\Program Files\\Netease\\MuMuPlayer-12.0\\shell\\MuMuManager.exe",
        "MuMuManager.exe"  # If in PATH
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            return path
    
    return None


def create_config():
    """Create configuration file"""
    print("Creating configuration file...")
    
    # Try to find MuMuManager.exe
    mumu_path = find_mumu_manager()
    
    if not mumu_path:
        print("MuMuManager.exe not found automatically.")
        mumu_path = input("Please enter the full path to MuMuManager.exe: ").strip()
        
        if not os.path.exists(mumu_path):
            print(f"Warning: Path {mumu_path} does not exist")
            print("You can update this later in config.json")
    
    config = {
        "mumu_manager_path": mumu_path,
        "default_backup_dir": "./backups",
        "auto_refresh_interval": 5,
        "max_concurrent_operations": 3,
        "timeout_settings": {
            "command_timeout": 60,
            "startup_timeout": 120,
            "shutdown_timeout": 60
        },
        "logging": {
            "enabled": True,
            "log_file": "instance_manager.log",
            "log_level": "INFO"
        },
        "ui_settings": {
            "window_width": 800,
            "window_height": 600,
            "theme": "default"
        },
        "emulator_defaults": {
            "performance_mode": "middle",
            "resolution_mode": "tablet.1",
            "renderer_mode": "vk"
        }
    }
    
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    
    print(f"Configuration saved to config.json")
    print(f"MuMu Manager path: {mumu_path}")


def create_shortcuts():
    """Create convenient shortcuts"""
    print("Creating shortcuts...")
    
    # Create batch file for CLI
    cli_batch = """@echo off
python "%~dp0instance_manager.py" %*
"""
    with open("instance_manager.bat", "w") as f:
        f.write(cli_batch)
    
    # Create batch file for GUI
    gui_batch = """@echo off
python "%~dp0gui_manager.py"
"""
    with open("gui_manager.bat", "w") as f:
        f.write(gui_batch)
    
    print("Created shortcuts:")
    print("  - instance_manager.bat (CLI)")
    print("  - gui_manager.bat (GUI)")


def test_installation():
    """Test if the installation works"""
    print("Testing installation...")
    
    try:
        # Test import
        from instance_manager import MuMuInstanceManager
        
        # Test initialization
        manager = MuMuInstanceManager()
        print("✓ Core functionality working")
        
        # Test GUI import
        import tkinter as tk
        print("✓ GUI dependencies available")
        
        return True
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def show_usage_info():
    """Show basic usage information"""
    print("\n" + "="*50)
    print("INSTALLATION COMPLETE!")
    print("="*50)
    print("\nQuick Start:")
    print("1. CLI Usage:")
    print("   instance_manager.bat info")
    print("   python instance_manager.py info")
    print("\n2. GUI Usage:")
    print("   gui_manager.bat")
    print("   python gui_manager.py")
    print("\n3. Examples:")
    print("   python examples.py")
    print("\n4. Documentation:")
    print("   See HUONG_DAN_SU_DUNG.md for detailed instructions")
    print("\nConfiguration file: config.json")
    print("Log file: instance_manager.log")


def main():
    """Main setup function"""
    print("MuMu Emulator Instance Manager Setup")
    print("=====================================")
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check if files exist
    required_files = [
        "instance_manager.py",
        "gui_manager.py", 
        "examples.py",
        "HUONG_DAN_SU_DUNG.md"
    ]
    
    missing_files = [f for f in required_files if not os.path.exists(f)]
    if missing_files:
        print(f"Error: Missing required files: {missing_files}")
        sys.exit(1)
    
    # Create configuration
    if not os.path.exists("config.json"):
        create_config()
    else:
        print("Configuration file already exists (config.json)")
        update = input("Update configuration? (y/n): ").lower().strip()
        if update == 'y':
            create_config()
    
    # Create shortcuts
    create_shortcuts()
    
    # Create backup directory
    os.makedirs("backups", exist_ok=True)
    print("Created backup directory: ./backups")
    
    # Test installation
    if test_installation():
        show_usage_info()
    else:
        print("\nInstallation test failed. Please check the errors above.")
        sys.exit(1)
    
    print("\nSetup completed successfully!")


if __name__ == "__main__":
    main()