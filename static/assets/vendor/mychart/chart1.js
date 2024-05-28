
    document.addEventListener('DOMContentLoaded', function () {
        var chartDataElement = document.getElementById('chart-data');
        var chartData = JSON.parse(chartDataElement.textContent);
    
        Morris.Area({
            element: 'areaChart',
            data: chartData,
            xkey: 'y',
            ykeys: ['a', 'b', 'c'],
            labels: ['Pouches', 'Machines', 'Operators'],
            behaveLikeLine: true,
            pointSize: 0,
            fillOpacity: 0.4,
            lineWidth: 0,
            hideHover: 'auto',
            resize: true,
            redraw: true,
            lineColors: ['#3659cd', '#a5acc3', '#dfe2ed', '#eef0f8'],
            gridLineColor: '#ccd2da',
            gridtextSize: 10
        });
    });
                                
                       