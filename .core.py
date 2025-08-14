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
    
    VERSION = "0.2.0-alpha"
    VERSION_NAME = "Cobra"
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
    
    # Enhanced security tools collection - 2025
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
    
    # Background colors for better visual impact
    BG_RED = Back.RED
    BG_GREEN = Back.GREEN
    BG_YELLOW = Back.YELLOW
    BG_BLUE = Back.BLUE
    BG_CYAN = Back.CYAN
    BG_WHITE = Back.WHITE
    
    # Enhanced status indicators with better Unicode symbols
    SUCCESS = f"{BG_GREEN}{WHITE}   ✅ SUCCESS   {RESET}"
    ERROR = f"{BG_RED}{WHITE}   ❌ ERROR   {RESET}"
    INFO = f"{BG_BLUE}{WHITE}   ℹ️  INFO   {RESET}"
    WARNING = f"{BG_YELLOW}{DARK}   ⚠️  WARNING   {RESET}"
    PROCESS = f"{BG_CYAN}{WHITE}   ⚡ PROCESS   {RESET}"
    SECURITY = f"{CYAN}🔒 SECURITY{RESET}"
    RETRY = f"{YELLOW}🔄 RETRY{RESET}"
    DOWNLOAD = f"{BLUE}📥 DOWNLOAD{RESET}"
    INSTALL = f"{GREEN}📦 INSTALL{RESET}"
    
    # Progress indicators
    PROGRESS_CHARS = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    
    @classmethod
    def create_banner_line(cls, char="═", width=80):
        """Create a banner line with specified character"""
        return f"{cls.CYAN}{char * width}{cls.RESET}"
    
    @classmethod
    def create_progress_bar(cls, current, total, width=50):
        """Create a visual progress bar"""
        if total == 0:
            return f"[{'█' * width}] 100%"
        
        filled = int(width * current // total)
        bar = '█' * filled + '░' * (width - filled)
        percentage = (current / total) * 100
        
        return f"{cls.GREEN}[{bar}]{cls.RESET} {percentage:.1f}%"
    
    @classmethod
    def create_section_header(cls, title, width=80):
        """Create a visually appealing section header"""
        title_len = len(title)
        padding = (width - title_len - 2) // 2
        
        return f"""
{cls.create_banner_line("═", width)}
{cls.CYAN}{'═' * padding} {cls.BOLD}{cls.WHITE}{title}{cls.RESET}{cls.CYAN} {'═' * padding}{cls.RESET}
{cls.create_banner_line("═", width)}
"""

class ProgressSpinner:
    """Animated progress spinner for long-running operations"""
    
    def __init__(self, message="Processing"):
        self.message = message
        self.running = False
        self.thread = None
        
    def start(self):
        """Start the spinner animation"""
        self.running = True
        self.thread = threading.Thread(target=self._spin)
        self.thread.daemon = True
        self.thread.start()
        
    def stop(self, final_message=None):
        """Stop the spinner animation"""
        self.running = False
        if self.thread:
            self.thread.join()
        
        # Clear the line and show final message
        print(f"\r{' ' * (len(self.message) + 10)}\r", end="")
        if final_message:
            print(final_message)
    
    def _spin(self):
        """Internal spinner animation loop"""
        i = 0
        while self.running:
            char = ColorManager.PROGRESS_CHARS[i % len(ColorManager.PROGRESS_CHARS)]
            print(f"\r{ColorManager.CYAN}{char}{ColorManager.RESET} {self.message}...", end="", flush=True)
            time.sleep(0.1)
            i += 1

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
            except exceptions as e:
                if attempt == max_retries:
                    raise e
                
                wait_time = delay * (backoff ** attempt) + random.uniform(0, 1)
                print(f"{ColorManager.RETRY} Attempt {attempt + 1}/{max_retries + 1} failed: {str(e)[:100]}...")
                print(f"{ColorManager.INFO} Retrying in {wait_time:.1f} seconds...")
                time.sleep(wait_time)
        
        return None

class Logger:
    """Advanced logging system with multiple output formats and enhanced visuals"""
    
    def __init__(self, log_dir: Path):
        self.log_dir = log_dir
        self.log_dir.mkdir(parents=True, exist_ok=True)
        
        self.main_log = log_dir / "installation.log"
        self.error_log = log_dir / "errors.log"
        self.success_log = log_dir / "successful_packages.log"
        self.failed_log = log_dir / "failed_packages.log"
        self.retry_log = log_dir / "retries.log"
        
        # Statistics tracking
        self.stats = {
            "success_count": 0,
            "error_count": 0,
            "warning_count": 0,
            "retry_count": 0,
            "start_time": datetime.now()
        }
        
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
        """Enhanced log message with visual improvements"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Update statistics
        if level == "SUCCESS":
            self.stats["success_count"] += 1
        elif level == "ERROR":
            self.stats["error_count"] += 1
        elif level == "WARNING":
            self.stats["warning_count"] += 1
        elif level == "RETRY":
            self.stats["retry_count"] += 1
        
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
        
        # Enhanced display to console with better formatting
        if display:
            color_map = {
                "SUCCESS": ColorManager.SUCCESS,
                "ERROR": ColorManager.ERROR,
                "INFO": ColorManager.INFO,
                "WARNING": ColorManager.WARNING,
                "PROCESS": ColorManager.PROCESS,
                "SECURITY": ColorManager.SECURITY,
                "RETRY": ColorManager.RETRY,
                "DOWNLOAD": ColorManager.DOWNLOAD,
                "INSTALL": ColorManager.INSTALL
            }
            
            indicator = color_map.get(level, f"[{level}]")
            
            # Add component context for better debugging
            if component != "system":
                component_text = f"{ColorManager.DIM}[{component}]{ColorManager.RESET} "
            else:
                component_text = ""
                
            print(f"{indicator} {component_text}{message}")
    
    def log_package(self, package: str, status: str, details: str = ""):
        """Enhanced package logging with visual feedback"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        try:
            if status == "success":
                with open(self.success_log, 'a', encoding='utf-8') as f:
                    f.write(f"[{timestamp}] {package}\n")
                print(f"{ColorManager.INSTALL} {ColorManager.GREEN}✓{ColorManager.RESET} {package}")
            elif status == "failed":
                with open(self.failed_log, 'a', encoding='utf-8') as f:
                    f.write(f"[{timestamp}] {package}: {details}\n")
                print(f"{ColorManager.ERROR} {ColorManager.RED}✗{ColorManager.RESET} {package}: {details[:50]}...")
        except Exception:
            pass
    
    def show_statistics(self):
        """Display installation statistics with enhanced visuals"""
        elapsed = datetime.now() - self.stats["start_time"]
        
        print(ColorManager.create_section_header("INSTALLATION STATISTICS"))
        
        stats_display = [
            ("Successful Operations", self.stats["success_count"], ColorManager.GREEN),
            ("Errors Encountered", self.stats["error_count"], ColorManager.RED),
            ("Warnings Generated", self.stats["warning_count"], ColorManager.YELLOW),
            ("Retry Operations", self.stats["retry_count"], ColorManager.CYAN),
            ("Total Elapsed Time", str(elapsed).split('.')[0], ColorManager.BLUE)
        ]
        
        for label, value, color in stats_display:
            print(f"{ColorManager.INFO} {label}: {color}{value}{ColorManager.RESET}")
        
        print(ColorManager.create_banner_line())

class SystemCleaner:
    """Enhanced system cleanup utilities with progress indicators"""
    
    def __init__(self, logger: Logger):
        self.logger = logger
    
    def cleanup_pacman_cache(self) -> bool:
        """Clean pacman cache thoroughly with progress indication"""
        spinner = ProgressSpinner("Cleaning pacman cache")
        spinner.start()
        
        try:
            self.logger.log("PROCESS", "Cleaning pacman cache", "cleaner")
            
            # Clean all cache
            result = subprocess.run(
                ["pacman", "-Scc", "--noconfirm"],
                capture_output=True,
                text=True,
                timeout=300
            )
            
            spinner.stop()
            
            if result.returncode == 0:
                self.logger.log("SUCCESS", "Pacman cache cleaned successfully", "cleaner")
                return True
            else:
                self.logger.log("WARNING", f"Cache cleanup warning: {result.stderr}", "cleaner")
                return False
                
        except Exception as e:
            spinner.stop()
            self.logger.log("ERROR", f"Cache cleanup failed: {str(e)}", "cleaner")
            return False
    
    def remove_db_locks(self) -> bool:
        """Remove pacman database locks with enhanced feedback"""
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
        """Refresh pacman databases with progress indication"""
        spinner = ProgressSpinner("Refreshing package databases")
        spinner.start()
        
        try:
            self.logger.log("PROCESS", "Refreshing package databases", "cleaner")
            
            # Force refresh
            result = subprocess.run(
                ["pacman", "-Syy"],
                capture_output=True,
                text=True,
                timeout=300
            )
            
            spinner.stop()
            
            if result.returncode == 0:
                self.logger.log("SUCCESS", "Package databases refreshed", "cleaner")
                return True
            else:
                self.logger.log("WARNING", f"Database refresh warning: {result.stderr}", "cleaner")
                return False
                
        except Exception as e:
            spinner.stop()
            self.logger.log("ERROR", f"Database refresh failed: {str(e)}", "cleaner")
            return False

class SystemInfo:
    """Enhanced system information and compatibility checker"""
    
    def __init__(self):
        self.distro_info = self._detect_distribution()
        self.is_arch_based = self._check_arch_compatibility()
        self.pacman_version = self._get_pacman_version()
        self.system_specs = self._get_system_specs()
        self.python_info = self._get_python_info()
        
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
        """Get enhanced system specifications"""
        specs = {}
        
        try:
            # RAM
            with open("/proc/meminfo", "r") as f:
                for line in f:
                    if line.startswith("MemTotal:"):
                        specs["ram_mb"] = int(line.split()[1]) // 1024
                    elif line.startswith("MemAvailable:"):
                        specs["available_ram_mb"] = int(line.split()[1]) // 1024
                        break
            
            # CPU cores and model
            specs["cpu_cores"] = os.cpu_count()
            
            try:
                with open("/proc/cpuinfo", "r") as f:
                    for line in f:
                        if line.startswith("model name"):
                            specs["cpu_model"] = line.split(":")[1].strip()
                            break
            except:
                specs["cpu_model"] = "Unknown"
            
            # Disk space
            stat = shutil.disk_usage("/")
            specs["disk_total_gb"] = stat.total // (1024**3)
            specs["disk_free_gb"] = stat.free // (1024**3)
            specs["disk_used_gb"] = (stat.total - stat.free) // (1024**3)
            
            # System uptime
            try:
                with open("/proc/uptime", "r") as f:
                    uptime_seconds = float(f.read().split()[0])
                    specs["uptime_hours"] = int(uptime_seconds // 3600)
            except:
                specs["uptime_hours"] = 0
                
            # Load average
            try:
                with open("/proc/loadavg", "r") as f:
                    specs["load_average"] = f.read().split()[0]
            except:
                specs["load_average"] = "0.00"
            
        except Exception:
            specs = {
                "ram_mb": 0, "available_ram_mb": 0, "cpu_cores": 1, 
                "cpu_model": "Unknown", "disk_total_gb": 0, "disk_free_gb": 0,
                "disk_used_gb": 0, "uptime_hours": 0, "load_average": "0.00"
            }
            
        return specs
    
    def _get_python_info(self) -> Dict[str, str]:
        """Get Python environment information"""
        info = {}
        
        try:
            info["version"] = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
            info["executable"] = sys.executable
            info["platform"] = sys.platform
            
            # Check for virtual environment
            if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
                info["virtual_env"] = True
            else:
                info["virtual_env"] = False
                
        except Exception:
            info = {"version": "unknown", "executable": "unknown", "platform": "unknown", "virtual_env": False}
            
        return info
    
    def display_system_info(self):
        """Display enhanced system information with better formatting"""
        print(ColorManager.create_section_header("SYSTEM INFORMATION"))
        
        # Distribution info
        print(f"{ColorManager.INFO} Distribution: {ColorManager.CYAN}{self.distro_info['name']}{ColorManager.RESET}")
        if self.distro_info['version']:
            print(f"{ColorManager.INFO} Version: {ColorManager.CYAN}{self.distro_info['version']}{ColorManager.RESET}")
        
        # System specs with visual indicators
        ram_color = ColorManager.GREEN if self.system_specs['ram_mb'] >= 4096 else ColorManager.YELLOW if self.system_specs['ram_mb'] >= 2048 else ColorManager.RED
        disk_color = ColorManager.GREEN if self.system_specs['disk_free_gb'] >= 20 else ColorManager.YELLOW if self.system_specs['disk_free_gb'] >= 10 else ColorManager.RED
        cpu_color = ColorManager.GREEN if self.system_specs['cpu_cores'] >= 4 else ColorManager.YELLOW if self.system_specs['cpu_cores'] >= 2 else ColorManager.RED
        
        print(f"{ColorManager.INFO} CPU: {cpu_color}{self.system_specs['cpu_model']}{ColorManager.RESET} ({cpu_color}{self.system_specs['cpu_cores']} cores{ColorManager.RESET})")
        print(f"{ColorManager.INFO} RAM: {ram_color}{self.system_specs['ram_mb']}MB{ColorManager.RESET} (Available: {ram_color}{self.system_specs.get('available_ram_mb', 'N/A')}MB{ColorManager.RESET})")
        print(f"{ColorManager.INFO} Disk: {disk_color}{self.system_specs['disk_free_gb']}GB free{ColorManager.RESET} / {self.system_specs['disk_total_gb']}GB total")
        print(f"{ColorManager.INFO} System Load: {ColorManager.CYAN}{self.system_specs['load_average']}{ColorManager.RESET}")
        print(f"{ColorManager.INFO} Uptime: {ColorManager.CYAN}{self.system_specs['uptime_hours']} hours{ColorManager.RESET}")
        
        # Python info
        print(f"{ColorManager.INFO} Python: {ColorManager.CYAN}{self.python_info['version']}{ColorManager.RESET}")
        print(f"{ColorManager.INFO} Pacman: {ColorManager.CYAN}{self.pacman_version}{ColorManager.RESET}")
        
        # System warnings with enhanced visuals
        warnings = []
        if self.system_specs['ram_mb'] < 2048:
            warnings.append(f"{ColorManager.WARNING} Low RAM detected (<2GB) - Installation may be slow")
        if self.system_specs['disk_free_gb'] < 10:
            warnings.append(f"{ColorManager.WARNING} Low disk space (<10GB) - Installation may fail")
        if float(self.system_specs['load_average']) > self.system_specs['cpu_cores']:
            warnings.append(f"{ColorManager.WARNING} High system load detected")
        
        if warnings:
            print("\n" + ColorManager.create_section_header("SYSTEM WARNINGS"))
            for warning in warnings:
                print(warning)
        else:
            print(f"\n{ColorManager.SUCCESS} System meets all recommended requirements!")
        
        print(ColorManager.create_banner_line())

class KeyringManager:
    """Enhanced BlackArch keyring and signature verification with multiple methods"""
    
    def __init__(self, logger: Logger, cache_dir: Path):
        self.logger = logger
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.cleaner = SystemCleaner(logger)
        
    def setup_blackarch_keyring(self) -> bool:
        """Setup BlackArch keyring with enhanced visual feedback"""
        print(ColorManager.create_section_header("BLACKARCH KEYRING SETUP"))
        self.logger.log("PROCESS", "Setting up BlackArch keyring with multiple methods", "keyring")
        
        # Clean system first
        self.cleaner.remove_db_locks()
        self.cleaner.cleanup_pacman_cache()
        
        methods = [
            ("Official strap.sh script", self._try_strap_installation),
            ("Direct keyring package", self._try_keyring_package_installation),
            ("Manual keyring setup", self._try_manual_keyring_setup),
            ("Alternative installation", self._try_alternative_keyring)
        ]
        
        for i, (method_name, method_func) in enumerate(methods, 1):
            print(f"\n{ColorManager.PROCESS} Method {i}/4: {method_name}")
            spinner = ProgressSpinner(f"Attempting {method_name}")
            spinner.start()
            
            try:
                if method_func():
                    spinner.stop(f"{ColorManager.SUCCESS} {method_name} successful!")
                    return True
                else:
                    spinner.stop(f"{ColorManager.ERROR} {method_name} failed")
            except Exception as e:
                spinner.stop(f"{ColorManager.ERROR} {method_name} failed: {str(e)[:50]}")
        
        self.logger.log("WARNING", "All keyring installation methods failed", "keyring")
        print(f"\n{ColorManager.WARNING} All keyring installation methods failed")
        return False
    
    def _try_strap_installation(self) -> bool:
        """Try BlackArch strap.sh installation with enhanced progress tracking"""
        for i, strap_url in enumerate(KygoXConfig.BLACKARCH_STRAP_URLS, 1):
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
                self.logger.log("WARNING", f"Strap method {i} failed: {str(e)}", "keyring")
                continue
        
        return False
    
    def _try_keyring_package_installation(self) -> bool:
        """Try direct keyring package installation with progress tracking"""
        for i, keyring_url in enumerate(KygoXConfig.BLACKARCH_KEYRING_URLS, 1):
            try:
                keyring_file = self.cache_dir / "blackarch-keyring.pkg.tar.xz"
                
                # Download keyring with retry and progress
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
                self.logger.log("WARNING", f"Direct keyring method {i} failed: {str(e)}", "keyring")
                continue
        
        return False
    
    def _try_manual_keyring_setup(self) -> bool:
        """Try manual keyring setup with detailed progress"""
        try:
            steps = [
                ("Initializing pacman keyring", self._init_keyring),
                ("Populating Arch keyring", self._populate_keyring),
                ("Adding BlackArch key", self._add_blackarch_key)
            ]
            
            for step_name, step_func in steps:
                print(f"{ColorManager.PROCESS} {step_name}...")
                if not RetryManager.retry_with_backoff(step_func):
                    return False
                print(f"{ColorManager.SUCCESS} {step_name} completed")
            
            self._add_blackarch_repo()
            self.logger.log("SUCCESS", "Manual keyring setup completed", "keyring")
            return True
                
        except Exception as e:
            self.logger.log("WARNING", f"Manual keyring setup failed: {str(e)}", "keyring")
        
        return False
    
    def _init_keyring(self):
        """Initialize pacman keyring"""
        result = subprocess.run(
            ["pacman-key", "--init"],
            capture_output=True,
            text=True,
            timeout=300
        )
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, "pacman-key", result.stderr)
        return True
    
    def _populate_keyring(self):
        """Populate keyring"""
        result = subprocess.run(
            ["pacman-key", "--populate", "archlinux"],
            capture_output=True,
            text=True,
            timeout=300
        )
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, "pacman-key", result.stderr)
        return True
    
    def _add_blackarch_key(self):
        """Add BlackArch key"""
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
    
    def _try_alternative_keyring(self) -> bool:
        """Try alternative keyring installation method"""
        try:
            commands = [
                (["pacman-key", "--init"], "Initialize keyring"),
                (["pacman-key", "--populate", "archlinux"], "Populate keyring"),
                (["pacman", "-Sy", "--noconfirm"], "Sync repositories")
            ]
            
            for cmd, desc in commands:
                print(f"{ColorManager.PROCESS} {desc}...")
                
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
                
                print(f"{ColorManager.SUCCESS} {desc} completed")
            
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
                
        except Exception as e:
            self.logger.log("WARNING", f"Alternative keyring method failed: {str(e)}", "keyring")
        
        return False
    
    def _download_file_with_progress(self, url: str, filepath: Path, timeout: int = None):
        """Download file with enhanced progress bar"""
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
                    unit_divisor=1024,
                    desc=f"{ColorManager.DOWNLOAD} {filepath.name}",
                    colour='cyan',
                    leave=False,
                    bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]'
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
        """Add BlackArch repository to pacman.conf with enhanced feedback"""
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
                print(f"{ColorManager.PROCESS} Finding best BlackArch mirror...")
                best_mirror = self._get_best_blackarch_mirror()
                blackarch_repo = f"\n[blackarch]\nSigLevel = Optional TrustAll\nServer = {best_mirror}\n"
                
                with open(pacman_conf, "a") as f:
                    f.write(blackarch_repo)
                
                print(f"{ColorManager.SUCCESS} BlackArch repository added")
                self.logger.log("SUCCESS", f"BlackArch repository added with mirror: {best_mirror}", "keyring")
                
                # Update package databases
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
                
                print(f"{ColorManager.WARNING} BlackArch added with signature verification disabled")
                self.logger.log("WARNING", "BlackArch added with signature verification disabled", "keyring")
                self._update_databases()
                
        except Exception as e:
            self.logger.log("ERROR", f"Failed to configure unsafe BlackArch repository: {str(e)}", "keyring")
    
    def _get_best_blackarch_mirror(self) -> str:
        """Find the fastest responding BlackArch mirror with progress indication"""
        best_mirror = KygoXConfig.BLACKARCH_MIRRORS[0]  # Default
        best_time = float('inf')
        
        for mirror in KygoXConfig.BLACKARCH_MIRRORS:
            try:
                start_time = time.time()
                # Test mirror response time
                test_url = mirror.replace('$repo', 'blackarch').replace('$arch', 'x86_64')
                response = requests.head(test_url, timeout=5)
                response_time = time.time() - start_time
                
                if response.status_code == 200 and response_time < best_time:
                    best_time = response_time
                    best_mirror = mirror
                    
            except Exception:
                continue
        
        self.logger.log("INFO", f"Selected fastest mirror: {best_mirror} ({best_time:.2f}s)", "keyring")
        return best_mirror
    
    def _update_databases(self):
        """Update package databases with enhanced feedback"""
        spinner = ProgressSpinner("Updating package databases")
        spinner.start()
        
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
        
        try:
            if RetryManager.retry_with_backoff(update_dbs):
                spinner.stop(f"{ColorManager.SUCCESS} Package databases updated")
                self.logger.log("SUCCESS", "Package databases updated", "keyring")
            else:
                spinner.stop(f"{ColorManager.WARNING} Failed to update package databases")
                self.logger.log("WARNING", "Failed to update package databases", "keyring")
        except:
            spinner.stop(f"{ColorManager.ERROR} Database update failed")
    
    def _verify_blackarch_setup(self):
        """Verify BlackArch setup with enhanced feedback"""
        try:
            spinner = ProgressSpinner("Verifying BlackArch setup")
            spinner.start()
            
            result = subprocess.run(
                ["pacman", "-Sl", "blackarch"],
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if result.returncode == 0 and result.stdout.strip():
                package_count = len(result.stdout.strip().split('\n'))
                spinner.stop(f"{ColorManager.SUCCESS} BlackArch verified: {package_count} packages available")
                self.logger.log("SUCCESS", f"BlackArch repository verified with {package_count} packages", "keyring")
            else:
                spinner.stop(f"{ColorManager.WARNING} BlackArch verification failed")
                self.logger.log("WARNING", "BlackArch repository verification failed", "keyring")
                
        except Exception as e:
            spinner.stop(f"{ColorManager.WARNING} Could not verify BlackArch setup")
            self.logger.log("WARNING", f"Could not verify BlackArch setup: {str(e)}", "keyring")

class PackageManager:
    """Enhanced package management with comprehensive retry logic and visual feedback"""
    
    def __init__(self, logger: Logger):
        self.logger = logger
        self.installed_packages = set()
        self.failed_packages = set()
        self.cleaner = SystemCleaner(logger)
        self.install_lock = threading.Lock()
        self.install_stats = {"attempted": 0, "successful": 0, "failed": 0, "retried": 0}
        
    def install_packages(self, packages: List[str], max_workers: int = 2) -> Dict[str, bool]:
        """Install packages with parallel execution and enhanced visual feedback"""
        print(ColorManager.create_section_header("PACKAGE INSTALLATION"))
        
        self.logger.log("PROCESS", f"Installing {len(packages)} packages with {max_workers} workers", "installer")
        self.install_stats["attempted"] = len(packages)
        
        # Clean system before installation
        self.cleaner.remove_db_locks()
        
        results = {}
        
        # Create progress tracking
        progress_bar = tqdm(
            total=len(packages),
            desc=f"{ColorManager.INSTALL} Installing packages",
            unit="pkg",
            colour='green',
            bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]'
        )
        
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
                            self.install_stats["successful"] += 1
                            self.logger.log_package(package, "success")
                        else:
                            self.failed_packages.add(package)
                            self.install_stats["failed"] += 1
                            
                        progress_bar.update(1)
                        
                        # Update progress bar description with stats
                        success_rate = (self.install_stats["successful"] / self.install_stats["attempted"]) * 100
                        progress_bar.set_description(
                            f"{ColorManager.INSTALL} Installing packages (Success: {success_rate:.1f}%)"
                        )
                            
                except Exception as e:
                    self.logger.log("ERROR", f"Exception during installation of {package}: {str(e)}", "installer")
                    results[package] = False
                    with self.install_lock:
                        self.failed_packages.add(package)
                        self.install_stats["failed"] += 1
                        progress_bar.update(1)
        
        progress_bar.close()
        
        # Display final statistics
        self._display_installation_summary()
        
        # Final cleanup
        self.cleaner.remove_db_locks()
        
        return results
    
    def _display_installation_summary(self):
        """Display installation summary with enhanced visuals"""
        print(ColorManager.create_section_header("INSTALLATION SUMMARY"))
        
        total = self.install_stats["attempted"]
        successful = self.install_stats["successful"]
        failed = self.install_stats["failed"]
        success_rate = (successful / total) * 100 if total > 0 else 0
        
        # Create visual progress bar for success rate
        progress_bar = ColorManager.create_progress_bar(successful, total, 30)
        
        print(f"{ColorManager.INFO} Total Packages: {ColorManager.CYAN}{total}{ColorManager.RESET}")
        print(f"{ColorManager.SUCCESS} Successful: {ColorManager.GREEN}{successful}{ColorManager.RESET}")
        print(f"{ColorManager.ERROR} Failed: {ColorManager.RED}{failed}{ColorManager.RESET}")
        print(f"{ColorManager.INFO} Success Rate: {progress_bar}")
        
        # Performance indicators
        if success_rate >= 90:
            print(f"{ColorManager.SUCCESS} Excellent installation performance!")
        elif success_rate >= 75:
            print(f"{ColorManager.WARNING} Good installation performance")
        elif success_rate >= 50:
            print(f"{ColorManager.WARNING} Moderate installation performance - check logs")
        else:
            print(f"{ColorManager.ERROR} Poor installation performance - system issues detected")
        
        print(ColorManager.create_banner_line())
    
    def _install_package_with_retry(self, package: str, index: int) -> bool:
        """Install a single package with comprehensive retry logic and visual feedback"""
        # Check if already installed first
        if self._is_package_installed(package):
            return True
        
        # Try different installation methods
        install_methods = [
            ("Official repos", self._install_from_official_repos),
            ("BlackArch", self._install_from_blackarch),
            ("AUR helper", self._install_from_aur_helper),
            ("Force install", self._install_with_force)
        ]
        
        for method_index, (method_name, install_method) in enumerate(install_methods):
            try:
                def attempt_install():
                    return install_method(package, index, method_index)
                
                if RetryManager.retry_with_backoff(
                    attempt_install,
                    exceptions=(subprocess.CalledProcessError, subprocess.TimeoutExpired, IOError)
                ):
                    return True
                    
            except Exception as e:
                self.install_stats["retried"] += 1
                continue
        
        # All methods failed
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
            return True
        else:
            error_msg = result.stderr.strip() or "Unknown error"
            raise subprocess.CalledProcessError(result.returncode, "pacman", error_msg)

