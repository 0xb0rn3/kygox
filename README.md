<div align="center">

```
░  ░░░░  ░░  ░░░░  ░░░      ░░░  ░░░░  ░
▒  ▒▒▒  ▒▒▒▒  ▒▒  ▒▒▒  ▒▒▒▒▒▒▒▒▒  ▒▒  ▒▒
▓     ▓▓▓▓▓▓▓    ▓▓▓▓  ▓▓▓   ▓▓▓▓    ▓▓▓
█  ███  ██████  █████  ████  ███  ██  ██
█  ████  █████  ██████      ███  ████  █
                                        
```

<h1>Arch Linux Security Arsenal Manager</h1>

<p>
  <img src="https://img.shields.io/badge/version-0.1%20stable-blue?style=flat-square" alt="Version">
  <img src="https://img.shields.io/badge/platform-Arch%20Linux-1793D1?style=flat-square&logo=arch-linux&logoColor=white" alt="Platform">
  <img src="https://img.shields.io/badge/license-WTFPL-red?style=flat-square" alt="License">
  <img src="https://img.shields.io/badge/tools-78000+-green?style=flat-square" alt="Tools">
  <img src="https://img.shields.io/badge/AUR-supported-orange?style=flat-square" alt="AUR">
</p>

<p>Transform your Arch system into a professional penetration testing platform with intelligent automation, AUR integration, and modern tooling.</p>

<p>
  <a href="#installation">Installation</a> •
  <a href="#features">Features</a> •
  <a href="#usage">Usage</a> •
  <a href="#categories">Categories</a> •
  <a href="#aur-support">AUR Support</a> •
  <a href="#documentation">Documentation</a>
</p>

</div>

---

## Overview

kyGX is a sophisticated security arsenal manager designed specifically for Arch Linux systems. It provides seamless integration with BlackArch repositories and AUR, offering access to over 2800 penetration testing tools from BlackArch plus 75,000+ packages from AUR through an intelligent, automated installation framework with smart fallback capabilities.

<details>
<summary><strong>Key Highlights</strong></summary>

<table>
<tr>
<td width="50%">

**Reliability**
- Multi-keyserver GPG management
- Automatic AUR fallback system
- Database conflict resolution
- State tracking and rollback
- Dual-source installation (BlackArch + AUR)

</td>
<td width="50%">

**Performance**
- Direct pacman integration
- Intelligent package caching
- Real-time tool discovery
- Optimized installation flow
- Automatic yay helper installation

</td>
</tr>
<tr>
<td width="50%">

**Organization**
- 10 security-focused categories
- Native BlackArch group integration
- Curated slim toolkit option
- AUR search functionality
- Clean tool filtering

</td>
<td width="50%">

**User Experience**
- Minimal CLI interface
- AUR-only installation mode
- Dry-run preview mode
- Comprehensive logging
- Built-in cleanup utilities
- Auto-config installation

</td>
</tr>
</table>

</details>

---

## Installation

```bash
git clone https://github.com/0xb0rn3/kyGX.git
cd kyGX
chmod +x kyGX
sudo ./kyGX
```

### Requirements

- Arch Linux or derivative (Archcraft, Manjaro, EndeavourOS, Garuda)
- Root/sudo privileges
- Active internet connection
- Dependencies: `curl`, `wget`, `python`, `jq`, `git`, `base-devel`
- yay (automatically installed if missing)

---

## Features

### AUR Integration & Smart Fallback

```
┌─────────────────────────────────────────┐
│ Intelligent Installation Flow           │
├─────────────────────────────────────────┤
│ 1. Attempt BlackArch repository         │
│ 2. On failure → Auto-retry via AUR      │
│ 3. Track and report fallback usage      │
│ 4. Detailed logging for debugging       │
└─────────────────────────────────────────┘
```

**New in v0.1:**
- **Automatic yay installation**: AUR helper installed automatically when needed
- **Smart fallback mechanism**: Failed BlackArch installs automatically retry via AUR
- **AUR-only mode**: Direct installation from AUR bypassing BlackArch
- **AUR search**: Interactive search and installation from 75,000+ packages
- **Default configs**: Auto-installs blackarch-menus, blackarch-config-gtk, blackarch-config-zsh
- **Dual updates**: Updates both pacman and AUR packages simultaneously

### Security & Reliability

```
┌─────────────────────────────────────────┐
│ Smart GPG Management                    │
├─────────────────────────────────────────┤
│ • Multi-keyserver fallback              │
│ • Automatic signature verification      │
│ • Key refresh and expiry handling       │
│ • Corruption recovery                   │
└─────────────────────────────────────────┘
```

