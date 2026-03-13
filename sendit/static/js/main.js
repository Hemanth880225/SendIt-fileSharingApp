// Toggle navigation for small screens
document.getElementById("hamburger").addEventListener("click", () => {
  const links = document.getElementById("nav-links");
  links.style.display = links.style.display === "flex" ? "none" : "flex";
});
