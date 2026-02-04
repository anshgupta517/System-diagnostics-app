import axios from 'axios';

const api = axios.create({
    baseURL: 'http://localhost:8000', // Hardcoded for Phase 1
    headers: {
        'Content-Type': 'application/json',
    },
});

export const sendMessage = async (message) => {
    try {
        const response = await api.post('/chat', { message });
        return response.data;
    } catch (error) {
        console.error("API Error:", error);
        throw error;
    }
};

export const checkBackendStatus = async () => {
    try {
        const response = await api.get('/');
        return response.data;
    } catch (error) {
        return { status: "Offline" };
    }
};
