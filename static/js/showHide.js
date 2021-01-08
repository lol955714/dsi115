function myFunction() {
    var x = document.getElementById("div");
var button = document.getElementById("button");
    if (x.style.display === "none") {
      x.style.display = "block";
    button.innerText = 'ocultar';
    } else {
      x.style.display = "none";
      button.innerText = 'Mostrar';
    }
  }