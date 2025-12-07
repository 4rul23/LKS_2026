FROM ubuntu:22.04

RUN apt-get update && apt-get install -y samba && rm -rf /var/lib/apt/lists/* && \
    mkdir -p /var/lib/samba && chmod 777 /var/lib/samba

COPY smb.conf /etc/samba/smb.conf

EXPOSE 1445

CMD ["/usr/sbin/smbd", "--foreground", "--no-process-group", "-s", "/etc/samba/smb.conf"]
