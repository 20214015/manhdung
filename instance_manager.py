#!/usr/bin/env python3
"""
MuMu Emulator Instance Manager

A Python wrapper for MuMuManager.exe that provides programmatic access to
emulator instance management functionality.

Author: Instance Management Software
Version: 1.0.0
"""

import subprocess
import json
import os
import sys
from typing import List, Dict, Optional, Union
from dataclasses import dataclass
from pathlib import Path


@dataclass
class EmulatorInfo:
    """Data class for emulator information"""
    index: str
    name: str
    adb_host_ip: Optional[str] = None
    adb_port: Optional[int] = None
    created_timestamp: Optional[int] = None
    disk_size_bytes: Optional[int] = None
    error_code: int = 0
    hyperv_enabled: bool = False
    is_android_started: bool = False
    is_main: bool = False
    is_process_started: bool = False
    player_state: Optional[str] = None
    vt_enabled: Optional[bool] = None


class MuMuInstanceManager:
    """MuMu Emulator Instance Manager
    
    This class provides a Python interface to manage MuMu emulator instances
    using the MuMuManager.exe command line tool.
    """
    
    def __init__(self, mumu_manager_path: str = "MuMuManager.exe"):
        """Initialize the instance manager
        
        Args:
            mumu_manager_path: Path to MuMuManager.exe executable
        """
        self.mumu_manager_path = mumu_manager_path
        self._validate_mumu_manager()
    
    def _validate_mumu_manager(self):
        """Validate that MuMuManager.exe is accessible"""
        try:
            result = subprocess.run(
                [self.mumu_manager_path, "--help"], 
                capture_output=True, 
                text=True, 
                timeout=10
            )
            if result.returncode != 0:
                print(f"Warning: MuMuManager.exe may not be properly installed or accessible")
        except (subprocess.TimeoutExpired, FileNotFoundError) as e:
            print(f"Warning: Could not validate MuMuManager.exe: {e}")
    
    def _run_command(self, args: List[str]) -> subprocess.CompletedProcess:
        """Run a MuMuManager command and return the result
        
        Args:
            args: Command arguments to pass to MuMuManager.exe
            
        Returns:
            CompletedProcess object with command result
        """
        cmd = [self.mumu_manager_path] + args
        try:
            result = subprocess.run(
                cmd, 
                capture_output=True, 
                text=True, 
                timeout=60,
                encoding='utf-8'
            )
            return result
        except subprocess.TimeoutExpired:
            raise Exception(f"Command timed out: {' '.join(cmd)}")
        except Exception as e:
            raise Exception(f"Failed to execute command: {e}")
    
    def get_emulator_info(self, vm_index: Union[str, int, List[Union[str, int]]] = "all") -> List[EmulatorInfo]:
        """Get information about emulator instances
        
        Args:
            vm_index: Emulator index(es) to query. Can be:
                     - "all" for all emulators
                     - Single index (str or int)
                     - List of indices
                     
        Returns:
            List of EmulatorInfo objects
        """
        if isinstance(vm_index, list):
            vm_index = ",".join(str(idx) for idx in vm_index)
        elif isinstance(vm_index, int):
            vm_index = str(vm_index)
        
        args = ["info", "-v", vm_index]
        result = self._run_command(args)
        
        if result.returncode != 0:
            raise Exception(f"Failed to get emulator info: {result.stderr}")
        
        # Parse JSON output (assuming MuMuManager returns JSON)
        try:
            data = json.loads(result.stdout)
            emulators = []
            
            if isinstance(data, list):
                for item in data:
                    emulators.append(EmulatorInfo(**item))
            elif isinstance(data, dict):
                emulators.append(EmulatorInfo(**data))
                
            return emulators
        except json.JSONDecodeError:
            # If not JSON, return basic info
            return [EmulatorInfo(index=str(vm_index), name="Unknown")]
    
    def create_emulator(self, vm_index: Optional[Union[str, int]] = None, count: int = 1) -> bool:
        """Create new emulator instances
        
        Args:
            vm_index: Specific index to create (optional)
            count: Number of emulators to create
            
        Returns:
            True if successful
        """
        args = ["create"]
        
        if vm_index is not None:
            args.extend(["-v", str(vm_index)])
        
        if count > 1:
            args.extend(["-n", str(count)])
        
        result = self._run_command(args)
        
        if result.returncode != 0:
            raise Exception(f"Failed to create emulator: {result.stderr}")
        
        return True
    
    def clone_emulator(self, vm_index: Union[str, int, List[Union[str, int]]], count: int = 1) -> bool:
        """Clone existing emulator instances
        
        Args:
            vm_index: Index(es) of emulator(s) to clone
            count: Number of times to clone each emulator
            
        Returns:
            True if successful
        """
        if isinstance(vm_index, list):
            vm_index = ",".join(str(idx) for idx in vm_index)
        elif isinstance(vm_index, int):
            vm_index = str(vm_index)
        
        args = ["clone", "-v", vm_index]
        
        if count > 1:
            args.extend(["-n", str(count)])
        
        result = self._run_command(args)
        
        if result.returncode != 0:
            raise Exception(f"Failed to clone emulator: {result.stderr}")
        
        return True
    
    def delete_emulator(self, vm_index: Union[str, int, List[Union[str, int]]]) -> bool:
        """Delete emulator instances
        
        Args:
            vm_index: Index(es) of emulator(s) to delete
            
        Returns:
            True if successful
        """
        if isinstance(vm_index, list):
            vm_index = ",".join(str(idx) for idx in vm_index)
        elif isinstance(vm_index, int):
            vm_index = str(vm_index)
        
        args = ["delete", "-v", vm_index]
        result = self._run_command(args)
        
        if result.returncode != 0:
            raise Exception(f"Failed to delete emulator: {result.stderr}")
        
        return True
    
    def rename_emulator(self, vm_index: Union[str, int, List[Union[str, int]]], name: str) -> bool:
        """Rename emulator instances
        
        Args:
            vm_index: Index(es) of emulator(s) to rename
            name: New name for the emulator(s)
            
        Returns:
            True if successful
        """
        if isinstance(vm_index, list):
            vm_index = ",".join(str(idx) for idx in vm_index)
        elif isinstance(vm_index, int):
            vm_index = str(vm_index)
        
        args = ["rename", "-v", vm_index, "-n", name]
        result = self._run_command(args)
        
        if result.returncode != 0:
            raise Exception(f"Failed to rename emulator: {result.stderr}")
        
        return True
    
    def launch_emulator(self, vm_index: Union[str, int, List[Union[str, int]]], package: Optional[str] = None) -> bool:
        """Launch emulator instances
        
        Args:
            vm_index: Index(es) of emulator(s) to launch
            package: Optional package to auto-launch with emulator
            
        Returns:
            True if successful
        """
        if isinstance(vm_index, list):
            vm_index = ",".join(str(idx) for idx in vm_index)
        elif isinstance(vm_index, int):
            vm_index = str(vm_index)
        
        args = ["control", "-v", vm_index, "launch"]
        
        if package:
            args.extend(["-pkg", package])
        
        result = self._run_command(args)
        
        if result.returncode != 0:
            raise Exception(f"Failed to launch emulator: {result.stderr}")
        
        return True
    
    def shutdown_emulator(self, vm_index: Union[str, int, List[Union[str, int]]]) -> bool:
        """Shutdown emulator instances
        
        Args:
            vm_index: Index(es) of emulator(s) to shutdown
            
        Returns:
            True if successful
        """
        if isinstance(vm_index, list):
            vm_index = ",".join(str(idx) for idx in vm_index)
        elif isinstance(vm_index, int):
            vm_index = str(vm_index)
        
        args = ["control", "-v", vm_index, "shutdown"]
        result = self._run_command(args)
        
        if result.returncode != 0:
            raise Exception(f"Failed to shutdown emulator: {result.stderr}")
        
        return True
    
    def restart_emulator(self, vm_index: Union[str, int, List[Union[str, int]]]) -> bool:
        """Restart emulator instances
        
        Args:
            vm_index: Index(es) of emulator(s) to restart
            
        Returns:
            True if successful
        """
        if isinstance(vm_index, list):
            vm_index = ",".join(str(idx) for idx in vm_index)
        elif isinstance(vm_index, int):
            vm_index = str(vm_index)
        
        args = ["control", "-v", vm_index, "restart"]
        result = self._run_command(args)
        
        if result.returncode != 0:
            raise Exception(f"Failed to restart emulator: {result.stderr}")
        
        return True
    
    def install_app(self, vm_index: Union[str, int, List[Union[str, int]]], apk_path: str) -> bool:
        """Install an application to emulator instances
        
        Args:
            vm_index: Index(es) of emulator(s) to install app on
            apk_path: Path to APK file to install
            
        Returns:
            True if successful
        """
        if isinstance(vm_index, list):
            vm_index = ",".join(str(idx) for idx in vm_index)
        elif isinstance(vm_index, int):
            vm_index = str(vm_index)
        
        if not os.path.exists(apk_path):
            raise FileNotFoundError(f"APK file not found: {apk_path}")
        
        args = ["control", "-v", vm_index, "app", "install", "-apk", apk_path]
        result = self._run_command(args)
        
        if result.returncode != 0:
            raise Exception(f"Failed to install app: {result.stderr}")
        
        return True
    
    def backup_emulator(self, vm_index: Union[str, int, List[Union[str, int]]], 
                       backup_dir: str, name: str, compressed: bool = False) -> bool:
        """Backup emulator instances
        
        Args:
            vm_index: Index(es) of emulator(s) to backup
            backup_dir: Directory to save backup files
            name: Base name for backup files
            compressed: Whether to compress the backup
            
        Returns:
            True if successful
        """
        if isinstance(vm_index, list):
            vm_index = ",".join(str(idx) for idx in vm_index)
        elif isinstance(vm_index, int):
            vm_index = str(vm_index)
        
        # Create backup directory if it doesn't exist
        os.makedirs(backup_dir, exist_ok=True)
        
        args = ["export", "-v", vm_index, "-d", backup_dir, "-n", name]
        
        if compressed:
            args.append("--zip")
        
        result = self._run_command(args)
        
        if result.returncode != 0:
            raise Exception(f"Failed to backup emulator: {result.stderr}")
        
        return True


