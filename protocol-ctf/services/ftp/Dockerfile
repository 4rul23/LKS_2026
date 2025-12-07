FROM ubuntu:22.04

RUN apt-get update && apt-get install -y vsftpd && rm -rf /var/lib/apt/lists/*

COPY vsftpd.conf /etc/vsftpd.conf
COPY vsftpd.banner /etc/vsftpd.banner
RUN mkdir -p /home/ftp/files && \
    chown ftp:ftp /home/ftp/files && \
    chmod 755 /home/ftp/files

EXPOSE 21 30000-30009

CMD ["/usr/sbin/vsftpd", "/etc/vsftpd.conf"]
