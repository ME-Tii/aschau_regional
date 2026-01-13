// JavaScript for expandable sidebar
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.querySelector('.main-content') || document.querySelector('.vereine-main');
    const toggleBtn = document.querySelector('.toggle-btn');
    if (sidebar) {
        sidebar.classList.toggle('collapsed');
        if (toggleBtn) toggleBtn.classList.toggle('rotated');
        if (window.innerWidth > 768) {
            if (sidebar.classList.contains('collapsed')) {
                if (mainContent) mainContent.style.marginLeft = '0';
            } else {
                if (mainContent) mainContent.style.marginLeft = '250px';
            }
        } else {
            sidebar.style.height = 'auto';
        }
    }
}

// Slideshow for background images
const heroElement = document.querySelector('.hero');
if (heroElement) {
    let currentSlide = 0;
    const slides = [
        '/static/pictures_slide_show/image1.jpeg',
        '/static/pictures_slide_show/image2.jpeg',
        '/static/pictures_slide_show/image3.png'
    ];

    // Initialize background
    heroElement.style.backgroundImage = `url('${slides[currentSlide]}')`;
    heroElement.style.backgroundPosition = 'center';
    heroElement.style.backgroundSize = 'cover';
    heroElement.style.backgroundRepeat = 'no-repeat';

    function changeSlide(direction) {
        currentSlide = (currentSlide + direction + slides.length) % slides.length;
        heroElement.style.backgroundImage = `url('${slides[currentSlide]}')`;
        heroElement.style.backgroundPosition = 'center';
        heroElement.style.backgroundSize = 'cover';
        heroElement.style.backgroundRepeat = 'no-repeat';
    }

    // Add event listeners for slide buttons
    const prevBtn = document.querySelector('.slide-btn.prev');
    const nextBtn = document.querySelector('.slide-btn.next');
    if (prevBtn) prevBtn.addEventListener('click', () => changeSlide(-1));
    if (nextBtn) nextBtn.addEventListener('click', () => changeSlide(1));
}

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Collapse sidebar on mobile by default
const sidebarEl = document.getElementById('sidebar');
if (sidebarEl && window.innerWidth <= 768) {
    sidebarEl.classList.add('collapsed');
}

// Hide slide buttons always
const buttons = document.querySelectorAll('.slide-btn');
buttons.forEach(btn => btn.style.display = 'none');