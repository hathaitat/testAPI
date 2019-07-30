google.charts.load('current', {'packages':['table']});
google.charts.setOnLoadCallback(drawChart);


function drawChart(){

//console.log(section);
var Netsale_TY = 0;
var Netsale_LY = 0;



var url_ = "http://10.17.2.210:1500/return_data";
// // var url_ = "http://127.0.0.1:5000/return_data";
$.get(url_,function(data){
var data_ = JSON.parse(data);

Netsale_TY = data_['Netsale_TY'];
Netsale_LY = data_['Netsale_LY'];

drawTable(Netsale_TY,Netsale_LY);
}); 
}

function drawTable(Netsale_TY,Netsale_LY) {
var x = parseInt(Netsale_TY);
var y = parseInt(Netsale_LY);


var data = new google.visualization.DataTable();
data.addColumn('number', 'This year');
data.addColumn('number', 'Last year');
data.addRows([
[x, y]   
]);

var table = new google.visualization.Table(document.getElementById('table_div'));

var formatter = new google.visualization.ColorFormat();
formatter.addRange(-20000, 0, 'white', '#33ff33');
formatter.addRange(0, null, 'red', '#33ff33');
formatter.format(data, 0); 
// formatter.format(data, 1); 
var formatter = new google.visualization.ArrowFormat();
formatter.format(data, 0);
formatter.format(data, 1);
table.draw(data, {allowHtml: true,width: '100%', height: '100%' });
}
