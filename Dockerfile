FROM ghcr.io/walkerlab/pytorch-jupyter:cuda-11.8.0-pytorch-1.13.0-torchvision-0.14.0-torchaudio-0.13.0-ubuntu-22.04

COPY . /src/project
RUN pip3 install -e /src/project[dev]