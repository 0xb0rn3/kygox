# KYGOX - Advanced Arch Linux Security Testing Suite

<div align="center">
  
![KYGOX Logo](https://img.shields.io/badge/KYGOX-Security%20Suite-red?style=for-the-badge&logo=archlinux&logoColor=white)

**A comprehensive, intelligent security testing suite installer for Arch Linux**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Arch Linux](https://img.shields.io/badge/Arch-Linux-1793D1?logo=arch-linux&logoColor=white)](https://archlinux.org/)
[![BlackArch](https://img.shields.io/badge/Black-Arch-6C7A89)](https://blackarch.org/)
[![Version](https://img.shields.io/badge/Version-0.0.4-success.svg)](https://github.com/0xb0rn3/kygox)
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

### 🎯 Multi-Modal Installation System
KYGOX offers unprecedented flexibility in how you deploy your security testing environment:

**All-Inclusive Mode** (`-a, --all`): Deploy the complete BlackArch repository with intelligent batching and progress tracking, perfect for comprehensive security testing labs.

**Group-Targeted Installation** (`-g, --group GROUP`): Install specific tool categories like exploitation, reconnaissance, forensics, or wireless tools, allowing for specialized deployment scenarios.

**Custom Package Lists** (`-p, --packages FILE`): Deploy from curated package lists, enabling standardized team environments and repeatable installations across multiple systems.

**Standard Security Core** (`-s, --standard-only`): Install essential security tools without the full BlackArch ecosystem, ideal for lightweight deployments or resource-constrained environments.

### 🚀 Performance & System Optimization

**Zen Kernel Integration** (`-z, --zen-kernel`): Automatically install and configure the Zen kernel for enhanced system performance during intensive security testing operations. The installer handles GRUB configuration updates and provides clear reboot notifications.

**Intelligent Dependency Management**: Advanced dependency resolution with conflict detection, automated overwrite handling, and smart retry mechanisms that adapt to different failure scenarios.

**AUR Integration with Privilege Management**: Seamless AUR package installation with proper user context preservation, ensuring security while maintaining functionality.

### 🔧 Enterprise-Grade Reliability

**Comprehensive Logging System**: Multi-level logging with categorized output (SUCCESS, WARNING, ERROR, INFO, KERNEL, SECURITY) and detailed timestamps for enterprise auditing requirements.

**Automatic Backup Management**: Creates timestamped backups of critical system configurations with organized directory structures for easy recovery.

**Intelligent Error Recovery**: Advanced error handling with automatic conflict resolution, dependency fixing, and retry mechanisms that learn from common installation failures.

**Progress Monitoring**: Real-time installation progress with ETA calculations, completion percentages, and detailed status reporting for large deployment operations.

### 💻 Enhanced User Experience

**Adaptive Interface Modes**: 
- **Interactive Mode**: Rich visual feedback with progress bars, colored output, and detailed status information
- **Quiet Mode** (`-q, --quiet`): Minimal output for scripted deployments and automated systems
- **Auto-Cleanup Mode** (`--auto-cleanup`): Unattended operation with automatic system maintenance

**Intelligent Output Management**: Color-coded messages with symbolic indicators, progress visualization, and context-aware information display that adapts to terminal capabilities.

**Installation Interruption Handling**: Graceful handling of Ctrl+C interruptions with cleanup prompts and system integrity preservation.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 🛠️ Installation & Quick Start

### System Requirements

KYGOX has been extensively tested and optimized for:
- **Arch Linux** (vanilla installations)
- **Garuda Linux** (full compatibility with enhanced features)
- **Archcraft Linux** (lightweight environment optimization)
- **Other Arch-based distributions** (automatic adaptation)

**Prerequisites**: Root privileges, internet connectivity, bash shell, and adequate storage space for selected packages.

### Installation Methods

**Direct Download & Execute**:
```bash
# Download the installer
curl -O https://raw.githubusercontent.com/0xb0rn3/kygox/main/run

# Make executable
chmod +x run

# Execute with desired options
sudo ./run --help
```

**Repository Clone**:
```bash
# Clone the complete repository
git clone https://github.com/0xb0rn3/kygox.git
cd kygox/

# Make executable and run
chmod +x run
sudo ./run [options]
```

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 📚 Comprehensive Usage Guide

### Command Line Interface

```bash
sudo ./run [options]

Installation Options:
  -a, --all               Install all security packages
  -g, --group GROUP       Install specific package group
  -p, --packages FILE     Install from custom package list
  -s, --standard-only     Install only standard security tools

System Options:
  -z, --zen-kernel        Install Zen kernel for better performance
  --no-standard-tools     Skip installation of standard security tools
  -q, --quiet             Run in quiet mode (minimal output)
  --auto-cleanup          Automatically clean up without prompting

  -h, --help              Show detailed help message
```

### Real-World Usage Examples

**Complete Security Lab Setup**:
```bash
# Install everything with performance optimization
sudo ./run -a -z
```

**Targeted Penetration Testing Environment**:
```bash
# Install exploitation tools with standard utilities
sudo ./run -g exploitation
```

**Custom Team Environment**:
```bash
# Deploy from standardized package list
sudo ./run -p team_tools.txt -z --auto-cleanup
```

**Lightweight Security Toolkit**:
```bash
# Essential tools only, no additional packages
sudo ./run -s --quiet
```

**Automated Deployment**:
```bash
# Unattended installation for automation scripts
sudo ./run -a --quiet --auto-cleanup --no-standard-tools
```

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 🔍 Advanced Architecture

### Core Security Tools Integration

KYGOX automatically deploys a curated collection of essential security tools including network scanners (nmap), traffic analyzers (wireshark), wireless security tools (aircrack-ng), password crackers (john, hydra), web application scanners (sqlmap, nikto, gobuster), and DNS reconnaissance tools (dnsenum, dnsrecon, fierce).

### AUR Package Management

The installer includes sophisticated AUR integration for specialized tools like apkid for Android analysis, android-apktool for reverse engineering, metasploit for exploitation frameworks, and burpsuite for web application security testing.

### Repository Management

KYGOX handles BlackArch repository configuration with intelligent detection of existing setups, secure repository addition, and proper GPG key management to ensure package authenticity and system security.

### System Integration Features

**Kernel Optimization**: Zen kernel installation includes automatic GRUB configuration updates, proper header installation for module compilation, and user notification for reboot requirements.

**Database Synchronization**: Intelligent package database updates with error handling and retry mechanisms to ensure consistent package availability.

**Service Management**: Proper handling of system services that may be affected by security tool installations, including network services and hardware access permissions.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 📊 Monitoring & Logging

### Comprehensive Logging System

KYGOX creates detailed logs in the `kygox_logs` directory structure:

**Primary Installation Log** (`installation.log`): Complete installation timeline with timestamped entries and categorized message levels.

**Package-Specific Logs** (`package_logs/`): Individual error logs for failed packages to assist with troubleshooting and manual resolution.

**Failed Package Tracking** (`failed_packages.txt`): Consolidated list of packages that couldn't be installed for easy retry or manual investigation.

**Backup Directory** (`backups/`): Organized storage of system configuration backups with restoration metadata.

### Progress Monitoring

Real-time progress tracking includes visual progress bars, percentage completion indicators, estimated time remaining calculations, and detailed status updates for each package installation attempt.

### Performance Metrics

The installer tracks and reports installation duration, success/failure rates, package counts, and system resource utilization to help optimize future deployments.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 🔧 Troubleshooting & Recovery

### Common Issue Resolution

**Package Conflicts**: KYGOX automatically detects and resolves file conflicts using intelligent overwrite strategies and conflict resolution algorithms.

**Dependency Problems**: Advanced dependency resolution with automatic flag selection and retry mechanisms that adapt to different package management scenarios.

**Network Issues**: Robust handling of network interruptions with automatic retry mechanisms and fallback strategies for package downloads.

**Permission Errors**: Proper privilege escalation handling with user context preservation for AUR builds and system modifications.

### Recovery Procedures

If installation issues occur, KYGOX provides multiple recovery options:

1. **Automated Recovery**: Built-in error resolution for common scenarios
2. **Manual Intervention**: Detailed error logs with specific resolution suggestions
3. **System Restoration**: Configuration backup restoration with guided procedures
4. **Partial Installation Recovery**: Resume interrupted installations from checkpoint data

### Debug Mode Operation

For advanced troubleshooting, enable detailed debugging:
```bash
# Run with maximum verbosity
sudo KYGOX_DEBUG=1 ./run -a

# Check specific component logs
tail -f kygox_logs/installation.log
```

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## ⚡ Performance Considerations

### System Resource Requirements

KYGOX is designed to be resource-efficient while handling large-scale package installations. Typical resource usage includes moderate CPU utilization during package compilation, network bandwidth dependent on selected packages, and storage requirements varying from 2GB for standard tools to 50GB+ for complete BlackArch installation.

### Optimization Strategies

The installer implements several performance optimizations including parallel package processing where safe, intelligent package ordering to minimize conflicts, efficient cache management to reduce download times, and progressive installation with checkpoint recovery to handle interruptions gracefully.

### Hardware Recommendations

For optimal performance, consider systems with SSD storage for faster package extraction, adequate RAM (8GB+) for compilation processes, reliable internet connection for package downloads, and sufficient disk space with 20% overhead for temporary files and logs.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 🛡️ Security Considerations

KYGOX implements several security measures to ensure safe installation of security tools. Package authenticity verification uses GPG signature checking, secure repository configuration, and checksum validation. The installer maintains proper privilege separation with user context preservation for AUR builds, minimal root privilege usage, and secure temporary file handling.

System integrity protection includes configuration backup before modifications, atomic operations where possible, and rollback capabilities for critical changes. The installer also provides audit trails with comprehensive logging, package installation tracking, and modification timestamps for compliance requirements.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 🔄 Updates & Maintenance

KYGOX is designed for easy maintenance and updates. The installer checks for repository updates, handles package database synchronization, and provides mechanisms for updating installed security tools.

For keeping your security toolkit current, regularly run system updates, monitor the KYGOX repository for new releases, and review security tool changelogs for important updates that may affect your testing procedures.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## ⚠️ Important Notices

**System Modification Warning**: KYGOX makes significant system modifications including repository additions, kernel installations, and extensive package deployments. Always ensure you have proper backups before installation.

**Security Tool Responsibility**: The tools installed by KYGOX are powerful security testing utilities. Users are responsible for ensuring all usage complies with applicable laws, regulations, and organizational policies.

**Production System Caution**: While KYGOX is stable and well-tested, consider the impact of installing hundreds of security tools on production systems. Testing in isolated environments is recommended.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 📜 License & Legal

KYGOX is released under the MIT License, providing flexibility for both personal and commercial use while maintaining open source principles.

The installer respects the licenses of all installed packages and provides mechanisms to review license information for compliance purposes.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 🤝 Contributing & Support

### Community Support

- **GitHub Issues**: Report bugs, request features, or ask questions
- **Documentation**: Comprehensive guides and troubleshooting resources
- **Community**: Join discussions about security testing and tool deployment

### Development Contributions

KYGOX welcomes contributions including bug fixes, feature enhancements, documentation improvements, and testing on additional Arch-based distributions.

### Professional Support

For enterprise deployments or custom requirements, contact the development team through the GitHub repository for professional consulting and support services.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 📬 Contact Information

- **Primary Developer**: 0xb0rn3
- **GitHub Repository**: [github.com/0xb0rn3/kygox](https://github.com/0xb0rn3/kygox)
- **Instagram**: @theehiv3
- **Issue Reporting**: Use GitHub Issues for bug reports and feature requests

<div align="center">
  <sub>🔒 Engineered with precision by 0xb0rn3 | Empowering security professionals worldwide</sub>
</div>