- **Progressive Error Recovery**: Three-tier automatic retry system
- **Lock File Management**: Automatic pacman database lock resolution
- **State Tracking**: JSON-based installation history with rollback capability
- **Conflict Resolution**: Intelligent handling of package conflicts
- **AUR Fallback**: Automatic retry via AUR when BlackArch installations fail

### Performance Optimizations

- Direct installation without batching overhead
- Category-based organization from BlackArch
- Real-time tool list fetching from blackarch.org
- Intelligent package caching system
- Parallel operation support where applicable
- Non-root yay execution for security

### Tool Organization

<table>
<tr>
<td width="33%">

**Information Gathering**
- Scanners
- Reconnaissance
- Fingerprinting
- OSINT tools

</td>
<td width="33%">

**Exploitation**
- Exploit frameworks
- Payload generators
- Backdoor tools
- Shellcode utilities

</td>
<td width="33%">

**Analysis**
- Vulnerability scanners
- Fuzzing tools
- Web analyzers
- Forensics utilities

</td>
</tr>
</table>

---

## Usage

### Interactive Mode

```bash
sudo ./kyGX
```

Launch the interactive menu to browse and install tools by category, search AUR, or use AUR-only installation.

### Slim Toolkit

```bash
sudo ./kyGX --slim
```

Install a curated collection of essential tools similar to Kali Linux defaults:

- `nmap`, `masscan`, `nikto`, `recon-ng`, `theharvester`
- `sqlmap`, `wpscan`, `metasploit`, `burpsuite`
- `john`, `hydra`, `hashcat`, `medusa`
- `aircrack-ng`, `reaver`, `wifite`
- `wireshark`, `ettercap`, `tcpdump`

Tools automatically fallback to AUR if not available in BlackArch.

### Setup BlackArch Repository

```bash
sudo ./kyGX --setup
```

Configure BlackArch repository, install yay, and setup default configuration packages:
- blackarch-menus
- blackarch-config-gtk
- blackarch-config-zsh

### AUR-Only Installation

```bash
sudo ./kyGX --aur
```

Install security tools directly from AUR, bypassing BlackArch repository.

### System Update

```bash
sudo ./kyGX --update
```

Update both official repositories and AUR packages:
- Arch Linux packages (pacman)
- BlackArch packages
- AUR packages (yay)

### Cleanup

```bash
sudo ./kyGX --cleanup
```

Remove BlackArch configuration and restore default `pacman.conf`.

### Command Reference

```
OPTIONS:
  -h, --help          Display help information
  -v, --verbose       Enable detailed output
  -n, --dry-run       Preview installations without changes
  -f, --force         Force installation bypassing checks
  --setup             Setup BlackArch + yay + default configs
  --update            Update system (pacman + AUR)
  --slim              Install curated slim toolkit
  --aur               AUR-only installation mode
  --cleanup           Remove BlackArch and restore config

EXAMPLES:
  sudo ./kyGX                # Interactive mode
  sudo ./kyGX --setup        # Complete setup with defaults
  sudo ./kyGX --slim         # Install essential tools
  sudo ./kyGX --aur          # AUR-only installation
  sudo ./kyGX -n             # Preview mode
  sudo ./kyGX --cleanup      # Complete removal
```

---

## AUR Support

### Automatic Fallback System

When a tool fails to install from BlackArch, kyGX automatically attempts installation from AUR:

```
[*] Installing nmap
[✓] nmap installed
[*] Installing custom-tool
[!] custom-tool failed via BlackArch, trying AUR fallback...
[✓] custom-tool installed via AUR

[+] Results: Installed: 2 | AUR Fallback: 1 | Failed: 0
```

### Interactive Menu Options

**From the main menu:**

```
AUR Options:
  y) Install tools from AUR only
  z) Search AUR for security tools
```

**Option Y - AUR-Only Installation:**
```bash
[*] Enter tool names to install from AUR (space-separated):
> metasploit-framework burpsuite ghidra

[*] Installing 3 tools from AUR
[✓] metasploit-framework installed
[✓] burpsuite installed  
[✓] ghidra installed
```

**Option Z - AUR Search:**
```bash
[*] Enter search term (e.g., 'exploit', 'scanner', 'recon'):
> wireless

[Search results displayed...]

[?] Install any of these? (y/n):
```

### YAY Helper

kyGX automatically detects and installs yay (Yet Another Yogurt) if not present:

```
[*] Installing yay (AUR helper)
[+] yay installed successfully
```

yay is executed as a non-root user for security best practices.

---

## Categories

<details open>
<summary><strong>Security Tool Categories</strong></summary>

### 1. Information Gathering
Network scanners, reconnaissance tools, fingerprinting utilities, OSINT frameworks
- Groups: `scanner`, `recon`, `fingerprint`, `osint`
- Sources: BlackArch + AUR fallback

