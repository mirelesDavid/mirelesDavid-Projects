import React from "react";
import { Typography } from "@mui/material";
import "./Footer.css"

const Footer = () => {
  const currentYear = new Date().getFullYear();
  return (
    <footer>
      <Typography variant="body2">
        Copyright {currentYear}
      </Typography>
    </footer>
  );
};

export default Footer;
