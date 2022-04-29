const card = document.querySelector('.card');
const cardtoggle = document.querySelector('.toggle');
cardtoggle.onclick = function(){
  card.classList.toggle('active')
}


let mybutton = document.getElementById("send-bid-button");

setTimeout(()=>{
  mybutton.style.display = "flex";
},3000)
