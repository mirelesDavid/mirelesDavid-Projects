import hanaClient from '@sap/hana-client';

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

export function connectToHana() {
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

export async function testConnection() {
  try {
    const connection = await connectToHana();
    connection.disconnect();
    return { success: true, message: 'Conexión exitosa a SAP HANA Cloud' };
  } catch (error) {
    return { success: false, error: 'Error al conectar a la base de datos', details: error.message };
  }
} 