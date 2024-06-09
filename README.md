# File Integrity Monitor

A Python-based File Integrity Monitor that uses MD5 hashing to verify the integrity of files. This project is designed to help maintain the integrity of critical files by detecting any changes made to them.

## Features

- **Check Integrity**: Verifies the integrity of files by comparing their current MD5 hash with the hash stored in the baseline.
- **Add File**: Adds a file and its MD5 hash to the baseline for future integrity checks.
- **Wipe Baseline**: Clears all entries from the baseline.

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/file-integrity-monitor.git
    cd file-integrity-monitor
    ```

2. Ensure you have the required libraries installed. You can do this by running:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```sh
    python file_integrity_monitor.py
    ```

2. Follow the on-screen instructions to either check the integrity of files, add a new file to the baseline, or wipe the baseline.

### Options

- **Check Integrity**: This option reads the `baseline.txt` file and compares the stored MD5 hashes with the current hashes of the files. It will notify you if any files have been altered.
- **Add File**: Prompts you to enter the full path of the file you want to add to the baseline. It calculates the MD5 hash of the file and stores it in `baseline.txt`.
- **Wipe Baseline**: Clears the `baseline.txt` file, removing all stored file paths and hashes.

## Example

1. **Add a file to the baseline**:
    ```sh
    Enter the FULL path of the file to add to the baseline: /path/to/your/file.txt
    ```

2. **Check integrity of files**:
    ```sh
    file: /path/to/your/file.txt has remained the same.
    ```

3. **Wipe the baseline**:
    ```sh
    The baseline has been successfully wiped.
    ```

## File Structure

```plaintext
.
├── file_integrity_monitor.py
└── baseline.txt
