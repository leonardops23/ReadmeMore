import axios from "axios";

const API_URL = 'http://127.0.0.1:8000/'

export const register = async (userData: {
  email: string;
  first_name: string;
  last_name: string;
  password: string;
  password_confirmation: string;
}) => {
  try {
    const res = await axios.post(`${API_URL}api/users/register/`, userData);
    return res.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      console.error('Registration error:', {
        status: error.response?.status,
        data: error.response?.data,
        headers: error.response?.headers
      });
    } else {
      console.error('Unexpected error:', error);
    }
    throw error;
  }
}

export const login = async (userData: {
  email: string;
  password: string;
}) => {
  try {
    const res = await axios.post(`${API_URL}api/users/login/`, userData);
    return res.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      console.error('Login error:', {
        status: error.response?.status,
        data: error.response?.data,
        headers: error.response?.headers
      });
    } else {
      console.error('Unexpected error:', error);
    }
    throw error;
  }
}
