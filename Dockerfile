FROM python:3
RUN pip3 install requests
COPY get_fedora_releases.py /get_fedora_releases.py
ENTRYPOINT ["/get_fedora_releases.py"]