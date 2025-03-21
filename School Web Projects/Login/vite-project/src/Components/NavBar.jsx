import React from "react";
import { AppBar, Toolbar, Typography, Button } from "@mui/material";
import { useNavigate } from 'react-router-dom';

export function NavBar(){
    const navigate = useNavigate();
    
    const handleLogout = () => {
        localStorage.removeItem('token');
        localStorage.removeItem('userData');
        localStorage.removeItem('userEmail');
        
        navigate('/');
    };

    return (
        <AppBar position="static">
          <Toolbar>
            <Typography variant="h6" sx={{ flexGrow: 1 }}>
              React Practice
            </Typography>
            <Button color="inherit" onClick={() => navigate('/mainpage')}>Home</Button>
            <Button color="inherit" onClick={() => navigate('/contact', { state: { email: localStorage.getItem('userEmail') } })}>Contact</Button>
            <Button color="inherit" onClick={handleLogout}>Logout</Button>
          </Toolbar>
        </AppBar>
      );
}