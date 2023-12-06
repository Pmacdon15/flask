# Flask Server

## Project Overview

This Flask project provides a simple web application that displays random memes and includes additional functionality such as a Google Maps embed and a Bootstrap navbar. The project is designed to be easily set up and run locally.


# Table of Contents

[Flask Server](#flask-server)
- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)
    1. [Random Meme Page](#random-meme-page)
    2. [Google Maps Embed Page](#google-maps-embed-page)
    3. [Bootstrap Navbar Page](#bootstrap-navbar-page)

## Prerequisites

Before running the project, ensure you have the following:

1. **Python**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## Installation

Clone the Repository:

```bash

git clone https://github.com/your-username/your-repo.git

```

1. Navigate to the Project Directory:

```bash

cd flash_server

```

2. Place .env file in flask_server directory. it should look like this:

```.env

api_key = "You Api key from Google Maps here"

```

## Running the Application

1. **Virtual Environment**: The virtual environment is included in this project please run the following command to start:

```bash

.\\myenv\Scripts\Activate

```

2. Run server:

```bash

python server.py

```

## Usage

1. ### Random Meme Page
Visit http://127.0.0.1:8080/ to view a page displaying a random meme. The meme is fetched from the "meme-api.com" API.

2. ### Google Maps Embed Page
Visit http://127.0.0.1:8080/map to view a page with a Google Maps embed. The location is set to "Calgary, Ab" by default, but you can modify it in the location variable in the map route.

3. ### Bootstrap Navbar Page
Visit http://127.0.0.1:8080/navbar to view a page with a Bootstrap navbar