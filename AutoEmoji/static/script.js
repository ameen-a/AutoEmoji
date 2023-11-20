document.addEventListener("DOMContentLoaded", function() {
    // get logo element
    const logo = document.querySelector(".logo");
  
    // init mouse position
    let mouseX = 0;
    
    // listen for mouse movement
    document.addEventListener("mousemove", function(event) {
      // get the mouse x pos
      mouseX = event.clientX;
      
      // rotate logo based on mouse pos
      const angle = (mouseX / window.innerWidth - 0.5) * 5;
      
      // apply rotation to logo
      logo.style.transform = `rotate(${angle}deg)`;
    });
  });
  