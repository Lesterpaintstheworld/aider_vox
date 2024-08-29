FROM python:3.10-slim
RUN apt-get update
RUN apt-get install -y less git build-essential
COPY . /aider_vox
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -e /aider_vox[dev]
RUN git config --global --add safe.directory /aider_vox
WORKDIR /aider_vox
