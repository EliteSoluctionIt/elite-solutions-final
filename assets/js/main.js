/* ==============================
   ELITE SOLUTIONS — MAIN.JS v3
   ============================== */

// Smooth Scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener("click", function (e) {
    const target = document.querySelector(this.getAttribute("href"));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: "smooth" });
    }
  });
});

// Header shadow on scroll
window.addEventListener("scroll", () => {
  const header = document.querySelector(".site-header");
  if (header) {
    if (window.scrollY > 20) header.classList.add("scrolled");
    else header.classList.remove("scrolled");
  }
});

// Fade-in on scroll
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add("visible");
      observer.unobserve(entry.target);
    }
  });
});
document.querySelectorAll(".fade-in, .card, .project-card").forEach(el => observer.observe(el));

// Footer year auto-update
const yearEl = document.getElementById("year");
if (yearEl) yearEl.textContent = new Date().getFullYear();
