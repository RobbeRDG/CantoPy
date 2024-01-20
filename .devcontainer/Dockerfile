FROM python:3.10-slim

# Configure new user
ARG USERNAME=robbe
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Set poetry environment variables
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=0 \
    POETRY_VERSION=1.7.1

# Set bash as the shell env
ENV SHELL=/bin/bash

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Install packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    git \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the default user
USER $USERNAME

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Update python path to add the cantopy package folder and add the poetry bin folder to the path 
ENV PYTHONPATH "${PYTHONPATH}:/workspaces/CantoPy/cantopy"
ENV PATH="${PATH}:${HOME}/.local/bin"




