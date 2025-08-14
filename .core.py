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
import tempfile
import random
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
    
    # Repository URLs - Multiple sources for reliability
    BLACKARCH_KEYRING_URLS = [
        "https://blackarch.org/keyring/blackarch-keyring.pkg.tar.xz",
        "https://www.blackarch.org/keyring/blackarch-keyring.pkg.tar.xz",
        "https://mirror.yandex.ru/mirrors/blackarch/blackarch/blackarch-keyring.pkg.tar.xz",
        "https://mirrors.kernel.org/blackarch/blackarch/blackarch-keyring.pkg.tar.xz",
        "https://ftp.halifax.rwth-aachen.de/blackarch/blackarch/blackarch-keyring.pkg.tar.xz"
    ]
    
    BLACKARCH_SIGNATURE_URLS = [
        "https://blackarch.org/keyring/blackarch-keyring.pkg.tar.xz.sig",
        "https://www.blackarch.org/keyring/blackarch-keyring.pkg.tar.xz.sig"
    ]
    
    BLACKARCH_STRAP_URLS = [
        "https://blackarch.org/strap.sh",
        "https://raw.githubusercontent.com/BlackArch/blackarch/master/scripts/strap.sh"
    ]
    
    BLACKARCH_MIRRORS = [
        "https://blackarch.org/blackarch/$repo/os/$arch",
        "https://mirror.yandex.ru/mirrors/blackarch/$repo/os/$arch",
        "https://mirrors.kernel.org/blackarch/$repo/os/$arch",
        "https://ftp.halifax.rwth-aachen.de/blackarch/$repo/os/$arch"
    ]
    
    ARCH_MIRRORS = [
        "https://mirror.rackspace.com/archlinux/$repo/os/$arch",
        "https://mirrors.kernel.org/archlinux/$repo/os/$arch",
        "https://mirror.osbeck.com/archlinux/$repo/os/$arch"
    ]
    
    # File paths
    LOG_DIR = Path("kygox_logs")
    BACKUP_DIR = LOG_DIR / "backups"
    CACHE_DIR = Path(".kygox_cache")
    DB_FILE = CACHE_DIR / "packages.db"
    TOOLKIT_FILE = "toolkit.txt"
    
    # Retry configuration
    MAX_RETRIES = 5
    RETRY_DELAY = 2.0
    BACKOFF_MULTIPLIER = 1.5
    DOWNLOAD_TIMEOUT = 300
    INSTALL_TIMEOUT = 1800
    
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
        "skipfish", "w3af", "arachni", "grabber",
        
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
    RETRY = f"[{YELLOW}🔄{RESET}]"

