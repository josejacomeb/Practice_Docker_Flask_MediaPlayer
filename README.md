# Practice_Docker_Flask_MediaPlayer
Program to practice the Docker platform, along with the Flask, OpenCV, Redis, Tesseract and Mosquitto libraries for transmitting image data to a webserver 

Images generated with Docker's BuildKit, example of generation

## Software used
- Docker
- OpenCV
- Flask
- Redis
- Tesseract
- Mosquitto

## Getting started
To run the code, please clone this repository
```commandline
git clone https://github.com/josejacomeb/Practice_Docker_Flask_MediaPlayer.git
```
Rename the `.env.example` file to `.env` and set up your environment files like it's explained inside the file, you can use the following command
```commandline
cp .env.example .env
```
### Optional: Use BuildKit
BuildKit is a useful tool to build faster docker images, just setup your environmental variables with the following command
```commandline
export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1
```

### Build and run the  container
```commandline
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build
```

### Stop the container
```commandline
docker-compose down
```

## Build the image standalone
```commandline
DOCKER_BUILDKIT=1 docker build --tag media_player .
```

## TODO
- [X] ~Build a Media Player Class with OpenCV~ 
- [ ] Develop a Flask Web server to show the data of the video
- [ ] Use Mosquitto to interchange information between OpenCV and Flask
- [ ] Use a DB to ask for user's access
- [ ] Practice well coding practices in Python
- [ ] Practice Kalman Filtering
