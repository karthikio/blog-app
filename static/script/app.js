let loaderContainer = document.getElementById('loader-container');
let loader = document.getElementById('loader');
let blocks = document.querySelector('#blocks');
let cross = document.getElementsByClassName('cross')
let messageContainer = document.querySelector('.message-container')


window.addEventListener('load', () => {
  // loader
  setTimeout(() => {
    loaderContainer.style.display = 'none';
    loader.style.display = 'none';
    blocks.classList.remove('hidden');
  }, 2000)

  
})

console.log(messageContainer)

cross.addEventListener('click', () => {
  messageContainer.display = 'none';
})