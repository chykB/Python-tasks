<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJmhRwWJ82DoVR7v1wUR5uoYWxC2e4qrRlNF7zYWyB0zHCq2QhZsvcek0MA7dl_jD8x3k&usqp=CAU">

# FastAPI User Full Name API

## Overview
This project is a FastAPI-based API for managing user full names. It provides endpoints for creating users with first and last names, as well as retrieving the full name.

## Installation
To run this project locally:

1. Clone the repository:
2. Install dependencies
3. Start the FastAPI server.

## Once the server is running
Once the server is running, you can access the API.

### Endpoints

- **POST /users/**
- Creates a new user with first and last names.

- **GET /user/**
- Retrieves the full name.

- **POST /upload_pdf/**
  - Uploads a PDF file and saves it to a specified directory path of your choice. Or automatically save to your current working directory

    #### Parameters
    - `file`: The PDF file to upload.
    - `directory_path` (query, optional): The directory path where the file will be saved. If not provided, the file will be saved to the current working directory.

    #### Responses
    - 200 OK: File uploaded successfully.
    - 400 Bad Request: If the uploaded file is not a PDF.
    - 500 Internal Server Error: If an error occurs during file upload.


