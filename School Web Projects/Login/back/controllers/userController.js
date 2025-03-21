import { connectToHana } from '../utils/database.js';

// Todos los try catch fueron con ayuda de Claude 3.7 Sonnet para que el codigo sea mas limpio y eficiente

export const getUserProfile = async (req, res) => {
  let connection;
  
  try {
    connection = await connectToHana();
    const query = `SELECT "ID", "Email", "CreatedAt", "LastLoginDate" FROM "Accounts" WHERE "ID" = ?`;
    
    connection.exec(query, [req.user.id], (err, results) => {
      if (err) {
        res.status(500).json({ error: 'Database query error', details: err.message });
        return;
      }
      
      if (results && results.length > 0) {
        res.status(200).json({ 
          success: true, 
          user: results[0]
        });
      } else {
        res.status(404).json({ 
          success: false, 
          message: 'User not found' 
        });
      }
      
      connection.disconnect();
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


export const getAllUsers = async (req, res) => {
  let connection;
  
  try {
    connection = await connectToHana();
    const query = `SELECT "ID", "Email", "CreatedAt", "LastLoginDate" FROM "Accounts"`;
    
    connection.exec(query, [], (err, results) => {
      if (err) {
        res.status(500).json({ 
          success: false, 
          error: 'Database query error', 
          details: err.message 
        });
        return;
      }
      
      res.status(200).json({ 
        success: true, 
        users: results
      });
      
      connection.disconnect();
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


export const getUserById = async (req, res) => {
  const { id } = req.params;
  let connection;
  
  try {
    connection = await connectToHana();
    const query = `SELECT "ID", "Email", "CreatedAt", "LastLoginDate" FROM "Accounts" WHERE "ID" = ?`;
    
    connection.exec(query, [id], (err, results) => {
      if (err) {
        res.status(500).json({ 
          success: false, 
          error: 'Database query error', 
          details: err.message 
        });
        return;
      }
      
      if (results && results.length > 0) {
        res.status(200).json({ 
          success: true, 
          user: results[0]
        });
      } else {
        res.status(404).json({ 
          success: false, 
          message: 'User not found' 
        });
      }
      
      connection.disconnect();
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


export const updateUser = async (req, res) => {
  const { id } = req.params;
  const { Email } = req.body;
  let connection;
  
  try {
    connection = await connectToHana();
    
    const checkQuery = `SELECT COUNT(*) AS "count" FROM "Accounts" WHERE "ID" = ?`;
    
    connection.exec(checkQuery, [id], (checkErr, checkResults) => {
      if (checkErr) {
        res.status(500).json({ 
          success: false, 
          error: 'Database query error', 
          details: checkErr.message 
        });
        return;
      }
      
      if (checkResults[0].count === 0) {
        res.status(404).json({ 
          success: false, 
          message: 'User not found' 
        });
        return;
      }
      
      const updateQuery = `UPDATE "Accounts" SET "Email" = ? WHERE "ID" = ?`;
      
      connection.exec(updateQuery, [Email, id], (updateErr) => {
        if (updateErr) {
          res.status(500).json({ 
            success: false, 
            error: 'Database query error', 
            details: updateErr.message 
          });
          return;
        }
        
        res.status(200).json({ 
          success: true, 
          message: 'User updated successfully'
        });
        
        connection.disconnect();
      });
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


export const deleteUser = async (req, res) => {
  const { id } = req.params;
  let connection;
  
  try {
    connection = await connectToHana();
    
    const checkQuery = `SELECT COUNT(*) AS "count" FROM "Accounts" WHERE "ID" = ?`;
    
    connection.exec(checkQuery, [id], (checkErr, checkResults) => {
      if (checkErr) {
        res.status(500).json({ 
          success: false, 
          error: 'Database query error', 
          details: checkErr.message 
        });
        return;
      }
      
      if (checkResults[0].count === 0) {
        res.status(404).json({ 
          success: false, 
          message: 'User not found' 
        });
        return;
      }
      
      const deleteQuery = `DELETE FROM "Accounts" WHERE "ID" = ?`;
      
      connection.exec(deleteQuery, [id], (deleteErr) => {
        if (deleteErr) {
          res.status(500).json({ 
            success: false, 
            error: 'Database query error', 
            details: deleteErr.message 
          });
          return;
        }
        
        res.status(200).json({ 
          success: true, 
          message: 'User deleted successfully'
        });
        
        connection.disconnect();
      });
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