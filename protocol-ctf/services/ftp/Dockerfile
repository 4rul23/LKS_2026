FROM ubuntu:22.04

RUN sed -i 's/archive.ubuntu.com/kartolo.sby.datautama.net.id/g' /etc/apt/sources.list && \
    sed -i 's/security.ubuntu.com/kartolo.sby.datautama.net.id/g' /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y vsftpd && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir -p /var/run/vsftpd/empty && \
    mkdir -p /home/ftp/files && \
    chown ftp:ftp /home/ftp/files

COPY vsftpd.conf /etc/vsftpd.conf
COPY vsftpd.banner /etc/vsftpd.banner
RUN sed -i 's/\r$//' /etc/vsftpd.conf

EXPOSE 21 30000-30009

CMD ["/usr/sbin/vsftpd", "/etc/vsftpd.conf"]
