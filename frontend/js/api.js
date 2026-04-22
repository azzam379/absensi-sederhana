// Pendeteksian Otomatis: Jika dibuka double-click (Local), tembak port 8000. 
// Jika di Vercel (Cloud), tembak relatif /api/
const IS_LOCAL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1' || window.location.protocol === 'file:';
const BASE_URL = IS_LOCAL ? 'http://127.0.0.1:8000/api' : '/api';

const api = {
    async get(endpoint) {
        const res = await fetch(`${BASE_URL}${endpoint}`);
        return res.json();
    },
    async post(endpoint, data) {
        const res = await fetch(`${BASE_URL}${endpoint}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        return res.json();
    },
    async delete(endpoint) {
        const res = await fetch(`${BASE_URL}${endpoint}`, { method: 'DELETE' });
        return res.json();
    }
};
