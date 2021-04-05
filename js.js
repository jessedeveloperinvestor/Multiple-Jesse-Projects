//Hi there
/*
this is a comment
*/
console.log('Are you ok?')
var y='hi'
var n=0
var ax=y
var $x=n+5
var _x='ok'
if(y=='hello'){
	console.log('great');
}
else if(y=='hi'){
	console.log($x);
}
else{
	console.log(_x);
}
//conditional switch:
var day='sun';
switch(day) {
    case 'mon':
break;
    case 'tue':
break;
    case 'wed':
break;
    case 'thu':
break;
    case 'fri':
break;
    case 'sat':
break;
default: 'sun';
break;
}
console.log(day)

//

function exibir(){
 var mes = parseInt(document.getElementById("numero").value);
 
 switch(mes){
  case 1:  alert("Janeiro");
  case 2:  alert("Fevereiro");
  case 3:  alert("Março");
  case 4:  alert("Abril");
  case 5:  alert("Maio");
  case 6:  alert("Junho");
  case 7:  alert("Julho");
  case 8:  alert("Agosto");
  case 9:  alert("Setembro");
  case 10: alert("Outubro");
  case 11: alert("Novembro");
  case 12: alert("Dezembro");
 }
}
