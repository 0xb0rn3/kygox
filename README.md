<div align="center">

```
██╗  ██╗██╗   ██╗ ██████╗  ██████╗ ██╗  ██╗
██║ ██╔╝╚██╗ ██╔╝██╔════╝ ██╔═══██╗╚██╗██╔╝
█████╔╝  ╚████╔╝ ██║  ███╗██║   ██║ ╚███╔╝ 
██╔═██╗   ╚██╔╝  ██║   ██║██║   ██║ ██╔██╗ 
██║  ██╗   ██║   ╚██████╔╝╚██████╔╝██╔╝ ██╗
╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
```

<h1>Arch Linux Security Arsenal Manager</h1>

<p>
  <img src="https://img.shields.io/badge/version-1.0.1-blue?style=flat-square" alt="Version">
  <img src="https://img.shields.io/badge/platform-Arch%20Linux-1793D1?style=flat-square&logo=arch-linux&logoColor=white" alt="Platform">
  <img src="https://img.shields.io/badge/license-WTFPL-red?style=flat-square" alt="License">
  <img src="https://img.shields.io/badge/tools-2800+-green?style=flat-square" alt="Tools">
</p>

<p>Transform your Arch system into a professional penetration testing platform with intelligent automation and modern tooling.</p>

<p>
  <a href="#installation">Installation</a> •
  <a href="#features">Features</a> •
  <a href="#usage">Usage</a> •
  <a href="#categories">Categories</a> •
  <a href="#documentation">Documentation</a>
</p>

</div>

---

## Overview

kygox is a sophisticated security arsenal manager designed specifically for Arch Linux systems. It provides seamless integration with BlackArch repositories, offering access to over 2800 penetration testing and security research tools through an intelligent, automated installation framework.

<details>
<summary><strong>Key Highlights</strong></summary>

<table>
<tr>
<td width="50%">

**Reliability**
- Multi-keyserver GPG management
- Automatic error recovery
- Database conflict resolution
- State tracking and rollback

</td>
<td width="50%">

**Performance**
- Direct pacman integration
- Intelligent package caching
- Real-time tool discovery
- Optimized installation flow

</td>
</tr>
<tr>
<td width="50%">

**Organization**
- 10 security-focused categories
- Native BlackArch group integration
- Curated slim toolkit option
- Clean tool filtering

</td>
<td width="50%">

**User Experience**
- Minimal CLI interface
- Dry-run preview mode
- Comprehensive logging
- Built-in cleanup utilities

</td>
</tr>
</table>

</details>

---

## Installation

```bash
git clone https://github.com/0xb0rn3/kygox.git
cd kygox
chmod +x kygox
sudo ./kygox
```

### Requirements

- Arch Linux or derivative (Archcraft, Manjaro, EndeavourOS, Garuda)
- Root/sudo privileges
- Active internet connection
- Dependencies: `curl`, `wget`, `python`, `jq`

---

## Features

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

### Performance Optimizations

- Direct installation without batching overhead
- Category-based organization from BlackArch
- Real-time tool list fetching from blackarch.org
- Intelligent package caching system
- Parallel operation support where applicable

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
sudo ./kygox
```

Launch the interactive menu to browse and install tools by category.

### Slim Toolkit

```bash
sudo ./kygox --slim
```

Install a curated collection of essential tools similar to Kali Linux defaults:

- `nmap`, `masscan`, `nikto`, `recon-ng`, `theharvester`
- `sqlmap`, `wpscan`, `metasploit`, `burpsuite`
- `john`, `hydra`, `hashcat`, `medusa`
- `aircrack-ng`, `reaver`, `wifite`
- `wireshark`, `ettercap`, `tcpdump`

### Setup BlackArch Repository

```bash
sudo ./kygox --setup
```

Configure BlackArch repository without installing tools.

### System Update

```bash
sudo ./kygox --update
```

Update BlackArch mirror list and refresh package databases.

### Cleanup

```bash
sudo ./kygox --cleanup
```

Remove BlackArch configuration and restore default `pacman.conf`.

### Command Reference

```
OPTIONS:
  -h, --help          Display help information
  -v, --verbose       Enable detailed output
  -n, --dry-run       Preview installations without changes
  -f, --force         Force installation bypassing checks
  --setup             Setup BlackArch repository only
  --update            Update system and mirrors
  --slim              Install curated slim toolkit
  --cleanup           Remove BlackArch and restore config

EXAMPLES:
  sudo ./kygox                # Interactive mode
  sudo ./kygox --setup        # Repository setup only
  sudo ./kygox --slim         # Install essential tools
  sudo ./kygox -n             # Preview mode
  sudo ./kygox --cleanup      # Complete removal
