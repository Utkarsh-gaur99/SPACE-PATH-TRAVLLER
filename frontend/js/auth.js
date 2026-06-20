const TOKEN_KEY = 'astropath_token';

function isAuthenticated() {
    return localStorage.getItem(TOKEN_KEY) !== null;
}

function requireAuth() {
    if(!isAuthenticated()) {
        window.location.href = '/login.html';
    }
}

function getToken() {
    return localStorage.getItem(TOKEN_KEY);
}

function setToken(token) {
    localStorage.setItem(TOKEN_KEY, token);
}

function logoutUser() {
    localStorage.removeItem(TOKEN_KEY);
    window.location.href = '/login.html';
}
