# Cryptocurrency Price Tracker (Blockchain.com Visual Clone)

This is a web application built using Node.js and Express that fetches and displays the current prices and 24-hour price changes of popular cryptocurrencies such as Bitcoin (BTC), Ethereum (ETH), Stellar (XLM), and Solana (SOL). The application utilizes the Blockchain.com API to retrieve the pricing data and aims to visually replicate the pricing section of the Blockchain.com website.

![image](https://github.com/mirelesDavid/mirelesDavid-Projects/assets/141588489/67cea702-4326-448a-bff8-4d684ae87156)

## Technologies Used

- Node.js
- Express.js
- Axios (for making HTTP requests)
- EJS (Embedded JavaScript) for templating

## Features

- Fetches and displays the current prices of BTC, ETH, XLM, and SOL in USD
- Calculates and displays the 24-hour price change (percentage) for each cryptocurrency
- Formats the prices with a maximum of two decimal places and uses locale-specific formatting
- Visual design inspired by the Blockchain.com website, mimicking the layout and styling of the pricing section

## Project Structure

The project follows a standard Express application structure, with the main file being `app.js`. The application is organized as follows:

- `app.js`: The entry point of the application, where the Express server is set up, routes are defined, and API requests are made.
- `public/`: Directory containing static assets like CSS and client-side JavaScript files.
- `views/`: Directory containing EJS templates for rendering the application's pages.

## Getting Started

1. Make sure you have Node.js installed on your machine.
2. Clone the repository or download the project files.
3. Navigate to the project directory and install the dependencies by running `npm install`.
4. Start the server with `node app.js`.
5. Open your web browser and visit `http://localhost:4000` to access the application.

## Routes

- `/`: Renders the index page, which displays the current prices and 24-hour price changes for BTC, ETH, XLM, and SOL in a layout similar to the Blockchain.com website.

## API Integration

The application fetches pricing data from the Blockchain.com API (`https://api.blockchain.com/v3/exchange/tickers`). It makes separate API requests for each cryptocurrency (BTC, ETH, XLM, and SOL) and retrieves the last trade price and the price from 24 hours ago.

## Visual Design

The visual design of the application is inspired by the pricing section of the Blockchain.com website. The layout, typography, and color scheme are similar to the original website, providing a familiar user experience for those familiar with Blockchain.com.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
