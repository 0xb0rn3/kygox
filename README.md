bkygo - BlackArch Installer for Arch Linux


Engineered by 0xb0rn3 | github.com/0xb0rn3

Overview
bkygo is a modular, robust, and user-friendly tool designed to automate the installation of BlackArch packages on Arch Linux. Built with a focus on reliability, performance, and user experience, it streamlines the deployment of penetration testing tools with advanced features like customizable banners, intelligent error handling, and comprehensive logging.
Features

Modular Architecture: Organized into core, package, system, and run components for maintainability and extensibility.
Customizable Banner Display: Configurable banner styles ("standard," "minimal," "matrix," "animated") with color options and animation toggling.
Interactive UI: Animated progress bars, styled menus (using dialog or fallback), and color-coded output for enhanced visibility.
Smart Package Management: Supports installing all BlackArch packages, specific groups, or custom lists with parallel installation capabilities.
Intelligent Error Handling: Automatic resolution of file conflicts, dependency issues, and installation retries with detailed logging.
Comprehensive Logging: Timestamped logs with rotation, stored in a configurable directory for troubleshooting.
Backup Management: Automatic backup of conflicting files with options to keep, move, or remove them.
System Validation: Pre-installation checks for disk space, architecture compatibility, and critical components.
AUR Integration: Seamless installation of AUR packages (e.g., yay, apkid) with user privilege management.
Performance Optimization: Resource-aware parallel installations and progress tracking with ETA estimates.
Configuration Flexibility: Customizable settings via a configuration file or environment variables.
Interruption Recovery: Graceful handling of interruptions (Ctrl+C) with optional backup cleanup.

Requirements

Arch Linux (or Arch-based distribution)
Root privileges (sudo or root user)
Internet connection
Bash shell
Optional: dialog for enhanced TUI (text-based user interface)

Installation

Clone or download the repository:
git clone https://github.com/0xb0rn3/bkygo.git

Or download the main script directly:
curl -O https://raw.githubusercontent.com/0xb0rn3/bkygo/main/Bkygo/run


Navigate to the Bkygo directory:
cd bkygo/Bkygo


Make the main script executable:
chmod +x run


Run with sudo:
sudo ./run



Directory Structure
The project is organized in the Bkygo directory:

core: Core module for configuration, logging, UI, error handling, and banner display.
package: Package management module for installation, conflict resolution, and parallel processing.
system: System module for repository setup, dependency resolution, and validation.
run: Main script orchestrating the installation process.

Usage Guide
Initial Setup
The run script performs the following steps:

Displays a customizable banner (configured via ~/.config/kygo/kygo.conf).
Verifies root privileges and captures the original user for AUR installations.
Adds the BlackArch repository to /etc/pacman.conf if not already present.
Updates package databases using pacman -Syy.
Installs yay (AUR helper) and base dependencies (base-devel, git).
Checks and installs required tools (e.g., nmap, metasploit) and AUR packages (e.g., apkid).

Installation Options
Run the script with one of the following options:

All Packages: Install the entire BlackArch repository.sudo ./Bkygo/run -a


Specific Group: Install packages from a BlackArch group (e.g., penetration, exploitation).sudo ./Bkygo/run -g penetration


Custom List: Install packages from a text file (one package per line).sudo ./Bkygo/run -p packages.txt



Banner Customization
The banner can be customized in ~/.config/kygo/kygo.conf:

ui.banner_style: Options are standard, minimal, matrix, or animated.
ui.animation: Set to true or false to enable/disable animations.
Example configuration:ui.banner_style=matrix
ui.animation=true



Conflict Resolution
The package module automatically handles:

File Conflicts: Backs up conflicting files to a designated directory with metadata for restoration.
Dependency Issues: Resolves missing dependencies using --needed or --overwrite flags.
Package Conflicts: Detects and resolves conflicts before installation.

Backup Management
Post-installation, the script offers options to:

Keep backup files in their original locations.
Move backups to blackarch_logs/backups/system_backups.
Remove all backup files.

Cache Management
Optionally clean the pacman cache to free disk space:

Prompted during execution, with logs stored in blackarch_logs/clean.log.

Configuration
Settings are stored in ~/.config/kygo/kygo.conf. Key options include:

LOG_LEVEL: Logging verbosity (DEBUG, INFO, WARNING, ERROR, CRITICAL).
PARALLEL_JOBS: Number of parallel installation jobs (default: 4).
ui.banner_style, ui.animation: Banner display settings.
app.version, app.codename, app.author, app.author_url: Metadata for the banner.

Environment variables can override settings (e.g., KYGO_LOG_LEVEL=DEBUG).
Log Files
Logs are stored in ~/.config/kygo/logs/ (or /tmp/logs/ if not configured):

kygo.log: Main log with all operations, rotated when exceeding 10MB.
update.log: Package database update logs.
install.log: Dependency and tool installation logs.
clean.log: Cache cleaning logs.

Error Handling
The core module implements robust error handling:

Retry Mechanisms: Retries installations with --overwrite or --needed flags.
Error Classification: Handles permission errors, installation failures, and unknown issues.
State Preservation: Logs errors with line numbers for debugging.

Interruption Recovery
If interrupted (Ctrl+C), the script:

Prompts to clean up backup files.
Preserves logs for troubleshooting.

Customization
Modify the following in core or run:

Log Directory: Change LOG_DIR in core for custom log storage.
Backup Directory: Adjust backup paths in package or run.
Banner Settings: Edit kygo.conf for banner style and animation.
AUR Packages: Update aur_packages array in run for custom AUR installations.

Troubleshooting
If issues occur:

Check kygo.log for detailed error messages.
Review specific logs (update.log, install.log, clean.log).
Verify pacman.conf includes the BlackArch repository.
Ensure sufficient disk space and internet connectivity.
Run with KYGO_LOG_LEVEL=DEBUG for verbose output:sudo KYGO_LOG_LEVEL=DEBUG ./Bkygo/run -a



License
bkygo is open source and licensed under the MIT License.
Disclaimer
Use at your own risk. Always back up your system before running the script, as it modifies system configurations and installs packages.
Contact & Support

GitHub: github.com/0xb0rn3
Issues: Report bugs or feature requests on the GitHub repository.
Email: Contact the author via GitHub for direct support.

