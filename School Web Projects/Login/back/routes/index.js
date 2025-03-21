import express from 'express';
import authRoutes from './authRoutes.js';
import userRoutes from './userRoutes.js';
import { authenticateToken } from '../middleware/authMiddleware.js';
import { getUserProfile } from '../controllers/userController.js';
import { login, register } from '../controllers/authController.js';

const router = express.Router();

router.get('/user-profile', authenticateToken, getUserProfile);
router.post('/login', login);
router.post('/register', register);

router.use('/auth', authRoutes);
router.use('/users', userRoutes);

export default router; 