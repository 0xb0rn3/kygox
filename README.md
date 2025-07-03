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
██╗  ██╗██╗   ██╗ ██████╗  ██████╗ ██╗  ██╗
██║ ██╔╝╚██╗ ██╔╝██╔════╝ ██╔═══██╗╚██╗██╔╝
█████╔╝  ╚████╔╝ ██║  ███╗██║   ██║ ╚███╔╝ 
██╔═██╗   ╚██╔╝  ██║   ██║██║   ██║ ██╔██╗ 
██║  ██╗   ██║   ╚██████╔╝╚██████╔╝██╔╝ ██╗
╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
```

## 📋 Overview

KYGOX (Advanced Arch Linux Security Testing Suite) represents the evolution of security tool deployment on Arch Linux systems. This enhanced edition transforms complex penetration testing environment setup into an intelligent, streamlined process with enterprise-grade reliability and comprehensive automation.

Built from the ground up with modularity, performance optimization, and user experience at its core, KYGOX delivers not just tool installation but a complete security testing ecosystem with advanced features like kernel optimization, intelligent dependency resolution, and sophisticated error recovery mechanisms.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## ✨ Advanced Features

### 🎯 Interactive Menu System
KYGOX features an intelligent menu-driven interface that guides users through installation options with visual feedback and real-time progress indicators. The system automatically detects your environment and presents appropriate installation categories.

### 📦 Categorized Installation Options

**Standard Suite** (⚙️): Industry-standard security tools including network scanners (nmap, masscan), traffic analyzers (wireshark, tcpdump), wireless security tools (aircrack-ng, bettercap), password crackers (john, hashcat, hydra), web application scanners (sqlmap, nikto, gobuster), and essential exploitation frameworks (metasploit, impacket).

**Red Team Arsenal** (🚀): Advanced offensive security tools including covenant, rubeus, mimikatz, eyewitness, nuclei, crackmapexec, subfinder, and specialized tools for advanced persistent threat simulation and red team operations.

**Blue Team Defense** (🛡️): Comprehensive defensive security tools including intrusion detection systems (suricata, snort, zeek), security monitoring (ossec, aide, tripwire), network analysis tools (zmap, hping3, netdiscover), and log analysis frameworks (graylog, elk stack components).

**Mobile Security** (📱): Specialized mobile application security testing tools including mobsf, drozer, apktool, frida-tools, objection, and iOS/Android reverse engineering utilities for comprehensive mobile security assessments.

**IoT & Hardware** (🔧): Internet of Things and hardware security testing tools including firmware analysis utilities (firmware-mod-kit, binwalk), hardware debugging tools (openocd, flashrom), and radio frequency analysis tools (rtl-sdr, hackrf, gnuradio).

**Complete Arsenal** (👑): Full deployment of all available security tools across all categories for comprehensive security testing laboratories.

### 🚀 Performance & System Optimization

**Zen Kernel Integration** (⚡): Automatically install and configure the Zen kernel for enhanced system performance during intensive security testing operations. The installer handles GRUB configuration updates and provides clear reboot notifications.

**Intelligent Package Management**: Advanced dependency resolution with automatic handling of both official Arch repositories and AUR packages. The system intelligently determines the best installation source for each tool and handles conflicts automatically.

**YAY AUR Helper Integration**: Seamless integration with the YAY AUR helper for accessing community-maintained security tools not available in official repositories.

### 🔧 Enterprise-Grade Reliability

**Comprehensive Progress Tracking**: Real-time visual progress indicators with animated spinners and percentage completion tracking for all installation phases.

**Automatic System Cleanup**: Built-in cleanup procedures that remove unnecessary packages and clear package caches to maintain system efficiency.

**Robust Error Handling**: Advanced error recovery mechanisms with graceful interrupt handling and system integrity preservation.

**Secure Installation Process**: Proper privilege management with user context preservation for AUR builds while maintaining security throughout the installation process.

### 💻 Enhanced User Experience

**Adaptive Interface**: Color-coded output with symbolic indicators, progress visualization, and context-aware information display that adapts to terminal capabilities.

**Multiple Operation Modes**: 
- **Interactive Mode**: Rich visual menu system with guided installation choices
- **Command Line Mode**: Direct category installation via command line parameters
- **Batch Mode**: Support for automated deployment scenarios

**Installation Interruption Handling**: Graceful handling of Ctrl+C interruptions with proper cleanup procedures and system integrity preservation.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 🛠️ Installation & Quick Start

### System Requirements

KYGOX has been extensively tested and optimized for Arch Linux and Arch-based distributions. The installer includes automatic detection for Debian-based systems and will redirect users to the appropriate KRILIN installer for those environments.

**Prerequisites**: Root privileges, internet connectivity, bash shell, and adequate storage space for selected tool categories.

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

Interactive Mode:
  sudo ./run                    # Launch interactive menu system

Direct Installation Options:
  -fullkit, --fullkit          # Install complete security arsenal
  -standard, --standard        # Install standard security tools
  -redteam, --redteam          # Install red team arsenal
  -blueteam, --blueteam        # Install blue team defense tools
  -mobile, --mobile            # Install mobile security tools
  -iot, --iot                  # Install IoT & hardware tools
  -zen, --zen                  # Install Zen kernel only

  -h, --help                   # Show help message
```

### Real-World Usage Examples

**Interactive Installation**:
```bash
# Launch the menu-driven interface
sudo ./run
```

