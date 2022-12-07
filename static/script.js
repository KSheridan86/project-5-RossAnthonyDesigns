// Code to hide the back to top button until the user scrolls down
let topBtn = document.querySelector('.top-btn');

function backToTop() {
    if (document.body.scrollTop > 600 || document.documentElement.scrollTop > 600) {
        topBtn.style.display = "block";
    } else {
        topBtn.style.display = "none";
    }
}

// This detects when the featured items(images) scroll into view and initiates the animation
function reveal() {
    var reveals = document.querySelectorAll(".fade-in");
    for (var i = 0; i < reveals.length; i++) {
        var windowHeight = window.innerHeight;
        var elementTop = reveals[i].getBoundingClientRect().top;
        var elementVisible = 150;

        if (elementTop < windowHeight - elementVisible) {
            reveals[i].classList.add("active");
        } else {
            reveals[i].classList.remove("active");
        }
    }
}

// To check the scroll position on page load
reveal();








window.addEventListener("scroll", reveal);
window.addEventListener("scroll", backToTop);