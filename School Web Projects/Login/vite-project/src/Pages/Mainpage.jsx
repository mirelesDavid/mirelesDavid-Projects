//Created by David Mireles using Cursor IDE with Claude 3.7 Sonnet Help to make code handle edge cases and make the FrontEnd look better.

import React, { useState, useEffect } from "react";
import { NavBar } from "../Components/NavBar";
import { 
  Container, 
  Typography, 
  Paper, 
  Box, 
  CircularProgress, 
  Button,
  TextField,
  Grid,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  IconButton,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Alert,
  Snackbar,
  InputAdornment
} from "@mui/material";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import DeleteIcon from '@mui/icons-material/Delete';
import EditIcon from '@mui/icons-material/Edit';
import RefreshIcon from '@mui/icons-material/Refresh';
import AddIcon from '@mui/icons-material/Add';
import SearchIcon from '@mui/icons-material/Search';
import ClearIcon from '@mui/icons-material/Clear';

export function Dashboard() {
  const [userData, setUserData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [users, setUsers] = useState([]);
  const [selectedUser, setSelectedUser] = useState(null);
  const [updateFormOpen, setUpdateFormOpen] = useState(false);
  const [createUserFormOpen, setCreateUserFormOpen] = useState(false);
  const [deleteConfirmOpen, setDeleteConfirmOpen] = useState(false);
  const [searchId, setSearchId] = useState('');
  const [updateFormData, setUpdateFormData] = useState({
    Email: ''
  });
  const [createUserFormData, setCreateUserFormData] = useState({
    Email: '',
    Password: ''
  });
  const [notification, setNotification] = useState({
    open: false,
    message: '',
    severity: 'success'
  });
  
  const navigate = useNavigate();

  const getToken = () => localStorage.getItem('token');

  const getAuthHeaders = () => ({
    headers: {
      'Authorization': `Bearer ${getToken()}`
    }
  });

  useEffect(() => {
    const fetchUserProfile = async () => {
      try {
        setLoading(true);
        
        const response = await axios.get('http://localhost:3000/api/user-profile', getAuthHeaders());
        
        if (response.data.success) {
          setUserData(response.data.user);
          fetchAllUsers();
        }
      } catch (err) {
        console.error('Error fetching user profile:', err);
        
        if (err.response && (err.response.status === 401 || err.response.status === 403)) {
          handleLogout();
          setError('Your session has expired.');
        } else {
          setError('Failed to load user profile. Please try again.');
        }
      } finally {
        setLoading(false);
      }
    };
    
    fetchUserProfile();
  }, [navigate]);

  const fetchAllUsers = async () => {
    try {
      setLoading(true);
      setSearchId('');
      const response = await axios.get('http://localhost:3000/api/users', getAuthHeaders());
      
      if (response.data.success) {
        setUsers(response.data.users);
      }
    } catch (err) {
      console.error('Error fetching users:', err);
      handleApiError(err, 'Failed to fetch users');
    } finally {
      setLoading(false);
    }
  };

  const fetchUserById = async () => {
    if (!searchId.trim()) {
      showNotification('Please enter a user ID', 'error');
      return;
    }
    
    try {
      setLoading(true);
      const response = await axios.get(`http://localhost:3000/api/users/${searchId}`, getAuthHeaders());
      
      if (response.data.success) {
        setUsers([response.data.user]);
        showNotification('User fetched successfully', 'success');
      }
    } catch (err) {
      console.error('Error fetching user by ID:', err);
      handleApiError(err, 'Failed to fetch user');
    } finally {
      setLoading(false);
    }
  };

  const handleUpdateUser = (user) => {
    setSelectedUser(user);
    setUpdateFormData({
      Email: user.Email
    });
    setUpdateFormOpen(true);
  };

  const handleDeleteUser = (user) => {
    setSelectedUser(user);
    setDeleteConfirmOpen(true);
  };

  const confirmDeleteUser = async () => {
    if (!selectedUser || (userData && selectedUser.ID === userData.ID)) {
      showNotification('You cannot delete your own account', 'error');
      setDeleteConfirmOpen(false);
      return;
    }
    
    try {
      setLoading(true);
      const response = await axios.delete(`http://localhost:3000/api/users/${selectedUser.ID}`, getAuthHeaders());
      
      if (response.data.success) {
        fetchAllUsers();
        showNotification('User deleted successfully', 'success');
      }
    } catch (err) {
      console.error('Error deleting user:', err);
      handleApiError(err, 'Failed to delete user');
    } finally {
      setLoading(false);
      setDeleteConfirmOpen(false);
    }
  };

  const handleUpdateFormChange = (e) => {
    const { name, value } = e.target;
    setUpdateFormData({
      ...updateFormData,
      [name]: value
    });
  };

  const submitUpdateUser = async () => {
    if (!selectedUser) return;
    
    try {
      setLoading(true);
      const response = await axios.put(
        `http://localhost:3000/api/users/${selectedUser.ID}`, 
        updateFormData,
        getAuthHeaders()
      );
      
      if (response.data.success) {
        fetchAllUsers();
        setUpdateFormOpen(false);
        showNotification('User updated successfully', 'success');
      }
    } catch (err) {
      console.error('Error updating user:', err);
      handleApiError(err, 'Failed to update user');
    } finally {
      setLoading(false);
    }
  };

  const handleCreateUserFormChange = (e) => {
    const { name, value } = e.target;
    setCreateUserFormData({
      ...createUserFormData,
      [name]: value
    });
  };

  const submitCreateUser = async () => {
    try {
      setLoading(true);
      
      const response = await axios.post(
        'http://localhost:3000/api/register', 
        createUserFormData,
        getAuthHeaders()
      );
      
      if (response.data.success) {
        fetchAllUsers();
        setCreateUserFormOpen(false);
        setCreateUserFormData({
          Email: '',
          Password: ''
        });
        showNotification('User created successfully', 'success');
      }
    } catch (err) {
      console.error('Error creating user:', err);
      handleApiError(err, 'Failed to create user');
    } finally {
      setLoading(false);
    }
  };

  const handleApiError = (err, defaultMessage) => {
    if (err.response) {
      if (err.response.status === 401 || err.response.status === 403) {
        handleLogout();
      } else {
        showNotification(err.response.data.message || defaultMessage, 'error');
      }
    } else {
      showNotification(defaultMessage, 'error');
    }
  };

  const showNotification = (message, severity) => {
    setNotification({
      open: true,
      message,
      severity
    });
  };

  const handleCloseNotification = () => {
    setNotification({
      ...notification,
      open: false
    });
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('userData');
    localStorage.removeItem('userEmail');
  };

  const formatDate = (dateString) => {
    if (!dateString) return 'N/A';
    const date = new Date(dateString);
    return date.toLocaleString();
  };

  return (
    <>
      <NavBar />
      <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
        {error && (
          <Alert severity="error" sx={{ mb: 3 }}>
            {error}
          </Alert>
        )}
        
        <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 3 }}>
          <Typography variant="h4" component="h1">
            User Management
          </Typography>
          <Box>
            <Button 
              variant="contained" 
              color="primary" 
              onClick={() => setCreateUserFormOpen(true)}
              startIcon={<AddIcon />}
            >
              Add User
            </Button>
            <IconButton 
              color="primary" 
              onClick={fetchAllUsers} 
              sx={{ ml: 1 }}
              title="Refresh users"
            >
              <RefreshIcon />
            </IconButton>
          </Box>
        </Box>
        
        <Paper sx={{ p: 2, mb: 3, borderRadius: 2 }}>
          <Grid container spacing={2} alignItems="center">
            <Grid item xs={12} md={6}>
              <TextField
                fullWidth
                label="Search User by ID"
                variant="outlined"
                size="small"
                value={searchId}
                onChange={(e) => setSearchId(e.target.value)}
                InputProps={{
                  endAdornment: (
                    <InputAdornment position="end">
                      {searchId && (
                        <IconButton
                          onClick={() => setSearchId('')}
                          edge="end"
                          size="small"
                        >
                          <ClearIcon />
                        </IconButton>
                      )}
                    </InputAdornment>
                  ),
                }}
              />
            </Grid>
            <Grid item xs={12} md={6}>
              <Button
                variant="contained"
                color="primary"
                onClick={fetchUserById}
                startIcon={<SearchIcon />}
                disabled={!searchId.trim()}
              >
                Search
              </Button>
              {searchId.trim() && users.length === 1 && (
                <Button
                  variant="outlined"
                  color="primary"
                  onClick={fetchAllUsers}
                  sx={{ ml: 2 }}
                >
                  Show All Users
                </Button>
              )}
            </Grid>
          </Grid>
        </Paper>
        
        {loading ? (
          <Box sx={{ display: 'flex', justifyContent: 'center', my: 4 }}>
            <CircularProgress />
          </Box>
        ) : (
          <TableContainer component={Paper} sx={{ borderRadius: 2, mb: 4 }}>
            <Table>
              <TableHead>
                <TableRow sx={{ backgroundColor: '#f5f5f5' }}>
                  <TableCell>ID</TableCell>
                  <TableCell>Email</TableCell>
                  <TableCell>Created Date</TableCell>
                  <TableCell>Last Login</TableCell>
                  <TableCell align="center">Actions</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {users.length > 0 ? (
                  users.map((user) => (
                    <TableRow key={user.ID} hover>
                      <TableCell>{user.ID}</TableCell>
                      <TableCell>{user.Email}</TableCell>
                      <TableCell>{formatDate(user.CreatedAt)}</TableCell>
                      <TableCell>{formatDate(user.LastLoginDate)}</TableCell>
                      <TableCell align="center">
                        <IconButton 
                          color="primary" 
                          onClick={() => handleUpdateUser(user)}
                          title="Edit user"
                        >
                          <EditIcon />
                        </IconButton>
                        {userData && user.ID === userData.ID ? (
                          <IconButton 
                            color="error" 
                            disabled={true}
                            title="You cannot delete your own account"
                          >
                            <DeleteIcon />
                          </IconButton>
                        ) : (
                          <IconButton 
                            color="error" 
                            onClick={() => handleDeleteUser(user)}
                            title="Delete user"
                          >
                            <DeleteIcon />
                          </IconButton>
                        )}
                      </TableCell>
                    </TableRow>
                  ))
                ) : (
                  <TableRow>
                    <TableCell colSpan={5} align="center">
                      No users found
                    </TableCell>
                  </TableRow>
                )}
              </TableBody>
            </Table>
          </TableContainer>
        )}
      </Container>
      
      <Dialog open={updateFormOpen} onClose={() => setUpdateFormOpen(false)} maxWidth="sm" fullWidth>
        <DialogTitle>Update User</DialogTitle>
        <DialogContent>
          <Box sx={{ pt: 2 }}>
            <TextField
              fullWidth
              margin="normal"
              label="Email"
              name="Email"
              value={updateFormData.Email}
              onChange={handleUpdateFormChange}
            />
          </Box>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setUpdateFormOpen(false)}>Cancel</Button>
          <Button 
            onClick={submitUpdateUser} 
            variant="contained" 
            color="primary"
            disabled={loading}
          >
            {loading ? <CircularProgress size={24} /> : 'Update'}
          </Button>
        </DialogActions>
      </Dialog>
      
      <Dialog open={createUserFormOpen} onClose={() => setCreateUserFormOpen(false)} maxWidth="sm" fullWidth>
        <DialogTitle>Create New User</DialogTitle>
        <DialogContent>
          <Box sx={{ pt: 2 }}>
            <TextField
              fullWidth
              margin="normal"
              label="Email"
              name="Email"
              value={createUserFormData.Email}
              onChange={handleCreateUserFormChange}
            />
            <TextField
              fullWidth
              margin="normal"
              label="Password"
              name="Password"
              type="password"
              value={createUserFormData.Password}
              onChange={handleCreateUserFormChange}
            />
          </Box>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setCreateUserFormOpen(false)}>Cancel</Button>
          <Button 
            onClick={submitCreateUser} 
            variant="contained" 
            color="primary"
            disabled={loading || !createUserFormData.Email || !createUserFormData.Password}
          >
            {loading ? <CircularProgress size={24} /> : 'Create'}
          </Button>
        </DialogActions>
      </Dialog>
      
      <Dialog open={deleteConfirmOpen} onClose={() => setDeleteConfirmOpen(false)}>
        <DialogTitle>Confirm Delete</DialogTitle>
        <DialogContent>
          <Typography>
            Are you sure you want to delete the user with email: {selectedUser?.Email}?
          </Typography>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setDeleteConfirmOpen(false)}>Cancel</Button>
          <Button 
            onClick={confirmDeleteUser} 
            variant="contained" 
            color="error"
          >
            Delete
          </Button>
        </DialogActions>
      </Dialog>
      
      <Snackbar 
        open={notification.open} 
        autoHideDuration={6000} 
        onClose={handleCloseNotification}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'right' }}
      >
        <Alert 
          onClose={handleCloseNotification} 
          severity={notification.severity} 
          sx={{ width: '100%' }}
        >
          {notification.message}
        </Alert>
      </Snackbar>
    </>
  );
}

export default Dashboard;