class RetryManager:
    """Advanced retry mechanism with exponential backoff"""
    
    @staticmethod
    def retry_with_backoff(func, *args, max_retries=None, delay=None, backoff=None, exceptions=(Exception,), **kwargs):
        """Execute function with retry logic and exponential backoff"""
        max_retries = max_retries or KygoXConfig.MAX_RETRIES
        delay = delay or KygoXConfig.RETRY_DELAY
        backoff = backoff or KygoXConfig.BACKOFF_MULTIPLIER
        
        for attempt in range(max_retries + 1):
            try:
                return func(*args, **kwargs)
            except Exception as e:
            self.logger.log("WARNING", f"Alternative keyring method failed: {str(e)}", "keyring")
        
        return False
    
    def _download_file_with_progress(self, url: str, filepath: Path, timeout: int = None):
        """Download file with progress bar and retry logic"""
        timeout = timeout or KygoXConfig.DOWNLOAD_TIMEOUT
        
        response = requests.get(url, stream=True, timeout=timeout)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        
        with open(filepath, 'wb') as f:
            if total_size > 0:
                with tqdm(
                    total=total_size,
                    unit='B',
                    unit_scale=True,
                    desc=f"Downloading {filepath.name}",
                    leave=False
                ) as pbar:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            pbar.update(len(chunk))
            else:
                # No content-length header, download without progress
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
    
    def _add_blackarch_repo(self):
        """Add BlackArch repository to pacman.conf safely"""
        pacman_conf = Path("/etc/pacman.conf")
        
        try:
            with open(pacman_conf, "r") as f:
                content = f.read()
            
            if "[blackarch]" not in content:
                # Backup original
                backup_path = pacman_conf.with_suffix(f'.bak.{int(time.time())}')
                shutil.copy2(pacman_conf, backup_path)
                self.logger.log("INFO", f"Backed up pacman.conf to {backup_path}", "keyring")
                
                # Add BlackArch repository with best mirror
                best_mirror = self._get_best_blackarch_mirror()
                blackarch_repo = f"\n[blackarch]\nSigLevel = Optional TrustAll\nServer = {best_mirror}\n"
                
                with open(pacman_conf, "a") as f:
                    f.write(blackarch_repo)
                
                self.logger.log("SUCCESS", f"BlackArch repository added with mirror: {best_mirror}", "keyring")
                
                # Update package databases with retry
                self._update_databases()
            else:
                self.logger.log("INFO", "BlackArch repository already configured", "keyring")
                
        except Exception as e:
            self.logger.log("ERROR", f"Failed to configure BlackArch repository: {str(e)}", "keyring")
    
    def _add_blackarch_repo_unsafe(self):
        """Add BlackArch repository without signature verification"""
        pacman_conf = Path("/etc/pacman.conf")
        
        try:
            with open(pacman_conf, "r") as f:
                content = f.read()
            
            if "[blackarch]" not in content:
                backup_path = pacman_conf.with_suffix(f'.bak.unsafe.{int(time.time())}')
                shutil.copy2(pacman_conf, backup_path)
                
                # Add with relaxed signature requirements
                best_mirror = self._get_best_blackarch_mirror()
                blackarch_repo = f"\n[blackarch]\nSigLevel = Never\nServer = {best_mirror}\n"
                
                with open(pacman_conf, "a") as f:
                    f.write(blackarch_repo)
                
                self.logger.log("WARNING", "BlackArch added with signature verification disabled", "keyring")
                self._update_databases()
                
        except Exception as e:
            self.logger.log("ERROR", f"Failed to configure unsafe BlackArch repository: {str(e)}", "keyring")
    
    def _get_best_blackarch_mirror(self) -> str:
        """Find the fastest responding BlackArch mirror"""
        self.logger.log("PROCESS", "Testing BlackArch mirrors for best response", "keyring")
        
        best_mirror = KygoXConfig.BLACKARCH_MIRRORS[0]  # Default
        best_time = float('inf')
        
        for mirror in KygoXConfig.BLACKARCH_MIRRORS:
            try:
                start_time = time.time()
                # Test mirror response time
                test_url = mirror.replace('$repo', 'blackarch').replace('$arch', 'x86_64')
                response = requests.head(test_url, timeout=10)
                response_time = time.time() - start_time
                
                if response.status_code == 200 and response_time < best_time:
                    best_time = response_time
                    best_mirror = mirror
                    
            except Exception:
                continue
        
        self.logger.log("INFO", f"Selected fastest mirror: {best_mirror}", "keyring")
        return best_mirror
    
    def _update_databases(self):
        """Update package databases with retry logic"""
        def update_dbs():
            result = subprocess.run(
                ["pacman", "-Syy"],
                capture_output=True,
                text=True,
                timeout=300
            )
            if result.returncode != 0:
                raise subprocess.CalledProcessError(result.returncode, "pacman", result.stderr)
            return True
        
        if RetryManager.retry_with_backoff(update_dbs):
            self.logger.log("SUCCESS", "Package databases updated", "keyring")
        else:
            self.logger.log("WARNING", "Failed to update package databases", "keyring")
    
    def _verify_blackarch_setup(self):
        """Verify BlackArch setup is working"""
        try:
            result = subprocess.run(
                ["pacman", "-Sl", "blackarch"],
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if result.returncode == 0 and result.stdout.strip():
                package_count = len(result.stdout.strip().split('\n'))
                self.logger.log("SUCCESS", f"BlackArch repository verified with {package_count} packages", "keyring")
            else:
                self.logger.log("WARNING", "BlackArch repository verification failed", "keyring")
                
        except Exception as e:
            self.logger.log("WARNING", f"Could not verify BlackArch setup: {str(e)}", "keyring")

class PackageManager:
    """Advanced package management with comprehensive retry logic"""
    
    def __init__(self, logger: Logger):
        self.logger = logger
        self.installed_packages = set()
        self.failed_packages = set()
        self.cleaner = SystemCleaner(logger)
        self.install_lock = threading.Lock()
        
    def install_packages(self, packages: List[str], max_workers: int = 2) -> Dict[str, bool]:
        """Install packages with parallel execution and retry logic"""
        self.logger.log("PROCESS", f"Installing {len(packages)} packages with {max_workers} workers", "installer")
        
        # Clean system before installation
        self.cleaner.remove_db_locks()
        
        results = {}
        
        # Process packages in smaller batches to avoid overwhelming the system
        batch_size = max(1, len(packages) // max_workers)
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_package = {}
            
            for i, package in enumerate(packages):
                future = executor.submit(self._install_package_with_retry, package, i)
                future_to_package[future] = package
            
            for future in as_completed(future_to_package):
                package = future_to_package[future]
                try:
                    success = future.result()
                    results[package] = success
                    
                    with self.install_lock:
                        if success:
                            self.installed_packages.add(package)
                            self.logger.log_package(package, "success")
                        else:
                            self.failed_packages.add(package)
                            
                except Exception as e:
                    self.logger.log("ERROR", f"Exception during installation of {package}: {str(e)}", "installer")
                    results[package] = False
                    with self.install_lock:
                        self.failed_packages.add(package)
        
        # Final cleanup
        self.cleaner.remove_db_locks()
        
        return results
    
    def _install_package_with_retry(self, package: str, index: int) -> bool:
        """Install a single package with comprehensive retry logic"""
        self.logger.log("PROCESS", f"[{index+1}] Installing {package}...", "installer")
        
        # Check if already installed first
        if self._is_package_installed(package):
            self.logger.log("INFO", f"[{index+1}] {package} already installed", "installer")
            return True
        
        # Try different installation methods
        install_methods = [
            self._install_from_official_repos,
            self._install_from_blackarch,
            self._install_from_aur_helper,
            self._install_with_force
        ]
        
        for method_index, install_method in enumerate(install_methods):
            try:
                def attempt_install():
                    return install_method(package, index, method_index)
                
                if RetryManager.retry_with_backoff(
                    attempt_install,
                    exceptions=(subprocess.CalledProcessError, subprocess.TimeoutExpired, IOError)
                ):
                    return True
                    
            except Exception as e:
                self.logger.log("RETRY", f"[{index+1}] Method {method_index+1} failed for {package}: {str(e)}", "installer")
                continue
        
        # All methods failed
        self.logger.log("ERROR", f"[{index+1}] All installation methods failed for {package}", "installer")
        self.logger.log_package(package, "failed", "All methods exhausted")
        return False
    
    def _is_package_installed(self, package: str) -> bool:
        """Check if package is already installed"""
        try:
            result = subprocess.run(
                ["pacman", "-Qi", package],
                capture_output=True,
                text=True,
                timeout=30
            )
            return result.returncode == 0
        except:
            return False
    
    def _install_from_official_repos(self, package: str, index: int, method: int) -> bool:
        """Install from official Arch repositories"""
        result = subprocess.run(
            ["pacman", "-S", "--noconfirm", "--needed", "--disable-download-timeout", package],
            capture_output=True,
            text=True,
            timeout=KygoXConfig.INSTALL_TIMEOUT
        )
        
        if result.returncode == 0:
            self.logger.log("SUCCESS", f"[{index+1}] Installed {package} from official repos", "installer")
            return True
        else:
            error_msg = result.stderr.strip() or "Unknown error"
            raise subprocess.CalledProcessError(result.returncode, "pacman", error_msg)
    
    def _install_from_blackarch(self, package: str, index: int, method: int) -> bool:
        """Install from BlackArch repository"""
        result = subprocess.run(
            ["pacman", "-S", "--noconfirm", "--needed", "--disable-download-timeout", f"blackarch/{package}"],
            capture_output=True,
            text=True,
            timeout=KygoXConfig.INSTALL_TIMEOUT
        )
        
        if result.returncode == 0:
            self.logger.log("SUCCESS", f"[{index+1}] Installed {package} from BlackArch", "installer")
            return True
        else:
            error_msg = result.stderr.strip() or "Unknown error"
            raise subprocess.CalledProcessError(result.returncode, "pacman", error_msg)
    
    def _install_from_aur_helper(self, package: str, index: int, method: int) -> bool:
        """Install using AUR helper if available"""
        aur_helpers = ["yay", "paru", "trizen", "pikaur"]
        
        for helper in aur_helpers:
            if shutil.which(helper):
                result = subprocess.run(
                    [helper, "-S", "--noconfirm", "--needed", package],
                    capture_output=True,
                    text=True,
                    timeout=KygoXConfig.INSTALL_TIMEOUT
                )
                
                if result.returncode == 0:
                    self.logger.log("SUCCESS", f"[{index+1}] Installed {package} via {helper}", "installer")
                    return True
        
        raise subprocess.CalledProcessError(1, "aur_helper", "No AUR helper available or all failed")
    
    def _install_with_force(self, package: str, index: int, method: int) -> bool:
        """Force install with relaxed constraints"""
        result = subprocess.run(
            ["pacman", "-S", "--noconfirm", "--needed", "--overwrite", "*", "--disable-download-timeout", package],
            capture_output=True,
            text=True,
            timeout=KygoXConfig.INSTALL_TIMEOUT
        )
        
        if result.returncode == 0:
            self.logger.log("SUCCESS", f"[{index+1}] Force installed {package}", "installer")
            return True
        else:
            error_msg = result.stderr.strip() or "Unknown error"
            raise subprocess.CalledProcessError(result.returncode, "pacman", error_msg)

class KygoXCore:
    """Main KygoX toolkit engine with comprehensive error handling"""
    
    def __init__(self):
        self.config = KygoXConfig()
        self.logger = Logger(self.config.LOG_DIR)
        self.system_info = SystemInfo()
        self.cleaner = SystemCleaner(self.logger)
        self.keyring_manager = KeyringManager(self.logger, self.config.CACHE_DIR)
        self.package_manager = PackageManager(self.logger)
        
        # Signal handlers
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)
    
    def _signal_handler(self, signum, frame):
        """Handle interruption signals"""
        self.logger.log("WARNING", "Installation interrupted by user", "system")
        self.cleanup()
        sys.exit(130)
    
    def cleanup(self):
        """Comprehensive cleanup of temporary files and resources"""
        try:
            self.logger.log("PROCESS", "Performing cleanup operations", "system")
            
            # Clean cache if exists
            if self.config.CACHE_DIR.exists():
                temp_files = list(self.config.CACHE_DIR.glob("*.tmp")) + \
                           list(self.config.CACHE_DIR.glob("*.part")) + \
                           list(self.config.CACHE_DIR.glob("*.download"))
                for temp_file in temp_files:
                    temp_file.unlink(missing_ok=True)
            
            # Remove database locks
            self.cleaner.remove_db_locks()
            
            # Clean pacman cache
            self.cleaner.cleanup_pacman_cache()
            
            self.logger.log("SUCCESS", "Cleanup completed", "system")
            
        except Exception as e:
            self.logger.log("WARNING", f"Cleanup warning: {str(e)}", "system")
    
    def run(self):
        """Main execution method with comprehensive error handling"""
        try:
            self._display_banner()
            self._check_prerequisites()
            self._prepare_system()
            self._setup_environment()
            self._install_toolkit()
            self._generate_report()
            self._final_cleanup()
            
        except KeyboardInterrupt:
            self.logger.log("WARNING", "Installation interrupted by user", "system")
            self.cleanup()
            sys.exit(130)
        except Exception as e:
            self.logger.log("ERROR", f"Fatal error: {str(e)}", "system")
            self.cleanup()
            sys.exit(1)
    
    def _display_banner(self):
        """Display application banner"""
        banner = f"""
{ColorManager.CYAN}
██╗  ██╗██╗   ██╗ ██████╗  ██████╗ ██╗  ██╗
██║ ██╔╝╚██╗ ██╔╝██╔════╝ ██╔═══██╗╚██╗██╔╝
███████╔╝ ╚████╔╝ ██║  ███╗██║   ██║ ╚███╔╝ 
██╔══██╗   ╚██╔╝  ██║   ██║██║   ██║ ██╔██╗ 
██║  ██║   ██║   ╚██████╔╝╚██████╔╝██╔╝ ██╗
╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
{ColorManager.RESET}
{ColorManager.BOLD}ARCH LINUX PENETRATION TESTING TOOLKIT{ColorManager.RESET}
{ColorManager.DIM}Professional Security Arsenal Deployment{ColorManager.RESET}

{ColorManager.BOLD}Version: {self.config.VERSION} | {self.config.VERSION_NAME}{ColorManager.RESET}
{ColorManager.DIM}Repository: {self.config.REPO_URL}{ColorManager.RESET}
"""
        print(banner)
    
    def _check_prerequisites(self):
        """Check system prerequisites"""
        self.logger.log("PROCESS", "Checking system prerequisites", "system")
        
        # Check if running as root
        if os.geteuid() != 0:
            self.logger.log("ERROR", "KygoX must be run as root", "system")
            sys.exit(1)
        
        # Check Arch compatibility
        if not self.system_info.is_arch_based:
            self.logger.log("ERROR", "KygoX requires Arch Linux or Arch-based distribution", "system")
            sys.exit(1)
        
        # Display system information
        self.logger.log("INFO", f"Distribution: {self.system_info.distro_info['name']}", "system")
        self.logger.log("INFO", f"Pacman version: {self.system_info.pacman_version}", "system")
        self.logger.log("INFO", f"RAM: {self.system_info.system_specs['ram_mb']}MB", "system")
        self.logger.log("INFO", f"CPU cores: {self.system_info.system_specs['cpu_cores']}", "system")
        self.logger.log("INFO", f"Free disk space: {self.system_info.system_specs['disk_free_gb']}GB", "system")
        
        # Check minimum requirements
        if self.system_info.system_specs['disk_free_gb'] < 5:
            self.logger.log("WARNING", "Low disk space detected (<5GB)", "system")
        
        if self.system_info.system_specs['ram_mb'] < 2048:
            self.logger.log("WARNING", "Low RAM detected (<2GB)", "system")
        
        self.logger.log("SUCCESS", "Prerequisites check completed", "system")
    
    def _prepare_system(self):
        """Prepare system for installation"""
        self.logger.log("PROCESS", "Preparing system for installation", "system")
        
        # Clean system thoroughly
        self.cleaner.remove_db_locks()
        self.cleaner.cleanup_pacman_cache()
        self.cleaner.refresh_pacman_databases()
        
        self.logger.log("SUCCESS", "System preparation completed", "system")
    
    def _setup_environment(self):
        """Setup installation environment"""
        self.logger.log("PROCESS", "Setting up installation environment", "system")
        
        # Create directories
        self.config.LOG_DIR.mkdir(parents=True, exist_ok=True)
        self.config.BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        self.config.CACHE_DIR.mkdir(parents=True, exist_ok=True)
        
        # Update system with retry
        self.logger.log("PROCESS", "Updating system packages", "system")
        
        def update_system():
            result = subprocess.run(
                ["pacman", "-Syu", "--noconfirm", "--disable-download-timeout"],
                capture_output=True,
                text=True,
                timeout=1200
            )
            if result.returncode != 0:
                raise subprocess.CalledProcessError(result.returncode, "pacman", result.stderr)
            return True
        
        if RetryManager.retry_with_backoff(update_system):
            self.logger.log("SUCCESS", "System updated successfully", "system")
        else:
            self.logger.log("WARNING", "System update had issues, continuing", "system")
        
        # Setup BlackArch keyring with multiple methods
        if not self.keyring_manager.setup_blackarch_keyring():
            self.logger.log("WARNING", "BlackArch keyring setup failed, continuing with core tools only", "system")
        
        self.logger.log("SUCCESS", "Environment setup completed", "system")
    
    def _install_toolkit(self):
        """Install security toolkit with comprehensive retry logic"""
        self.logger.log("PROCESS", "Starting comprehensive toolkit installation", "installer")
        
        # Combine core and trending tools
        all_tools = list(set(self.config.CORE_TOOLS + self.config.TRENDING_2025))
        
        # Remove any empty or invalid package names
        all_tools = [pkg for pkg in all_tools if pkg and pkg.strip()]
        
        self.logger.log("INFO", f"Installing {len(all_tools)} security tools", "installer")
        
        # Install packages with retry logic
        results = self.package_manager.install_packages(all_tools, max_workers=2)
        
        # Summary
        successful = sum(1 for success in results.values() if success)
        failed = len(results) - successful
        success_rate = (successful / len(results)) * 100 if results else 0
        
        self.logger.log("INFO", f"Installation completed: {successful} successful, {failed} failed ({success_rate:.1f}% success rate)", "installer")
        
        # If success rate is low, try failed packages again with single thread
        if success_rate < 50 and self.package_manager.failed_packages:
            self.logger.log("PROCESS", "Retrying failed packages with single-threaded approach", "installer")
            failed_list = list(self.package_manager.failed_packages)
            self.package_manager.failed_packages.clear()
            
            retry_results = self.package_manager.install_packages(failed_list, max_workers=1)
            retry_successful = sum(1 for success in retry_results.values() if success)
            
            if retry_successful > 0:
                self.logger.log("SUCCESS", f"Retry successful: {retry_successful} additional packages installed", "installer")
    
    def _generate_report(self):
        """Generate comprehensive installation report"""
        self.logger.log("PROCESS", "Generating comprehensive installation report", "system")
        
        report_file = self.config.LOG_DIR / "installation_report.txt"
        
        try:
            with open(report_file, 'w', encoding='utf-8') as f:
                f.write(f"KygoX Installation Report\n")
                f.write(f"=" * 80 + "\n\n")
                f.write(f"Version: {self.config.VERSION} ({self.config.VERSION_NAME})\n")
                f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"System: {self.system_info.distro_info['name']}\n")
                f.write(f"Pacman Version: {self.system_info.pacman_version}\n")
                f.write(f"RAM: {self.system_info.system_specs['ram_mb']}MB\n")
                f.write(f"CPU Cores: {self.system_info.system_specs['cpu_cores']}\n")
                f.write(f"Disk Space: {self.system_info.system_specs['disk_free_gb']}GB free\n\n")
                
                total_attempted = len(self.config.CORE_TOOLS + self.config.TRENDING_2025)
                installed_count = len(self.package_manager.installed_packages)
                failed_count = len(self.package_manager.failed_packages)
                success_rate = (installed_count / total_attempted) * 100 if total_attempted > 0 else 0
                
                f.write(f"INSTALLATION SUMMARY\n")
                f.write(f"-" * 50 + "\n")
                f.write(f"Total Packages Attempted: {total_attempted}\n")
                f.write(f"Successfully Installed: {installed_count}\n")
                f.write(f"Failed Installations: {failed_count}\n")
                f.write(f"Success Rate: {success_rate:.1f}%\n\n")
                
                if self.package_manager.installed_packages:
                    f.write("SUCCESSFULLY INSTALLED PACKAGES\n")
                    f.write("-" * 50 + "\n")
                    for pkg in sorted(self.package_manager.installed_packages):
                        f.write(f"  ✓ {pkg}\n")
                    f.write("\n")
                
                if self.package_manager.failed_packages:
                    f.write("FAILED PACKAGE INSTALLATIONS\n")
                    f.write("-" * 50 + "\n")
                    for pkg in sorted(self.package_manager.failed_packages):
                        f.write(f"  ✗ {pkg}\n")
                    f.write("\n")
                
                f.write("TOOL CATEGORIES INSTALLED\n")
                f.write("-" * 50 + "\n")
                categories = {
                    "Network Tools": ["nmap", "masscan", "rustscan", "wireshark-qt", "tcpdump"],
                    "Web Security": ["burpsuite", "owasp-zap", "sqlmap", "nikto", "gobuster"],
                    "Exploitation": ["metasploit", "empire", "beef", "searchsploit"],
                    "Password Tools": ["john", "hashcat", "hydra", "medusa"],
                    "Forensics": ["volatility3", "autopsy", "binwalk", "foremost"],
                    "Reverse Engineering": ["ghidra", "radare2", "gdb", "strings"],
                    "Mobile Security": ["apktool", "jadx", "frida", "objection"],
                    "OSINT": ["theharvester", "recon-ng", "sherlock", "spiderfoot"]
                }
                
                for category, tools in categories.items():
                    installed_in_category = [tool for tool in tools if tool in self.package_manager.installed_packages]
                    if installed_in_category:
                        f.write(f"{category}: {len(installed_in_category)}/{len(tools)} tools\n")
                        for tool in installed_in_category:
                            f.write(f"    • {tool}\n")
                        f.write("\n")
                
                f.write(f"DETAILED LOGS\n")
                f.write(f"-" * 50 + "\n")
                f.write(f"Main Log: {self.config.LOG_DIR / 'installation.log'}\n")
                f.write(f"Error Log: {self.config.LOG_DIR / 'errors.log'}\n")
                f.write(f"Success Log: {self.config.LOG_DIR / 'successful_packages.log'}\n")
                f.write(f"Failed Log: {self.config.LOG_DIR / 'failed_packages.log'}\n")
                f.write(f"Retry Log: {self.config.LOG_DIR / 'retries.log'}\n")
                f.write(f"Cache Directory: {self.config.CACHE_DIR}\n\n")
                
                f.write(f"RECOMMENDATIONS\n")
                f.write(f"-" * 50 + "\n")
                if failed_count > 0:
                    f.write(f"• Review failed packages log for troubleshooting\n")
                    f.write(f"• Consider manual installation of critical failed tools\n")
                    f.write(f"• Run 'pacman -Syu' to update system packages\n")
                
                if success_rate > 80:
                    f.write(f"• Excellent installation rate! System ready for penetration testing\n")
                elif success_rate > 60:
                    f.write(f"• Good installation rate. Most essential tools available\n")
                else:
                    f.write(f"• Consider troubleshooting system issues and re-running installation\n")
                
                f.write(f"• Verify BlackArch repository is properly configured\n")
                f.write(f"• Consider installing AUR helper (yay, paru) for additional tools\n")
                
        except Exception as e:
            self.logger.log("ERROR", f"Failed to generate report: {str(e)}", "system")
            return
        
        self.logger.log("SUCCESS", f"Installation report saved to {report_file}", "system")
    
    def _final_cleanup(self):
        """Perform final cleanup operations"""
        self.logger.log("PROCESS", "Performing final cleanup", "system")
        
        # Clean system one final time
        self.cleaner.remove_db_locks()
        self.cleaner.cleanup_pacman_cache()
        
        # Generate toolkit summary file
        toolkit_summary = self.config.LOG_DIR / "installed_tools.txt"
        try:
            with open(toolkit_summary, 'w', encoding='utf-8') as f:
                f.write("KygoX Installed Security Tools\n")
                f.write("=" * 50 + "\n")
                for tool in sorted(self.package_manager.installed_packages):
                    f.write(f"{tool}\n")
        except Exception:
            pass
        
        self.logger.log("SUCCESS", "KygoX installation completed successfully!", "system")
        print(f"\n{ColorManager.SUCCESS} {ColorManager.BOLD}Installation Complete!{ColorManager.RESET}")
        print(f"{ColorManager.INFO} Installed: {len(self.package_manager.installed_packages)} tools")
        print(f"{ColorManager.INFO} Report: {self.config.LOG_DIR / 'installation_report.txt'}")

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="KygoX - Arch Linux Penetration Testing Toolkit",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Examples:
  python3 {sys.argv[0]}              # Full installation with retry logic
  python3 {sys.argv[0]} --core-only  # Core tools only
  python3 {sys.argv[0]} --check      # System check only
  python exceptions as e:
                if attempt == max_retries:
                    raise e
                
                wait_time = delay * (backoff ** attempt) + random.uniform(0, 1)
                time.sleep(wait_time)
        
        return None