def main():
    """Main function for CLI usage"""
    if len(sys.argv) < 2:
        print("MuMu Emulator Instance Manager")
        print("Usage: python instance_manager.py <command> [arguments]")
        print("\nAvailable commands:")
        print("  info [vm_index]                     - Get emulator information")
        print("  create [vm_index] [count]           - Create new emulator(s)")
        print("  clone <vm_index> [count]            - Clone existing emulator(s)")
        print("  delete <vm_index>                   - Delete emulator(s)")
        print("  rename <vm_index> <name>            - Rename emulator(s)")
        print("  launch <vm_index> [package]         - Launch emulator(s)")
        print("  shutdown <vm_index>                 - Shutdown emulator(s)")
        print("  restart <vm_index>                  - Restart emulator(s)")
        print("  install <vm_index> <apk_path>       - Install app to emulator(s)")
        print("  backup <vm_index> <dir> <name>      - Backup emulator(s)")
        return
    
    manager = MuMuInstanceManager()
    command = sys.argv[1].lower()
    
    try:
        if command == "info":
            vm_index = sys.argv[2] if len(sys.argv) > 2 else "all"
            emulators = manager.get_emulator_info(vm_index)
            for emu in emulators:
                print(f"Emulator {emu.index}: {emu.name}")
                print(f"  State: {emu.player_state}")
                print(f"  Android Started: {emu.is_android_started}")
                print(f"  Process Started: {emu.is_process_started}")
                if emu.adb_port:
                    print(f"  ADB Port: {emu.adb_port}")
                print()
        
        elif command == "create":
            vm_index = sys.argv[2] if len(sys.argv) > 2 else None
            count = int(sys.argv[3]) if len(sys.argv) > 3 else 1
            manager.create_emulator(vm_index, count)
            print(f"Successfully created {count} emulator(s)")
        
        elif command == "clone":
            if len(sys.argv) < 3:
                print("Error: vm_index required for clone command")
                return
            vm_index = sys.argv[2]
            count = int(sys.argv[3]) if len(sys.argv) > 3 else 1
            manager.clone_emulator(vm_index, count)
            print(f"Successfully cloned emulator(s) {count} time(s)")
        
        elif command == "delete":
            if len(sys.argv) < 3:
                print("Error: vm_index required for delete command")
                return
            vm_index = sys.argv[2]
            manager.delete_emulator(vm_index)
            print(f"Successfully deleted emulator(s) {vm_index}")
        
        elif command == "rename":
            if len(sys.argv) < 4:
                print("Error: vm_index and name required for rename command")
                return
            vm_index = sys.argv[2]
            name = sys.argv[3]
            manager.rename_emulator(vm_index, name)
            print(f"Successfully renamed emulator(s) {vm_index} to '{name}'")
        
        elif command == "launch":
            if len(sys.argv) < 3:
                print("Error: vm_index required for launch command")
                return
            vm_index = sys.argv[2]
            package = sys.argv[3] if len(sys.argv) > 3 else None
            manager.launch_emulator(vm_index, package)
            print(f"Successfully launched emulator(s) {vm_index}")
        
        elif command == "shutdown":
            if len(sys.argv) < 3:
                print("Error: vm_index required for shutdown command")
                return
            vm_index = sys.argv[2]
            manager.shutdown_emulator(vm_index)
            print(f"Successfully shutdown emulator(s) {vm_index}")
        
        elif command == "restart":
            if len(sys.argv) < 3:
                print("Error: vm_index required for restart command")
                return
            vm_index = sys.argv[2]
            manager.restart_emulator(vm_index)
            print(f"Successfully restarted emulator(s) {vm_index}")
        
        elif command == "install":
            if len(sys.argv) < 4:
                print("Error: vm_index and apk_path required for install command")
                return
            vm_index = sys.argv[2]
            apk_path = sys.argv[3]
            manager.install_app(vm_index, apk_path)
            print(f"Successfully installed app to emulator(s) {vm_index}")
        
        elif command == "backup":
            if len(sys.argv) < 5:
                print("Error: vm_index, directory, and name required for backup command")
                return
            vm_index = sys.argv[2]
            backup_dir = sys.argv[3]
            name = sys.argv[4]
            compressed = "--zip" in sys.argv
            manager.backup_emulator(vm_index, backup_dir, name, compressed)
            print(f"Successfully backed up emulator(s) {vm_index}")
        
        else:
            print(f"Unknown command: {command}")
    
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()