class KygoXCore:
    """Main KygoX toolkit engine with enhanced visuals and comprehensive error handling"""
    
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
        print(f"\n{ColorManager.WARNING} Installation interrupted by user")
        self.logger.log("WARNING", "Installation interrupted by user", "system")
        self.cleanup()
        sys.exit(130)
    
    def cleanup(self):
        """Comprehensive cleanup with enhanced feedback"""
        try:
            print(f"{ColorManager.PROCESS} Performing cleanup operations...")
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
            
            print(f"{ColorManager.SUCCESS} Cleanup completed")
            self.logger.log("SUCCESS", "Cleanup completed", "system")
            
        except Exception as e:
            print(f"{ColorManager.WARNING} Cleanup warning: {str(e)}")
            self.logger.log("WARNING", f"Cleanup warning: {str(e)}", "system")
    
    def run(self):
        """Main execution method with enhanced visual feedback"""
        try:
            self._display_banner()
            self._check_prerequisites()
            self._prepare_system()
            self._setup_environment()
            self._install_toolkit()
            self._generate_report()
            self._final_cleanup()
            
        except KeyboardInterrupt:
            print(f"\n{ColorManager.WARNING} Installation interrupted by user")
            self.logger.log("WARNING", "Installation interrupted by user", "system")
            self.cleanup()
            sys.exit(130)
        except Exception as e:
            print(f"\n{ColorManager.ERROR} Fatal error: {str(e)}")
            self.logger.log("ERROR", f"Fatal error: {str(e)}", "system")
            self.cleanup()
            sys.exit(1)
    
    def _display_banner(self):
        """Display enhanced application banner"""
        banner = f"""
{ColorManager.CYAN}{ColorManager.BOLD}
██╗  ██╗██╗   ██╗ ██████╗  ██████╗ ██╗  ██╗
██║ ██╔╝╚██╗ ██╔╝██╔════╝ ██╔═══██╗╚██╗██╔╝
█████╔╝  ╚████╔╝ ██║  ███╗██║   ██║ ╚███╔╝ 
██╔═██╗   ╚██╔╝  ██║   ██║██║   ██║ ██╔██╗ 
██║  ██║   ██║   ╚██████╔╝╚██████╔╝██╔╝ ██╗
╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
{ColorManager.RESET}
{ColorManager.create_banner_line("━", 60)}
{ColorManager.BOLD}{ColorManager.WHITE}    ARCH LINUX PENETRATION TESTING TOOLKIT    {ColorManager.RESET}
{ColorManager.DIM}         Professional Security Arsenal Deployment         {ColorManager.RESET}
{ColorManager.create_banner_line("━", 60)}

{ColorManager.INFO} Version: {ColorManager.CYAN}{self.config.VERSION}{ColorManager.RESET} | {ColorManager.PURPLE}{self.config.VERSION_NAME}{ColorManager.RESET}
{ColorManager.INFO} Repository: {ColorManager.BLUE}{self.config.REPO_URL}{ColorManager.RESET}
{ColorManager.INFO} Author: {ColorManager.GREEN}0xbv1 | 0xb0rn3{ColorManager.RESET}

{ColorManager.create_banner_line("═", 60)}
"""
        print(banner)
    
    def _check_prerequisites(self):
        """Enhanced system prerequisites check with detailed feedback"""
        print(ColorManager.create_section_header("PREREQUISITES CHECK"))
        
        self.logger.log("PROCESS", "Checking system prerequisites", "system")
        
        # Check if running as root
        if os.geteuid() != 0:
            print(f"{ColorManager.ERROR} KygoX must be run as root")
            self.logger.log("ERROR", "KygoX must be run as root", "system")
            sys.exit(1)
        else:
            print(f"{ColorManager.SUCCESS} Running with root privileges")
        
        # Check Arch compatibility
        if not self.system_info.is_arch_based:
            print(f"{ColorManager.ERROR} KygoX requires Arch Linux or Arch-based distribution")
            self.logger.log("ERROR", "KygoX requires Arch Linux or Arch-based distribution", "system")
            sys.exit(1)
        else:
            print(f"{ColorManager.SUCCESS} Compatible Arch-based system detected")
        
        # Display enhanced system information
        self.system_info.display_system_info()
        
        print(f"{ColorManager.SUCCESS} Prerequisites check completed")
        self.logger.log("SUCCESS", "Prerequisites check completed", "system")
    
    def _prepare_system(self):
        """Enhanced system preparation with visual feedback"""
        print(ColorManager.create_section_header("SYSTEM PREPARATION"))
        
        self.logger.log("PROCESS", "Preparing system for installation", "system")
        
        # Clean system thoroughly with progress indication
        steps = [
            ("Removing database locks", self.cleaner.remove_db_locks),
            ("Cleaning pacman cache", self.cleaner.cleanup_pacman_cache),
            ("Refreshing package databases", self.cleaner.refresh_pacman_databases)
        ]
        
        for step_name, step_func in steps:
            print(f"{ColorManager.PROCESS} {step_name}...")
            if step_func():
                print(f"{ColorManager.SUCCESS} {step_name} completed")
            else:
                print(f"{ColorManager.WARNING} {step_name} had issues, continuing...")
        
        print(f"{ColorManager.SUCCESS} System preparation completed")
        self.logger.log("SUCCESS", "System preparation completed", "system")
    
    def _setup_environment(self):
        """Enhanced environment setup with detailed progress"""
        print(ColorManager.create_section_header("ENVIRONMENT SETUP"))
        
        self.logger.log("PROCESS", "Setting up installation environment", "system")
        
        # Create directories with feedback
        directories = [
            ("Log directory", self.config.LOG_DIR),
            ("Backup directory", self.config.BACKUP_DIR),
            ("Cache directory", self.config.CACHE_DIR)
        ]
        
        for dir_name, dir_path in directories:
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"{ColorManager.SUCCESS} {dir_name} ready: {ColorManager.CYAN}{dir_path}{ColorManager.RESET}")
        
        # Update system with enhanced feedback
        print(f"\n{ColorManager.PROCESS} Updating system packages...")
        spinner = ProgressSpinner("Updating system packages")
        spinner.start()
        
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
        
        try:
            if RetryManager.retry_with_backoff(update_system):
                spinner.stop(f"{ColorManager.SUCCESS} System updated successfully")
                self.logger.log("SUCCESS", "System updated successfully", "system")
            else:
                spinner.stop(f"{ColorManager.WARNING} System update had issues, continuing")
                self.logger.log("WARNING", "System update had issues, continuing", "system")
        except Exception as e:
            spinner.stop(f"{ColorManager.WARNING} System update failed: {str(e)[:50]}")
        
        # Setup BlackArch keyring with comprehensive feedback
        if not self.keyring_manager.setup_blackarch_keyring():
            print(f"{ColorManager.WARNING} BlackArch keyring setup failed, continuing with core tools only")
            self.logger.log("WARNING", "BlackArch keyring setup failed, continuing with core tools only", "system")
        
        print(f"\n{ColorManager.SUCCESS} Environment setup completed")
        self.logger.log("SUCCESS", "Environment setup completed", "system")
    
    def _install_toolkit(self):
        """Enhanced toolkit installation with comprehensive progress tracking"""
        print(ColorManager.create_section_header("SECURITY TOOLKIT INSTALLATION"))
        
        self.logger.log("PROCESS", "Starting comprehensive toolkit installation", "installer")
        
        # Combine core and trending tools
        all_tools = list(set(self.config.CORE_TOOLS + self.config.TRENDING_2025))
        
        # Remove any empty or invalid package names
        all_tools = [pkg for pkg in all_tools if pkg and pkg.strip()]
        
        print(f"{ColorManager.INFO} Total packages to install: {ColorManager.CYAN}{len(all_tools)}{ColorManager.RESET}")
        print(f"{ColorManager.INFO} Installation method: {ColorManager.CYAN}Multi-threaded with retry logic{ColorManager.RESET}")
        
        # Show tool categories
        self._display_tool_categories()
        
        # Install packages with enhanced visual feedback
        results = self.package_manager.install_packages(all_tools, max_workers=2)
        
        # Enhanced summary with recommendations
        self._display_final_installation_summary(results)
    
    def _display_tool_categories(self):
        """Display tool categories being installed"""
        print(f"\n{ColorManager.INFO} Security Tool Categories:")
        
        categories = [
            ("🌐 Network & Web Security", ["nmap", "burpsuite", "sqlmap", "wireshark-qt"]),
            ("🔓 Exploitation & Post-Exploitation", ["metasploit", "empire", "impacket", "bloodhound"]),
            ("🔐 Password & Cryptography", ["john", "hashcat", "hydra", "steghide"]),
            ("🔍 Forensics & Analysis", ["volatility3", "autopsy", "binwalk", "ghidra"]),
            ("📱 Mobile & IoT Security", ["apktool", "frida", "jadx", "arduino"]),
            ("🕵️ OSINT & Reconnaissance", ["theharvester", "recon-ng", "sherlock", "maltego"]),
            ("☁️ Cloud & Container Security", ["trivy", "docker-bench-security", "prowler"]),
            ("🤖 AI/ML Security Testing", ["garak", "counterfit", "adversarial-robustness-toolbox"])
        ]
        
        for category, sample_tools in categories:
            available_tools = [tool for tool in sample_tools if tool in (self.config.CORE_TOOLS + self.config.TRENDING_2025)]
            if available_tools:
                print(f"  {ColorManager.CYAN}{category}{ColorManager.RESET}: {len(available_tools)} tools")
    
    def _display_final_installation_summary(self, results):
        """Display comprehensive installation summary"""
        successful = sum(1 for success in results.values() if success)
        failed = len(results) - successful
        success_rate = (successful / len(results)) * 100 if results else 0
        
        print(ColorManager.create_section_header("FINAL INSTALLATION SUMMARY"))
        
        # Create detailed progress visualization
        progress_bar = ColorManager.create_progress_bar(successful, len(results), 40)
        
        summary_data = [
            ("Total Packages Attempted", len(results), ColorManager.BLUE),
            ("Successfully Installed", successful, ColorManager.GREEN),
            ("Failed Installations", failed, ColorManager.RED),
            ("Success Rate", f"{success_rate:.1f}%", ColorManager.CYAN)
        ]
        
        for label, value, color in summary_data:
            print(f"{ColorManager.INFO} {label}: {color}{value}{ColorManager.RESET}")
        
        print(f"{ColorManager.INFO} Progress: {progress_bar}")
        
        # Performance assessment with recommendations
        if success_rate >= 90:
            print(f"\n{ColorManager.SUCCESS} Excellent! Your penetration testing arsenal is ready!")
            print(f"{ColorManager.INFO} Recommendation: All essential tools installed successfully")
        elif success_rate >= 75:
            print(f"\n{ColorManager.SUCCESS} Good installation rate achieved!")
            print(f"{ColorManager.WARNING} Consider manually installing failed critical tools")
        elif success_rate >= 50:
            print(f"\n{ColorManager.WARNING} Moderate success rate - some issues detected")
            print(f"{ColorManager.INFO} Check error logs and retry failed installations")
        else:
            print(f"\n{ColorManager.ERROR} Low success rate - significant system issues detected")
            print(f"{ColorManager.WARNING} Review system requirements and error logs")
        
        # If success rate is low, offer retry for failed packages
        if success_rate < 75 and self.package_manager.failed_packages:
            print(f"\n{ColorManager.PROCESS} Attempting single-threaded retry for failed packages...")
            failed_list = list(self.package_manager.failed_packages)
            self.package_manager.failed_packages.clear()
            
            retry_results = self.package_manager.install_packages(failed_list, max_workers=1)
            retry_successful = sum(1 for success in retry_results.values() if success)
            
            if retry_successful > 0:
                print(f"{ColorManager.SUCCESS} Retry successful: {retry_successful} additional packages installed")
                self.logger.log("SUCCESS", f"Retry successful: {retry_successful} additional packages installed", "installer")
    
    def _generate_report(self):
        """Generate comprehensive installation report with enhanced formatting"""
        print(ColorManager.create_section_header("GENERATING INSTALLATION REPORT"))
        
        self.logger.log("PROCESS", "Generating comprehensive installation report", "system")
        
        report_file = self.config.LOG_DIR / "installation_report.txt"
        
        try:
            with open(report_file, 'w', encoding='utf-8') as f:
                # Header with ASCII art
                f.write("╔═══════════════════════════════════════════════════════════════════════════════╗\n")
                f.write("║                           KYGOX INSTALLATION REPORT                          ║\n")
                f.write("╚═══════════════════════════════════════════════════════════════════════════════╝\n\n")
                
                # Basic information
                f.write(f"Version: {self.config.VERSION} ({self.config.VERSION_NAME})\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Duration: {datetime.now() - self.logger.stats['start_time']}\n")
                f.write("=" * 80 + "\n\n")
                
                # System information
                f.write("SYSTEM INFORMATION\n")
                f.write("-" * 50 + "\n")
                f.write(f"Distribution: {self.system_info.distro_info['name']}\n")
                f.write(f"Version: {self.system_info.distro_info.get('version', 'N/A')}\n")
                f.write(f"CPU: {self.system_info.system_specs['cpu_model']} ({self.system_info.system_specs['cpu_cores']} cores)\n")
                f.write(f"RAM: {self.system_info.system_specs['ram_mb']}MB (Available: {self.system_info.system_specs.get('available_ram_mb', 'N/A')}MB)\n")
                f.write(f"Disk: {self.system_info.system_specs['disk_free_gb']}GB free / {self.system_info.system_specs['disk_total_gb']}GB total\n")
                f.write(f"Python: {self.system_info.python_info['version']}\n")
                f.write(f"Pacman: {self.system_info.pacman_version}\n")
                f.write(f"System Load: {self.system_info.system_specs['load_average']}\n")
                f.write(f"Uptime: {self.system_info.system_specs['uptime_hours']} hours\n\n")
                
                # Installation statistics
                total_attempted = len(self.config.CORE_TOOLS + self.config.TRENDING_2025)
                installed_count = len(self.package_manager.installed_packages)
                failed_count = len(self.package_manager.failed_packages)
                success_rate = (installed_count / total_attempted) * 100 if total_attempted > 0 else 0
                
                f.write("INSTALLATION SUMMARY\n")
                f.write("-" * 50 + "\n")
                f.write(f"Total Packages Attempted: {total_attempted}\n")
                f.write(f"Successfully Installed: {installed_count}\n")
                f.write(f"Failed Installations: {failed_count}\n")
                f.write(f"Success Rate: {success_rate:.1f}%\n")
                f.write(f"Retry Operations: {self.package_manager.install_stats.get('retried', 0)}\n\n")
                
                # Performance metrics
                f.write("PERFORMANCE METRICS\n")
                f.write("-" * 50 + "\n")
                f.write(f"Total Successful Operations: {self.logger.stats['success_count']}\n")
                f.write(f"Total Errors: {self.logger.stats['error_count']}\n")
                f.write(f"Total Warnings: {self.logger.stats['warning_count']}\n")
                f.write(f"Total Retries: {self.logger.stats['retry_count']}\n\n")
                
                # Successfully installed packages
                if self.package_manager.installed_packages:
                    f.write("SUCCESSFULLY INSTALLED PACKAGES\n")
                    f.write("-" * 50 + "\n")
                    for pkg in sorted(self.package_manager.installed_packages):
                        f.write(f"  ✓ {pkg}\n")
                    f.write("\n")
                
                # Failed packages
                if self.package_manager.failed_packages:
                    f.write("FAILED PACKAGE INSTALLATIONS\n")
                    f.write("-" * 50 + "\n")
                    for pkg in sorted(self.package_manager.failed_packages):
                        f.write(f"  ✗ {pkg}\n")
                    f.write("\n")
                
                # Tool categories analysis
                f.write("SECURITY TOOL CATEGORIES ANALYSIS\n")
                f.write("-" * 50 + "\n")
                categories = {
                    "Network & Scanning": ["nmap", "masscan", "rustscan", "wireshark-qt", "tcpdump"],
                    "Web Application Security": ["burpsuite", "owasp-zap", "sqlmap", "nikto", "gobuster"],
                    "Exploitation Tools": ["metasploit", "empire", "beef", "searchsploit"],
                    "Password & Cracking": ["john", "hashcat", "hydra", "medusa"],
                    "Digital Forensics": ["volatility3", "autopsy", "binwalk", "foremost"],
                    "Reverse Engineering": ["ghidra", "radare2", "gdb", "strings"],
                    "Mobile Security": ["apktool", "jadx", "frida", "objection"],
                    "OSINT & Reconnaissance": ["theharvester", "recon-ng", "sherlock", "spiderfoot"],
                    "Post-Exploitation": ["impacket", "responder", "crackmapexec", "bloodhound"],
                    "Cloud & Container Security": ["trivy", "docker-bench-security", "prowler"],
                    "AI/ML Security": ["garak", "counterfit", "adversarial-robustness-toolbox"]
                }
                
                for category, tools in categories.items():
                    installed_in_category = [tool for tool in tools if tool in self.package_manager.installed_packages]
                    if installed_in_category:
                        coverage = (len(installed_in_category) / len(tools)) * 100
                        f.write(f"{category}: {len(installed_in_category)}/{len(tools)} tools ({coverage:.0f}% coverage)\n")
                        for tool in installed_in_category:
                            f.write(f"    • {tool}\n")
                        f.write("\n")
                
                # System recommendations
                f.write("SYSTEM RECOMMENDATIONS\n")
                f.write("-" * 50 + "\n")
                
                if failed_count > 0:
                    f.write("• Review failed packages in the error logs for troubleshooting\n")
                    f.write("• Consider manual installation of critical failed tools\n")
                    f.write("• Run 'pacman -Syu' to ensure system is up to date\n")
                
                if success_rate > 90:
                    f.write("• Excellent installation rate! System is ready for professional penetration testing\n")
                    f.write("• All essential security tools are available and ready to use\n")
                elif success_rate > 75:
                    f.write("• Good installation rate achieved\n")
                    f.write("• Most essential tools are available for security testing\n")
                elif success_rate > 50:
                    f.write("• Moderate installation rate - some tools may be missing\n")
                    f.write("• Consider troubleshooting failed packages and re-running installation\n")
                else:
                    f.write("• Low installation rate detected - significant issues present\n")
                    f.write("• System troubleshooting recommended before use\n")
                    f.write("• Consider checking system resources and network connectivity\n")
                
                f.write("• Verify BlackArch repository configuration: pacman -Sl blackarch\n")
                f.write("• Consider installing an AUR helper (yay, paru) for additional tools\n")
                f.write("• Regular system updates recommended: pacman -Syu\n")
                f.write("• Backup important configurations before major system changes\n\n")
                
                # File locations
                f.write("LOG FILES AND RESOURCES\n")
                f.write("-" * 50 + "\n")
                f.write(f"Main Installation Log: {self.config.LOG_DIR / 'installation.log'}\n")
                f.write(f"Error Log: {self.config.LOG_DIR / 'errors.log'}\n")
                f.write(f"Success Log: {self.config.LOG_DIR / 'successful_packages.log'}\n")
                f.write(f"Failed Packages Log: {self.config.LOG_DIR / 'failed_packages.log'}\n")
                f.write(f"Retry Operations Log: {self.config.LOG_DIR / 'retries.log'}\n")
                f.write(f"Cache Directory: {self.config.CACHE_DIR}\n")
                f.write(f"Backup Directory: {self.config.BACKUP_DIR}\n\n")
                
                # Footer
                f.write("=" * 80 + "\n")
                f.write("KygoX - Arch Linux Penetration Testing Toolkit\n")
                f.write(f"Repository: {self.config.REPO_URL}\n")
                f.write("Author: 0xbv1 | 0xb0rn3\n")
                f.write("=" * 80 + "\n")
        
        except Exception as e:
            print(f"{ColorManager.ERROR} Failed to generate report: {str(e)}")
            self.logger.log("ERROR", f"Failed to generate report: {str(e)}", "system")
            return
        
        print(f"{ColorManager.SUCCESS} Installation report generated: {ColorManager.CYAN}{report_file}{ColorManager.RESET}")
        self.logger.log("SUCCESS", f"Installation report saved to {report_file}", "system")
    
    def _final_cleanup(self):
        """Enhanced final cleanup with detailed feedback"""
        print(ColorManager.create_section_header("FINAL CLEANUP"))
        
        self.logger.log("PROCESS", "Performing final cleanup", "system")
        
        # Clean system one final time
        cleanup_steps = [
            ("Removing database locks", self.cleaner.remove_db_locks),
            ("Cleaning pacman cache", self.cleaner.cleanup_pacman_cache)
        ]
        
        for step_name, step_func in cleanup_steps:
            print(f"{ColorManager.PROCESS} {step_name}...")
            if step_func():
                print(f"{ColorManager.SUCCESS} {step_name} completed")
        
        # Generate toolkit summary file
        toolkit_summary = self.config.LOG_DIR / "installed_tools.txt"
        try:
            with open(toolkit_summary, 'w', encoding='utf-8') as f:
                f.write("KygoX Installed Security Tools\n")
                f.write("=" * 50 + "\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Total Tools: {len(self.package_manager.installed_packages)}\n")
                f.write("=" * 50 + "\n\n")
                
                for tool in sorted(self.package_manager.installed_packages):
                    f.write(f"{tool}\n")
            
            print(f"{ColorManager.SUCCESS} Tool summary saved: {ColorManager.CYAN}{toolkit_summary}{ColorManager.RESET}")
            
        except Exception as e:
            print(f"{ColorManager.WARNING} Could not generate tool summary: {str(e)}")
        
        # Display final statistics
        self.logger.show_statistics()
        
        # Final success message with enhanced visuals
        print(ColorManager.create_section_header("INSTALLATION COMPLETE"))
        
        print(f"""
{ColorManager.SUCCESS} {ColorManager.BOLD}KygoX Security Toolkit Installation Complete!{ColorManager.RESET}

{ColorManager.INFO} Installation Summary:
  • Installed Tools: {ColorManager.GREEN}{len(self.package_manager.installed_packages)}{ColorManager.RESET}
  • Failed Installations: {ColorManager.RED}{len(self.package_manager.failed_packages)}{ColorManager.RESET}
  • Success Rate: {ColorManager.CYAN}{(len(self.package_manager.installed_packages) / len(self.config.CORE_TOOLS + self.config.TRENDING_2025)) * 100:.1f}%{ColorManager.RESET}

{ColorManager.INFO} Resources:
  • Installation Report: {ColorManager.CYAN}{self.config.LOG_DIR / 'installation_report.txt'}{ColorManager.RESET}
  • Installed Tools List: {ColorManager.CYAN}{self.config.LOG_DIR / 'installed_tools.txt'}{ColorManager.RESET}
  • All Logs: {ColorManager.CYAN}{self.config.LOG_DIR}{ColorManager.RESET}

{ColorManager.INFO} Next Steps:
  • Verify tools: {ColorManager.CYAN}pacman -Qs blackarch{ColorManager.RESET}
  • Update system: {ColorManager.CYAN}sudo pacman -Syu{ColorManager.RESET}
  • Repository: {ColorManager.BLUE}{self.config.REPO_URL}{ColorManager.RESET}

{ColorManager.create_banner_line("🎯", 60)}
{ColorManager.BOLD}{ColorManager.GREEN}    Your Arch Linux penetration testing arsenal is ready!    {ColorManager.RESET}
{ColorManager.create_banner_line("🎯", 60)}
""")
        
        self.logger.log("SUCCESS", "KygoX installation completed successfully!", "system")

