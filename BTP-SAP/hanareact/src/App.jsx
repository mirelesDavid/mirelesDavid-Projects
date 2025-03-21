import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { 
  Container, 
  Paper, 
  Typography, 
  Table, 
  TableBody, 
  TableCell, 
  TableContainer, 
  TableHead, 
  TableRow,
  Box,
  CircularProgress,
  Alert,
  Fade,
  useTheme,
  ThemeProvider,
  createTheme,
  CssBaseline
} from '@mui/material';
import { motion } from 'framer-motion';

// Create a custom theme with futuristic colors
const darkTheme = createTheme({
  palette: {
    mode: 'dark',
    primary: {
      main: '#00bcd4',
    },
    secondary: {
      main: '#7c4dff',
    },
    background: {
      default: '#121212',
      paper: '#1E1E1E',
    },
  },
  typography: {
    fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif',
    h4: {
      fontWeight: 600,
      letterSpacing: '0.05em',
    },
  },
  components: {
    MuiTableCell: {
      styleOverrides: {
        root: {
          borderBottom: '1px solid rgba(81, 81, 81, 1)',
        },
        head: {
          backgroundColor: '#252525',
          color: '#00bcd4',
          fontWeight: 'bold',
        },
      },
    },
    MuiPaper: {
      styleOverrides: {
        root: {
          backgroundImage: 'linear-gradient(rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.05))',
          boxShadow: '0 8px 40px rgba(0, 0, 0, 0.12)',
          borderRadius: 12,
        },
      },
    },
  },
});

// Custom styled motion components
const MotionContainer = motion(Box);
const MotionTableRow = motion(TableRow);

function App() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const theme = useTheme();

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        setLoading(true);
        // Assuming your backend is running on the same host but different port
        const response = await axios.get('http://localhost:3000/api/data/USUARIOS');
        setUsers(response.data);
        setError(null);
      } catch (err) {
        console.error('Error fetching users:', err);
        setError('Failed to load user data. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    fetchUsers();
  }, []);

  // Format date for better display
  const formatDate = (dateString) => {
    if (!dateString) return 'N/A';
    const date = new Date(dateString);
    return date.toLocaleString();
  };

  return (
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
      <Container maxWidth="lg" sx={{ py: 4 }}>
        <MotionContainer
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          sx={{ mb: 4 }}
        >
          <Typography 
            variant="h4" 
            component="h1" 
            gutterBottom 
            align="center"
            sx={{ 
              color: 'primary.main',
              textTransform: 'uppercase',
              letterSpacing: '0.1em',
              mb: 3,
              textShadow: '0 0 10px rgba(0, 188, 212, 0.5)'
            }}
          >
            User Management Dashboard
          </Typography>
          
          <Typography 
            variant="subtitle1" 
            align="center" 
            sx={{ 
              mb: 5, 
              color: 'text.secondary',
              maxWidth: '700px',
              mx: 'auto'
            }}
          >
            A comprehensive view of all users registered in the HANA database system
          </Typography>
        </MotionContainer>

        <Fade in={true} timeout={1000}>
          <Paper 
            elevation={3} 
            sx={{ 
              p: 3,
              borderRadius: 4,
              overflow: 'hidden',
              position: 'relative',
              '&::before': {
                content: '""',
                position: 'absolute',
                top: 0,
                left: 0,
                width: '100%',
                height: '4px',
                background: 'linear-gradient(90deg, #00bcd4, #7c4dff)',
              }
            }}
          >
            {loading ? (
              <Box sx={{ display: 'flex', justifyContent: 'center', p: 4 }}>
                <CircularProgress color="secondary" />
              </Box>
            ) : error ? (
              <Alert severity="error" sx={{ mb: 2 }}>{error}</Alert>
            ) : (
              <TableContainer component={Paper} elevation={0} sx={{ backgroundColor: 'transparent' }}>
                <Table sx={{ minWidth: 650 }}>
                  <TableHead>
                    <TableRow>
                      <TableCell>ID</TableCell>
                      <TableCell>Name</TableCell>
                      <TableCell>Email</TableCell>
                      <TableCell>Role</TableCell>
                      <TableCell>Registration Date</TableCell>
                    </TableRow>
                  </TableHead>
                  <TableBody>
                    {users.length > 0 ? (
                      users.map((user, index) => (
                        <MotionTableRow 
                          key={user.ID}
                          initial={{ opacity: 0, x: -20 }}
                          animate={{ opacity: 1, x: 0 }}
                          transition={{ duration: 0.3, delay: index * 0.05 }}
                          whileHover={{ 
                            backgroundColor: 'rgba(0, 188, 212, 0.08)',
                            transition: { duration: 0.2 }
                          }}
                        >
                          <TableCell>{user.ID}</TableCell>
                          <TableCell>{user.NOMBRE}</TableCell>
                          <TableCell>{user.EMAIL}</TableCell>
                          <TableCell>{user.ROL}</TableCell>
                          <TableCell>{formatDate(user.FECHA_REGISTRO)}</TableCell>
                        </MotionTableRow>
                      ))
                    ) : (
                      <TableRow>
                        <TableCell colSpan={5} align="center">No users found</TableCell>
                      </TableRow>
                    )}
                  </TableBody>
                </Table>
              </TableContainer>
            )}
          </Paper>
        </Fade>
        
        <Box 
          component={motion.div}
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1.2, duration: 0.8 }}
          sx={{ 
            mt: 4, 
            textAlign: 'center',
            color: 'text.secondary',
            fontSize: '0.875rem'
          }}
        >
          <Typography variant="body2">
            © {new Date().getFullYear()} SAP HANA User Management System
          </Typography>
        </Box>
      </Container>
    </ThemeProvider>
  );
}

export default App;