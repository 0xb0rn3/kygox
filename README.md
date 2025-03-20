# bkygo - BlackArch Installer for Arch Linux

![BlackArch Logo](https://blackarch.org/images/blackarch-logo.png)

> Engineered by 0xb0rn3 | github.com/0xb0rn3

## Overview

`bkygo` is a powerful tool that automates the installation of BlackArch packages on Arch Linux with enhanced visual feedback, intelligent error handling, and robust logging. It's designed to make the BlackArch deployment process smooth, reliable, and user-friendly.

## Features

- **Interactive UI**: Animated progress bars, styled headers, and color-coded output for better visibility
- **Smart Error Resolution**: Automatic handling of file conflicts and dependency issues
- **Comprehensive Logging**: Detailed logs with timestamped entries for troubleshooting
- **Flexible Installation Options**: Install all packages, specific groups, or a custom list
- **Backup Management**: Automatic backup of conflicting files with restore metadata
- **Performance Tracking**: Real-time progress monitoring and time estimates

## Requirements

- Arch Linux (or Arch-based distribution)
- Root privileges
- Internet connection
- Bash shell

## Installation

1. Download the script:
   ```bash
   curl -O https://raw.githubusercontent.com/0xb0rn3/bkygo/main/run
   ```

2. Make it executable:
   ```bash
   chmod +x run
   ```

3. Run with sudo:
   ```bash
   sudo ./run
   ```

## Usage Guide

### Initial Setup

The script will:
1. Verify root privileges
2. Add the BlackArch repository to your system
3. Update package databases
4. Fetch the complete list of BlackArch packages

### Installation Methods

Choose from three installation options:
- **All packages**: Install the complete BlackArch repository
- **Specific group**: Install packages from a selected BlackArch group
- **Custom list**: Provide a text file with package names to install

### Conflict Resolution

The script automatically handles:
- **File conflicts**: Backs up conflicting files and retries installation
- **Dependency issues**: Attempts to resolve missing dependencies
- **Package ownership conflicts**: Intelligently manages package conflicts

### Backup Management

After installation, you can:
- Keep all backup files in their original locations
- Move all backups to a centralized folder
- Remove all backup files

### Cache Management

Optionally clean the pacman cache to free disk space after installation.

## Log Files

The script maintains several log files:
- `blackarch_logs/installation.log`: Main log with all operations
- `blackarch_logs/package_logs/`: Individual package installation logs
- `blackarch_logs/failed_packages.txt`: List of packages that failed to install
- `blackarch_logs/skipped_packages.txt`: List of packages that were skipped

## Error Handling

The script implements multiple retry mechanisms:
1. Attempts standard installation
2. Tries installation with `--overwrite` flag
3. Tries installation with `--needed` flag
4. Analyzes and resolves specific error types

## Interruption Recovery

If the script is interrupted (Ctrl+C), it offers to clean up backup files before exiting.

## Customization

You can modify these variables at the top of the script to customize behavior:
- `LOG_DIR`: Location for log files
- `BACKUP_DIR`: Location for file backups
- Visual elements (colors, symbols, etc.)

## Troubleshooting

If you encounter issues:
1. Check the main log file (`blackarch_logs/installation.log`)
2. Look for specific package errors in `blackarch_logs/package_logs/`
3. Try reinstalling failed packages individually
4. Check system configuration (particularly pacman.conf)

## License

This script is open source and available under the MIT License.

## Disclaimer

Use at your own risk. Always backup your system before making significant changes.

## Contact & Support

- GitHub: [github.com/0xb0rn3](https://github.com/0xb0rn3)
- Issues: Report issues through the GitHub repository
