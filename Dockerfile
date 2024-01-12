FROM python:3.11-slim-bookworm

# RUN apt-get update
RUN apt-get update && apt-get install -y \
  curl \
  # procps \
  # build-essential \
  # libtbb2 \
  # libtbb-dev \
  # libjpeg-dev \
  # libpng-dev \
  # libtiff-dev \
  # libglib2.0-0 \
  # # libappindicator3-1 \
  # libatk-bridge2.0-0 \
  # libgtk-3-0 \
  # lsb-release \
  # libsm6 \
  # libxext6 \
  # libavformat-dev \
  # libpq-dev \
  # libgbm1 \
  # MySQL
  gcc \
  default-libmysqlclient-dev

ENV TZ Asia/Tokyo

WORKDIR /usr/src/app
COPY ./app ./
COPY ./poetry.lock ./pyproject.toml ./
# RUN pip install --upgrade pip

# Poetryのパスを設定
ENV PATH /root/.local/bin:$PATH

# Poetryをインストール
RUN curl -sSL https://install.python-poetry.org | python - \
  # Poetryが仮想環境を生成しないようにする
  && poetry config virtualenvs.create false \
  && poetry install

# Supercronicをインストール
# Latest releases available at https://github.com/aptible/supercronic/releases
ENV SUPERCRONIC_URL=https://github.com/aptible/supercronic/releases/download/v0.2.29/supercronic-linux-amd64 \
  SUPERCRONIC=supercronic-linux-amd64 \
  SUPERCRONIC_SHA1SUM=cd48d45c4b10f3f0bfdd3a57d054cd05ac96812b

RUN curl -fsSLO "$SUPERCRONIC_URL" \
  && echo "${SUPERCRONIC_SHA1SUM}  ${SUPERCRONIC}" | sha1sum -c - \
  && chmod +x "$SUPERCRONIC" \
  && mv "$SUPERCRONIC" "/usr/local/bin/${SUPERCRONIC}" \
  && ln -s "/usr/local/bin/${SUPERCRONIC}" /usr/local/bin/supercronic

# You might need to change this depending on where your crontab is located
COPY crontab crontab
