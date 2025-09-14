# kygoX v0.2.0 "Phoenix"

<div align="center">

```
██╗  ██╗██╗   ██╗ ██████╗  ██████╗ ██╗  ██╗
██║ ██╔╝╚██╗ ██╔╝██╔════╝ ██╔═══██╗╚██╗██╔╝
█████╔╝  ╚████╔╝ ██║  ███╗██║   ██║ ╚███╔╝ 
██╔═██╗   ╚██╔╝  ██║   ██║██║   ██║ ██╔██╗ 
██║  ██╗   ██║   ╚██████╔╝╚██████╔╝██╔╝ ██╗
╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
```

**Professional Arch Linux Security Testing Suite**  
*Dynamic • Intelligent • Reliable*

[![Version](https://img.shields.io/badge/version-0.2.0--phoenix-orange.svg)](https://github.com/0xb0rn3/kygox)
[![License](https://img.shields.io/badge/license-WTFPL-red.svg)](#license)
[![Architecture](https://img.shields.io/badge/architecture-bash--python-blue.svg)](https://github.com/0xb0rn3/kygox)
[![Platform](https://img.shields.io/badge/platform-arch--linux-1793d1.svg)](https://archlinux.org)

</div>

---

## Advanced Security Arsenal Management

kygoX v0.2.0 represents a complete architectural transformation, introducing dynamic repository analysis, intelligent tool categorization, and enterprise-grade reliability for Arch Linux security professionals. This version eliminates complexity while maximizing functionality through streamlined bash operations and targeted Python intelligence.

### Revolutionary Features

**Dynamic Tool Discovery**: Real-time scanning of security repositories provides live counts of available tools across all categories, ensuring users always see current arsenal capabilities.

**Intelligent Category Analysis**: When selecting categories, kygoX performs live analysis to show exactly how many tools are available, their installation status, and detailed package information before installation begins.

**Streamlined Architecture**: Bash handles all system operations and package management for maximum reliability, while Python provides sophisticated error monitoring and repository analysis only where needed.

---

## Core Capabilities

### Dynamic Repository Intelligence
- **Live Tool Counting**: Dashboard displays total available security tools in real-time
- **Category-Specific Analysis**: Deep scanning shows exact tool counts per category
- **Installation Status Tracking**: Pre-installation validation shows what's already installed
- **Repository Health Monitoring**: Continuous validation of repository accessibility and integrity

### Professional Installation Engine
- **Sequential Processing**: Reliable single-threaded installation with comprehensive error handling
- **Intelligent Retry Logic**: Automatic recovery from common installation failures
- **Real-time Monitoring**: Python-based process monitoring detects and resolves errors during installation
- **Auto-fixing Capabilities**: Automatic resolution of lock files, cache issues, and database problems

### Enterprise User Experience
- **Interactive Dashboard**: Live statistics and tool availability information
- **Category Preview System**: See exactly what tools are available before installing
- **Comprehensive Logging**: Detailed operation tracking with multiple verbosity levels
- **Graceful Error Handling**: Intelligent recovery from network, repository, and system issues

---

## Quick Start Guide

### Prerequisites
- Arch Linux or Arch-based distribution (Manjaro, EndeavourOS, Garuda, etc.)
- Root privileges (sudo access)
- Internet connectivity for repository access
- Minimum 5GB free disk space (20GB+ recommended for comprehensive installations)

### Installation

```bash
# Clone the repository
git clone https://github.com/0xb0rn3/kygox.git
cd kygox

# Make executable and run
chmod +x kygox
sudo ./kygox
```

kygoX automatically handles all setup requirements including dependency installation, repository configuration, and security tool database initialization.

### Command Line Options

```bash
# Standard interactive mode
sudo ./kygox

# Verbose output for troubleshooting
sudo ./kygox --verbose

# Preview mode - see what would be installed
sudo ./kygox --dry-run

# Update repository database
sudo ./kygox --update-db

# Disable automatic error fixing
sudo ./kygox --no-auto-fix
```

---

## Security Tool Arsenal

### Dynamic Category System

kygoX organizes security tools into eight comprehensive categories, each with live tool counting and availability analysis:

| Category | Focus Area | Typical Tools |
|----------|------------|---------------|
| **Information Gathering** | Network reconnaissance, OSINT | nmap, masscan, rustscan, dnsrecon, theharvester |
| **Vulnerability Analysis** | Security assessment, scanning | nikto, dirb, gobuster, sqlmap, lynis |
| **Web Application Analysis** | Web security testing | burpsuite, zaproxy, w3af, arachni |
| **Password Attacks** | Authentication testing | john, hashcat, hydra, medusa, crunch |
| **Wireless Attacks** | WiFi and wireless security | aircrack-ng, wifite, reaver, kismet |
| **Exploitation Tools** | Penetration testing frameworks | metasploit, exploitdb, set, beef |
| **Digital Forensics** | Forensics and incident response | autopsy, volatility, binwalk, sleuthkit |
| **Sniffing & Spoofing** | Network monitoring, manipulation | wireshark, ettercap, responder, mitmproxy |

### Category Analysis Example

When you select a category, kygoX provides detailed analysis:

```
Analyzing Information Gathering Tools...
✓ Found 312 tools in Information Gathering category

Available tools (showing first 20):
• nmap (available)
• masscan (available) 
• rustscan (available)
✓ dnsrecon (installed)
... and 292 more tools

Proceed with installation of this category? [Y/n]:
```

---

## Advanced Usage

### Interactive Dashboard

The main dashboard shows live repository statistics:

```
📊 Security Arsenal Dashboard: 2847 tools available

System Information:
• OS: Arch Linux
• Kernel: 6.1.0-arch1-1
• Available Security Tools: 2847
```

### Custom Package Selection

Expert users can select specific tools:

```bash
# Select option 9 for custom selection
# Example input: nmap nikto sqlmap burpsuite metasploit
```

### Category-Specific Installation

Preview any category before installation:

1. Select category (1-8)
2. View analysis of available tools
3. See installation status for each tool
4. Choose to proceed or return to menu

---

## Technical Architecture

### Streamlined Design Philosophy

kygoX v0.2.0 employs a focused architecture approach:

**Bash Core Engine**: All system operations, package management, and repository interactions use native bash commands for maximum reliability and compatibility with Arch systems.

**Targeted Python Intelligence**: Python components handle only specific tasks requiring advanced processing - error monitoring during installations and repository analysis for tool categorization.

**Direct Repository Integration**: Uses native pacman commands for all package operations, eliminating external dependencies and improving reliability.

### Error Handling System

The Python error monitoring system provides sophisticated installation oversight:

- **Real-time Process Monitoring**: Watches pacman output during installations
- **Pattern Recognition**: Detects common failure scenarios and suggests fixes
- **Automatic Recovery**: Applies fixes for lock files, cache issues, and database problems
- **Intelligent Retry Logic**: Implements progressive retry strategies with different approaches

### Security Repository Integration

kygoX integrates seamlessly with security tool repositories:

- **Dynamic Discovery**: Live scanning of available packages and categories
- **Intelligent Categorization**: Keyword-based tool classification
- **Repository Health Checks**: Continuous validation of repository accessibility
- **Package Verification**: Pre-installation validation prevents failed operations

---

## System Requirements

### Minimum Specifications
- **OS**: Arch Linux or compatible distribution
- **RAM**: 2GB (4GB+ recommended for large installations)
- **Storage**: 5GB free space (20GB+ for comprehensive toolkit)
- **Network**: Stable internet connection for repository access
- **Privileges**: Root access via sudo

### Recommended Setup
- **OS**: Latest Arch Linux with updated packages
- **RAM**: 8GB for optimal performance during installations
- **Storage**: 50GB+ for complete security testing environment
- **Network**: High-speed connection for faster downloads
- **CPU**: Multi-core processor for better compilation performance

### Supported Distributions

| Distribution | Status | Notes |
|-------------|--------|-------|
| Arch Linux | ✅ Full Support | Primary development platform |
| Manjaro | ✅ Full Support | Extensively tested |
| EndeavourOS | ✅ Full Support | Community verified |
| Garuda Linux | ✅ Full Support | Gaming-focused Arch variant |
| ArcoLinux | ✅ Full Support | Educational Arch distribution |
| Artix Linux | ⚠️ Partial Support | systemd-free Arch variant |
| Other Arch-based | ✅ Likely Compatible | May require minor adjustments |
| Debian/Ubuntu | ❌ Not Supported | Use [KRILIN](https://github.com/0xb0rn3/krilin) instead |

---

## Troubleshooting

### Common Issues

**Repository Access Problems**
```bash
# Test connectivity
ping -c 3 archlinux.org

# Update mirror list
sudo pacman-mirrors --fasttrack

# Manual repository update
sudo ./kygox --update-db
```

**Package Installation Failures**
```bash
# Check system status
sudo pacman -Syu

# Verify disk space
df -h /

# Review detailed logs
tail -f ~/.kygox/kygox.log
```

**Permission or Lock Issues**
```bash
# Remove pacman lock files
sudo rm -f /var/lib/pacman/db.lck

# Kill hanging processes
sudo pkill -f pacman

# Restart kygoX
sudo ./kygox
```

### Debug Mode

Enable comprehensive logging:

```bash
sudo ./kygox --verbose
```

This provides detailed information about:
- Repository scanning operations
- Package availability checks
- Installation progress and errors
- System state changes

### Log Analysis

kygoX maintains detailed logs for troubleshooting:

```bash
# Main operation log
cat ~/.kygox/kygox.log

# Installation monitoring
tail -f ~/.kygox/kygox.log

# System status check
sudo ./kygox --update-db
```

---

## Development

### Architecture Overview

The simplified architecture makes contributions straightforward:

**Bash Components**:
- Main application logic and user interface
- All pacman operations and system integration
- Category definitions and tool management
- Command-line argument processing

**Python Components**:
- Installation error monitoring (`error_handler.py`)
- Repository analysis tools (`tool_analyzer.py`)
- Package categorization algorithms

### Contributing Guidelines

1. **Test on Clean Systems**: Verify functionality on fresh Arch installations
2. **Follow Bash Best Practices**: Use proper error handling and quoting
3. **Document Changes**: Update help text and comments for new features
4. **Maintain Compatibility**: Ensure changes work across supported distributions

### Enhancement Opportunities

- **Additional Categories**: Expand tool categorization schemes
- **Performance Optimization**: Improve large-scale installation efficiency
- **Integration Features**: Add support for automated deployment scenarios
- **Monitoring Enhancements**: Expand system health checking capabilities

---

## Support and Community

### Getting Help

- **Documentation**: Comprehensive help available via `sudo ./kygox --help`
- **Logs**: Detailed troubleshooting information in `~/.kygox/kygox.log`
- **Issues**: Report bugs and request features on GitHub

### Community Resources

- **Repository**: [https://github.com/0xb0rn3/kygox](https://github.com/0xb0rn3/kygox)
- **Issue Tracker**: GitHub Issues for bug reports and feature requests
- **Discussions**: Community engagement through GitHub Discussions

### Contact Information

- **Developer**: 0xb0rn3 (0xbv1)
- **Email**: q4n0@proton.me
- **Social Media**: [@theehiv3](https://instagram.com/theehiv3) | [@0xbv1](https://x.com/0xbv1)

---

## Legal Information

### License

This software is released under the **WTFPL (Do What The F*ck You Want To Public License)**. Users may use, modify, and distribute this software for any purpose without restriction.

### Disclaimer

This software is provided without warranty. Users assume full responsibility for compliance with applicable laws and regulations when using security testing tools. kygoX is intended for authorized security testing and educational purposes only.

### Ethical Use

Security tools included in kygoX are powerful instruments that should be used responsibly:

- Obtain proper authorization before testing systems
- Respect privacy and confidentiality requirements  
- Follow applicable laws and regulations
- Use tools only for legitimate security purposes

---

## Related Projects

- **[KRILIN](https://github.com/0xb0rn3/krilin)** - Debian/Ubuntu security toolkit installer
- **[Arch Linux](https://archlinux.org)** - The foundation distribution
- **[Security Tool Repositories](https://github.com/topics/security-tools)** - Additional security resources

---

<div align="center">

**Transform Your Arch System Into a Professional Security Platform**

*kygoX v0.2.0 Phoenix - Simplified Excellence in Security Tool Management*

⭐ **Star this repository if kygoX enhances your security workflow!**

</div>
