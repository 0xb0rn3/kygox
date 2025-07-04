# KYGOX - Advanced Arch Linux Security Testing Suite

<div align="center">
  
![KYGOX Logo](https://img.shields.io/badge/KYGOX-Security%20Suite-red?style=for-the-badge&logo=archlinux&logoColor=white)

**A comprehensive, intelligent security testing suite installer for Arch Linux**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Arch Linux](https://img.shields.io/badge/Arch-Linux-1793D1?logo=arch-linux&logoColor=white)](https://archlinux.org/)
[![BlackArch](https://img.shields.io/badge/Black-Arch-6C7A89)](https://blackarch.org/)
[![Version](https://img.shields.io/badge/Version-0.1.5-success.svg)](https://github.com/0xb0rn3/kygox)
[![Enhanced Edition](https://img.shields.io/badge/Latest-Version-gold?style=flat-square)](https://github.com/0xb0rn3/kygox)
[![Engineered by 0xb0rn3](https://img.shields.io/badge/Engineered%20by-0xb0rn3-orange)](https://github.com/0xb0rn3)

</div>

```
██╗  ██╗██╗   ██╗ ██████╗  ██████╗ ██████╗ ██╗ █████╗ ██████╗██╗  ██╗
██║ ██╔╝╚██╗ ██╔╝██╔════╝ ██╔═══██╗ ██╔══██╗██║ ██╔══██╗██╔════╝██║ ██╔╝
█████╔╝  ╚████╔╝ ██║  ███╗██║   ██║ ██████╔╝██║ ███████║██║     █████╔╝ 
██╔═██╗   ╚██╔╝  ██║   ██║██║   ██║ ██╔══██╗██║ ██╔══██║██║     ██╔═██╗ 
██║  ██╗   ██║   ╚██████╔╝╚██████╔╝ ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗
╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
```

## 📋 Overview

KYGOX (Advanced Arch Linux Security Testing Suite) represents the evolution of security tool deployment on Arch Linux systems. This enhanced edition transforms complex penetration testing environment setup into an intelligent, streamlined process with enterprise-grade reliability and comprehensive automation.

Built from the ground up with modularity, performance optimization, and user experience at its core, KYGOX delivers not just tool installation but a complete security testing ecosystem with advanced features like intelligent dependency resolution, sophisticated error recovery mechanisms, and comprehensive backup management.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## ✨ Advanced Features

### 🎯 Intelligent Installation System
KYGOX features an advanced installation system that handles complex package dependencies, file conflicts, and provides robust error recovery. The system automatically detects and resolves conflicts while maintaining detailed logs of all operations.

### 📦 Flexible Installation Options

**Complete Arsenal** (--all): Install all available BlackArch security tools for comprehensive penetration testing laboratories. This option deploys the entire BlackArch repository, providing access to thousands of security tools across all categories.

**Package Groups** (--group): Install specific BlackArch package groups such as exploitation, wireless, web, forensics, crypto, and more. This targeted approach allows users to install only the tools relevant to their specific security testing needs.

**Custom Package Lists** (--packages): Install from custom package lists using the included `default` file or your own custom lists. This provides ultimate flexibility for creating tailored security environments.

### 🚀 Enterprise-Grade Reliability

**Advanced Conflict Resolution**: Sophisticated file conflict handling with automatic backup creation, intelligent package removal, and restoration capabilities. The system can handle complex dependency chains and version conflicts automatically.

**Comprehensive Backup System**: Automatic backup of conflicting files with organized storage in timestamped directories. Users can choose to keep, move, or remove backups after installation completion.

**Intelligent Retry Mechanisms**: Failed packages are automatically retried using the YAY AUR helper, providing multiple installation pathways and maximizing success rates.

**Robust Error Recovery**: Advanced error handling with detailed logging, graceful interruption management, and system integrity preservation throughout the installation process.

### 🔧 Advanced Package Management

**Dual Repository Support**: Seamless integration with both official Arch repositories and AUR packages through the YAY helper. The system intelligently determines the best installation source for each tool.

**BlackArch Integration**: Automatic BlackArch repository setup with proper GPG key management and secure repository configuration. The system handles all aspects of BlackArch integration transparently.

**Dependency Resolution**: Intelligent dependency management that automatically installs required base packages, development tools, and system libraries needed for security tool compilation and operation.

### 💻 Enhanced User Experience

**Visual Progress Tracking**: Real-time progress indicators with detailed package information, success/failure tracking, and comprehensive installation statistics.

**Detailed Logging**: Complete installation logs with categorized message levels, error details, and package-specific logs for troubleshooting and audit purposes.

**Flexible Operation Modes**: 
- **Interactive Mode**: Rich visual interface with real-time progress updates
- **Quiet Mode**: Minimal output for automated deployments
- **Auto-cleanup Mode**: Automatic backup and cache management

**Graceful Interruption Handling**: Proper handling of Ctrl+C interruptions with cleanup procedures and system integrity preservation.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 🛠️ Installation & Quick Start

### System Requirements

KYGOX has been extensively tested and optimized for Arch Linux and Arch-based distributions. The installer requires root privileges, internet connectivity, and adequate storage space for selected tool categories.

**Prerequisites**: Root privileges, internet connectivity, bash shell, and sufficient storage space (varies by installation type: 2GB minimum for targeted installations, 20GB+ for complete arsenal).

### Installation Methods

**Direct Download & Execute**:
```bash
# Download the installer
curl -O https://raw.githubusercontent.com/0xb0rn3/kygox/main/run

# Make executable
chmod +x run

# Execute with desired options
sudo ./run
```

**Repository Clone**:
```bash
# Clone the complete repository
git clone https://github.com/0xb0rn3/kygox.git
cd kygox/

# Make executable and run
chmod +x run
sudo ./run
```

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 📚 Comprehensive Usage Guide

### Command Line Interface

```bash
sudo ./run [options]

Installation Options:
  -a, --all                    # Install all BlackArch packages
  -g, --group GROUP           # Install specific package group
  -p, --packages FILE         # Install from custom package list

Operation Modes:
  -q, --quiet                 # Quiet mode with minimal output
  --auto-cleanup              # Automatic backup and cache cleanup

  -h, --help                  # Show help message
```

### Real-World Usage Examples

**Complete Security Arsenal**:
```bash
# Install all available BlackArch tools
sudo ./run --all
```

**Targeted Security Categories**:
```bash
# Install exploitation tools
sudo ./run --group exploitation

# Install wireless security tools
sudo ./run --group wireless

# Install web application testing tools
sudo ./run --group webapp
```

**Custom Tool Selection**:
```bash
# Install from the included default package list
sudo ./run --packages default

# Install from your custom package list
sudo ./run --packages my_custom_tools.txt
```

**Automated Deployment**:
```bash
# Silent installation with automatic cleanup
sudo ./run --packages default --quiet --auto-cleanup
```

### Using the Default Package List

KYGOX includes a curated `default` package list that contains essential tools for red team operations, blue team defense, and bug bounty hunting. This carefully selected collection provides a comprehensive foundation for security testing without the storage requirements of a full BlackArch installation.

The default list includes:
- **Network Discovery & Scanning**: nmap, masscan, zmap, unicornscan
- **Web Application Testing**: sqlmap, nikto, gobuster, dirb, wfuzz, ffuf, whatweb
- **Wireless Security**: aircrack-ng, bettercap, kismet, wifite
- **Password Attacks**: john, hashcat, hydra, medusa, patator
- **Exploitation Frameworks**: metasploit, impacket, covenant, empire
- **Reconnaissance**: theHarvester, recon-ng, sublist3r, amass
- **Forensics & Analysis**: volatility, autopsy, sleuthkit, foremost
- **And many more specialized tools for comprehensive security testing

To use the default package list:
```bash
sudo ./run --packages default
```

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 🔍 Advanced Architecture

### Core System Integration

KYGOX automatically handles complex system integration tasks including BlackArch repository setup, GPG key management, package database synchronization, and dependency resolution. The system maintains security through proper privilege management and secure repository configuration.

### Intelligent Package Management

The installer implements sophisticated package management including automatic conflict resolution, intelligent retry mechanisms, and comprehensive backup systems. Failed installations are automatically retried using alternative installation methods to maximize success rates.

### Backup and Recovery System

KYGOX includes a comprehensive backup system that automatically creates timestamped backups of conflicting files, organizes them in structured directories, and provides flexible cleanup options. The system ensures that no system files are lost during the installation process.

### Logging and Monitoring

The installer maintains detailed logs of all operations in the `bkygo_logs` directory, including main installation logs, package-specific error logs, and lists of failed and skipped packages. This comprehensive logging system enables effective troubleshooting and installation auditing.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 📊 Installation Categories

### Available BlackArch Groups

KYGOX supports installation of specific BlackArch package groups, allowing users to install only the tools relevant to their security testing needs. Popular groups include:

- **exploitation**: Exploitation tools and frameworks
- **wireless**: Wireless security testing tools
- **webapp**: Web application security tools
- **scanner**: Network and vulnerability scanners
- **forensic**: Digital forensics and analysis tools
- **crypto**: Cryptographic tools and utilities
- **social**: Social engineering tools
- **mobile**: Mobile security testing tools
- **hardware**: Hardware security testing tools
- **malware**: Malware analysis and reverse engineering

To see all available groups:
```bash
pacman -Sg | grep blackarch
```

### Custom Package Lists

Users can create custom package lists by creating text files with one package name per line. The installer will attempt to install each package using the most appropriate method (official repos, BlackArch, or AUR).

Example custom list format:
```
nmap
sqlmap
metasploit
wireshark-qt
aircrack-ng
john
```

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 🔧 Troubleshooting & Recovery

### Automatic Error Recovery

KYGOX implements multiple error recovery mechanisms including automatic file conflict resolution, dependency issue handling, and intelligent retry logic. The system attempts to resolve issues automatically before requiring user intervention.

### Backup Management

The installer creates comprehensive backups of any conflicting files and provides flexible cleanup options. Users can choose to keep backups in place, move them to organized directories, or remove them after successful installation.

### Installation Resumption

If an installation is interrupted, users can resume by re-running the installer with the same options. The system will skip already-installed packages and continue with remaining installations.

### Log Analysis

Detailed logs are maintained in the `bkygo_logs` directory, including main installation logs, package-specific error logs, and failed package lists. These logs provide comprehensive information for troubleshooting installation issues.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## ⚡ Performance Considerations

### System Resource Management

KYGOX is designed to efficiently manage system resources during installation. The installer handles large package installations with appropriate progress tracking and resource utilization monitoring.

### Storage Requirements

Storage requirements vary significantly based on installation type:
- **Targeted Groups**: 1-5GB depending on the group
- **Default Package List**: Approximately 3-5GB
- **Complete Arsenal**: 20GB+ for full BlackArch installation

### Installation Optimization

The system implements several performance optimizations including intelligent package ordering, efficient dependency resolution, and optimized compilation flags for AUR packages.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 🛡️ Security Considerations

### Privilege Management

KYGOX implements careful privilege management throughout the installation process. The system requires root privileges for system modifications while preserving user context for AUR builds, ensuring security without compromising functionality.

### Repository Security

The installer maintains security through proper GPG key management for BlackArch repository additions, secure repository configuration procedures, and verification of package authenticity during installation.

### System Integrity

Installation procedures include comprehensive backup systems, proper cleanup of temporary files, and careful handling of system configurations to prevent security vulnerabilities and ensure system stability.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 🔄 Updates & Maintenance

### Package Updates

Installed packages can be updated using standard Arch Linux package management tools:
```bash
# Update all packages
sudo pacman -Syu

# Update AUR packages
yay -Syu
```

### System Maintenance

The installer includes automatic system cleanup procedures that remove unnecessary packages and clear package caches to maintain system efficiency. Users can also manually clean package caches:
```bash
# Clean package cache
sudo pacman -Sc
```

### Version Management

The current stable version is 0.1.5, with ongoing development focused on improving installation reliability, expanding tool coverage, and enhancing user experience through better error handling and progress tracking.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## ⚠️ Important Notices

**System Modification Warning**: KYGOX makes significant system modifications including repository additions and extensive package deployments. The installer performs these operations with appropriate safeguards, but users should understand the scope of changes and ensure adequate system backups.

**Root Privilege Requirement**: KYGOX requires root privileges for system modifications while maintaining proper user context for AUR builds. The installer validates privilege levels and user context before beginning installation procedures.

**Storage Space Requirements**: Security tool installations can consume significant storage space. Users should ensure adequate free space before beginning large installations and consider storage requirements when selecting installation options.

**Security Tool Responsibility**: The tools installed by KYGOX are powerful security testing utilities designed for legitimate security testing purposes. Users are responsible for ensuring all usage complies with applicable laws, regulations, and organizational policies.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 📜 License & Legal

KYGOX is released under the MIT License, providing flexibility for both personal and commercial use while maintaining open source principles. The installer respects the licenses of all deployed tools and integrates with established package management systems.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 🤝 Contributing & Support

### Community Support

- **GitHub Repository**: [github.com/0xb0rn3/kygox](https://github.com/0xb0rn3/kygox)
- **Instagram**: @theehiv3
- **Issue Reporting**: Use GitHub Issues for bug reports and feature requests

### Development Contributions

KYGOX welcomes contributions including bug fixes, tool additions, user interface improvements, and testing on additional Arch-based distributions. Please submit pull requests with detailed descriptions of changes and improvements.

### Professional Support

For enterprise deployments or specialized requirements, contact the development team through the GitHub repository for professional consulting and support services.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 📬 Contact Information

- **Primary Developer**: 0xb0rn3
- **GitHub Repository**: [github.com/0xb0rn3/kygox](https://github.com/0xb0rn3/kygox)
- **Instagram**: @theehiv3
- **Issue Reporting**: Use GitHub Issues for bug reports and feature requests

<div align="center">
  <sub>🔒 Engineered with precision by 0xb0rn3 | Empowering security professionals worldwide</sub>
</div>
