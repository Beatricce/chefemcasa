var x = document.getElementById("cliente");
var y = document.getElementById("chef");
var b1 = document.getElementById("bt1");
var b2 = document.getElementById("bt2");
var bt_login = document.getElementById("bt_login");

x.style.display = "none";
y.style.display = "none";
b1.style.display = "none";
b2.style.display = "none";

function show_buttons() {

	b1.style.display = "block";
	b2.style.display = "block";
	bt_login.style.display = "none"
}

function add_input() {

	//Create and append select list
	var lista = document.createElement("select");

	//Create array of options to be added
	var array = ["--Selecione culinária--","Árabe","Italina","Espanhola","Mexicana","Africana","Chinesa","Argentina","Coreana","Tailandesa","Japonesa","Mediterrânea","Francesa","Baiana","Mineira","Paulista","Catarinense","Nordestina","Colombiana","Indiana","Marroquina","Frutos do mar","Peruana","Portuguesa","Chilena","Nordestina","Vegetariana"];

	//Create and append the options
	for (var i = 0; i < array.length; i++) {
	    var option = document.createElement("option");
	    option.value = array[i];
	    option.text = array[i];
	    lista.appendChild(option);
	}

  	document.getElementById("add_input").appendChild(lista);
}

function cliente() {
	if (x.style.display === "none") {
	x.style.display = "block";
	}
	y.style.display = "none";
}

function chef() {
	if (y.style.display === "none") {
	y.style.display = "block";
	}
	x.style.display = "none";
}

