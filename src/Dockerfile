from debian:bookworm-slim

COPY ./entrypoint.sh /

RUN apt-get update && \
	apt install -y net-tools \
	iproute2 iputils-ping

RUN chmod 777 entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]