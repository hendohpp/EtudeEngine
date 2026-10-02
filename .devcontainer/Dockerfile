# syntax=docker/dockerfile:1
FROM debian:stable-slim
ENV DEBIAN_FRONTEND=noninteractive

# install development tools
RUN <<EOF
apt-get update
apt-get install -y --no-install-recommends \
    bash \
    git \
    tree \
    g++ \
    make \
    cmake \
    python3 \
    python3-pip \
    python3-venv \
    curl \
    ca-certificates \
    graphviz \
    xz-utils \
    texlive-latex-base \
    texlive-latex-recommended \
    texlive-science \
    texlive-pictures \
    texlive-fonts-recommended \
    lmodern \
    ghostscript

# ieeetran latex template
mkdir -p /usr/share/texmf/tex/latex/IEEEtran
curl -Ls "https://mirrors.ctan.org/macros/latex/contrib/IEEEtran/IEEEtran.cls" \
    -o /usr/share/texmf/tex/latex/IEEEtran/IEEEtran.cls
texhash

# clean apt caches and remove documentation
rm -rf /var/lib/apt/lists/*
rm -rf /usr/share/doc/* /usr/share/man/* /usr/share/texmf/doc
EOF

# install typst markup language
RUN <<EOF
TYPST_ARCH="$(uname -m)"
curl -Ls "https://github.com/typst/typst/releases/download/v0.15.1/typst-${TYPST_ARCH}-unknown-linux-musl.tar.xz" \
    | tar -xJ -C /usr/local/bin --strip-components=1 "typst-${TYPST_ARCH}-unknown-linux-musl/typst"
EOF

# create user for vscode
RUN useradd -m -s /bin/bash vscode
USER vscode

# create and activate python virtual env
RUN python3 -m venv /home/vscode/venv
ENV PATH="/home/vscode/venv/bin:$PATH"

# set internal default shell 
ENV SHELL=/bin/bash