### 2. Vulnerability Analysis
Vulnerability scanners, fuzzing tools, exploitation frameworks
- Groups: `scanner`, `fuzzer`, `exploitation`
- Sources: BlackArch + AUR fallback

### 3. Web Application Analysis
Web testing proxies, scanners, injection tools
- Groups: `webapp`, `proxy`, `scanner`
- Sources: BlackArch + AUR fallback

### 4. Password Attacks
Password crackers, hash tools, wordlist generators
- Groups: `cracker`, `password`, `crypto`
- Sources: BlackArch + AUR fallback

### 5. Wireless Attacks
WiFi testing, Bluetooth tools, NFC utilities
- Groups: `wireless`, `bluetooth`, `nfc`
- Sources: BlackArch + AUR fallback

### 6. Exploitation Tools
Exploit frameworks, backdoors, payload generators
- Groups: `exploitation`, `backdoor`, `binary`
- Sources: BlackArch + AUR fallback

### 7. Digital Forensics
Forensic analysis, malware research, reverse engineering
- Groups: `forensic`, `malware`, `reversing`
- Sources: BlackArch + AUR fallback

### 8. Sniffing & Spoofing
Network sniffers, protocol spoofing, MITM tools
- Groups: `sniffer`, `spoof`, `proxy`
- Sources: BlackArch + AUR fallback

### 9. Post Exploitation
Persistence tools, tunneling, privilege escalation
- Groups: `backdoor`, `tunnel`, `keylogger`
- Sources: BlackArch + AUR fallback

### 10. Social Engineering
Phishing frameworks, social engineering toolkits
- Groups: `social`, `voip`
- Sources: BlackArch + AUR fallback

</details>

---

## Documentation

### Architecture

```
kyGX v0.1
├── Core Components
│   ├── GPG key management
│   ├── Repository configuration
│   ├── YAY helper management
│   └── Tool list caching
├── Installation Engine
│   ├── Direct pacman integration
│   ├── AUR fallback system
│   ├── Error recovery system
│   └── State management
└── User Interface
    ├── Interactive menu
    ├── AUR search & install
    ├── Command-line options
    └── Progress tracking
```

### Installation Flow

```
User Request
    ↓
Try BlackArch Repository
    ↓
Success? → [✓] Install Complete
    ↓ No
Try AUR Fallback (yay)
    ↓
Success? → [✓] Install Complete (AUR)
    ↓ No
[✗] Report Failure
```

### File Locations

| Path | Purpose |
|------|---------|
| `~/.kyGX/kyGX.log` | Operation logs with AUR tracking |
| `~/.config/kyGX/` | Configuration directory |
| `~/.config/kyGX/.toollist.json` | Cached BlackArch tool list |
| `~/.config/kyGX/.aur_tools.json` | AUR tools cache |
| `~/.config/kyGX/backups/` | Configuration backups |

### How It Works

**Tool Discovery**

kyGX fetches the tool list directly from blackarch.org/tools.html and caches it locally. AUR tools are discovered through yay search functionality.

**Installation Strategy**

- Tools are installed individually via pacman
- Failed installations automatically retry via yay (AUR)
- Real-time progress tracking with fallback indicators
- Failed installations are logged but don't halt the process
- Only security tools are installed (excludes desktop environments)

**Cleanup Process**

Cleanup restores the original Arch Linux configuration, removes BlackArch mirrors, and cleans both tool caches. Configuration backups are timestamped for recovery.

---

## Troubleshooting

### Common Issues

<details>
<summary><strong>GPG Key Errors</strong></summary>

```bash
# Refresh keyring
sudo pacman-key --refresh-keys
sudo pacman -Sy archlinux-keyring blackarch-keyring
```

</details>

<details>
<summary><strong>Database Lock</strong></summary>

```bash
# Remove lock file
sudo rm /var/lib/pacman/db.lck
sudo pacman -Sy
```

</details>

<details>
<summary><strong>YAY Installation Failures</strong></summary>

```bash
# Manual yay installation
sudo pacman -S --needed git base-devel
cd /tmp
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
```

</details>

<details>
<summary><strong>AUR Fallback Not Working</strong></summary>

```bash
# Check yay is installed
which yay

# Check logs
tail -f ~/.kyGX/kyGX.log

# Look for AUR entries
grep "AUR" ~/.kyGX/kyGX.log
```

</details>

<details>
<summary><strong>Mirror Issues</strong></summary>

```bash
# Update mirrors
sudo ./kyGX --update
# Or manually
sudo pacman -Sy
```

</details>

### Debug Mode

```bash
# Enable verbose logging
sudo ./kyGX -v

# Check logs for AUR activity
cat ~/.kyGX/kyGX.log | grep -E "(AUR|BLACKARCH)"

# Preview without installation
sudo ./kyGX -n
```

