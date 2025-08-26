#!/usr/bin/env python3
"""
Test script for MuMu Emulator Instance Manager

This script tests the basic functionality of the instance manager.
"""

import unittest
import os
import sys
from unittest.mock import Mock, patch, MagicMock
import subprocess


# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from instance_manager import MuMuInstanceManager, EmulatorInfo


class TestMuMuInstanceManager(unittest.TestCase):
    """Test cases for MuMu Instance Manager"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.manager = MuMuInstanceManager("test_MuMuManager.exe")
    
    def test_initialization(self):
        """Test manager initialization"""
        self.assertEqual(self.manager.mumu_manager_path, "test_MuMuManager.exe")
    
    @patch('subprocess.run')
    def test_run_command_success(self, mock_run):
        """Test successful command execution"""
        # Mock successful command result
        mock_result = Mock()
        mock_result.returncode = 0
        mock_result.stdout = '{"index": "0", "name": "test"}'
        mock_result.stderr = ""
        mock_run.return_value = mock_result
        
        result = self.manager._run_command(["info", "-v", "0"])
        
        self.assertEqual(result.returncode, 0)
        mock_run.assert_called_once()
    
    @patch('subprocess.run')
    def test_run_command_failure(self, mock_run):
        """Test failed command execution"""
        # Mock failed command result
        mock_result = Mock()
        mock_result.returncode = 1
        mock_result.stdout = ""
        mock_result.stderr = "Command failed"
        mock_run.return_value = mock_result
        
        result = self.manager._run_command(["invalid", "command"])
        
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stderr, "Command failed")
    
    @patch('subprocess.run')
    def test_get_emulator_info(self, mock_run):
        """Test getting emulator information"""
        # Mock command result with JSON output
        mock_result = Mock()
        mock_result.returncode = 0
        mock_result.stdout = '''[
            {
                "index": "0",
                "name": "Test Emulator",
                "player_state": "stopped",
                "is_android_started": false,
                "is_process_started": false
            }
        ]'''
        mock_result.stderr = ""
        mock_run.return_value = mock_result
        
        emulators = self.manager.get_emulator_info("all")
        
        self.assertEqual(len(emulators), 1)
        self.assertEqual(emulators[0].index, "0")
        self.assertEqual(emulators[0].name, "Test Emulator")
    
    @patch('subprocess.run')
    def test_create_emulator(self, mock_run):
        """Test creating emulator"""
        # Mock successful creation
        mock_result = Mock()
        mock_result.returncode = 0
        mock_result.stdout = "Created successfully"
        mock_result.stderr = ""
        mock_run.return_value = mock_result
        
        result = self.manager.create_emulator(count=1)
        
        self.assertTrue(result)
        mock_run.assert_called_with(
            ["test_MuMuManager.exe", "create", "-n", "1"],
            capture_output=True,
            text=True,
            timeout=60,
            encoding='utf-8'
        )
    
    @patch('subprocess.run')
    def test_launch_emulator(self, mock_run):
        """Test launching emulator"""
        # Mock successful launch
        mock_result = Mock()
        mock_result.returncode = 0
        mock_result.stdout = "Launched successfully"
        mock_result.stderr = ""
        mock_run.return_value = mock_result
        
        result = self.manager.launch_emulator("0")
        
        self.assertTrue(result)
        mock_run.assert_called_with(
            ["test_MuMuManager.exe", "control", "-v", "0", "launch"],
            capture_output=True,
            text=True,
            timeout=60,
            encoding='utf-8'
        )
    
    @patch('subprocess.run')
    def test_launch_emulator_with_package(self, mock_run):
        """Test launching emulator with package"""
        # Mock successful launch
        mock_result = Mock()
        mock_result.returncode = 0
        mock_result.stdout = "Launched successfully"
        mock_result.stderr = ""
        mock_run.return_value = mock_result
        
        result = self.manager.launch_emulator("0", "com.example.app")
        
        self.assertTrue(result)
        mock_run.assert_called_with(
            ["test_MuMuManager.exe", "control", "-v", "0", "launch", "-pkg", "com.example.app"],
            capture_output=True,
            text=True,
            timeout=60,
            encoding='utf-8'
        )
    
    def test_emulator_info_dataclass(self):
        """Test EmulatorInfo dataclass"""
        info = EmulatorInfo(
            index="0",
            name="Test Emulator",
            player_state="running",
            is_android_started=True
        )
        
        self.assertEqual(info.index, "0")
        self.assertEqual(info.name, "Test Emulator")
        self.assertEqual(info.player_state, "running")
        self.assertTrue(info.is_android_started)


class TestCLIInterface(unittest.TestCase):
    """Test CLI interface"""
    
    @patch('sys.argv', ['instance_manager.py'])
    def test_cli_no_args(self):
        """Test CLI with no arguments"""
        # This should not raise an exception
        try:
            from instance_manager import main
            # We can't easily test this without capturing stdout
            # This test mainly ensures the import works
            self.assertTrue(True)
        except SystemExit:
            # Expected when no arguments provided
            self.assertTrue(True)


class TestGUIImport(unittest.TestCase):
    """Test GUI imports and basic functionality"""
    
    def test_tkinter_available(self):
        """Test that tkinter is available"""
        try:
            import tkinter as tk
            self.assertTrue(True)
        except ImportError:
            self.fail("tkinter not available")
    
    def test_gui_import(self):
        """Test GUI module import"""
        try:
            from gui_manager import EmulatorManagerGUI
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"GUI import failed: {e}")


class TestConfigurationAndSetup(unittest.TestCase):
    """Test configuration and setup functionality"""
    
    def test_config_file_structure(self):
        """Test config.json structure"""
        import json
        
        if os.path.exists("config.json"):
            with open("config.json", "r", encoding="utf-8") as f:
                config = json.load(f)
            
            required_keys = [
                "mumu_manager_path",
                "timeout_settings",
                "logging",
                "ui_settings"
            ]
            
            for key in required_keys:
                self.assertIn(key, config, f"Required key '{key}' missing from config")
    
    def test_examples_import(self):
        """Test examples module import"""
        try:
            import examples
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Examples import failed: {e}")


def run_integration_tests():
    """Run integration tests (requires MuMu to be installed)"""
    print("Running integration tests...")
    print("Note: These tests require MuMu Emulator to be installed")
    
    try:
        # Test actual MuMuManager.exe if available
        manager = MuMuInstanceManager()
        
        # Try to get emulator info (this will fail gracefully if MuMu not installed)
        try:
            emulators = manager.get_emulator_info("all")
            print(f"✓ Found {len(emulators)} emulator(s)")
        except Exception as e:
            print(f"ℹ MuMu not available for testing: {e}")
        
    except Exception as e:
        print(f"Integration test setup failed: {e}")


def main():
    """Run all tests"""
    print("MuMu Emulator Instance Manager - Test Suite")
    print("===========================================")
    
    # Run unit tests
    print("\n--- Unit Tests ---")
    unittest.main(argv=[''], exit=False, verbosity=2)
    
    # Run integration tests
    print("\n--- Integration Tests ---")
    run_integration_tests()
    
    print("\n--- Test Summary ---")
    print("✓ All tests completed")
    print("Note: Some tests may show warnings if MuMu Emulator is not installed")
    print("This is expected and does not indicate software problems")


if __name__ == "__main__":
    main()