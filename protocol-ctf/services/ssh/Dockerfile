FROM ubuntu:22.04

RUN apt-get update && apt-get install -y openssh-server sudo && \
    rm -rf /var/lib/apt/lists/* && \
    useradd -m -s /bin/bash sysadmin && \
    echo 'sysadmin:trailblazer2025' | chpasswd && \
    echo 'sysadmin ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers.d/sysadmin

COPY banner /etc/ssh/banner
COPY authorized_keys /tmp/authorized_keys
COPY files /home/sysadmin/files

RUN mkdir -p /var/run/sshd && \
    mkdir -p /home/sysadmin/.ssh && \
    cat /tmp/authorized_keys > /home/sysadmin/.ssh/authorized_keys && \
    chown -R sysadmin:sysadmin /home/sysadmin/.ssh /home/sysadmin/files && \
    chmod 700 /home/sysadmin/.ssh && \
    chmod 600 /home/sysadmin/.ssh/authorized_keys && \
    rm /tmp/authorized_keys && \
    sed -i 's/#?PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config && \
    echo "Banner /etc/ssh/banner" >> /etc/ssh/sshd_config

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