```

---

## Categories

<details open>
<summary><strong>Security Tool Categories</strong></summary>

### 1. Information Gathering
Network scanners, reconnaissance tools, fingerprinting utilities, OSINT frameworks
- Groups: `scanner`, `recon`, `fingerprint`, `osint`

### 2. Vulnerability Analysis
Vulnerability scanners, fuzzing tools, exploitation frameworks
- Groups: `scanner`, `fuzzer`, `exploitation`

### 3. Web Application Analysis
Web testing proxies, scanners, injection tools
- Groups: `webapp`, `proxy`, `scanner`

### 4. Password Attacks
Password crackers, hash tools, wordlist generators
- Groups: `cracker`, `password`, `crypto`

### 5. Wireless Attacks
WiFi testing, Bluetooth tools, NFC utilities
- Groups: `wireless`, `bluetooth`, `nfc`

### 6. Exploitation Tools
Exploit frameworks, backdoors, payload generators
- Groups: `exploitation`, `backdoor`, `binary`

### 7. Digital Forensics
Forensic analysis, malware research, reverse engineering
- Groups: `forensic`, `malware`, `reversing`

### 8. Sniffing & Spoofing
Network sniffers, protocol spoofing, MITM tools
- Groups: `sniffer`, `spoof`, `proxy`

### 9. Post Exploitation
Persistence tools, tunneling, privilege escalation
- Groups: `backdoor`, `tunnel`, `keylogger`

### 10. Social Engineering
Phishing frameworks, social engineering toolkits
- Groups: `social`, `voip`

</details>

---

## Documentation

### Architecture

```
kygox
├── Core Components
│   ├── GPG key management
│   ├── Repository configuration
│   └── Tool list caching
├── Installation Engine
│   ├── Direct pacman integration
│   ├── Error recovery system
│   └── State management
└── User Interface
    ├── Interactive menu
    ├── Command-line options
    └── Progress tracking
```

### File Locations

| Path | Purpose |
|------|---------|
| `~/.kygox/kygox.log` | Operation logs |
| `~/.config/kygox/` | Configuration directory |
| `~/.config/kygox/.toollist.json` | Cached tool list |
| `~/.config/kygox/backups/` | Configuration backups |

### How It Works

**Tool Discovery**

kygox fetches the tool list directly from blackarch.org/tools.html and caches it locally. This ensures access to the latest security tools organized by their official categories.

**Installation Strategy**

- Tools are installed individually via pacman
- Real-time progress tracking
- Failed installations are logged but don't halt the process
- Only security tools are installed (excludes desktop environments)

**Cleanup Process**

Cleanup restores the original Arch Linux configuration, removes BlackArch mirrors, and cleans the tool cache. Configuration backups are timestamped for recovery.

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
<summary><strong>Mirror Issues</strong></summary>

```bash
# Update mirrors
sudo ./kygox --update
# Or manually
sudo pacman -Sy
```

</details>

### Debug Mode

```bash
# Enable verbose logging
sudo ./kygox -v

# Check logs
cat ~/.kygox/kygox.log

# Preview without installation
sudo ./kygox -n
```

### Configuration Restoration

Backups are stored in `~/.config/kygox/backups/` with timestamps. To manually restore:

```bash
# List backups
ls -lh ~/.config/kygox/backups/

# Restore pacman.conf
sudo cp ~/.config/kygox/backups/pacman.conf.* /etc/pacman.conf
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

**Legal Notice**: Unauthorized access to computer systems is illegal. The author assumes no liability for misuse of this tool.

---

## Development

### Contributing

Contributions are welcome. Please:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request with detailed description
4. Follow the existing code style

### Roadmap

- [ ] GUI interface
- [ ] Docker containerization
- [ ] AUR package release
- [ ] Automatic update checker
- [ ] Enhanced error diagnostics
- [ ] Multi-language support
- [ ] Integration with security frameworks

---

## Support

<table>
<tr>
<td align="center" width="25%">

**Repository**

[GitHub](https://github.com/0xb0rn3/kygox)

</td>
<td align="center" width="25%">

**Issues**

[Bug Reports](https://github.com/0xb0rn3/kygox/issues)

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

**Made for security professionals and researchers**

<sub>Tested on Arch Linux | Archcraft | Manjaro | EndeavourOS | Garuda</sub>

[![Arch Linux](https://img.shields.io/badge/Arch-1793D1?style=flat-square&logo=arch-linux&logoColor=white)](https://archlinux.org/)
[![BlackArch](https://img.shields.io/badge/BlackArch-000000?style=flat-square&logo=linux&logoColor=white)](https://blackarch.org/)

</div>
