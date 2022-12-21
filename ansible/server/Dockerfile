FROM alpine:3.17

RUN apk add --no-cache openssh-client ansible git sshpass openssh openrc

RUN mkdir -p /root/.ssh
RUN echo "Host *" > /root/.ssh/config && echo " StrictHostKeyChecking no" >> /root/.ssh/config
EXPOSE 22

COPY ./ansible /ansible
WORKDIR /ansible