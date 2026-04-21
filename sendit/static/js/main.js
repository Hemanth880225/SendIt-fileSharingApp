// Toggle navigation for small screens
document.getElementById("hamburger").addEventListener("click", () => {
  const links = document.getElementById("nav-links");
  links.style.display = links.style.display === "flex" ? "none" : "flex";
});


// =============================
// Dropdown (file actions menu)
// =============================

// open/close dropdown
document.querySelectorAll(".dropdown-btn").forEach(btn => {
  btn.addEventListener("click", function (e) {
    e.stopPropagation();

    // close all dropdowns first
    document.querySelectorAll(".dropdown").forEach(d => d.classList.remove("show"));

    // open clicked one
    this.parentElement.classList.toggle("show");
  });
});

// close dropdown when clicking outside
window.addEventListener("click", function () {
  document.querySelectorAll(".dropdown").forEach(d => d.classList.remove("show"));
});