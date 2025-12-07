FROM alpine:latest

RUN apk add --no-cache dnsmasq

COPY dnsmasq.conf /etc/dnsmasq.conf

EXPOSE 53/udp
EXPOSE 53/tcp

CMD ["dnsmasq", "-C", "/etc/dnsmasq.conf"]
