FROM ubuntu:22.04

RUN apt-get update && apt-get install -y openssh-server sudo && \
    rm -rf /var/lib/apt/lists/* && \
    useradd -m -s /bin/bash sysadmin && \
    echo 'sysadmin:trailblazer2025' | chpasswd && \
    echo 'sysadmin ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers.d/sysadmin

COPY banner /etc/ssh/banner

RUN mkdir -p /var/run/sshd && \
    sed -i 's/#?PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    echo "Banner /etc/ssh/banner" >> /etc/ssh/sshd_config

# Key auth removed - use password from FTP hint

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
