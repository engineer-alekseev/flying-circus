# Room Booking Microservice

## Overview
This microservice application is designed for booking rooms and managing related functionalities. It leverages various technologies and services to provide a seamless experience for users.

## Architecture and Technologies Used
The microservice application follows a microservices architecture, with individual components handling specific tasks. Here is a high-level overview of the architecture:
- Redis: Used for caching to improve performance.
- PostgreSQL: Stores permanent data related to room bookings, users, and other relevant information.
- FastAPI: Acts as the HTTP wrapper for the microservice, providing a fast and efficient web framework.
- Celery: Manages asynchronous tasks and messages within the application.
- Telegram Bot: Integrated with the application for communication and notifications.
- Mail Service: Used for sending emails related to room bookings and other notifications.

## Deployment
The microservice application is deployed using Docker Compose, which orchestrates the containerized services. The deployment process is automated through a Makefile, making it easy to start and manage the application.
Just write in cmd ***Make** and enjoy



## Getting Started
To run the microservice application locally, follow these steps:
- Clone the repository.
- Install Docker and Docker Compose.
Run ***make*** the application.

## Contributing
If you would like to contribute to the project, please follow these guidelines:
Feel free to customize this template to fit the specific details and structure of your microservice architecture, this project has no license.