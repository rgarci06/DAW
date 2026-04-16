const boto = document.getElementById("btnEstats");
const divEstats = document.getElementById("estats");

boto.addEventListener("click", function () {
  const xhr = new XMLHttpRequest();
  divEstats.innerHTML = ""; // Netegem abans de començar

  // Aquesta funció s'executa cada cop que canvia el readyState
  xhr.onreadystatechange = function () {
    divEstats.innerHTML += `<p>Estat readyState: <strong>${xhr.readyState}</strong></p>`;
  };
  
  xhr.open("GET", "missatge.txt", true);
  xhr.send();
});