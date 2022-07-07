// hamburger-icon
const iconMenu = document.querySelector(".header__hamburger-icon");
const menuBody = document.querySelector(".header__hamburger-nav-menu");
if (iconMenu) {
  iconMenu.addEventListener("click", function (e) {
    // document.body.classList.toggle('body_lock')
    iconMenu.classList.toggle("header__hamburger-icon_active");
    menuBody.classList.toggle("header__hamburger-nav-menu_active");
  });
}

// Scroll on click
const links = document.querySelectorAll(".header__navbar-list-link");
//FIXME: добавить скролл до верха вместе с синей шапкой 
links.forEach((link) => {
  link.addEventListener("click", () => {
    const item = document.getElementById(link.getAttribute("data-link"));
    item.scrollIntoView({
      behavior: "smooth",
      block: "center",
    });
  });
});

// Open and close card functionality
const card = document.querySelector(".equipment__list-item");
const cardtoggle = document.querySelector(".equipment__list-item-button");
cardtoggle.onclick = function () {
  card.classList.toggle("equipment__list-item_open");
  cardtoggle.classList.toggle("equipment__list-item-button_toggle");
};

// Delay in the appearance of the send bid button
let mybutton = document.getElementById("send-bid-button");
setTimeout(() => {
  mybutton.style.display = "flex";
}, 3000);
