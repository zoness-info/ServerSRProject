
document.addEventListener('DOMContentLoaded', function () {
    var chartDataElement = document.getElementById('chart-data');
    var chartData = JSON.parse(chartDataElement.textContent);

    Morris.Area({
        element: 'areaChart',
        data: chartData,
        xkey: 'y',
        ykeys: ['a', 'b', 'c'],
        behaveLikeLine: true,
        pointSize: 0,
        labels: ['Pouches', 'Machines', 'Operators'],
        colors: ['#3659cd', '#a5acc3', '#dfe2ed', '#eef0f8'],
        gridLineColor: '#ccd2da',
        lineColors: ['#3659cd', '#a5acc3', '#dfe2ed', '#eef0f8'],
        gridtextSize: 10,
        fillOpacity: 0.4,
        lineWidth: 0,
        hideHover: 'auto',
        resize: true,
        redraw: true
    });
});
