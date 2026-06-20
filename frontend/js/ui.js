// Generate stars for background
function generateStars(count) {
    const container = document.getElementById('stars-container');
    if(!container) return;
    
    for (let i = 0; i < count; i++) {
        let star = document.createElement('div');
        star.className = 'star';
        
        let x = Math.random() * 100;
        let y = Math.random() * 100;
        let duration = Math.random() * 3 + 2;
        let delay = Math.random() * 2;
        
        star.style.left = `${x}vw`;
        star.style.top = `${y}vh`;
        star.style.animationDuration = `${duration}s`;
        star.style.animationDelay = `${delay}s`;
        
        container.appendChild(star);
    }
}

// Update Navigation based on Auth state
function updateNavForAuth() {
    const token = localStorage.getItem('astropath_token');
    const navLinks = document.getElementById('nav-links');
    if(!navLinks) return;
    
    if(token) {
        navLinks.innerHTML = `
            <li><a href="/dashboard.html">Dashboard</a></li>
            <li><a href="/new_mission.html">New Mission</a></li>
            <li><a href="/missions.html">History</a></li>
            <li><a href="/planets.html">Planets</a></li>
            <li><a href="#" onclick="logoutUser()">Logout</a></li>
        `;
    } else {
        navLinks.innerHTML = `
            <li><a href="/login.html">Login</a></li>
            <li><a href="/register.html">Register</a></li>
        `;
    }
}
