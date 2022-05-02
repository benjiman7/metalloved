const card = document.querySelector('.equipment__list-item');
const cardtoggle = document.querySelector('.equipment__list-item-button');
cardtoggle.onclick = function(){
  card.classList.toggle('equipment__list-item_open')
  cardtoggle.classList.toggle('equipment__list-item-button_toggle')
}


let mybutton = document.getElementById("send-bid-button");

setTimeout(()=>{
  mybutton.style.display = "flex";
},3000)
