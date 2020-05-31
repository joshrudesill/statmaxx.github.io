// Load google charts
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
  var data = google.visualization.arrayToDataTable([
  ['Sybmbol', 'Distribution Share'],
  ['FB', 5123],
  ['AMZN', 6012],
  ['TSLA', 4012],
  ['SHIP', 1024],
  ['Other', 14012]
]);

  // Optional; add a title and set the width and height of the chart
  var options = {
                chartArea: {height: '85%', width: '95%',},
                backgroundColor: 'transparent',
                legend: {alignment: 'center'},
                };

  // Display the chart inside the <div> element with id="piechart"
  var chart = new google.visualization.PieChart(document.getElementById('piechart'));
  chart.draw(data, options);
}
