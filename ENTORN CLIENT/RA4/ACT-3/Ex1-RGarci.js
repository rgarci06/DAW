const boto = document.getElementById("btnCarregar");
const paragraf = document.getElementById("paragraf");

boto.addEventListener("click", function () {
  const xhr = new XMLHttpRequest();
  xhr.open("GET", "missatge.txt", true);

  xhr.onreadystatechange = function () {
    // readyState 4 vol dir que la petició ha acabat, status 200 vol dir "OK"
    if (xhr.readyState === 4 && xhr.status === 200) {
      paragraf.textContent = xhr.responseText;
    }
  };

  xhr.send();
});