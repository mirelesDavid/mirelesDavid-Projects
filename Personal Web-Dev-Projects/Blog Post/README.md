# Blog Web Application

This is a simple blog web application built using Node.js and Express. It allows users to create, edit, and delete blog posts. The application stores the post data in-memory, but it can be easily extended to use a database for persistent storage.
![image](https://github.com/mirelesDavid/mirelesDavid-Projects/assets/141588489/3a1129b5-bd4e-4750-8d26-e308b39b1e12)

## Technologies Used

- Node.js
- Express.js
- EJS (Embedded JavaScript) for templating
- body-parser middleware

## Features

- Create new blog posts with a title, description, author, and image
- View a list of all blog posts
- Edit existing blog posts
- Delete blog posts
![image](https://github.com/mirelesDavid/mirelesDavid-Projects/assets/141588489/b8e963e7-563f-40e5-91fc-3db9f02bf00a)

## Project Structure

The project follows a standard Express application structure, with the main file being `app.js`. The application is organized into different routes and functionality:

- `app.js`: The entry point of the application, where the Express server is set up and routes are defined.
- `public/`: Directory containing static assets like CSS and client-side JavaScript files.
- `views/`: Directory containing EJS templates for rendering the application's pages.

## Getting Started

1. Make sure you have Node.js installed on your machine.
2. Clone the repository or download the project files.
3. Navigate to the project directory and install the dependencies by running `npm install`.
4. Start the server with `node app.js`.
5. Open your web browser and visit `http://localhost:3000` to access the application.

## Routes

- `/`: Renders the index page, which displays a list of all blog posts.
- `/create`: Renders the create page, where users can create a new blog post.
- `/edit`: Renders the edit page, where users can edit an existing blog post.
- `/post-create`: Handles the POST request for creating a new blog post.
- `/edit-post`: Handles the POST request for retrieving an existing blog post for editing.
- `/modify`: Handles the POST request for modifying (updating or deleting) an existing blog post.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
