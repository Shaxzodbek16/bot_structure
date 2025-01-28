# Aiogram Bot Template

This repository provides a **ready-to-use** template for building Telegram bots with [Aiogram](https://docs.aiogram.dev/) and [SQLAlchemy](https://docs.sqlalchemy.org/) for database management. It supports **PostgreSQL** and **SQLite** out of the box, and includes a **Docker** and **docker-compose** setup for convenient deployment.

---

## Table of Contents

1. [Project Structure](#project-structure)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Database Connections](#database-connections)
    - [PostgreSQL (`postgres.py`)](#postgres.py)
    - [SQLite (`sqlite.py`)](#sqlite.py)
6. [Running Migrations](#running-migrations)
7. [Running the Bot Locally](#running-the-bot-locally)
8. [Logging](#logging)
9. [Using Docker](#using-docker)
    - [Dockerfile](#dockerfile)
    - [docker-compose](#docker-compose)
10. [Folder Details](#folder-details)
11. [License](#license)

---

## Project Structure

```plaintext
.
├── Dockerfile
├── README.md
├── alembic.ini
├── app
│   ├── __init__.py
│   ├── bot
│   │   ├── __init__.py
│   │   ├── constants
│   │   │   └── __init__.py
│   │   ├── extensions
│   │   │   └── __init__.py
│   │   ├── filters
│   │   │   └── __init__.py
│   │   ├── handlers
│   │   │   └── __init__.py
│   │   ├── keyboards
│   │   │   └── __init__.py
│   │   ├── middlewares
│   │   │   └── __init__.py
│   │   ├── models
│   │   │   └── __init__.py
│   │   ├── routers
│   │   │   └── __init__.py
│   │   └── state
│   │       └── __init__.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── constants
│   │   │   └── __init__.py
│   │   ├── databases
│   │   │   ├── __init__.py
│   │   │   ├── postgres.py
│   │   │   └── sqlite.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   └── users.py
│   │   └── settings
│   │       ├── __init__.py
│   │       └── config.py
│   └── server
│       ├── __init__.py
│       └── server.py
├── docker-compose.yml
├── entrypoint.sh
├── example.env
├── media
│   └── all_mdiea_files.jpg
├── migrations
│   ├── README
│   ├── env.py
│   ├── script.py.mako
│   └── versions
├── requirements.txt
└── venv