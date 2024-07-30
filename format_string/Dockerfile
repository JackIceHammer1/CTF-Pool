FROM ubuntu:latest

RUN apt update -y
RUN apt install -y socat



COPY ./format .

EXPOSE 1234
CMD ["socat", "TCP4-LISTEN:1234,reuseaddr,fork", "SYSTEM:./format"]
