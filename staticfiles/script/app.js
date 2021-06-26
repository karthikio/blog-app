let loaderContainer = document.getElementById('loader-container');
let loader = document.getElementById('loader');
let blocks = document.querySelector('#blocks');
let menu = document.getElementById('id_menu_container');
let menu2 = document.getElementById('id_menu_container_2');
let navSmall = document.getElementById('nav-small');
let line1 = document.querySelector('.menu-line1');
let line2 = document.querySelector('.menu-line2');
let line3 = document.querySelector('.menu-line3');


window.addEventListener('load', () => {
  // loader
  setTimeout(() => {
    loaderContainer.style.display = 'none';
    blocks.classList.remove('hidden');
  }, 2000)
})

// hamburger menu toggle 
menu.addEventListener('click', () =>{
  navSmall.style.width = '60%';
  line1.style.marginLeft = '8px';
  line1.style.marginRight = '15px';
  line1.style.width = '16px';
  line2.style.width = '28px';
  line3.style.width = '12px';
})

menu2.addEventListener('click', () => {
  navSmall.style.width = '0';
  line2.style.width = '0';
  line1.style.width = '0';
  line3.style.width = '0';
})