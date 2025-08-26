#!/usr/bin/env python3
"""
Example scripts for MuMu Emulator Instance Manager

This file contains practical examples of how to use the instance manager
for common automation tasks.
"""

from instance_manager import MuMuInstanceManager
import time
import json
import os


def example_basic_operations():
    """Example: Basic emulator operations"""
    print("=== Basic Operations Example ===")
    
    # Initialize the manager
    manager = MuMuInstanceManager()
    
    # Get information about all emulators
    print("Getting emulator information...")
    emulators = manager.get_emulator_info("all")
    for emu in emulators:
        print(f"Emulator {emu.index}: {emu.name} - State: {emu.player_state}")
    
    # Create a new emulator
    print("\nCreating a new emulator...")
    try:
        manager.create_emulator(count=1)
        print("Successfully created new emulator")
    except Exception as e:
        print(f"Failed to create emulator: {e}")


def example_batch_operations():
    """Example: Batch operations on multiple emulators"""
    print("=== Batch Operations Example ===")
    
    manager = MuMuInstanceManager()
    
    # Get all emulator indices
    emulators = manager.get_emulator_info("all")
    indices = [emu.index for emu in emulators]
    
    if not indices:
        print("No emulators found")
        return
    
    print(f"Found {len(indices)} emulator(s): {', '.join(indices)}")
    
    # Launch all emulators
    print("Launching all emulators...")
    try:
        manager.launch_emulator("all")
        print("Successfully launched all emulators")
        
        # Wait a bit for startup
        time.sleep(10)
        
        # Check status
        emulators = manager.get_emulator_info("all")
        for emu in emulators:
            print(f"Emulator {emu.index}: {emu.player_state}")
            
    except Exception as e:
        print(f"Failed batch operation: {e}")


def example_app_installation():
    """Example: Install apps to multiple emulators"""
    print("=== App Installation Example ===")
    
    manager = MuMuInstanceManager()
    
    # Example APK path (change to actual path)
    apk_path = "example_app.apk"
    
    if not os.path.exists(apk_path):
        print(f"APK file not found: {apk_path}")
        print("Please provide a valid APK file path")
        return
    
    # Install to all emulators
    try:
        manager.install_app("all", apk_path)
        print(f"Successfully installed {apk_path} to all emulators")
    except Exception as e:
        print(f"Failed to install app: {e}")


def example_backup_automation():
    """Example: Automated backup of all emulators"""
    print("=== Backup Automation Example ===")
    
    manager = MuMuInstanceManager()
    
    # Create backup directory
    backup_dir = "./automated_backups"
    os.makedirs(backup_dir, exist_ok=True)
    
    # Get timestamp for backup name
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    
    try:
        # Backup all emulators
        backup_name = f"auto_backup_{timestamp}"
        manager.backup_emulator("all", backup_dir, backup_name, compressed=True)
        print(f"Successfully created backup: {backup_name}")
        
    except Exception as e:
        print(f"Failed to create backup: {e}")


def example_emulator_farm_setup():
    """Example: Setting up a farm of emulators"""
    print("=== Emulator Farm Setup Example ===")
    
    manager = MuMuInstanceManager()
    
    # Configuration for the farm
    farm_size = 5
    farm_name_prefix = "Farm_Instance"
    
    print(f"Setting up emulator farm with {farm_size} instances...")
    
    try:
        # Create multiple emulators
        manager.create_emulator(count=farm_size)
        print(f"Created {farm_size} emulators")
        
        # Get the newly created emulators
        emulators = manager.get_emulator_info("all")
        
        # Rename emulators with farm naming convention
        for i, emu in enumerate(emulators[-farm_size:]):  # Get last N emulators
            farm_name = f"{farm_name_prefix}_{i+1:02d}"
            manager.rename_emulator(emu.index, farm_name)
            print(f"Renamed emulator {emu.index} to {farm_name}")
        
        # Launch all farm emulators
        farm_indices = [emu.index for emu in emulators[-farm_size:]]
        manager.launch_emulator(farm_indices)
        print("Launched all farm emulators")
        
    except Exception as e:
        print(f"Failed to setup emulator farm: {e}")


def example_monitoring_script():
    """Example: Monitor emulator status and restart if needed"""
    print("=== Monitoring Script Example ===")
    
    manager = MuMuInstanceManager()
    
    def monitor_emulators():
        """Monitor and restart failed emulators"""
        try:
            emulators = manager.get_emulator_info("all")
            
            for emu in emulators:
                print(f"Checking emulator {emu.index}: {emu.name}")
                
                # Check if emulator should be running but isn't
                if not emu.is_process_started:
                    print(f"Emulator {emu.index} is not running, attempting to start...")
                    try:
                        manager.launch_emulator(emu.index)
                        print(f"Successfully started emulator {emu.index}")
                    except Exception as e:
                        print(f"Failed to start emulator {emu.index}: {e}")
                
                # Check if Android is not started
                elif not emu.is_android_started:
                    print(f"Android not started in emulator {emu.index}, restarting...")
                    try:
                        manager.restart_emulator(emu.index)
                        print(f"Successfully restarted emulator {emu.index}")
                    except Exception as e:
                        print(f"Failed to restart emulator {emu.index}: {e}")
                
                else:
                    print(f"Emulator {emu.index} is running normally")
                    
        except Exception as e:
            print(f"Monitoring error: {e}")
    
    # Run monitoring
    print("Starting emulator monitoring...")
    monitor_emulators()


def example_configuration_management():
    """Example: Managing emulator configurations"""
    print("=== Configuration Management Example ===")
    
    manager = MuMuInstanceManager()
    
    # Example configuration changes
    config_changes = {
        "resolution_mode": "tablet.1",
        "performance_mode": "high",
        "renderer_mode": "vk"
    }
    
    print("This example shows how configuration management would work")
    print("Note: Configuration management requires additional implementation")
    print(f"Example configuration changes: {json.dumps(config_changes, indent=2)}")


def main():
    """Run all examples"""
    print("MuMu Emulator Instance Manager - Examples")
    print("=========================================\n")
    
    examples = [
        example_basic_operations,
        example_batch_operations,
        example_app_installation,
        example_backup_automation,
        example_emulator_farm_setup,
        example_monitoring_script,
        example_configuration_management
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"\n--- Example {i}: {example.__doc__.split(':')[1].strip()} ---")
        try:
            example()
        except Exception as e:
            print(f"Example failed: {e}")
        
        if i < len(examples):
            input("\nPress Enter to continue to next example...")


if __name__ == "__main__":
    main()