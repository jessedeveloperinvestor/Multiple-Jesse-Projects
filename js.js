//Hi there
/*
this is a comment
*/
console.log('Are you ok?');
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
console.log(day);
console.log('');

//loops

let lang=['python','javascript','css','html']
lang.forEach(item => console.log(item));

for(var n=1;n<=10;n++)
  console.log(n);

var a=[1,2,3,4];
a.forEach(item => console.log('array '+item));

for(var item in a)
  console.log(item);

for(var item of a)
  console.log(item);