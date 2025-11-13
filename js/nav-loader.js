// Navigation loader - dynamically inject navigation into all pages
document.addEventListener('DOMContentLoaded', function() {
    const navContainer = document.getElementById('nav-container');
    
    if (navContainer) {
        const navHTML = `
            <nav class="main-nav">
                <div class="nav-container">
                    <a href="index.html" class="nav-logo">ORO & AQUAE</a>
                </div>
            </nav>
        `;
        
        navContainer.innerHTML = navHTML;
    }
});