def main():
    """Enhanced main entry point with comprehensive argument handling"""
    parser = argparse.ArgumentParser(
        description="KygoX - Enhanced Arch Linux Penetration Testing Toolkit",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
{ColorManager.BOLD}Examples:{ColorManager.RESET}
  python3 {sys.argv[0]}                    # Full installation with enhanced UI
  python3 {sys.argv[0]} --core-only        # Core security tools only
  python3 {sys.argv[0]} --trending-only    # Latest 2025 security tools
  python3 {sys.argv[0]} --max-workers 4    # Use 4 parallel installation threads
  python3 {sys.argv[0]} --check            # System compatibility check only

{ColorManager.BOLD}Security Toolkit Categories:{ColorManager.RESET}
  🌐 Network Discovery & Scanning       🔓 Web Application Security
  ⚡ Exploitation & Penetration        🔐 Password Attacks & Cracking  
  🔍 Digital Forensics & Analysis      🔧 Reverse Engineering & Analysis
  📱 Mobile Security Testing           🕵️ Information Gathering (OSINT)
  🚀 Post-Exploitation Tools           🛡️ Vulnerability Assessment
  🎭 Steganography & Cryptography      🔌 Hardware & IoT Security
  🎯 Social Engineering Tools          ☁️ Cloud & Container Security
  🤖 AI/ML Security Testing            🔄 DevSecOps & Automation Tools

{ColorManager.BOLD}Author:{ColorManager.RESET} 0xbv1 | 0xb0rn3
{ColorManager.BOLD}Contact:{ColorManager.RESET} IG: theehiv3 | X: 0xbv1 | Email: q4n0@proton.me
{ColorManager.BOLD}Repository:{ColorManager.RESET} {KygoXConfig.REPO_URL}
{ColorManager.BOLD}License:{ColorManager.RESET} Do whatever the hell you want, but don't blame me when it breaks
"""
    )
    
    parser.add_argument(
        "--version", 
        action="version", 
        version=f"KygoX {KygoXConfig.VERSION} ({KygoXConfig.VERSION_NAME})"
    )
    
    parser.add_argument(
        "--core-only",
        action="store_true",
        help="Install only core security tools (faster installation)"
    )
    
    parser.add_argument(
        "--trending-only",
        action="store_true", 
        help="Install only trending 2025 security tools"
    )
    
    parser.add_argument(
        "--check",
        action="store_true",
        help="Perform system compatibility check only"
    )
    
    parser.add_argument(
        "--setup-keyring",
        action="store_true",
        help="Setup BlackArch keyring only"
    )
    
    parser.add_argument(
        "--cleanup",
        action="store_true",
        help="Cleanup system and remove temporary files"
    )
    
    parser.add_argument(
        "--max-workers",
        type=int,
        default=2,
        help="Maximum number of parallel installation workers (default: 2)"
    )
    
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="INFO",
        help="Set logging level (default: INFO)"
    )
    
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable colored output"
    )
    
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate installation without actually installing packages"
    )
    
    args = parser.parse_args()
    
    # Disable colors if requested
    if args.no_color:
        ColorManager.SUCCESS = "[SUCCESS]"
        ColorManager.ERROR = "[ERROR]"
        ColorManager.INFO = "[INFO]"
        ColorManager.WARNING = "[WARNING]"
        ColorManager.PROCESS = "[PROCESS]"
        ColorManager.SECURITY = "[SECURITY]"
        ColorManager.RETRY = "[RETRY]"
        ColorManager.DOWNLOAD = "[DOWNLOAD]"
        ColorManager.INSTALL = "[INSTALL]"
        ColorManager.CYAN = ColorManager.GREEN = ColorManager.RED = ""
        ColorManager.YELLOW = ColorManager.BLUE = ColorManager.PURPLE = ""
        ColorManager.WHITE = ColorManager.BOLD = ColorManager.RESET = ""
    
    try:
        # Handle specific actions
        if args.check:
            print(f"{ColorManager.create_section_header('SYSTEM COMPATIBILITY CHECK')}")
            core = KygoXCore()
            core._display_banner()
            core._check_prerequisites()
            print(f"\n{ColorManager.SUCCESS} System compatibility check passed!")
            print(f"{ColorManager.INFO} Your system is ready for KygoX installation")
            return 0
        
        if args.cleanup:
            print(f"{ColorManager.create_section_header('SYSTEM CLEANUP')}")
            core = KygoXCore()
            core.cleanup()
            print(f"{ColorManager.SUCCESS} System cleanup completed!")
            return 0
        
        if args.setup_keyring:
            print(f"{ColorManager.create_section_header('BLACKARCH KEYRING SETUP')}")
            core = KygoXCore()
            core._display_banner()
            core._check_prerequisites()
            core._prepare_system()
            
            # Create directories
            core.config.LOG_DIR.mkdir(parents=True, exist_ok=True)
            core.config.CACHE_DIR.mkdir(parents=True, exist_ok=True)
            
            if core.keyring_manager.setup_blackarch_keyring():
                print(f"{ColorManager.SUCCESS} BlackArch keyring setup completed successfully!")
                return 0
            else:
                print(f"{ColorManager.ERROR} BlackArch keyring setup failed!")
                return 1
        
        # Dry run mode
        if args.dry_run:
            print(f"{ColorManager.create_section_header('DRY RUN MODE')}")
            print(f"{ColorManager.WARNING} This is a simulation - no packages will be installed")
            
            core = KygoXCore()
            
            # Modify configuration based on arguments
            if args.core_only:
                core.config.TRENDING_2025 = []
                print(f"{ColorManager.INFO} Mode: Core tools only")
            elif args.trending_only:
                core.config.CORE_TOOLS = []
                print(f"{ColorManager.INFO} Mode: Trending 2025 tools only")
            
            all_tools = list(set(core.config.CORE_TOOLS + core.config.TRENDING_2025))
            print(f"{ColorManager.INFO} Would install {len(all_tools)} packages")
            print(f"{ColorManager.INFO} Worker threads: {args.max_workers}")
            print(f"{ColorManager.INFO} Log level: {args.log_level}")
            
            print(f"\n{ColorManager.SUCCESS} Dry run completed - use without --dry-run to install")
            return 0
        
        # Main installation
        core = KygoXCore()
        
        # Modify configuration based on arguments
        if args.core_only:
            core.config.TRENDING_2025 = []
            core.logger.log("INFO", "Running in core-only mode", "system")
        elif args.trending_only:
            core.config.CORE_TOOLS = []
            core.logger.log("INFO", "Running in trending-only mode", "system")
        
        # Set max workers
        if hasattr(args, 'max_workers') and args.max_workers:
            core.logger.log("INFO", f"Using {args.max_workers} worker threads", "system")
        
        # Run the main installation
        core.run()
        return 0
        
    except KeyboardInterrupt:
        print(f"\n{ColorManager.WARNING} Installation interrupted by user")
        return 130
    except Exception as e:
        print(f"{ColorManager.ERROR} Fatal error: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