class Logger:
    """Advanced logging system with multiple output formats"""
    
    def __init__(self, log_dir: Path):
        self.log_dir = log_dir
        self.log_dir.mkdir(parents=True, exist_ok=True)
        
        self.main_log = log_dir / "installation.log"
        self.error_log = log_dir / "errors.log"
        self.success_log = log_dir / "successful_packages.log"
        self.failed_log = log_dir / "failed_packages.log"
        self.retry_log = log_dir / "retries.log"
        
        # Setup logging with custom formatter
        class ComponentFormatter(logging.Formatter):
            def format(self, record):
                if not hasattr(record, 'component'):
                    record.component = 'system'
                return super().format(record)
        
        formatter = ComponentFormatter('%(asctime)s - %(levelname)s - %(component)s - %(message)s')
        
        # File handler
        file_handler = logging.FileHandler(self.main_log)
        file_handler.setFormatter(formatter)
        
        # Console handler with reduced verbosity
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARNING)
        console_handler.setFormatter(formatter)
        
        logging.basicConfig(
            level=logging.DEBUG,
            handlers=[file_handler]
        )
        
        self.logger = logging.getLogger('KygoX')
        
    def log(self, level: str, message: str, component: str = "system", display: bool = True):
        """Log message with level and component"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Write to main log
        try:
            with open(self.main_log, 'a', encoding='utf-8') as f:
                f.write(f"[{timestamp}] [{level}] [{component}] {message}\n")
        except Exception:
            pass
        
        # Write to specific logs
        if level == "ERROR":
            try:
                with open(self.error_log, 'a', encoding='utf-8') as f:
                    f.write(f"[{timestamp}] [{component}] {message}\n")
            except Exception:
                pass
        elif level == "RETRY":
            try:
                with open(self.retry_log, 'a', encoding='utf-8') as f:
                    f.write(f"[{timestamp}] [{component}] {message}\n")
            except Exception:
                pass
        
        # Display to console
        if display:
            color_map = {
                "SUCCESS": ColorManager.SUCCESS,
                "ERROR": ColorManager.ERROR,
                "INFO": ColorManager.INFO,
                "WARNING": ColorManager.WARNING,
                "PROCESS": ColorManager.PROCESS,
                "SECURITY": ColorManager.SECURITY,
                "RETRY": ColorManager.RETRY
            }
            
            indicator = color_map.get(level, f"[{level}]")
            print(f"{indicator} {message}")
    
    def log_package(self, package: str, status: str, details: str = ""):
        """Log package installation status"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        try:
            if status == "success":
                with open(self.success_log, 'a', encoding='utf-8') as f:
                    f.write(f"[{timestamp}] {package}\n")
            elif status == "failed":
                with open(self.failed_log, 'a', encoding='utf-8') as f:
                    f.write(f"[{timestamp}] {package}: {details}\n")
        except Exception:
            pass

