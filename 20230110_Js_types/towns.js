document.getElementById("button").onclick = function () {
    var towns = ['Москва', 'Амстердам', 'Пермь'];
    
    let input = document.querySelector('input');
    var input_us = document.getElementById("user_text").value;
    if (input_us == towns[0]) {
        message = 'Правильный город!';
    }
    console.log(input.value);
    //alert(input_us);
    document.getElementById('block').innerHTML = message;
}
