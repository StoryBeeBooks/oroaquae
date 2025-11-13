// Footer Loader Script - Dynamically insert footer HTML
document.addEventListener('DOMContentLoaded', function() {
    const footerHTML = `
    <footer class="footer">
        <div class="footer-container">
            <p class="footer-copyright">ARTWORKS © THE ARTIST. COPYRIGHT © 2025 ORO & AQUAE</p>
            
            <div class="footer-links">
                <a href="about.html">About</a>
                <a href="faq.html">FAQ</a>
                <a href="cookie-policy.html">Cookie Policy</a>
                <a href="terms-of-use.html">Terms of Use</a>
                <a href="privacy-policy.html">Privacy Policy</a>
                <a href="web-accessibility.html">Accessibility</a>
            </div>
            
            <p class="footer-contact"><a href="mailto:info@oroaquae.com">info@oroaquae.com</a></p>
        </div>
    </footer>
    `;
    
    const footerContainer = document.getElementById('footer-container');
    if (footerContainer) {
        footerContainer.innerHTML = footerHTML;
    }
});

