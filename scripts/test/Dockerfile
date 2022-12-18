FROM ubuntu:latest

RUN apt update -y && apt install -y python3 python3-pip
ADD requirements.txt /test_results/requirements.txt
ADD src /test_results/src
WORKDIR /test_results
RUN pip3 install -r requirements.txt

RUN python3 -m pytest src --alluredir=./allure

CMD tail -f /dev/null