class SystemCleaner:
    """System cleanup utilities"""
    
    def __init__(self, logger: Logger):
        self.logger = logger
    
    def cleanup_pacman_cache(self) -> bool:
        """Clean pacman cache thoroughly"""
        try:
            self.logger.log("PROCESS", "Cleaning pacman cache", "cleaner")
            
            # Clean all cache
            result = subprocess.run(
                ["pacman", "-Scc", "--noconfirm"],
                capture_output=True,
                text=True,
                timeout=300
            )
            
            if result.returncode == 0:
                self.logger.log("SUCCESS", "Pacman cache cleaned", "cleaner")
                return True
            else:
                self.logger.log("WARNING", f"Cache cleanup warning: {result.stderr}", "cleaner")
                return False
                
        except Exception as e:
            self.logger.log("ERROR", f"Cache cleanup failed: {str(e)}", "cleaner")
            return False
    
    def remove_db_locks(self) -> bool:
        """Remove pacman database locks"""
        try:
            lock_files = [
                "/var/lib/pacman/db.lck",
                "/var/cache/pacman/pkg/db.lck"
            ]
            
            removed_any = False
            for lock_file in lock_files:
                if Path(lock_file).exists():
                    os.remove(lock_file)
                    self.logger.log("SUCCESS", f"Removed lock file: {lock_file}", "cleaner")
                    removed_any = True
            
            if not removed_any:
                self.logger.log("INFO", "No database locks found", "cleaner")
            
            return True
            
        except Exception as e:
            self.logger.log("ERROR", f"Failed to remove db locks: {str(e)}", "cleaner")
            return False
    
    def refresh_pacman_databases(self) -> bool:
        """Refresh pacman databases"""
        try:
            self.logger.log("PROCESS", "Refreshing package databases", "cleaner")
            
            # Force refresh
            result = subprocess.run(
                ["pacman", "-Syy"],
                capture_output=True,
                text=True,
                timeout=300
            )
            
            if result.returncode == 0:
                self.logger.log("SUCCESS", "Package databases refreshed", "cleaner")
                return True
            else:
                self.logger.log("WARNING", f"Database refresh warning: {result.stderr}", "cleaner")
                return False
                
        except Exception as e:
            self.logger.log("ERROR", f"Database refresh failed: {str(e)}", "cleaner")
            return False

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
            self.distro_info["id"] in ["arch", "manjaro", "endeavouros", "garuda", "artix", "blackarch", "archcraft"]
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
    """BlackArch keyring and signature verification with multiple methods"""
    
    def __init__(self, logger: Logger, cache_dir: Path):
        self.logger = logger
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.cleaner = SystemCleaner(logger)
        
    def setup_blackarch_keyring(self) -> bool:
        """Setup BlackArch keyring with multiple fallback methods"""
        self.logger.log("PROCESS", "Setting up BlackArch keyring with multiple methods", "keyring")
        
        # Clean system first
        self.cleaner.remove_db_locks()
        self.cleaner.cleanup_pacman_cache()
        
        # Method 1: Try official strap.sh script
        if self._try_strap_installation():
            return True
        
        # Method 2: Try direct keyring package installation
        if self._try_keyring_package_installation():
            return True
        
        # Method 3: Try manual keyring setup
        if self._try_manual_keyring_setup():
            return True
        
        # Method 4: Try alternative installation
        if self._try_alternative_keyring():
            return True
        
        self.logger.log("WARNING", "All keyring installation methods failed", "keyring")
        return False
    
    def _try_strap_installation(self) -> bool:
        """Try BlackArch strap.sh installation"""
        self.logger.log("PROCESS", "Trying strap.sh installation method", "keyring")
        
        for strap_url in KygoXConfig.BLACKARCH_STRAP_URLS:
            try:
                strap_file = self.cache_dir / "strap.sh"
                
                # Download strap script with retry
                def download_strap():
                    response = requests.get(strap_url, timeout=KygoXConfig.DOWNLOAD_TIMEOUT)
                    response.raise_for_status()
                    with open(strap_file, 'wb') as f:
                        f.write(response.content)
                    return True
                
                if RetryManager.retry_with_backoff(
                    download_strap,
                    exceptions=(requests.RequestException, IOError)
                ):
                    # Make executable and run
                    strap_file.chmod(0o755)
                    
                    def run_strap():
                        result = subprocess.run(
                            ["bash", str(strap_file)],
                            capture_output=True,
                            text=True,
                            timeout=KygoXConfig.INSTALL_TIMEOUT,
                            cwd="/tmp"
                        )
                        if result.returncode == 0:
                            return True
                        else:
                            raise subprocess.CalledProcessError(result.returncode, "strap.sh", result.stderr)
                    
                    if RetryManager.retry_with_backoff(
                        run_strap,
                        exceptions=(subprocess.CalledProcessError, subprocess.TimeoutExpired)
                    ):
                        self.logger.log("SUCCESS", "BlackArch installed via strap.sh", "keyring")
                        self._verify_blackarch_setup()
                        return True
                
            except Exception as e:
                self.logger.log("WARNING", f"Strap method failed for {strap_url}: {str(e)}", "keyring")
                continue
        
        return False
    
    def _try_keyring_package_installation(self) -> bool:
        """Try direct keyring package installation"""
        self.logger.log("PROCESS", "Trying direct keyring package installation", "keyring")
        
        for keyring_url in KygoXConfig.BLACKARCH_KEYRING_URLS:
            try:
                keyring_file = self.cache_dir / "blackarch-keyring.pkg.tar.xz"
                
                # Download keyring with retry
                def download_keyring():
                    self._download_file_with_progress(keyring_url, keyring_file)
                    return True
                
                if RetryManager.retry_with_backoff(
                    download_keyring,
                    exceptions=(requests.RequestException, IOError)
                ):
                    # Install keyring
                    def install_keyring():
                        result = subprocess.run(
                            ["pacman", "-U", "--noconfirm", "--overwrite", "*", str(keyring_file)],
                            capture_output=True,
                            text=True,
                            timeout=KygoXConfig.INSTALL_TIMEOUT
                        )
                        if result.returncode == 0:
                            return True
                        else:
                            raise subprocess.CalledProcessError(result.returncode, "pacman", result.stderr)
                    
                    if RetryManager.retry_with_backoff(
                        install_keyring,
                        exceptions=(subprocess.CalledProcessError, subprocess.TimeoutExpired)
                    ):
                        self.logger.log("SUCCESS", "BlackArch keyring installed directly", "keyring")
                        self._add_blackarch_repo()
                        return True
                
            except Exception as e:
                self.logger.log("WARNING", f"Direct keyring method failed for {keyring_url}: {str(e)}", "keyring")
                continue
        
        return False
    
    def _try_manual_keyring_setup(self) -> bool:
        """Try manual keyring setup"""
        self.logger.log("PROCESS", "Trying manual keyring setup", "keyring")
        
        try:
            # Initialize pacman keyring
            def init_keyring():
                result = subprocess.run(
                    ["pacman-key", "--init"],
                    capture_output=True,
                    text=True,
                    timeout=300
                )
                if result.returncode != 0:
                    raise subprocess.CalledProcessError(result.returncode, "pacman-key", result.stderr)
                return True
            
            # Populate keyring
            def populate_keyring():
                result = subprocess.run(
                    ["pacman-key", "--populate", "archlinux"],
                    capture_output=True,
                    text=True,
                    timeout=300
                )
                if result.returncode != 0:
                    raise subprocess.CalledProcessError(result.returncode, "pacman-key", result.stderr)
                return True
            
            # Add BlackArch key
            def add_blackarch_key():
                # Download and add BlackArch master key
                result = subprocess.run([
                    "curl", "-O", "https://blackarch.org/keyring/blackarch-keyring.pkg.tar.xz"
                ], cwd=str(self.cache_dir), capture_output=True, text=True, timeout=120)
                
                if result.returncode == 0:
                    # Extract and install
                    result2 = subprocess.run([
                        "pacman", "-U", "--noconfirm", 
                        str(self.cache_dir / "blackarch-keyring.pkg.tar.xz")
                    ], capture_output=True, text=True, timeout=300)
                    
                    if result2.returncode == 0:
                        return True
                
                raise subprocess.CalledProcessError(1, "manual keyring", "Failed to add BlackArch key")
            
            # Execute steps with retry
            if (RetryManager.retry_with_backoff(init_keyring) and
                RetryManager.retry_with_backoff(populate_keyring) and
                RetryManager.retry_with_backoff(add_blackarch_key)):
                
                self.logger.log("SUCCESS", "Manual keyring setup completed", "keyring")
                self._add_blackarch_repo()
                return True
                
        except Exception as e:
            self.logger.log("WARNING", f"Manual keyring setup failed: {str(e)}", "keyring")
        
        return False
    
    def _try_alternative_keyring(self) -> bool:
        """Try alternative keyring installation method"""
        self.logger.log("PROCESS", "Trying alternative keyring method", "keyring")
        
        try:
            # Skip signature verification and force install
            commands = [
                ["pacman-key", "--init"],
                ["pacman-key", "--populate", "archlinux"],
                ["pacman", "-Sy", "--noconfirm"],
            ]
            
            for cmd in commands:
                def run_cmd():
                    result = subprocess.run(
                        cmd,
                        capture_output=True,
                        text=True,
                        timeout=300
                    )
                    if result.returncode != 0:
                        raise subprocess.CalledProcessError(result.returncode, " ".join(cmd), result.stderr)
                    return True
                
                if not RetryManager.retry_with_backoff(run_cmd):
                    return False
            
            # Add BlackArch repo without keyring first
            self._add_blackarch_repo_unsafe()
            
            # Try to install BlackArch keyring from repo
            def install_from_repo():
                result = subprocess.run(
                    ["pacman", "-S", "--noconfirm", "--disable-download-timeout", "blackarch-keyring"],
                    capture_output=True,
                    text=True,
                    timeout=600
                )
                if result.returncode == 0:
                    return True
                raise subprocess.CalledProcessError(result.returncode, "pacman", result.stderr)
            
            if RetryManager.retry_with_backoff(install_from_repo):
                self.logger.log("SUCCESS", "Alternative keyring method succeeded", "keyring")
                return True
                
        except
