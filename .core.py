#!/usr/bin/env python3
"""
KYGOX - Arch Linux Penetration Testing Toolkit Core Engine
Author: 0xbv1 | 0xb0rn3 
Contact: IG: theehiv3 | X: 0xbv1 | Threads: theehiv3 | Email: q4n0@proton.me
License: Do whatever the hell you want, but don't blame me when it breaks
"""

import os
import sys
import json
import time
import shutil
import signal
import hashlib
import sqlite3
import tarfile
import logging
import argparse
import threading
import subprocess
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Set, Tuple, Optional, Union
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urljoin, urlparse

try:
    import requests
    from tqdm import tqdm
    from colorama import init, Fore, Back, Style
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import padding
    from packaging import version
except ImportError as e:
    print(f"[ERROR] Missing required Python package: {e}")
    print("[INFO] Run the setup script first: sudo ./run --setup")
    sys.exit(1)

# Initialize colorama
init(autoreset=True)

class KygoXConfig:
    """Core configuration and constants"""
    
    VERSION = "0.1.9-alpha"
    VERSION_NAME = "Venom"
    SCRIPT_NAME = "KygoX"
    REPO_URL = "https://github.com/0xb0rn3/kygox"
    ALT_REPO = "https://github.com/0xb0rn3/krilin"
    
    # Repository URLs
    BLACKARCH_KEYRING_URL = "https://www.blackarch.org/keyring/blackarch-keyring.pkg.tar.xz"
    BLACKARCH_KEYRING_SIG = "https://www.blackarch.org/keyring/blackarch-keyring.pkg.tar.xz.sig"
    BLACKARCH_MIRROR = "https://blackarch.org/blackarch/$repo/os/$arch"
    ARCH_MIRROR = "https://mirror.rackspace.com/archlinux/$repo/os/$arch"
    
    # File paths
    LOG_DIR = Path("kygox_logs")
    BACKUP_DIR = LOG_DIR / "backups"
    CACHE_DIR = Path(".kygox_cache")
    DB_FILE = CACHE_DIR / "packages.db"
    TOOLKIT_FILE = "toolkit.txt"
    
    # Core security tools collection - 2025
    CORE_TOOLS = [
        # Network Discovery & Scanning
        "nmap", "masscan", "rustscan", "zmap", "angry-ip-scanner",
        "netdiscover", "arp-scan", "fping", "hping", "traceroute",
        
        # Network Analysis & Monitoring
        "wireshark-qt", "wireshark-cli", "tcpdump", "ettercap", "bettercap",
        "kismet", "aircrack-ng", "wifite", "reaver", "pixiewps",
        
        # Web Application Security
        "burpsuite", "owasp-zap", "sqlmap", "nikto", "dirb",
        "gobuster", "ffuf", "feroxbuster", "whatweb", "wpscan",
        "nuclei", "httpx", "subfinder", "amass", "aquatone",
        
        # Exploitation & Penetration Testing
        "metasploit", "empire", "powersploit", "beef", "armitage",
        "searchsploit", "exploit-db", "msfdb", "msfvenom", "shellter",
        
        # Password Attacks & Cracking
        "john", "hashcat", "hydra", "medusa", "ncrack",
        "crunch", "cewl", "rsmangler", "maskprocessor", "statsprocessor",
        
        # Digital Forensics & Analysis
        "volatility3", "autopsy", "sleuthkit", "binwalk", "foremost",
        "bulk-extractor", "dc3dd", "ddrescue", "guymager", "dff",
        
        # Reverse Engineering & Analysis
        "ghidra", "radare2", "rizin", "gdb", "objdump",
        "strace", "ltrace", "hexdump", "strings", "file",
        
        # Mobile Security
        "apktool", "jadx", "dex2jar", "smali", "baksmali",
        "mobsf", "qark", "drozer", "objection", "frida",
        
        # Information Gathering & OSINT
        "theharvester", "recon-ng", "maltego", "sherlock", "spiderfoot",
        "dmitry", "fierce", "dnsrecon", "dnsmap", "dnsenum",
        
        # Post-Exploitation & Persistence
        "impacket", "responder", "crackmapexec", "bloodhound", "neo4j",
        "mimikatz", "pypykatz", "lsassy", "secretsdump", "ntlmrelayx",
        
        # Vulnerability Assessment
        "openvas", "greenbone-security-assistant", "lynis", "chkrootkit", "rkhunter",
        "nikto", "skipfish", "w3af", "arachni", "grabber",
        
        # Steganography & Crypto
        "steghide", "outguess", "stegsolve", "zsteg", "exiftool",
        "hashpump", "hash-identifier", "hashid", "hash-buster", "findmyhash",
        
        # Hardware & IoT Security
        "minicom", "picocom", "screen", "cu", "arduino",
        "platformio", "esptool", "avrdude", "openocd", "sigrok-cli",
        
        # Social Engineering
        "social-engineer-toolkit", "king-phisher", "gophish", "evilginx2", "modlishka"
    ]
    
    # Trending 2025 tools
    TRENDING_2025 = [
        # Modern Web Security
        "katana", "naabu", "dnsx", "interactsh", "notify",
        "chaos-client", "uncover", "tlsx", "asnmap", "cdncheck",
        
        # AI/ML Security Testing
        "garak", "counterfit", "adversarial-robustness-toolbox", "foolbox", "cleverhans",
        
        # Container & Cloud Security
        "trivy", "grype", "syft", "docker-bench-security", "kube-bench",
        "checkov", "terrascan", "tfsec", "prowler", "scout-suite",
        
        # Modern C2 & RATs
        "sliver", "havoc", "covenant", "villain", "poshc2",
        
        # Advanced OSINT
        "maltego", "spiderfoot", "osrframework", "photon", "carbon14",
        
        # Blockchain & Crypto Security  
        "mythril", "slither", "echidna", "manticore", "securify",
        
        # API Security Testing
        "postman", "insomnia", "burp-suite-pro", "apicheck", "mitmproxy",
        
        # DevSecOps Tools
        "semgrep", "bandit", "safety", "pip-audit", "gitleaks",
        "truffleHog", "detect-secrets", "secretlint", "git-secrets", "repo-supervisor"
    ]
    
    # BlackArch categories
    BLACKARCH_CATEGORIES = {
        "webapp": "Web Application Security",
        "scanner": "Vulnerability Scanners", 
        "exploitation": "Exploitation Tools",
        "forensic": "Digital Forensics",
        "crypto": "Cryptography Tools",
        "networking": "Network Tools",
        "wireless": "Wireless Security",
        "reversing": "Reverse Engineering",
        "malware": "Malware Analysis",
        "social": "Social Engineering",
        "mobile": "Mobile Security",
        "hardware": "Hardware Security",
        "automation": "Automation Tools",
        "defensive": "Defensive Security",
        "recon": "Reconnaissance",
        "database": "Database Tools"
    }

