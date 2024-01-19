FROM python:3
RUN pip3 install fedora-distro-aliases
COPY get_fedora_releases.py /get_fedora_releases.py
ENTRYPOINT ["/get_fedora_releases.py"]