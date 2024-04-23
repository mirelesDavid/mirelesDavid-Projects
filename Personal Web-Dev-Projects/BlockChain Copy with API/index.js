import express from "express";
import bodyParser from "body-parser";
import axios from "axios";

const app = express();
const port = 4000;
app.use(express.static("./public"));
app.use(bodyParser.urlencoded({ extended: true }));

const API_URL = "https://api.blockchain.com/v3/exchange/tickers";

app.get("/", async (req, res) => {
  try {
      const btc_price = await axios.get(API_URL + "/BTC-USD");
      const eth_price = await axios.get(API_URL + "/ETH-USD");
      const xlm_price = await axios.get(API_URL + "/XLM-USD");
      const sol_price = await axios.get(API_URL + "/SOL-USD");

      const formatPrice = (price) => parseFloat(price).toLocaleString(undefined, { maximumFractionDigits: 2 });
      
      const calculateChange = (currentPrice, oldPrice) => {
          const change = currentPrice - oldPrice;
          const percentageChange = (change / oldPrice) * 100;
          return percentageChange.toFixed(2);
      };

      const btcChange = calculateChange(btc_price.data.last_trade_price, btc_price.data.price_24h);
      const ethChange = calculateChange(eth_price.data.last_trade_price, eth_price.data.price_24h);
      const xlmChange = calculateChange(xlm_price.data.last_trade_price, xlm_price.data.price_24h);
      const solChange = calculateChange(sol_price.data.last_trade_price, sol_price.data.price_24h);

      res.render("index.ejs", {
          btcPrice: formatPrice(btc_price.data.last_trade_price),
          ethPrice: formatPrice(eth_price.data.last_trade_price),
          xlmPrice: formatPrice(xlm_price.data.last_trade_price),
          solPrice: formatPrice(sol_price.data.last_trade_price),
          btcChange,
          ethChange,
          xlmChange,
          solChange
      });

  } catch (error) {
      console.log(error.response.data);
      res.status(500);
  }
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`)
});
