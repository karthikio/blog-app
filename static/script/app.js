let loaderContainer = document.getElementById('loader-container');
let loader = document.getElementById('loader');
let blocks = document.querySelector('#blocks');


window.addEventListener('load', () => {
  // loader
  setTimeout(() => {
    loaderContainer.style.display = 'none';
    loader.style.display = 'none';
    blocks.classList.remove('hidden');
  }, 2000)

  
})


fetch('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=API_KEY')
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => console.log(err))