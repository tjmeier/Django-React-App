//interceptor of requests to add the correct headers - using axios interceptor 
import axios from 'axios';
import { ACCESS_TOKEN } from './constants';

const apiUrl = '/choreo-apis/django-react-application/backend/v1'; //links to backend service url in Choreo 

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL ? import.meta.env.VITE_API_URL : apiUrl,
});

api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem(ACCESS_TOKEN);
        if (token) {
            //passing JWT access token through an authorization header
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) =>{
        return Promise.reject(error);
    }
);

export default api;