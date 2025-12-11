// NAAS Portal - Countdown Timer Script

document.addEventListener('DOMContentLoaded', function() {
    // Get the election date from the countdown badge or set default
    const currentYear = new Date().getFullYear();
    let electionDate = new Date(currentYear, 11, 26, 0, 0, 0); // December 26
    
    // If election date has passed, use next year
    if (electionDate < new Date()) {
        electionDate = new Date(currentYear + 1, 11, 26, 0, 0, 0);
    }
    
    function updateCountdown() {
        const now = new Date();
        const diff = electionDate - now;
        
        if (diff <= 0) {
            // Election day or past
            updateDisplay(0, 0, 0, 0);
            const badge = document.getElementById('countdown-badge');
            if (badge) {
                badge.textContent = 'Election Day!';
                badge.classList.add('bg-gold', 'text-dark');
                badge.classList.remove('bg-dark-green');
            }
            return;
        }
        
        const days = Math.floor(diff / (1000 * 60 * 60 * 24));
        const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((diff % (1000 * 60)) / 1000);
        
        updateDisplay(days, hours, minutes, seconds);
        updateBadge(days);
    }
    
    function updateDisplay(days, hours, minutes, seconds) {
        // Update individual countdown boxes if they exist
        const daysEl = document.getElementById('countdown-days');
        const hoursEl = document.getElementById('countdown-hours');
        const minutesEl = document.getElementById('countdown-minutes');
        const secondsEl = document.getElementById('countdown-seconds');
        
        if (daysEl) daysEl.textContent = String(days).padStart(2, '0');
        if (hoursEl) hoursEl.textContent = String(hours).padStart(2, '0');
        if (minutesEl) minutesEl.textContent = String(minutes).padStart(2, '0');
        if (secondsEl) secondsEl.textContent = String(seconds).padStart(2, '0');
    }
    
    function updateBadge(days) {
        const badge = document.getElementById('countdown-badge');
        if (badge) {
            if (days === 0) {
                badge.textContent = 'Today!';
            } else if (days === 1) {
                badge.textContent = '1 day remaining';
            } else {
                badge.textContent = days + ' days remaining';
            }
        }
    }
    
    // Update immediately and then every second
    updateCountdown();
    setInterval(updateCountdown, 1000);
});

// Utility function to format dates
function formatDate(date) {
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    return date.toLocaleDateString('en-US', options);
}

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Auto-dismiss alerts after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
});
