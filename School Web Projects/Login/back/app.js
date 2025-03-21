import express from 'express';
import bodyParser from 'body-parser';
import { fileURLToPath } from 'url';
import { dirname } from 'path';
import cors from 'cors';
import routes from './routes/index.js';


const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);


const app = express();
const PORT = process.env.PORT || 3000;


app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));


app.get('/api/test-connection', async (req, res) => {
  try {
    const { testConnection } = await import('./utils/database.js');
    const result = await testConnection();
    
    if (result.success) {
      res.status(200).json({ message: result.message });
    } else {
      res.status(500).json({ error: result.error, details: result.details });
    }
  } catch (error) {
    console.error('Error al probar la conexión:', error);
    res.status(500).json({ error: 'Error al conectar a la base de datos', details: error.message });
  }
});

app.use('/api', routes);

app.listen(PORT, () => {
  console.log(`Servidor ejecutándose en el puerto ${PORT}`);
});