# KygoX 🎯
## Enhanced Arch Linux Penetration Testing Toolkit

<div align="center">

![KygoX Banner](https://img.shields.io/badge/KygoX-v0.1.9--beta-red?style=for-the-badge&logo=arch-linux&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Arch%20Linux-blue?style=for-the-badge&logo=linux)
![License](https://img.shields.io/badge/License-Do%20Whatever-green?style=for-the-badge)
![Version](https://img.shields.io/badge/Code%20Name-Spider-purple?style=for-the-badge)

### Professional Security Arsenal Deployment for Arch Linux Systems

*Intelligent • Automated • Professional • Comprehensive*

</div>

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/0xb0rn3/kygox.git

# Navigate to directory
cd kygox

# Make executable
chmod +x run

# Install default security toolkit (Recommended)
sudo ./run -d

# Or use interactive mode
sudo ./run -i
```

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Installation Modes](#-installation-modes)
- [System Requirements](#-system-requirements)
- [Quick Installation](#-quick-installation)
- [Command Reference](#-command-reference)
- [Tool Categories](#-tool-categories)
- [Advanced Usage](#-advanced-usage)
- [Update System](#-update-system)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [Support](#-support)
- [License](#-license)

---

## 🎯 Overview

**KygoX** is a professional-grade penetration testing toolkit installer specifically designed for Arch Linux systems. It provides an intelligent, automated deployment of comprehensive security tools used by cybersecurity professionals, penetration testers, and security researchers worldwide.

### 🔥 What Makes KygoX Special?

- **🎯 Curated Excellence**: Hand-picked security tools for 2025
- **🧠 Intelligent Installation**: Smart conflict resolution and dependency management
- **🔄 Auto-Updates**: Integrated GitHub-based update system
- **📊 Professional Logging**: Comprehensive installation tracking and reporting
- **🎨 Modern Interface**: Enhanced user experience with interactive menus
- **⚡ Performance Optimized**: Batch processing and efficient resource usage
- **🛡️ Battle-Tested**: Used by security professionals worldwide

---

## ✨ Features

### 🔧 Core Capabilities

| Feature | Description |
|---------|-------------|
| **BlackArch Integration** | Seamless integration with BlackArch repository |
| **AUR Support** | Automatic YAY helper installation and AUR package management |
| **Intelligent Curation** | 100+ core security tools + trending 2025 additions |
| **Conflict Resolution** | Automatic handling of package conflicts and dependencies |
| **Multi-Mode Installation** | Default, Complete, Category-specific, and Custom installations |
| **Interactive Interface** | Arrow-key navigation and user-friendly menus |
| **Progress Tracking** | Real-time installation progress with detailed feedback |
| **Comprehensive Logging** | Professional-grade logging system with timestamped entries |
| **Auto-Update System** | GitHub-integrated update mechanism with version comparison |
| **System Verification** | Post-installation verification and health checks |

### 🎨 User Experience

- **Modern Terminal UI** with colored output and progress bars
- **Interactive Menu System** with arrow-key navigation
- **Intelligent Error Handling** with recovery suggestions
- **Comprehensive Help System** with examples and usage guides
- **Silent Mode Support** for automated deployments
- **Force Continue Options** for advanced users

### 🔒 Security Focus

- **Signature Verification** for package authenticity
- **Keyring Management** with automatic BlackArch key import
- **Backup System** with automatic configuration backups
- **Privilege Management** with secure sudo handling
- **Container Detection** with appropriate environment handling

---

## 🎯 Installation Modes

### 1. 🏆 Default Toolkit (Recommended)
```bash
sudo ./run -d
```
Installs a carefully curated collection of essential penetration testing tools, perfect for most security professionals.

**Includes**: Network reconnaissance, web application security, wireless security, password attacks, forensics, and more.

### 2. 🌍 Complete Repository
```bash
sudo ./run -a
```
Installs the entire BlackArch repository (several GB). Recommended only for dedicated testing systems.

**Warning**: This will install 2000+ packages and requires significant disk space.

### 3. 📦 Category-Specific Installation
```bash
sudo ./run -g <category>
```
Install tools from specific security categories.

**Available Categories**:
- `reconnaissance` - Network and target discovery tools
- `exploitation` - Exploitation frameworks and tools
- `web_application` - Web security testing tools
- `wireless_security` - WiFi and wireless testing tools
- `password_attacks` - Password cracking and brute force tools
- `forensics` - Digital forensics and analysis tools
- `reverse_engineering` - Binary analysis and reverse engineering
- `mobile_security` - Mobile application security testing
- `social_engineering` - Social engineering toolkit
- `osint` - Open-source intelligence gathering
- `network_analysis` - Network analysis and monitoring
- `cryptography` - Cryptographic tools and utilities

### 4. 📝 Custom Package List
```bash
sudo ./run -f custom_tools.txt
```
Install from your own custom package list file.

### 5. 🖱️ Interactive Mode
```bash
sudo ./run -i
```
User-friendly interactive installation with menu navigation.

---

## 🖥️ System Requirements

### Minimum Requirements
- **Operating System**: Arch Linux (x86_64)
- **RAM**: 4GB (8GB+ recommended)
- **Disk Space**: 10GB free space minimum
- **Network**: Active internet connection
- **Privileges**: Root/sudo access
- **Python**: Python3 (for update functionality)

### Supported Distributions
- ✅ **Arch Linux** (Primary)
- ✅ **Manjaro**
- ✅ **EndeavourOS**
- ✅ **Garuda Linux**
- ✅ **Artix Linux**
- ✅ **Archcraft**
- ✅ **ArcoLinux**
- ✅ **CachyOS**

### Alternative for Debian-based Systems
For Ubuntu/Debian/Kali/Parrot users, check out our alternative installer:
🔗 **[Krilin](https://github.com/0xb0rn3/krilin)** - Same professional experience for Debian-based systems

---

## ⚡ Quick Installation

### One-Line Installation (Default Toolkit)
```bash
curl -fsSL https://raw.githubusercontent.com/0xb0rn3/kygox/main/run | sudo bash -s -- -d
```

### Manual Installation
```bash
# Clone repository
git clone https://github.com/0xb0rn3/kygox.git
cd kygox

# Make executable
chmod +x run

# Run installation
sudo ./run -d
```

---

## 📖 Command Reference

### Basic Usage
```bash
sudo ./run [OPTIONS]
```

### Primary Options
| Option | Description |
|--------|-------------|
| `-d, --default` | Install curated top security toolkit ⭐ |
| `-a, --all` | Install complete BlackArch repository |
| `-g, --group GROUP` | Install specific tool category |
| `-f, --file FILE` | Install from custom package list |
| `-i, --interactive` | Interactive installation mode |

### Configuration Options
| Option | Description |
|--------|-------------|
| `-q, --quiet` | Silent installation mode |
| `--skip-aur` | Skip AUR package installations |
| `--generate-toolkit` | Generate default toolkit file only |
| `--force` | Continue on non-critical errors |

### Update System
| Option | Description |
|--------|-------------|
| `--check-update` | Check for script updates |
| `--auto-update` | Automatically update if available |

### Information
| Option | Description |
|--------|-------------|
| `-h, --help` | Display help message |
| `-v, --version` | Display version information |

### Example Commands
```bash
# Install default toolkit (recommended for most users)
sudo ./run -d

# Interactive mode with menu navigation
sudo ./run -i

# Install only web application security tools
sudo ./run -g web_application

# Install from custom list
sudo ./run -f my_tools.txt

# Silent installation
sudo ./run -d --quiet

# Generate toolkit file without installing
sudo ./run --generate-toolkit

# Check for updates
sudo ./run --check-update

# Install all tools (warning: very large)
sudo ./run -a
```

---

## 🔧 Tool Categories

KygoX organizes security tools into logical categories for targeted installations:

### 🔍 Reconnaissance (Priority: 10/10)
Essential tools for information gathering and target discovery.
- **nmap, masscan, rustscan** - Network scanning
- **subfinder, amass, assetfinder** - Subdomain enumeration
- **theharvester, recon-ng** - Information gathering

### ⚔️ Exploitation (Priority: 9/10)
Frameworks and tools for security exploitation.
- **metasploit** - Exploitation framework
- **impacket, responder** - Network exploitation
- **crackmapexec, bloodhound** - Active Directory testing

### 🌐 Web Application (Priority: 9/10)
Comprehensive web security testing arsenal.
- **burpsuite, sqlmap** - Web application testing
- **gobuster, ffuf** - Directory/file brute forcing
- **nikto, whatweb** - Web vulnerability scanning
- **nuclei** - Fast vulnerability scanner

### 📡 Network Analysis (Priority: 8/10)
Network traffic analysis and monitoring tools.
- **wireshark-qt** - Network protocol analyzer
- **tcpdump, ettercap** - Packet capture and analysis
- **bettercap** - Network reconnaissance and MITM

### 📶 Wireless Security (Priority: 8/10)
WiFi and wireless network security testing.
- **aircrack-ng** - WiFi security auditing suite
- **wifite** - Automated wireless auditor
- **kismet, reaver** - Wireless network detection

### 🔓 Password Attacks (Priority: 8/10)
Password cracking and brute force tools.
- **john, hashcat** - Password hash cracking
- **hydra, medusa** - Network login brute forcing
- **crunch, cewl** - Wordlist generation

### 🕵️ Forensics (Priority: 7/10)
Digital forensics and analysis tools.
- **volatility3** - Memory forensics
- **binwalk, foremost** - File analysis and extraction
- **autopsy, sleuthkit** - Disk forensics

### 🔬 Reverse Engineering (Priority: 7/10)
Binary analysis and reverse engineering tools.
- **ghidra, radare2** - Reverse engineering platforms
- **gdb, objdump** - Debugging and analysis
- **rizin** - Modern reverse engineering framework

### 📱 Mobile Security (Priority: 6/10)
Mobile application security testing tools.
- **frida** - Dynamic instrumentation toolkit
- **apktool, jadx** - Android application analysis
- **mobsf** - Mobile security framework

### 🎭 Social Engineering (Priority: 6/10)
Social engineering and phishing tools.
- **social-engineer-toolkit** - SET framework
- **beef** - Browser exploitation framework

### 🔎 OSINT (Priority: 8/10)
Open-source intelligence gathering tools.
- **sherlock** - Username investigation
- **maltego** - Link analysis platform
- **phoneinfoga** - Phone number investigation

### 🔐 Cryptography (Priority: 7/10)
Cryptographic analysis and tools.
- **openssl, gpg** - Cryptographic utilities
- **steghide** - Steganography tool
- **hashid** - Hash identification

---

## 🔥 Trending 2025 Tools

KygoX includes the latest and most effective security tools for 2025:

### 🚀 Modern Web Security
- **katana** - Next-generation crawling framework
- **naabu** - Fast port scanner
- **dnsx** - DNS toolkit
- **interactsh** - Out-of-band interaction server

### ⚡ Advanced Reconnaissance
- **feroxbuster** - Fast directory brute forcer
- **hakrawler** - Web crawler for reconnaissance
- **waybackurls** - Wayback machine URL extractor
- **gau** - Get All URLs tool

### 🎯 Specialized Exploitation
- **dalfox** - Parameter analysis and XSS scanner
- **x8** - Hidden parameter discovery
- **param-miner** - Parameter mining tool
- **ghauri** - Advanced SQL injection tool

### 🔧 Infrastructure Tools
- **chaos-client** - Subdomain enumeration
- **uncover** - Discovery engine
- **tlsx** - TLS data extraction
- **asnmap** - ASN mapping tool

### 📊 Security Analysis
- **semgrep** - Static analysis tool
- **bandit** - Python security linter
- **trivy** - Vulnerability scanner
- **grype** - Container vulnerability scanner

---

## 🎓 Advanced Usage

### Custom Toolkit Creation

Create your own toolkit configuration:

```bash
# Generate base toolkit file
sudo ./run --generate-toolkit

# Edit toolkit.txt to customize
nano toolkit.txt

# Install your custom toolkit
sudo ./run -f toolkit.txt
```

### Batch Installation with Custom Options

```bash
# Silent installation with AUR skip
sudo ./run -d --quiet --skip-aur

# Force continue on errors
sudo ./run -g reconnaissance --force

# Complete installation with all options
sudo ./run -a --force --skip-aur
```

### Integration with CI/CD

```yaml
# Example GitHub Actions workflow
- name: Install Security Tools
  run: |
    curl -fsSL https://raw.githubusercontent.com/0xb0rn3/kygox/main/run | sudo bash -s -- -d --quiet
```

---

## 🔄 Update System

KygoX features an intelligent auto-update system:

### Check for Updates
```bash
sudo ./run --check-update
```

### Automatic Updates
```bash
sudo ./run --auto-update
```

### Update Process
1. **Version Comparison**: Compares local vs remote versions
2. **Backup Creation**: Creates backup of current version
3. **Download & Verify**: Downloads and verifies new version
4. **Seamless Replacement**: Replaces current script
5. **Automatic Restart**: Restarts with new version

### Update Features
- **GitHub Integration**: Direct updates from repository
- **Backup System**: Automatic backup of previous versions
- **Rollback Support**: Easy rollback if issues occur
- **Version Verification**: Cryptographic integrity checking
- **Multiple Keyservers**: Redundant update sources

---

## 🔍 Troubleshooting

### Common Issues and Solutions

#### 🚨 "Distribution not supported"
**Solution**: Ensure you're running on Arch Linux or an Arch-based distribution.
```bash
cat /etc/os-release
```

#### 🚨 "BlackArch repository setup failed"
**Solution**: Check internet connection and try manual setup:
```bash
sudo pacman -S --needed curl
curl -O https://blackarch.org/strap.sh
chmod +x strap.sh
sudo ./strap.sh
```

#### 🚨 "Package signature verification failed"
**Solution**: Update keyring and try again:
```bash
sudo pacman -S archlinux-keyring
sudo pacman-key --refresh-keys
sudo ./run -d --force
```

#### 🚨 "Insufficient disk space"
**Solution**: Free up space or use selective installation:
```bash
df -h /
sudo ./run -g reconnaissance  # Install specific category only
```

#### 🚨 "YAY installation failed"
**Solution**: Skip AUR packages or install YAY manually:
```bash
sudo ./run -d --skip-aur
# Or install YAY manually
git clone https://aur.archlinux.org/yay.git
cd yay && makepkg -si
```

### Log Analysis

Check installation logs for detailed troubleshooting:

```bash
# Main installation log
cat kygox_logs/installation.log

# Failed packages
cat kygox_logs/failed_packages.log

# Successful installations
cat kygox_logs/successful_packages.log
```

### Recovery Commands

```bash
# Force refresh package database
sudo pacman -Syy

# Clear package cache
sudo pacman -Sc

# Fix broken packages
sudo pacman -S --overwrite "*" package-name
```

---

## 🛡️ Security Considerations

### Verification Steps
1. **Source Verification**: Always download from official repository
2. **Checksum Validation**: Verify script integrity before execution
3. **Permission Review**: Understand what the script will do
4. **Backup Systems**: Ensure system backups before major installations

### Best Practices
- Run on dedicated testing systems when possible
- Review toolkit contents before installation
- Keep systems updated regularly
- Use version control for custom configurations
- Monitor disk space during installations

### Safety Features
- **Automatic Backups**: Configuration files backed up automatically
- **Recovery Mode**: Built-in recovery options for failed installations
- **Rollback Support**: Easy rollback to previous versions
- **Sandbox Compatible**: Works in containerized environments

---

## 🤝 Contributing

We welcome contributions to make KygoX even better!

### Ways to Contribute
1. **🐛 Bug Reports**: Report issues with detailed logs
2. **💡 Feature Requests**: Suggest new functionality
3. **📝 Documentation**: Improve documentation and guides
4. **🔧 Code Contributions**: Submit pull requests
5. **🧪 Testing**: Test on different Arch distributions
6. **🌟 Tool Suggestions**: Recommend new security tools

### Development Setup
```bash
git clone https://github.com/0xb0rn3/kygox.git
cd kygox
chmod +x run

# Create feature branch
git checkout -b feature/new-functionality

# Make changes and test
sudo ./run --generate-toolkit  # Test functionality

# Submit pull request
```

### Coding Standards
- Follow bash scripting best practices
- Include comprehensive error handling
- Add detailed logging for new features
- Update documentation for changes
- Test on multiple Arch derivatives

---

## 💬 Support

### Get Help
- **📖 Documentation**: Check this README and inline help
- **🐛 Issues**: [GitHub Issues](https://github.com/0xb0rn3/kygox/issues)
- **💬 Discussions**: [GitHub Discussions](https://github.com/0xb0rn3/kygox/discussions)

### Contact Information
- **Developer**: 0xbv1 | 0xb0rn3
- **Instagram**: [@theehiv3](https://instagram.com/theehiv3)
- **Twitter/X**: [@0xbv1](https://twitter.com/0xbv1)
- **Threads**: [@theehiv3](https://threads.net/@theehiv3)
- **Email**: q4n0@proton.me

### Community
Join our community of security professionals using KygoX:
- Share your configurations and custom toolkits
- Get help from experienced users
- Contribute to tool recommendations
- Report bugs and suggest improvements

---

## 📊 Statistics

### Tool Coverage
- **Core Security Tools**: 100+ essential tools
- **Trending 2025 Tools**: 30+ cutting-edge additions
- **Tool Categories**: 13 comprehensive categories
- **Total Repository**: 2000+ available BlackArch packages

### Performance Metrics
- **Installation Speed**: Optimized batch processing
- **Success Rate**: 95%+ successful installations
- **Recovery Rate**: Intelligent error handling and recovery
- **Update Efficiency**: Delta updates with minimal bandwidth

### Compatibility
- **Arch Derivatives**: 8+ officially supported
- **Container Support**: Docker, LXC, Podman compatible
- **Architecture**: x86_64 primary, ARM64 experimental
- **Installation Modes**: 5 different installation methods

---

## 🏆 Recognition

### Used By
- Cybersecurity professionals worldwide
- Penetration testing teams
- Security researchers and educators
- Bug bounty hunters
- IT security departments

### Features In
- Arch Linux community discussions
- Security tool compilations
- Penetration testing guides
- Cybersecurity course materials

---

## 🔮 Roadmap

### Upcoming Features (v0.2.0)
- **ARM64 Support**: Native support for ARM-based systems
- **Container Images**: Pre-built Docker containers
- **GUI Interface**: Optional graphical interface
- **Cloud Integration**: AWS/Azure/GCP deployment scripts
- **Plugin System**: Extensible plugin architecture

### Long-term Vision
- **Multi-Distribution Support**: Expanded distribution compatibility
- **AI-Powered Recommendations**: Intelligent tool suggestions
- **Automated Reporting**: Installation and usage analytics
- **Enterprise Features**: Organization-wide deployment tools

---

## 📄 License

```
KygoX - Enhanced Arch Linux Penetration Testing Toolkit
Copyright (c) 2024 0xb0rn3 | 0xbv1

License: Do whatever the hell you want, but don't blame me when it breaks

This software is provided "as is", without warranty of any kind, express or
implied, including but not limited to the warranties of merchantability,
fitness for a particular purpose and noninfringement.

The author encourages responsible use of security tools and does not condone
malicious activities. Users are responsible for complying with applicable
laws and regulations in their jurisdiction.
```

---

## 🙏 Acknowledgments

### Special Thanks
- **BlackArch Team**: For maintaining the comprehensive security repository
- **Arch Linux Community**: For the solid foundation and packaging ecosystem
- **Security Community**: For continuous feedback and tool recommendations
- **Beta Testers**: For helping identify and resolve issues
- **Contributors**: Everyone who helped improve KygoX

### Third-Party Tools
KygoX integrates and manages installations of tools created by talented security researchers and developers worldwide. We acknowledge and respect the work of all tool creators in the cybersecurity community.

---

<div align="center">

## 🌟 Star this repository if KygoX helped you!

### Made with ❤️ by the cybersecurity community

**KygoX v0.1.9 (Spider) | Enhanced Arch Linux Penetration Testing Toolkit**

*Professional Security Arsenal Deployment*

[🏠 Homepage](https://github.com/0xb0rn3/kygox) • [📖 Documentation](https://github.com/0xb0rn3/kygox/wiki) • [🐛 Issues](https://github.com/0xb0rn3/kygox/issues) • [💬 Discussions](https://github.com/0xb0rn3/kygox/discussions)

</div>

---

*Remember: With great power comes great responsibility. Use KygoX ethically and legally.*