### Configuration Restoration

Backups are stored in `~/.config/kyGX/backups/` with timestamps. To manually restore:

```bash
# List backups
ls -lh ~/.config/kyGX/backups/

# Restore pacman.conf
sudo cp ~/.config/kyGX/backups/pacman.conf.* /etc/pacman.conf
```

---

## Security Considerations

This tool provides access to penetration testing and security research software. Users must:

- Obtain written authorization before conducting security assessments
- Define clear scope and rules of engagement
- Use isolated environments (VMs, dedicated hardware)
- Document methodology and findings
- Comply with applicable laws and regulations
- Follow industry standards (PTES, OWASP, NIST)
- Maintain professional ethics
- Verify AUR packages before installation

**Legal Notice**: Unauthorized access to computer systems is illegal. The author assumes no liability for misuse of this tool.

**AUR Security**: While kyGX automates AUR installation, users should be aware that AUR packages are user-submitted and should be reviewed before installation in production environments.

---

## Development

### Publishing to AUR

To publish kyGX to AUR:

1. Create AUR account at https://aur.archlinux.org
2. Generate SSH keys and add to AUR account
3. Clone the AUR package:
```bash
git clone ssh://aur@aur.archlinux.org/kyGX.git
```
4. Create PKGBUILD file (see AUR Publishing section below)
5. Update .SRCINFO:
```bash
makepkg --printsrcinfo > .SRCINFO
```
6. Commit and push:
```bash
git add PKGBUILD .SRCINFO
git commit -m "Initial commit: kyGX v0.1"
git push
```

### PKGBUILD Template

```bash
# Maintainer: 0xb0rn3 <q4n0@proton.me>
pkgname=kyGX
pkgver=0.1
pkgrel=1
pkgdesc="Arch Linux Security Arsenal Manager with AUR support"
arch=('any')
url="https://github.com/0xb0rn3/kyGX"
license=('WTFPL')
depends=('bash' 'curl' 'wget' 'python' 'jq' 'git' 'base-devel' 'pacman')
optdepends=('yay: AUR helper for automatic fallback'
            'blackarch-keyring: BlackArch repository support')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('SKIP')

package() {
    cd "$srcdir/$pkgname-$pkgver"
    install -Dm755 kyGX "$pkgdir/usr/bin/kyGX"
    install -Dm644 README.md "$pkgdir/usr/share/doc/$pkgname/README.md"
}
```

### Contributing

Contributions are welcome. Please:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request with detailed description
4. Follow the existing code style

### Roadmap

- [x] AUR integration and fallback
- [x] Automatic yay installation
- [x] AUR search functionality
- [x] Default configuration packages
- [ ] GUI interface
- [ ] Docker containerization
- [ ] AUR package release (v0.1 ready)
- [ ] Automatic update checker
- [ ] Multi-language support
- [ ] Integration with security frameworks

---

## Support

<table>
<tr>
<td align="center" width="25%">

**Repository**

[GitHub](https://github.com/0xb0rn3/kyGX)

</td>
<td align="center" width="25%">

**Issues**

[Bug Reports](https://github.com/0xb0rn3/kyGX/issues)

</td>
<td align="center" width="25%">

**Author**

0xb0rn3

</td>
<td align="center" width="25%">

**Contact**

q4n0@proton.me

</td>
</tr>
</table>

### Social

- Instagram: [@theehiv3](https://instagram.com/theehiv3)
- Twitter: [@0xbv1](https://twitter.com/0xbv1)

---

## Changelog

### v0.1 (Stable)
- ✅ AUR integration with automatic fallback
- ✅ Automatic yay helper installation
- ✅ AUR-only installation mode
- ✅ Interactive AUR search functionality
- ✅ Default BlackArch config auto-installation
- ✅ Dual-source updates (pacman + AUR)
- ✅ Non-root yay execution for security
- ✅ Detailed installation tracking with source reporting

---

## License

```
DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
Version 2, December 2004

Copyright (C) 2024 0xb0rn3 <q4n0@proton.me>

Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.

DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

0. You just DO WHAT THE FUCK YOU WANT TO.
```

---

<div align="center">

**kyGX v0.1**

**Made for security professionals and researchers**

<sub>Tested on Arch Linux | Archcraft | Manjaro | EndeavourOS | Garuda</sub>

[![Arch Linux](https://img.shields.io/badge/Arch-1793D1?style=flat-square&logo=arch-linux&logoColor=white)](https://archlinux.org/)
[![BlackArch](https://img.shields.io/badge/BlackArch-000000?style=flat-square&logo=linux&logoColor=white)](https://blackarch.org/)
[![AUR](https://img.shields.io/badge/AUR-Ready-orange?style=flat-square)](https://aur.archlinux.org/)

</div>
