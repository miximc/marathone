// let, var или const?
// https://habr.com/ru/company/ruvds/blog/420359/

var towns = ['Москва', 'Архангельск', 'Кострома', 'Амстердам'];

function get_next_city(my_city) {
	// то, что в описании функции - формальные параметры.
	// они видны только этой функции
	
	// Фактические параметры - то, что передаётся извне, при вызове.
	// Они могут быть различными, не обязаны совпадать по имени
	// с формальными, даже желательно - другими.
	// также в функцию могут передаваться значения,
	// выражения и вызовы других функций
	
	// Если аргументов, которые фактически переданы функции,
	// недостаточно
	            // условие ПРОДОЛЖЕНИЯ ЦИКЛА
	for (var i = 0; i < towns.length; i++) {
		// проверить: [-1]
		//console.log();
		if (towns[i][0].toLowerCase() === my_city[my_city.length - 1]) {
			let result = towns[i];
			towns = towns.filter(
			                item => item !== result);
			// Фильтр принимает в качестве параметра
			// функцию, которая принимает элемент
			// (он передастся туда автоматически в процессе работы фильтра)
            // для каждого элмента решаем: оставить или убрать
            // true - оставить			
			
			console.log(towns);
			return result;
		}
	}
	return "Ты выиграл!"
}

// Стрелочная функция - без имени
// без ключевого слова function
const save = () => {
	var town = document.getElementById('town').value;
	document.getElementById('play').innerHTML = town;
	towns = towns.filter(
                item => item !== town);
	console.log(towns);
	document.getElementById('play').innerHTML += ", " +  get_next_city(town);
	
}

const del_all_towns = (arr) => {
	for (var i = 0; i < arr.length; i++) {
		arr[i] = '';
	}
	arr.push('ХАХАХА');
	arr = arr.filter(item => false);
	// объект заменился!
	console.log("После фильтра: ", arr);
	//for (var i = 0; i < arr.length; i++) {
	//	arr[i] = '';
	//}
}

function two_params(p1, p2) {
	console.log("p1 :", p1);
	console.log("p2 :", p2);
	if (typeof p2 === "undefined") {
		console.log("Второй не определен");
	}
}

function main() {
    console.log(towns[0]);
	del_all_towns(towns);
	console.log("А список есть?", towns);
	two_params(1, 2, 3);
	two_params(1);	
}

// Когда мы цепляем функцию к событию
// "подписываемся на событие" (термин из JAVA)
// в коде javascript, мы НЕ ВЫЗЫВАЕМ ФУНКИЮ!
// она вызовется сама в момент наступления события
window.onload = main;

// Когда мы пишем реакцию на событие в HTML
// мы ВЫЗЫВАЕМ функцию.
/*

<button onclick='save()'>
Сохранить</button>

*/