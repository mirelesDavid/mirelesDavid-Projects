// app.js - Archivo principal del backend

import express from 'express';
import hanaClient from '@sap/hana-client';
import bodyParser from 'body-parser';
import dotenv from 'dotenv';
import { fileURLToPath } from 'url';
import { dirname } from 'path';
import cors from 'cors';

dotenv.config();
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3000;


app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));


const connectionConfig = {
  serverNode: '37dfb9d0-2fa6-47ff-b712-92b0fcd1cb56.hana.trial-us10.hanacloud.ondemand.com:443',
  uid: 'DBADMIN',
  pwd: 'Maple340',
  encrypt: true, 
  sslValidateCertificate: false,
  sslCryptoProvider: 'openssl',
  connectTimeout: 15000,
  reconnect: true,
  maxReconnects: 3
};


function connectToHana() {
  const conn = hanaClient.createConnection();
  
  return new Promise((resolve, reject) => {
    conn.connect(connectionConfig, (err) => {
      if (err) {
        reject(err);
        return;
      }
      resolve(conn);
    });
  });
}

app.get('/api/test-connection', async (req, res) => {
  try {
    const connection = await connectToHana();
    connection.disconnect();
    res.status(200).json({ message: 'Conexión exitosa a SAP HANA Cloud' });
  } catch (error) {
    console.error('Error al conectar a SAP HANA:', error);
    res.status(500).json({ error: 'Error al conectar a la base de datos', details: error.message });
  }
});


app.get('/api/data/:tableName', async (req, res) => {
  const { tableName } = req.params;
  let connection;
  
  try {
    connection = await connectToHana();
    
    const query = `SELECT * FROM "${tableName}" LIMIT 100`;
    
    connection.exec(query, (err, results) => {
      if (err) {
        console.error('Error al ejecutar la consulta:', err);
        res.status(500).json({ error: 'Error al ejecutar la consulta', details: err.message });
        return;
      }
      
      connection.disconnect();
      res.status(200).json(results);
    });
  } catch (error) {
    console.error('Error al conectar a SAP HANA:', error);
    res.status(500).json({ error: 'Error al conectar a la base de datos', details: error.message });
    
    if (connection) {
      connection.disconnect();
    }
  }
});

// Ejemplo de ruta para insertar datos (INSERT)
app.post('/api/data/:tableName', async (req, res) => {
  const { tableName } = req.params;
  const data = req.body;
  let connection;
  
  try {
    connection = await connectToHana();
    
    // Construir la consulta INSERT dinámicamente
    const columns = Object.keys(data).join('", "');
    const placeholders = Object.keys(data).map(() => '?').join(', ');
    const values = Object.values(data);
    
    const query = `INSERT INTO "${tableName}" ("${columns}") VALUES (${placeholders})`;
    
    connection.exec(query, values, (err, results) => {
      if (err) {
        console.error('Error al insertar datos:', err);
        res.status(500).json({ error: 'Error al insertar datos', details: err.message });
        return;
      }
      
      connection.disconnect();
      res.status(201).json({ message: 'Datos insertados correctamente', affectedRows: results });
    });
  } catch (error) {
    console.error('Error al conectar a SAP HANA:', error);
    res.status(500).json({ error: 'Error al conectar a la base de datos', details: error.message });
    
    if (connection) {
      connection.disconnect();
    }
  }
});

// Ejemplo de ruta para actualizar datos (UPDATE)
app.put('/api/data/:tableName/:id', async (req, res) => {
  const { tableName, id } = req.params;
  const data = req.body;
  let connection;
  
  try {
    connection = await connectToHana();
    
    // Construir la consulta UPDATE dinámicamente
    const setClause = Object.keys(data).map(key => `"${key}" = ?`).join(', ');
    const values = [...Object.values(data), id];
    
    const query = `UPDATE "${tableName}" SET ${setClause} WHERE "ID" = ?`;
    
    connection.exec(query, values, (err, results) => {
      if (err) {
        console.error('Error al actualizar datos:', err);
        res.status(500).json({ error: 'Error al actualizar datos', details: err.message });
        return;
      }
      
      connection.disconnect();
      res.status(200).json({ message: 'Datos actualizados correctamente', affectedRows: results });
    });
  } catch (error) {
    console.error('Error al conectar a SAP HANA:', error);
    res.status(500).json({ error: 'Error al conectar a la base de datos', details: error.message });
    
    if (connection) {
      connection.disconnect();
    }
  }
});

// Ejemplo de ruta para eliminar datos (DELETE)
app.delete('/api/data/:tableName/:id', async (req, res) => {
  const { tableName, id } = req.params;
  let connection;
  
  try {
    connection = await connectToHana();
    
    const query = `DELETE FROM "${tableName}" WHERE "ID" = ?`;
    
    connection.exec(query, [id], (err, results) => {
      if (err) {
        console.error('Error al eliminar datos:', err);
        res.status(500).json({ error: 'Error al eliminar datos', details: err.message });
        return;
      }
      
      connection.disconnect();
      res.status(200).json({ message: 'Datos eliminados correctamente', affectedRows: results });
    });
  } catch (error) {
    console.error('Error al conectar a SAP HANA:', error);
    res.status(500).json({ error: 'Error al conectar a la base de datos', details: error.message });
    
    if (connection) {
      connection.disconnect();
    }
  }
});

// Ejemplo de ruta para ejecutar una consulta personalizada
app.post('/api/query', async (req, res) => {
  const { query, params = [] } = req.body;
  let connection;
  
  try {
    connection = await connectToHana();
    
    connection.exec(query, params, (err, results) => {
      if (err) {
        console.error('Error al ejecutar la consulta:', err);
        res.status(500).json({ error: 'Error al ejecutar la consulta', details: err.message });
        return;
      }
      
      connection.disconnect();
      res.status(200).json(results);
    });
  } catch (error) {
    console.error('Error al conectar a SAP HANA:', error);
    res.status(500).json({ error: 'Error al conectar a la base de datos', details: error.message });
    
    if (connection) {
      connection.disconnect();
    }
  }
});

// Iniciar el servidor
app.listen(PORT, () => {
  console.log(`Servidor corriendo en el puerto ${PORT}`);
});

export default app;