FROM ubuntu:latest

USER root
RUN apt update -y \
    && apt install docker.io curl -y

RUN curl -L "https://github.com/docker/compose/releases/download/v2.12.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose

RUN apt install git

RUN git clone https://github.com/romanovsavelij/MathDailyBot
WORKDIR /MathDailyBot

# RUN apt install systemctl -y
# RUN whoami
# RUN systemctl status docker
# RUN systemctl start docker
# RUN docker run hello-world
# RUN /usr/local/bin/docker-compose up

CMD ["docker-compose", "up", "-d"]
