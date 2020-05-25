FROM ubuntu:16.04

RUN apt-get update -y && \  
    apt-get install -y python3-pip python3-dev

RUN pip3 install Flask

WORKDIR /nisum

COPY . /nisum

EXPOSE 5002

ENTRYPOINT ["python3"]
CMD ["app.py"]
