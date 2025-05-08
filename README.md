# BKYGO

<div align="center">
  
![bkygo Logo](https://img.shields.io/badge/BKYGO-BlackArch%20Installer-black?style=for-the-badge&logo=archlinux&logoColor=white)

**A modular, robust BlackArch installer for Arch Linux**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Arch Linux](https://img.shields.io/badge/Arch-Linux-1793D1?logo=arch-linux&logoColor=white)](https://archlinux.org/)
[![BlackArch](https://img.shields.io/badge/Black-Arch-6C7A89)](https://blackarch.org/)
[![Version](https://img.shields.io/badge/Version-1.0-success.svg)](https://github.com/0xb0rn3/bkygo)
[![Engineered by 0xb0rn3](https://img.shields.io/badge/Engineered%20by-0xb0rn3-orange)](https://github.com/0xb0rn3)

</div>

## 📋 Overview

BKYGO is a sophisticated tool designed to streamline the installation of BlackArch packages on Arch Linux systems. With its focus on performance, reliability, and user experience, it transforms the deployment of penetration testing tools from a complex process into a seamless operation.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## ✨ Features

### 🧩 Core Architecture

- **Modular Design**: Organized into distinct components for maintainability and extensibility
- **Intelligent Error Handling**: Automatic resolution of common installation issues 
- **Comprehensive Logging**: Detailed timestamped logs for troubleshooting
- **Configuration Flexibility**: Customizable settings via config file or environment variables

### 🎯 Installation Capabilities

- **Full Repository Support**: Install all BlackArch packages with a single command
- **Group-Based Installation**: Deploy specific tool categories (reconnaissance, exploitation, etc.)
- **Custom Package Lists**: Install from user-defined package lists
- **Parallel Processing**: Multi-threaded installation for optimal performance
- **AUR Integration**: Seamless installation of AUR packages with privilege management

### 💻 User Experience

- **Interactive UI**: Rich text-based interface with progress indicators
- **Customizable Banners**: Multiple banner styles with animation options
- **Color-Coded Output**: Enhanced visibility for important information
- **Progress Tracking**: Real-time status updates with ETA estimates

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 🚀 Installation

### Prerequisites

- Arch Linux (or Arch-based distribution)
- Root privileges (sudo/root)
- Internet connection
- Bash shell
- Optional: `dialog` for enhanced TUI

### Quick Setup

```bash
# Clone the repository
git clone https://github.com/0xb0rn3/bkygo.git

# Navigate to the directory
cd bkygo/

# Make executable
chmod +x run

# Execute with sudo
sudo ./run
```

### Direct Download

```bash
# Download the main script
curl -O https://raw.githubusercontent.com/0xb0rn3/bkygo/main/run

# Make executable
chmod +x run

# Execute with sudo
sudo ./run
```

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 🛠️ Usage Guide

### Basic Commands

```bash
# Install all BlackArch packages
sudo ./bkygo/run -a

# Install specific package group
sudo ./bkygo/run -g penetration

# Install from custom package list
sudo ./bkygo/run -p packages.txt
```

### Banner Customization

Edit `~/.config/kygo/kygo.conf` to set banner preferences:

```
ui.banner_style=matrix    # Options: standard, minimal, matrix, animated
ui.animation=true         # Enable/disable animations
```

### Configuration Options

Key settings in `~/.config/kygo/kygo.conf`:

```
LOG_LEVEL=INFO            # DEBUG, INFO, WARNING, ERROR, CRITICAL
PARALLEL_JOBS=4           # Number of parallel installation jobs
```

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 📁 Project Structure

```
bkygo/
├── core/           # Core functionality modules
│   ├── config      # Configuration management
│   ├── log         # Logging utilities
│   ├── ui          # User interface components
│   └── error       # Error handling mechanisms
├── package/        # Package management modules
│   ├── install     # Installation procedures
│   ├── conflict    # Conflict resolution
│   └── parallel    # Parallel processing
├── system/         # System interaction modules
│   ├── repo        # Repository management
│   ├── depend      # Dependency resolution
│   └── validate    # System validation
└── run             # Main execution script
```

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 📊 Advanced Features

### Conflict Resolution

BKYGO automatically handles:

- **File conflicts**: Backs up conflicting files with restoration metadata
- **Dependency issues**: Resolves with intelligent flag selection
- **Package conflicts**: Pre-installation detection and resolution

### Backup Management

Post-installation options:

- Keep backups in original locations
- Move to centralized backup directory
- Remove all backup files

### Interruption Recovery

If interrupted (Ctrl+C), BKYGO:

- Prompts for backup cleanup
- Preserves logs for troubleshooting

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 🔍 Troubleshooting

If issues occur:

1. Check `~/.config/kygo/logs/kygo.log` for detailed error messages
2. Review specialized logs (`update.log`, `install.log`, `clean.log`)
3. Verify BlackArch repository in `/etc/pacman.conf`
4. Ensure sufficient disk space and network connectivity
5. Run with debug logging:
   ```bash
   sudo KYGO_LOG_LEVEL=DEBUG ./Bkygo/run -a
   ```

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## ⚠️ Disclaimer

Use at your own risk. Always back up your system before running BKYGO, as it modifies system configurations and installs packages.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 📜 License

BKYGO is open source and licensed under the [MIT License](https://opensource.org/licenses/MIT).

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 📬 Contact & Support

- **GitHub**: [github.com/0xb0rn3](https://github.com/0xb0rn3)
- **Issues**: Report bugs or feature requests on the GitHub repository
- **Email**: Contact the author via GitHub for direct support

<div align="center">
  <sub>Built with ❤️ by 0xb0rn3</sub>
</div>