class ColorManager:
    """Enhanced color management for terminal output"""
    
    # Color definitions
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    PURPLE = Fore.MAGENTA
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE
    DARK = Fore.BLACK + Style.BRIGHT
    BOLD = Style.BRIGHT
    DIM = Style.DIM
    RESET = Style.RESET_ALL
    
    # Status indicators
    SUCCESS = f"[{GREEN}✓{RESET}]"
    ERROR = f"[{RED}✗{RESET}]"
    INFO = f"[{BLUE}ℹ{RESET}]"
    WARNING = f"[{YELLOW}⚠{RESET}]"
    PROCESS = f"[{PURPLE}⚡{RESET}]"
    SECURITY = f"[{CYAN}🔒{RESET}]"

class Logger:
    """Advanced logging system with multiple output formats"""
    
    def __init__(self, log_dir: Path):
        self.log_dir = log_dir
        self.log_dir.mkdir(parents=True, exist_ok=True)
        
        self.main_log = log_dir / "installation.log"
        self.error_log = log_dir / "errors.log"
        self.success_log = log_dir / "successful_packages.log"
        self.failed_log = log_dir / "failed_packages.log"
        
        # Setup logging
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(component)s - %(message)s',
            handlers=[
                logging.FileHandler(self.main_log),
                logging.StreamHandler()
            ]
        )
        
        self.logger = logging.getLogger('KygoX')
        
    def log(self, level: str, message: str, component: str = "system", display: bool = True):
        """Log message with level and component"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Write to main log
        with open(self.main_log, 'a') as f:
            f.write(f"[{timestamp}] [{level}] [{component}] {message}\n")
        
        # Write to specific logs
        if level == "ERROR":
            with open(self.error_log, 'a') as f:
                f.write(f"[{timestamp}] [{component}] {message}\n")
        
        # Display to console
        if display:
            color_map = {
                "SUCCESS": ColorManager.SUCCESS,
                "ERROR": ColorManager.ERROR,
                "INFO": ColorManager.INFO,
                "WARNING": ColorManager.WARNING,
                "PROCESS": ColorManager.PROCESS,
                "SECURITY": ColorManager.SECURITY
            }
            
            indicator = color_map.get(level, f"[{level}]")
            print(f"{indicator} {message}")
    
    def log_package(self, package: str, status: str, details: str = ""):
        """Log package installation status"""
        if status == "success":
            with open(self.success_log, 'a') as f:
                f.write(f"{package}\n")
        elif status == "failed":
            with open(self.failed_log, 'a') as f:
                f.write(f"{package}: {details}\n")

class SystemInfo:
    """System information and compatibility checker"""
    
    def __init__(self):
        self.distro_info = self._detect_distribution()
        self.is_arch_based = self._check_arch_compatibility()
        self.pacman_version = self._get_pacman_version()
        self.system_specs = self._get_system_specs()
        
    def _detect_distribution(self) -> Dict[str, str]:
        """Detect Linux distribution information"""
        info = {"id": "", "version": "", "name": "", "codename": ""}
        
        try:
            with open("/etc/os-release", "r") as f:
                for line in f:
                    if line.startswith("ID="):
                        info["id"] = line.split("=", 1)[1].strip().strip('"').lower()
                    elif line.startswith("VERSION_ID="):
                        info["version"] = line.split("=", 1)[1].strip().strip('"')
                    elif line.startswith("NAME="):
                        info["name"] = line.split("=", 1)[1].strip().strip('"')
                    elif line.startswith("VERSION_CODENAME="):
                        info["codename"] = line.split("=", 1)[1].strip().strip('"')
        except FileNotFoundError:
            # Fallback detection
            if Path("/etc/arch-release").exists():
                info["id"] = "arch"
                info["name"] = "Arch Linux"
            elif Path("/etc/manjaro-release").exists():
                info["id"] = "manjaro"
                info["name"] = "Manjaro Linux"
                
        return info
    
    def _check_arch_compatibility(self) -> bool:
        """Check if system is Arch-based"""
        arch_indicators = [
            Path("/etc/arch-release").exists(),
            Path("/etc/manjaro-release").exists(),
            shutil.which("pacman") is not None,
            self.distro_info["id"] in ["arch", "manjaro", "endeavouros", "garuda", "artix", "blackarch"]
        ]
        
        return any(arch_indicators)
    
    def _get_pacman_version(self) -> str:
        """Get pacman version"""
        try:
            result = subprocess.run(
                ["pacman", "--version"],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                return result.stdout.split("\n")[0].split()[-1].strip("v")
        except:
            pass
        return "unknown"
    
    def _get_system_specs(self) -> Dict[str, Union[int, str]]:
        """Get basic system specifications"""
        specs = {}
        
        try:
            # RAM
            with open("/proc/meminfo", "r") as f:
                for line in f:
                    if line.startswith("MemTotal:"):
                        specs["ram_mb"] = int(line.split()[1]) // 1024
                        break
            
            # CPU cores
            specs["cpu_cores"] = os.cpu_count()
            
            # Disk space
            stat = shutil.disk_usage("/")
            specs["disk_total_gb"] = stat.total // (1024**3)
            specs["disk_free_gb"] = stat.free // (1024**3)
            
        except Exception:
            specs = {"ram_mb": 0, "cpu_cores": 1, "disk_total_gb": 0, "disk_free_gb": 0}
            
        return specs

class KeyringManager:
    """BlackArch keyring and signature verification"""
    
    def __init__(self, logger: Logger, cache_dir: Path):
        self.logger = logger
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
    def setup_blackarch_keyring(self) -> bool:
        """Setup BlackArch keyring for package verification"""
        self.logger.log("PROCESS", "Setting up BlackArch keyring", "keyring")
        
        try:
            # Download keyring
            keyring_file = self.cache_dir / "blackarch-keyring.pkg.tar.xz"
            signature_file = self.cache_dir / "blackarch-keyring.pkg.tar.xz.sig"
            
            # Download keyring package
            self._download_file(KygoXConfig.BLACKARCH_KEYRING_URL, keyring_file)
            self._download_file(KygoXConfig.BLACKARCH_KEYRING_SIG, signature_file)
            
            # Install keyring
            result = subprocess.run(
                ["pacman", "-U", "--noconfirm", str(keyring_file)],
                capture_output=True,
                text=True,
                timeout=300
            )
            
            if result.returncode == 0:
                self.logger.log("SUCCESS", "BlackArch keyring installed successfully", "keyring")
                
                # Add BlackArch repository
                self._add_blackarch_repo()
                return True
            else:
                self.logger.log("ERROR", f"Failed to install keyring: {result.stderr}", "keyring")
                return False
                
        except Exception as e:
            self.logger.log("ERROR", f"Keyring setup failed: {str(e)}", "keyring")
            return False
    
    def _download_file(self, url: str, filepath: Path, timeout: int = 300):
        """Download file with progress bar"""
        response = requests.get(url, stream=True, timeout=timeout)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        
        with open(filepath, 'wb') as f, tqdm(
            total=total_size,
            unit='B',
            unit_scale=True,
            desc=f"Downloading {filepath.name}"
        ) as pbar:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    pbar.update(len(chunk))
    
    def _add_blackarch_repo(self):
        """Add BlackArch repository to pacman.conf"""
        pacman_conf = Path("/etc/pacman.conf")
        
        try:
            with open(pacman_conf, "r") as f:
                content = f.read()
            
            if "[blackarch]" not in content:
                blackarch_repo = "\n[blackarch]\nServer = https://blackarch.org/blackarch/$repo/os/$arch\n"
                
                # Backup original
