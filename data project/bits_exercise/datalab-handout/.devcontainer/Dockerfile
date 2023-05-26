FROM mcr.microsoft.com/devcontainers/cpp:0-debian-11

# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get -y install --no-install-recommends \
  libwww-perl gcc-multilib \
  && rm -rf /var/lib/apt/lists/*