**Complete Security Lab Setup**:
```bash
# Install everything with performance optimization
sudo ./run -fullkit
```

**Targeted Penetration Testing Environment**:
```bash
# Install red team tools for offensive security
sudo ./run -redteam
```

**Mobile Security Testing Lab**:
```bash
# Deploy mobile security testing tools
sudo ./run -mobile
```

**Performance Optimization Only**:
```bash
# Install Zen kernel for better performance
sudo ./run -zen
```

**Standard Security Toolkit**:
```bash
# Essential tools for general security testing
sudo ./run -standard
```

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 🔍 Advanced Architecture

### Core Security Tools Integration

KYGOX automatically deploys curated collections of security tools organized by use case. The standard suite includes essential tools like nmap for network discovery, wireshark for traffic analysis, aircrack-ng for wireless security, john and hashcat for password cracking, sqlmap for database security testing, and metasploit for exploitation frameworks.

### BlackArch Repository Integration

The installer seamlessly integrates with BlackArch repository infrastructure while maintaining system security through proper GPG key management and repository configuration. The system disguises the BlackArch repository name for operational security purposes.

### AUR Package Management

KYGOX includes sophisticated AUR integration through the YAY helper, enabling installation of community-maintained security tools. The system properly handles user context switching to ensure AUR packages are built with appropriate privileges while maintaining system security.

### System Integration Features

**Kernel Optimization**: Zen kernel installation includes automatic GRUB configuration updates with proper bootloader management and user notification for reboot requirements.

**Package Database Management**: Intelligent package database synchronization with error handling and retry mechanisms to ensure consistent package availability.

**Security Repository Setup**: Automated BlackArch repository configuration with proper signature verification and secure repository addition procedures.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 📊 Monitoring & Logging

### Comprehensive Logging System

KYGOX creates detailed logs in the `~/.kygox` directory structure within the user's home directory. The logging system maintains complete installation timelines with categorized message levels and detailed progress tracking.

### Progress Monitoring

Real-time progress tracking includes visual progress indicators with animated spinners, percentage completion tracking for category installations, and detailed status updates for each installation phase.

### System State Management

The installer maintains temporary working directories in `/tmp/kygox_$$` with automatic cleanup procedures and organized tool source storage in `/opt/kygox` for easy access and management.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 🔧 Troubleshooting & Recovery

### Automatic System Detection

KYGOX automatically detects the system distribution and redirects Debian-based users to the appropriate KRILIN installer, ensuring compatibility and preventing installation issues on unsupported systems.

### Package Conflict Resolution

The system intelligently handles package conflicts by attempting official repository installation first, then falling back to AUR packages when necessary. This approach minimizes conflicts while ensuring comprehensive tool availability.

### Installation Recovery

If installation issues occur, KYGOX provides multiple recovery mechanisms including automatic cleanup of temporary files, proper signal handling for interrupted installations, and preservation of system integrity through careful privilege management.

### Environment Validation

The installer performs comprehensive environment validation including root privilege verification, user context preservation, and system compatibility checks before beginning any installation procedures.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## ⚡ Performance Considerations

### System Resource Management

KYGOX is designed to efficiently manage system resources during installation. The installer creates organized directory structures for logs and temporary files while maintaining proper ownership and permissions throughout the process.

### Installation Optimization

The system implements several performance optimizations including intelligent tool categorization to minimize conflicts, proper package ordering to reduce dependency issues, and efficient progress tracking that doesn't impact installation performance.

### Storage Requirements

Storage requirements vary significantly based on selected categories, ranging from approximately 2GB for standard tools to 20GB+ for complete arsenal deployment. The installer provides clear category descriptions to help users make informed decisions about storage allocation.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 🛡️ Security Considerations

### Privilege Management

KYGOX implements careful privilege management throughout the installation process. The system requires root privileges for package installation while preserving user context for AUR builds, ensuring security without compromising functionality.

### Repository Security

The installer maintains security through proper GPG key management for repository additions, secure repository configuration procedures, and verification of package authenticity during installation.

### System Integrity

Installation procedures include comprehensive system integrity checks, proper cleanup of temporary files, and careful handling of system configurations to prevent security vulnerabilities.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 🔄 Updates & Maintenance

### Tool Categories

KYGOX organizes security tools into logical categories that can be updated independently. Users can install additional categories at any time by re-running the installer with different options.

### System Maintenance

The installer includes automatic system cleanup procedures that remove unnecessary packages and clear package caches to maintain system efficiency and free up storage space.

### Version Management

The current stable version is 0.1.5, with ongoing development focused on expanding tool categories, improving installation reliability, and enhancing user experience through better progress tracking and error handling.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## ⚠️ Important Notices

**System Modification Warning**: KYGOX makes significant system modifications including repository additions, kernel installations, and extensive package deployments. The installer performs these operations with appropriate safeguards but users should understand the scope of changes.

**Debian System Redirection**: The installer automatically detects Debian-based systems and redirects users to the KRILIN installer specifically designed for those environments, preventing compatibility issues and ensuring optimal tool deployment.

**Root Privilege Requirement**: KYGOX requires root privileges for system modifications while maintaining proper user context for AUR builds. The installer validates privilege levels and user context before beginning installation procedures.

**Security Tool Responsibility**: The tools installed by KYGOX are powerful security testing utilities. Users are responsible for ensuring all usage complies with applicable laws, regulations, and organizational policies.

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

KYGOX welcomes contributions including bug fixes, tool category expansions, user interface improvements, and testing on additional Arch-based distributions.

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
