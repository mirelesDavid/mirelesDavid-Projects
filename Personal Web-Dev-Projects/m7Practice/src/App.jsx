import { useState } from "react";
import Header from "./Header.jsx"; 
import Footer from "./Footer.jsx";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import "./App.css";

function App() {
  const [burger, setBurger] = useState("");

  return (
    <>
      <Header /> 

      <div className="centerButtons">
        <Button variant="contained" color="primary" onClick={() => setBurger("Western Bacon")}>
          Western Bacon
        </Button>
        <Button variant="contained" color="secondary" onClick={() => setBurger("Famous Star")}>
          Famous Star
        </Button>
      </div>

      <div className="inputContainer">
        <TextField
          label="Escribe tu hamburguesa"
          id="filled-hidden-label-small"
          defaultValue="Small"
          variant="filled"
          size="small"
          value={burger}
          onChange={(e) => setBurger(e.target.value)}
        />
      </div>

      <p>Escogiste la hamburguesa: {burger || "Ninguna"}</p>

      <Footer />
    </>
  );
}

export default App;
