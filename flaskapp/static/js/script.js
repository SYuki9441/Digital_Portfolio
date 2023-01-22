const burger = document.querySelector('.burger');
const nav = document.querySelector('.nav-links');
const navLinks = document.querySelectorAll('.nav-links li');


burger.addEventListener("click", () => {
    nav.classList.toggle("nav-active");
    navLinks.forEach((link, index) => { 
        if (link.style.animation) {
            link.style.animation = "";
        } else {
            link.style.animation = `navLinksFade 0.5s ease forwards ${index / 7 + 0.5}s`;
        }
     });
     burger.classList.toggle("toggle");
});





/* This code was adapted from a post by Programmingtutorial. 5-1-2022 */
/* https://www.youtube.com/watch?v=feu9m1E4T9E */
/* Accessed: 15-1-2023 */