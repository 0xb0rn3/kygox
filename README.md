# KygoX v0.1.9-alpha "Venom"

<div align="center">

```
██╗  ██╗██╗   ██╗ ██████╗  ██████╗ ██╗  ██╗
██║ ██╔╝╚██╗ ██╔╝██╔════╝ ██╔═══██╗╚██╗██╔╝
███████╔╝ ╚████╔╝ ██║  ███╗██║   ██║ ╚███╔╝ 
██╔══██╗   ╚██╔╝  ██║   ██║██║   ██║ ██╔██╗ 
██║  ██║   ██║   ╚██████╔╝╚██████╔╝██╔╝ ██╗
╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
```

**Professional Arch Linux Penetration Testing Toolkit**  
*Self-Healing • Signature Verified • Production Ready*

[![Version](https://img.shields.io/badge/version-0.1.9--alpha-blue.svg)](https://github.com/0xb0rn3/kygox)
[![License](https://img.shields.io/badge/license-DWYWDBMWIIB-red.svg)](#license)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://python.org)
[![Arch](https://img.shields.io/badge/distro-arch--based-1793d1.svg)](https://archlinux.org)

</div>

---

## 🎯 Overview

KygoX is a professional-grade penetration testing toolkit installer designed specifically for Arch Linux and Arch-based distributions. Built with Python 3, it provides a comprehensive, self-healing installation system for security tools with advanced features like signature verification, parallel installation, and database-driven package management.

### ✨ Key Features

- 🔧 **Self-Healing Architecture** - Automatic error recovery and retry mechanisms
- 🔒 **Security First** - BlackArch keyring integration with cryptographic verification
- 📦 **150+ Security Tools** - Curated collection of modern penetration testing tools
- ⚡ **Parallel Installation** - Multi-threaded package installation with progress tracking
- 🗄️ **Database-Driven** - SQLite-based package management and installation history
- 🎨 **Rich Interface** - Interactive menus with colorized output and progress bars
- 🔄 **Auto-Updates** - Built-in version checking and automatic updates
- 📊 **Comprehensive Logging** - Detailed logs with multiple output formats

---

## 🚀 Quick Start

### Prerequisites

- Arch Linux or Arch-based distribution (Manjaro, EndeavourOS, Garuda, etc.)
- Root privileges (sudo access)
- Internet connection
- Python 3.8+ (auto-installed if missing)

### Installation

```bash
# Clone the repository
git clone https://github.com/0xb0rn3/kygox.git
cd kygox

# Make the runner executable
chmod +x run

# Run with interactive mode (recommended for first use)
sudo ./run
```

### Quick Install Options

```bash
# Install core security toolkit (recommended)
sudo ./run && python3 .core.py --install core

# Install complete security arsenal
sudo ./run && python3 .core.py --install full

# Setup BlackArch repository and install all tools
sudo ./run && python3 .core.py --blackarch
```

---

## 📖 Usage

### Interactive Mode

Launch the interactive menu system:

```bash
sudo ./run
sudo ./run -q                    # Quick setup with recommended settings
sudo ./run --workers 4          # Set specific worker count
sudo ./run --core-only           # Core tools only
sudo ./run --trending-only       # Trending 2025 tools only
sudo ./run --log-level DEBUG     # Set logging level
sudo ./run --no-interactive      # Skip interactive mode
sudo ./run -h or ./run -h        # Toolkit usage help
```

The interactive mode provides:
- Guided toolkit selection
- Package search and discovery
- System information display
- Update management
- Real-time installation progress

### Command Line Interface

Once the environment is setup, use the Python core directly:

```bash
# Install specific toolkits
python3 .core.py --install core      # Essential security tools
python3 .core.py --install web       # Web application security
python3 .core.py --install network   # Network penetration testing
python3 .core.py --install wireless  # WiFi security tools
python3 .core.py --install forensics # Digital forensics
python3 .core.py --install mobile    # Mobile security testing

# Package management
python3 .core.py --search nmap       # Search for packages
python3 .core.py --list              # List available toolkits
python3 .core.py --from-file tools.txt  # Install from custom file

# System operations
python3 .core.py --update            # Check for updates
python3 .core.py --refresh           # Refresh package database
python3 .core.py --info              # Show system information
```

### Advanced Options

```bash
# Installation behavior
python3 .core.py --install core --no-verify    # Skip signature verification
python3 .core.py --install full --parallel 5   # Use 5 parallel workers
python3 .core.py --install web --quiet         # Minimal output
python3 .core.py --install network --force     # Continue on errors

# BlackArch integration
python3 .core.py --blackarch                   # Full BlackArch setup
```

---

## 🛠️ Security Toolkits

### Core Toolkit (50 packages)
Essential penetration testing tools for most security assessments.

**Categories Include:**
- Network scanning (nmap, masscan, rustscan)
- Web application testing (burpsuite, owasp-zap, sqlmap)
- Password attacks (john, hashcat, hydra)
- Wireless security (aircrack-ng, wifite, kismet)
- Digital forensics (volatility3, autopsy, binwalk)

### Full Arsenal (150+ packages)
Complete security toolkit with modern 2025 tools.

**Additional Categories:**
- Advanced OSINT tools
- Container & cloud security
- AI/ML security testing
- Blockchain security analysis
- Modern C2 frameworks
- DevSecOps integration tools

### Specialized Toolkits

| Toolkit | Description | Package Count |
|---------|-------------|---------------|
| **Web** | Web application penetration testing | ~20 packages |
| **Network** | Network security and analysis | ~15 packages |
| **Wireless** | WiFi and wireless security testing | ~12 packages |
| **Forensics** | Digital forensics and incident response | ~18 packages |
| **Mobile** | Android and iOS security testing | ~14 packages |
| **BlackArch** | Complete BlackArch repository access | 2000+ packages |

---

## 🏗️ Architecture

### File Structure

```
kygox/
├── run                    # Bash runner and environment setup
├── .core.py              # Hidden Python engine (main application)
├── toolkit.txt           # Default toolkit configuration
├── kygox_logs/           # Installation logs and history
│   ├── installation.log  # Main installation log
│   ├── successful_packages.log
│   ├── failed_packages.log
│   └── backups/          # Configuration backups
└── .kygox_cache/         # Cache and database files
    ├── packages.db       # SQLite package database
    └── downloads/        # Downloaded files
```

### Core Components

- **SystemInfo** - Distribution detection and compatibility checking
- **PackageDatabase** - SQLite-based package management with history tracking
- **KeyringManager** - BlackArch keyring setup and signature verification
- **PackageManager** - Parallel installation with comprehensive error handling
- **ToolkitManager** - Multiple security toolkit configurations and management
- **UpdateManager** - Automatic script updates and version management
- **ColorManager** - Rich terminal output with progress visualization

### Security Features

- **Signature Verification** - Cryptographic package validation using BlackArch keyring
- **Repository Integrity** - Automatic verification of package sources and mirrors
- **Secure Downloads** - HTTPS-only downloads with certificate validation
- **Permission Management** - Proper privilege escalation and user context preservation
- **Audit Trail** - Complete installation history with forensic-level logging

---

## 🔧 Configuration

### Custom Package Lists

Create custom toolkit files:

```bash
# Create custom toolkit
cat > my_tools.txt << EOF
# Custom Security Tools
nmap
burpsuite
metasploit
wireshark-qt
ghidra
EOF

# Install custom toolkit
python3 .core.py --from-file my_tools.txt
```

### Environment Variables

```bash
export KYGOX_PARALLEL_JOBS=5        # Parallel installation workers
export KYGOX_VERIFY_SIGNATURES=true # Enable signature verification
export KYGOX_LOG_LEVEL=INFO         # Logging verbosity
```

### Database Queries

Access installation history:

```bash
sqlite3 .kygox_cache/packages.db "SELECT * FROM installation_history ORDER BY timestamp DESC LIMIT 10;"
```

---

## 📊 System Requirements

### Minimum Requirements
- **OS**: Arch Linux or Arch-based distribution
- **RAM**: 2GB (4GB+ recommended)
- **Storage**: 5GB free space (10GB+ for full arsenal)
- **Network**: Stable internet connection
- **Privileges**: Root access (sudo)

### Recommended Specifications
- **OS**: Latest Arch Linux with updated packages
- **RAM**: 8GB for optimal parallel installation
- **Storage**: 20GB+ for complete toolkit with cache
- **CPU**: Multi-core processor for parallel operations
- **Network**: High-speed connection for faster downloads

### Supported Distributions

| Distribution | Status | Notes |
|-------------|--------|-------|
| Arch Linux | ✅ Full Support | Primary target platform |
| Manjaro | ✅ Full Support | Tested and verified |
| EndeavourOS | ✅ Full Support | Community tested |
| Garuda Linux | ✅ Full Support | Gaming-focused Arch |
| ArcoLinux | ✅ Full Support | Educational Arch variant |
| Artix Linux | ✅ Partial Support | systemd-free Arch |
| BlackArch | ✅ Full Support | Security-focused Arch |
| Debian/Ubuntu | ❌ Use Alternative | See [krilin](https://github.com/0xb0rn3/krilin) |

---

## 🐛 Troubleshooting

### Common Issues

**Package Installation Fails**
```bash
# Refresh package databases
python3 .core.py --refresh

# Try with signature verification disabled
python3 .core.py --install core --no-verify

# Check logs for specific errors
tail -f kygox_logs/installation.log
```

**Permission Errors**
```bash
# Ensure running as root
sudo python3 .core.py --install core

# Check original user detection
echo $SUDO_USER
```

**Network Issues**
```bash
# Test connectivity
ping -c 3 archlinux.org

# Update mirrorlist
sudo pacman-mirrors --fasttrack

# Check DNS resolution
nslookup blackarch.org
```

**BlackArch Keyring Issues**
```bash
# Manually setup keyring
sudo pacman -S blackarch-keyring

# Import BlackArch keys
sudo pacman-key --populate blackarch
```

### Debug Mode

Enable verbose logging:

```bash
python3 .core.py --install core --verbose
```

### Log Analysis

Check installation logs:

```bash
# Main installation log
less kygox_logs/installation.log

# Failed packages only
cat kygox_logs/failed_packages.log

# Installation statistics
grep "SUCCESS\|ERROR" kygox_logs/installation.log | sort | uniq -c
```

---

## 🔄 Updates

### Automatic Updates

KygoX includes built-in update management:

```bash
# Check for updates
python3 .core.py --update

# Enable auto-update (interactive prompt)
python3 .core.py --interactive
```

### Manual Updates

```bash
# Pull latest changes
git pull origin main

# Re-run setup if needed
sudo ./run --setup
```

### Version History

- **v0.1.9-alpha "Venom"** - Complete Python rewrite with database integration
- **v0.1.8-beta** - Added BlackArch repository support
- **v0.1.7-beta** - Parallel installation and progress tracking
- **v0.1.6-alpha** - Initial Python conversion from bash

---

## 🤝 Contributing

### Development Setup

```bash
# Fork and clone
git clone https://github.com/yourusername/kygox.git
cd kygox

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python3 -m pytest tests/

# Code formatting
black .core.py
flake8 .core.py
```

### Adding New Tools

1. **Update tool lists** in `KygoXConfig.CORE_TOOLS` or `KygoXConfig.TRENDING_2025`
2. **Test installation** on clean Arch system
3. **Add categorization** in `PackageManager._categorize_package()`
4. **Update documentation** in README.md
5. **Submit pull request** with detailed description

### Reporting Issues

When reporting bugs, please include:

- System information (`python3 .core.py --info`)
- Error logs (`kygox_logs/installation.log`)
- Steps to reproduce
- Expected vs actual behavior

---

## 📄 License

**"Do Whatever You Want, But Don't Blame Me When It Breaks" (DWYWDBMWIIB)**

This software is provided as-is, without any warranty or guarantee. You are free to use, modify, and distribute this software for any purpose, including commercial use. However, the authors are not responsible for any damage, data loss, or other issues that may arise from using this software.

By using this software, you acknowledge that you understand the risks involved and accept full responsibility for any consequences.

---

## 👥 Credits

### Author
- **0xbv1** (0xb0rn3) - Lead Developer and Security Researcher

### Contact
- **Instagram**: [@theehiv3](https://instagram.com/theehiv3)
- **X/Twitter**: [@0xbv1](https://x.com/0xbv1)
- **Threads**: [@theehiv3](https://threads.net/@theehiv3)
- **Email**: q4n0@proton.me

### Acknowledgments
- Arch Linux community for the solid foundation
- BlackArch team for the comprehensive security repository
- Python community for the excellent libraries
- Security researchers and tool developers worldwide

---

## 🔗 Related Projects

- **[krilin](https://github.com/0xb0rn3/krilin)** - Debian/Ubuntu version of KygoX
- **[BlackArch](https://blackarch.org)** - Arch-based penetration testing distribution
- **[Arch Linux](https://archlinux.org)** - The base distribution

---

<div align="center">

**⭐ Star this repository if you find it useful!**

*Built with ❤️ for the cybersecurity community*

</div>
