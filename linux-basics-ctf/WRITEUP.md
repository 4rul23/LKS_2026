# 🐧 Linux Basics CTF - Writeup

## Challenge Info
- **Name:** The Lost Key
- **Difficulty:** Easy
- **Category:** Linux Fundamentals

## Solution: Connect the Dots

### Step 1: Login dan Baca README
```bash
ssh ctfuser@localhost -p 2222
# Password: intership2024

cat README.txt
```

**Output:**
```
=== Server Maintenance Notes ===

Previous sysadmin left suddenly.
We need to recover some important data.

Start by checking the backup logs:
  /var/log/backup.log
```

**Clue:** Cek `/var/log/backup.log`

---

### Step 2: Analisis Backup Log
```bash
cat /var/log/backup.log
```

**Output:**
```
[2024-01-15 09:00:01] Backup job started
[2024-01-15 09:00:15] Scanning /home directories...
[2024-01-15 09:01:22] Copying /home/admin/documents...
[2024-01-15 09:01:45] WARNING: admin user left sensitive data unencrypted
[2024-01-15 09:02:00] Backup completed successfully
[2024-01-15 09:02:01] Archive saved to /var/backups/backup-2024-01-15.tar.gz
```

**Clue:** User `admin` meninggalkan data sensitif. Cek home directory admin.

---

### Step 3: Explore Admin User
```bash
ls /home
# Output: admin  ctfuser

ls -la /home/admin
```

Lihat ada `.bash_history`:
```bash
cat /home/admin/.bash_history
```

**Output:**
```
ls -la
cd /var/backups
ls -la
mkdir -p /opt/.system
mv recovery_key.txt /opt/.system/.secret_key
# moved the key to /opt/.system for safekeeping
logout
```

**Clue:** Key dipindahkan ke `/opt/.system/.secret_key`

---

### Step 4: Get the Flag
```bash
ls -la /opt
# Output: .system (hidden directory)

ls -la /opt/.system
# Output: .secret_key (hidden file)

cat /opt/.system/.secret_key
```

**Flag:**
```
STELKCSC{c0nn3ct_th3_d0ts_l1nux_m4st3r}
```

---

## Skills Tested
1. `cat` - Membaca file
2. `ls -la` - Melihat hidden files & directories
3. `cd` - Navigasi direktori
4. Log analysis - Memahami isi log file
5. User enumeration - Melihat user lain di `/home`
6. `.bash_history` - Memahami command history

## Command Summary
```bash
ssh ctfuser@localhost -p 2222
cat README.txt
cat /var/log/backup.log
ls /home
cat /home/admin/.bash_history
cat /opt/.system/.secret_key
```
