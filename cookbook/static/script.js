let screenWidth = window.innerWidth;
let navToggleShow = document.getElementById('nav-toggle-show');
let navToggleClose = document.getElementById('nav-toggle-close');

if (screenWidth < 500){
    document.getElementById('nav-bar').style.display = 'none';
    
    /** Hides close button on page load */
    navToggleClose.style.display = 'none';
    
    navToggleShow.addEventListener('click', function(){
        navToggleClose.style.display = 'inline';
        document.getElementById('nav-bar').style.display = 'inline';
        navToggleShow.style.display = 'none';
    });
    navToggleClose.addEventListener('click', function(){
        navToggleClose.style.display = 'none';
        document.getElementById('nav-bar').style.display = 'none';
        navToggleShow.style.display = 'inline';
    })
}
/** Hides toggle buttons if screensize is over 500px */
if (screenWidth >= 500) {
    navToggleClose.style.display = 'none';
    navToggleShow.style.display = 'none';
}