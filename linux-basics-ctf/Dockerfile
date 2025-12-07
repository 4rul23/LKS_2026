FROM ubuntu:22.04

# Install SSH server only (minimal)
RUN apt-get update && apt-get install -y \
    openssh-server \
    && rm -rf /var/lib/apt/lists/*

# Create SSH directory
RUN mkdir /var/run/sshd

# Create challenge user (restricted to bash for shared instance)
RUN useradd -m -s /bin/bash ctfuser && \
    echo "ctfuser:intership2024" | chpasswd

# Create admin user (for investigation)
RUN useradd -m -s /bin/bash admin

# ===========================================
# STEP 1: Initial clue in README.txt
# ===========================================
RUN echo "=== Server Maintenance Notes ===" > /home/ctfuser/README.txt && \
    echo "" >> /home/ctfuser/README.txt && \
    echo "Previous sysadmin left suddenly." >> /home/ctfuser/README.txt && \
    echo "We need to recover some important data." >> /home/ctfuser/README.txt && \
    echo "" >> /home/ctfuser/README.txt && \
    echo "Start by checking the backup logs:" >> /home/ctfuser/README.txt && \
    echo "  /var/log/backup.log" >> /home/ctfuser/README.txt

# ===========================================
# STEP 2: Backup log with clue about admin
# ===========================================
RUN echo "[2024-01-15 09:00:01] Backup job started" > /var/log/backup.log && \
    echo "[2024-01-15 09:00:15] Scanning /home directories..." >> /var/log/backup.log && \
    echo "[2024-01-15 09:01:22] Copying /home/admin/documents..." >> /var/log/backup.log && \
    echo "[2024-01-15 09:01:45] WARNING: admin user left sensitive data unencrypted" >> /var/log/backup.log && \
    echo "[2024-01-15 09:02:00] Backup completed successfully" >> /var/log/backup.log && \
    echo "[2024-01-15 09:02:01] Archive saved to /var/backups/backup-2024-01-15.tar.gz" >> /var/log/backup.log

# ===========================================
# STEP 3: Admin's bash history with final clue
# ===========================================
RUN echo "ls -la" > /home/admin/.bash_history && \
    echo "cd /var/backups" >> /home/admin/.bash_history && \
    echo "ls -la" >> /home/admin/.bash_history && \
    echo "mkdir -p /opt/.system" >> /home/admin/.bash_history && \
    echo "mv recovery_key.txt /opt/.system/.secret_key" >> /home/admin/.bash_history && \
    echo "# moved the key to /opt/.system for safekeeping" >> /home/admin/.bash_history && \
    echo "logout" >> /home/admin/.bash_history

# ===========================================
# STEP 4: The hidden flag
# ===========================================
RUN mkdir -p /opt/.system && \
    echo "STELKCSC{c0nn3ct_th3_d0ts_l1nux_m4st3r}" > /opt/.system/.secret_key

# ===========================================
# Create some decoy files to make it realistic
# ===========================================
RUN mkdir -p /var/backups && \
    echo "Backup archive placeholder" > /var/backups/backup-2024-01-15.tar.gz

RUN mkdir -p /home/admin/documents && \
    echo "Project planning document" > /home/admin/documents/project.txt && \
    echo "Meeting notes from Q4" > /home/admin/documents/notes.txt

# ===========================================
# SECURITY: Lock down all files (read-only for ctfuser)
# ===========================================
# All challenge files owned by root - users can only READ
RUN chown -R root:root /home/ctfuser && \
    chown -R root:root /home/admin && \
    chown -R root:root /opt/.system && \
    chown root:root /var/log/backup.log

# Set readable permissions
RUN chmod 755 /home/ctfuser && \
    chmod 644 /home/ctfuser/README.txt && \
    chmod 755 /home/admin && \
    chmod 755 /home/admin/documents && \
    chmod 644 /home/admin/documents/* && \
    chmod 644 /home/admin/.bash_history && \
    chmod 755 /opt/.system && \
    chmod 644 /opt/.system/.secret_key && \
    chmod 644 /var/log/backup.log

# ===========================================
# SSH Configuration
# ===========================================
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

# Expose SSH port
EXPOSE 22

# Start SSH service
CMD ["/usr/sbin/sshd", "-D"]
