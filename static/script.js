// JavaScript for expandable sidebar
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.querySelector('.main-content');
    const toggleBtn = document.querySelector('.toggle-btn');
    sidebar.classList.toggle('collapsed');
    toggleBtn.classList.toggle('rotated');
    if (window.innerWidth > 768) {
        if (sidebar.classList.contains('collapsed')) {
            mainContent.style.marginLeft = '0';
        } else {
            mainContent.style.marginLeft = '250px';
        }
    } else {
        sidebar.style.height = 'auto';
    }
}

// Slideshow for background images
let currentSlide = 0;
const slides = [
    'static/pictures_slide_show/image1.jpeg',
    'static/pictures_slide_show/image2.jpeg',
    'static/pictures_slide_show/image3.png'
];

// Initialize background
document.body.style.backgroundImage = `url('${slides[currentSlide]}')`;
document.body.style.backgroundPosition = window.innerWidth <= 768 ? 'center top' : 'center';
document.body.style.backgroundSize = 'cover';
document.body.style.backgroundRepeat = 'no-repeat';

function changeSlide(direction) {
    currentSlide = (currentSlide + direction + slides.length) % slides.length;
    document.body.style.backgroundImage = `url('${slides[currentSlide]}')`;
    document.body.style.backgroundPosition = window.innerWidth <= 768 ? 'center top' : 'center';
    document.body.style.backgroundSize = 'cover';
    document.body.style.backgroundRepeat = 'no-repeat';
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
if (window.innerWidth <= 768) {
    document.getElementById('sidebar').classList.add('collapsed');
}