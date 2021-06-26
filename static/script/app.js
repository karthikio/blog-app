let loaderContainer = document.getElementById('loader-container');
let loader = document.getElementById('loader');
let blocks = document.querySelector('#blocks');
let menu = document.getElementById('id_menu_container');
let menu2 = document.getElementById('id_menu_container_2');
let navSmall = document.getElementById('nav-small');


window.addEventListener('load', () => {
  // loader
  setTimeout(() => {
    loaderContainer.style.display = 'none';
    blocks.classList.remove('hidden');
  }, 2000)
})

menu.addEventListener('click', () =>{
  navSmall.style.width = '60%';
})

menu2.addEventListener('click', () => {
  navSmall.style.width = '0';
})