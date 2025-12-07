FROM ubuntu:22.04

RUN sed -i 's/archive.ubuntu.com/kartolo.sby.datautama.net.id/g' /etc/apt/sources.list && \
    sed -i 's/security.ubuntu.com/kartolo.sby.datautama.net.id/g' /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y bind9 bind9utils bind9-doc dnsutils && \
    rm -rf /var/lib/apt/lists/*

COPY named.conf /etc/bind/named.conf
COPY db.trailblazer.corp /etc/bind/db.trailblazer.corp
RUN sed -i 's/\r$//' /etc/bind/named.conf && \
    sed -i 's/\r$//' /etc/bind/db.trailblazer.corp

EXPOSE 53/udp
EXPOSE 53/tcp

CMD ["/usr/sbin/named", "-g", "-c", "/etc/bind/named.conf", "-u", "bind"]
