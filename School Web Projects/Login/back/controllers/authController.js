import bcrypt from 'bcrypt';
import jwt from 'jsonwebtoken';
import { connectToHana } from '../utils/database.js';

//Implemetnacion de JWT fue con ayuda de Claude 3.7 Sonnet
// Todos los try catch fueron con ayuda de Claude 3.7 Sonnet para que el codigo sea mas limpio y eficiente
const JWT_SECRET = process.env.JWT_SECRET || 'your-secret-key';

export const login = async (req, res) => {
  const email = req.body.email || req.body.Email;
  const password = req.body.password || req.body.Password;
  
  if (!email || !password) {
    return res.status(400).json({ 
      success: false, 
      error: 'Validation error', 
      details: 'Email and password are required' 
    });
  }
  
  let connection;

  try {
    connection = await connectToHana();
    const query = `SELECT * FROM "Accounts" WHERE "Email" = ?`;
    
    connection.exec(query, [email], async (err, results) => {
      if (err) {
        res.status(500).json({ error: 'Database query error', details: err.message });
        return;
      }
      
      if (results && results.length > 0) {
        const user = results[0];
        let passwordMatch = false;
        
        if (user.Password && user.Password.startsWith('$2')) {
          passwordMatch = await bcrypt.compare(password, user.Password);
        } else {
          passwordMatch = (password === user.Password);
        }
        
        if (passwordMatch) {
          const updateQuery = `UPDATE "Accounts" SET "LastLoginDate" = CURRENT_TIMESTAMP WHERE "Email" = ?`;
          
          connection.exec(updateQuery, [email], (updateErr) => {
            if (updateErr) {
              console.error('Error updating LastLoginDate:', updateErr);
            }
            
            const userForToken = {
              id: user.ID,
              email: user.Email
            };
            
            const token = jwt.sign(userForToken, JWT_SECRET, { expiresIn: '24h' });
            
            const safeUser = { ...user };
            delete safeUser.Password;
            
            res.status(200).json({ 
              success: true, 
              message: 'Login successful', 
              user: safeUser,
              token
            });
          });
        } else {
          res.status(401).json({ 
            success: false, 
            message: 'Invalid email or password' 
          });
        }
      } else {
        res.status(401).json({ 
          success: false, 
          message: 'Invalid email or password' 
        });
      }
    });
  } catch (error) {
    res.status(500).json({ 
      success: false, 
      error: 'Database connection error', 
      details: error.message 
    });
    
    if (connection) {
      connection.disconnect();
    }
  }
};

export const register = async (req, res) => {
  const email = req.body.email || req.body.Email;
  const password = req.body.password || req.body.Password;
  
  if (!email || !password) {
    return res.status(400).json({ 
      success: false, 
      error: 'Validation error', 
      details: 'Email and password are required' 
    });
  }
  
  let connection;

  try {
    const saltRounds = 10;
    const hashedPassword = await bcrypt.hash(password, saltRounds);
    
    connection = await connectToHana();
    const checkQuery = `SELECT COUNT(*) AS "count" FROM "Accounts" WHERE "Email" = ?`;
    
    connection.exec(checkQuery, [email], (checkErr, checkResults) => {
      if (checkErr) {
        res.status(500).json({ error: 'Database query error', details: checkErr.message });
        return;
      }
      
      if (checkResults[0].count > 0) {
        res.status(409).json({ success: false, message: 'User with this email already exists' });
        return;
      }
      
      const insertQuery = `INSERT INTO "Accounts" ("Email", "Password", "CreatedAt", "LastLoginDate") 
                          VALUES (?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)`;
      
      connection.exec(insertQuery, [email, hashedPassword], (insertErr) => {
        if (insertErr) {
          res.status(500).json({ error: 'Database query error', details: insertErr.message });
          return;
        }
        
        res.status(201).json({ 
          success: true, 
          message: 'User registered successfully'
        });
      });
    });
  } catch (error) {
    res.status(500).json({ 
      success: false, 
      error: 'Registration error', 
      details: error.message 
    });
    
    if (connection) {
      connection.disconnect();
    }
  }
}; 