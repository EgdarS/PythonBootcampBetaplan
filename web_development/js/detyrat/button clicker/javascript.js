function alertCustom(element){
    alert('Ninja was liked')
}

function changeText(navButton){
    navButton.innerText = 'Logout'
}

var button = document.getElementById('myButton')
button.addEventListener('click',function(){
    button.remove()
});