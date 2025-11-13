// Footer Loader Script
document.addEventListener('DOMContentLoaded', function() {
    // Load footer from footer.html
    fetch('footer.html')
        .then(response => response.text())
        .then(html => {
            // Create a container for the footer if it doesn't exist
            let footerContainer = document.getElementById('footer-container');
            if (!footerContainer) {
                footerContainer = document.createElement('div');
                footerContainer.id = 'footer-container';
                document.body.appendChild(footerContainer);
            }
            footerContainer.innerHTML = html;
        })
        .catch(error => console.error('Error loading footer:', error));
});
