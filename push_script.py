#!/usr/bin/env python3
import subprocess
import sys

def push_to_github():
    try:
        # Add all changes
        subprocess.run(['git', 'add', '.'], check=True)
        # Commit if there are changes
        result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
        if result.stdout.strip():
            subprocess.run(['git', 'commit', '-m', 'Auto commit'], check=True)
        # Push
        subprocess.run(['git', 'push', 'origin', 'main'], check=True)
        print("Successfully pushed to GitHub")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    push_to_github()