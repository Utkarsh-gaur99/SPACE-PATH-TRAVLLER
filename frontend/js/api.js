const API_BASE = window.location.origin;

async function apiCall(endpoint, method = 'GET', data = null) {
    const headers = {
        'Content-Type': 'application/json'
    };
    
    const token = getToken();
    if(token) {
        headers['Authorization'] = `Bearer ${token}`;
    }
    
    const options = {
        method,
        headers
    };
    
    if(data) {
        if(method !== 'GET') {
            options.body = JSON.stringify(data);
        }
    }
    
    try {
        const response = await fetch(`${API_BASE}${endpoint}`, options);
        if(!response.ok) {
            const errData = await response.json().catch(() => ({}));
            throw new Error(errData.detail || 'API Error');
        }
        return await response.json();
    } catch (error) {
        console.error('API Error:', error);
        return null;
    }
}

// Auth endpoints
async function registerUser(username, email, password) {
    try {
        const res = await fetch(`${API_BASE}/auth/register`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({username, email, password})
        });
        const data = await res.json();
        if(res.ok) return {success: true, data};
        return {success: false, message: data.detail};
    } catch(e) {
        return {success: false, message: e.message};
    }
}

async function loginUser(username, password) {
    try {
        const formData = new URLSearchParams();
        formData.append('username', username);
        formData.append('password', password);
        
        const res = await fetch(`${API_BASE}/auth/login`, {
            method: 'POST',
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            body: formData
        });
        
        if(res.ok) {
            const data = await res.json();
            setToken(data.access_token);
            return true;
        }
        return false;
    } catch (e) {
        console.error(e);
        return false;
    }
}

// Dashboard
async function getDashboardStats() {
    return await apiCall('/dashboard/');
}

// Planets
async function getPlanets() {
    return await apiCall('/planets/');
}

// Missions
async function calculateMission(source, destination, speed) {
    return await apiCall('/mission/calculate', 'POST', {source, destination, speed});
}

async function saveMission(missionData) {
    return await apiCall('/mission/save', 'POST', missionData);
}

async function getMissions() {
    return await apiCall('/mission/history');
}

async function deleteMission(id) {
    return await apiCall(`/mission/${id}`, 'DELETE');
}
