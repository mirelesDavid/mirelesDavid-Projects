import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import bodyParser from 'body-parser';
import jwt from 'jsonwebtoken';
import { createServer } from 'http';
import { Server } from 'socket.io';

dotenv.config();

const app = express();
const httpServer = createServer(app);
const io = new Server(httpServer, {
  cors: {
    origin: "*",
    methods: ["GET", "POST"]
  }
});
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/api/test', (req, res) => {
  res.json({ message: 'API is working!' });
});

io.on('connection', (socket) => {
  console.log('New user connected:', socket.id);
  
  socket.on('join', (username) => {
    socket.username = username;
    io.emit('message', {
      user: 'system',
      text: `${username} has joined the chat`,
      timestamp: new Date().toISOString()
    });
    console.log(`${username} joined the chat`);
  });
  
  socket.on('send-message', (message) => {
    io.emit('message', {
      user: socket.username,
      text: message,
      timestamp: new Date().toISOString()
    });
  });
  
  socket.on('disconnect', () => {
    if (socket.username) {
      io.emit('message', {
        user: 'system',
        text: `${socket.username} has left the chat`,
        timestamp: new Date().toISOString()
      });
      console.log(`${socket.username} left the chat`);
    }
  });
});

httpServer.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

export default app;
