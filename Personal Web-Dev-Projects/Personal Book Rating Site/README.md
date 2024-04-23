# Book Review Web Application

This is a web application built using Node.js and Express that allows users to create, view, edit, and delete book reviews. It utilizes PostgreSQL as the database, and the application leverages various libraries such as `pg` for interacting with PostgreSQL, `axios` for making HTTP requests, and `express` for setting up the server.
![image](https://github.com/mirelesDavid/mirelesDavid-Projects/assets/141588489/aafa6162-4b1a-4708-a3c2-e802f1a38dc5)

## Features

- Create new book reviews with a title, description, rating, and author
- View a list of all book reviews with their details
- Edit existing book reviews
- Delete book reviews
- Fetch and display book cover images from the Open Library API based on the book's ISBN

## Technologies Used

- Node.js
- Express.js
- PostgreSQL
- Axios
- EJS (Embedded JavaScript) for templating

![image](https://github.com/mirelesDavid/mirelesDavid-Projects/assets/141588489/e02555fa-503f-4694-9be5-b77b8b0e7680)
## Project Structure

The project follows a standard Express application structure, with the main file being `app.js`. The application is organized into different routes and functionality:

- `app.js`: The entry point of the application, where the Express server is set up and routes are defined.
- `public/`: Directory containing static assets like CSS and client-side JavaScript files.
- `views/`: Directory containing EJS templates for rendering the application's pages.

## Getting Started

1. Make sure you have Node.js and PostgreSQL installed on your machine.
2. Clone the repository or download the project files.
3. Navigate to the project directory and install the dependencies by running `npm install`.
4. Set up the PostgreSQL database and update the connection details in `app.js`.
5. Start the server with `node app.js`.
6. Open your web browser and visit `http://localhost:3000` to access the application.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
