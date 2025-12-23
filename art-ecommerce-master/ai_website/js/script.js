// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Observe sections for scroll animation
const sections = document.querySelectorAll('section');

const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('show');
        } else {
             entry.target.classList.remove('show'); //Optional: remove class when not in view
        }
    });
}, {
    threshold: 0.2 // Adjust threshold as needed
});

sections.forEach(section => {
    section.classList.add('hidden'); // Initially hide the sections
    observer.observe(section);
});
