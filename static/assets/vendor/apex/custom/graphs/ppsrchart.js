document.addEventListener('DOMContentLoaded', function() {
    // Get the raw JSON data from the pre tag
    // const rawData = document.getElementById('raw-json-data').textContent.trim();
    
    // // Log the raw data to the console
    // // console.log('Raw JSON Data:', rawData);

    
    //     // Parse the JSON data
    //     const chartData = JSON.parse(rawData);
        
    //     // Log the parsed data to the console to verify
    //     // console.log('Parsed Chart Data:', chartData);

    //     const dates = chartData.map(item => item.date);
    //     const expectedValues = chartData.map(item => item.expbox);
    //     const actualValues = chartData.map(item => item.actbox);

        const options1 = {
            series: [67],
            chart: {
            height: 100,
            type: 'radialBar',
            offsetY: -10
          },
          plotOptions: {
            radialBar: {
              startAngle: -135,
              endAngle: 135,
              dataLabels: {
                name: {
                  fontSize: '16px',
                  color: undefined,
                  offsetY: 120,
                  offsetX: 0
                },
                value: {
                  offsetY: -10,
                  offsetX: 0,
                  fontSize: '15px',
                  color: undefined,
                  formatter: function (val) {
                    return val + "%";
                  }
                }
              }
            }
          },
          fill: {
            type: 'gradient',
            gradient: {
                shade: 'dark',
                shadeIntensity: 0.15,
                inverseColors: false,
                opacityFrom: 1,
                opacityTo: 1,
                stops: [0, 50, 65, 91]
            },
          },
          stroke: {
            dashArray: 4
          },
        //   labels: ['1'],
          };
  
        const chart1 = new ApexCharts(document.querySelector("#PVR1Chart"), options1);
          chart1.render();

// PVR-2 Chart
const options2 = {
    series: [35],
    chart: {
    height: 100,
    type: 'radialBar',
    offsetY: -10
  },
  plotOptions: {
    radialBar: {
      startAngle: -135,
      endAngle: 135,
      dataLabels: {
        name: {
          fontSize: '16px',
          color: undefined,
          offsetY: 120,
          offsetX: 0
        },
        value: {
          offsetY: -10,
          offsetX: 0,
          fontSize: '15px',
          color: undefined,
          formatter: function (val) {
            return val + "%";
          }
        }
      }
    }
  },
  fill: {
    type: 'gradient',
    gradient: {
        shade: 'dark',
        shadeIntensity: 0.15,
        inverseColors: false,
        opacityFrom: 1,
        opacityTo: 1,
        stops: [0, 50, 65, 91]
    },
  },
  stroke: {
    dashArray: 4
  },
//   labels: ['1'],
  };

const chart2 = new ApexCharts(document.querySelector("#PVR2Chart"), options2);
  chart2.render();

     
    });


// document.addEventListener('DOMContentLoaded', function() {
//     const monthNames = [
//         "January", "February", "March", "April", "May", "June",
//         "July", "August", "September", "October", "November", "December"
//     ];
//     const now = new Date();
//     const currentMonth = monthNames[now.getMonth()];
//     const currentYear = now.getFullYear();
//     document.getElementById('current-month').textContent = currentMonth;
//     document.getElementById('current-year').textContent = currentYear;
// });



// Chart for Month---------------------------------------------------------------
// Get the raw JSON data from the pre tag
// document.addEventListener('DOMContentLoaded', function() {
// const rawData = document.getElementById('raw-json-month').textContent.trim();
    
// // Log the raw data to the console
// // console.log('Raw JSON Data:', rawData);

// try {
//     // Parse the JSON data
//     const chartData = JSON.parse(rawData);
    
//     // Log the parsed data to the console to verify
//     console.log('Parsed Chart Data:', chartData);

//     const months = chartData.map(item => item.month);
//     console.log('month',months)
//     const expectedValues = chartData.map(item => item.exp_total);
//     console.log('exp val',expectedValues)
//     const actualValues = chartData.map(item => item.act_total);
//     console.log('actvalue',actualValues)
//     // const options = {
//     //     series: [{
//     //         name: 'Expected',
//     //         data: expectedValues
//     //     }, {
//     //         name: 'Actual',
//     //         data: actualValues
//     //     }],
//     //     chart: {
//     //         type: 'area',
//     //         height: 350
//     //     },
//     //     dataLabels: {
//     //         enabled: true,
//     //         formatter: function(val) {
//     //             return val;
//     //         },
//     //         style: {
//     //             colors: ['#F44336', '#E91E63', '#9C27B0', '#673AB7', '#3F51B5']
//     //             // colors: ['rgba(244, 67, 54, 0.7)', 'rgba(233, 30, 99, 0.7)', 'rgba(156, 39, 176, 0.7)', 'rgba(103, 58, 183, 0.7)', 'rgba(63, 81, 181, 0.7)']
//     //         }
//     //     },
//     //     markers: {
//     //         size: 5,
//     //         colors: ['#FFA41B', '#E91E63'],
//     //         // colors: ['rgba(255, 164, 27, 0.7)', 'rgba(233, 30, 99, 0.7)'],
//     //         strokeColor: '#fff',
//     //         strokeWidth: 2,
//     //         // strokeColor: 'transparent', // No stroke around markers
//     //         // strokeWidth: 0, // No stroke width
//     //         hover: {
//     //             size: 7,
//     //         }
//     //     },
//     //     xaxis: {
//     //         categories: months
//     //     }
//     // };
    


//     // var options = {
//     //     series: [
//     //         {
//     //             name: "Expected",
//     //             type: "column",
//     //             data: expectedValues,
//     //         },
//     //         {
//     //             name: "Actual",
//     //             type: "area",
//     //             data: actualValues,
//     //         },
//     //     ],
//     //     chart: {
//     //         height: 300,
//     //         type: "line",
//     //         toolbar: {
//     //             show: true,
//     //         },
//     //     },
//         // dataLabels: {
//         //     enabled: true,
//         //     formatter: function(val) {
//         //         return val;
//         //     },
//         //     style: {
//         //         // colors: ['#F44336', '#E91E63', '#9C27B0', '#673AB7', '#3F51B5']
//         //         colors: ['rgba(244, 67, 54, 0.7)', 'rgba(233, 30, 99, 0.7)', 'rgba(156, 39, 176, 0.7)', 'rgba(103, 58, 183, 0.7)', 'rgba(63, 81, 181, 0.7)']
//         //     }
//         // },
//     //     stroke: {
//     //         width: [0, 3],
//     //         curve: "smooth",
//     //     },
//     //     plotOptions: {
//     //         bar: {
//     //             columnWidth: "70%",
//     //             borderRadius: 8,
//     //             distributed: true,
//     //             dataLabels: {
//     //                 position: "top",
//     //             },
//     //         },
//     //     },
    
//     //     fill: {
//     //         opacity: [0.85, 0.25, 1],
//     //         gradient: {
//     //             inverseColors: false,
//     //             shade: "light",
//     //             type: "vertical",
//     //             opacityFrom: 0.85,
//     //             opacityTo: 0.55,
//     //             stops: [0, 100, 100, 100],
//     //         },
//     //     },    
//     //     markers: {
//     //         size: 0,
//     //     },
//     //     xaxis: {
//     //         categories: [
//     //             "Jan",
//     //             "Feb",
//     //             "Mar",
//     //             "Apr",
//     //             "May",
//     //             "Jun",
//     //             "Jul",
//     //             "Aug",
//     //             "Sep",
//     //             "Oct",
//     //             "Nov",
//     //             "Dec",
//     //         ],
//     //         axisBorder: {
//     //             show: false,
//     //         },
//     //         tooltip: {
//     //             enabled: true,
//     //         },
//     //         labels: {
//     //             show: true,
//     //             rotate: -45,
//     //             rotateAlways: true,
//     //         },
//     //     },
//     //     yaxis: {
//     //         show: false,
//     //     },
//     //     legend: {
//     //         show: false,
//     //     },
//     //     grid: {
//     //         borderColor: "#dae1ea",
//     //         strokeDashArray: 5,
//     //         xaxis: {
//     //             lines: {
//     //                 show: true,
//     //             },
//     //         },
//     //         yaxis: {
//     //             lines: {
//     //                 show: false,
//     //             },
//     //         },
//     //         padding: {
//     //             top: 0,
//     //             right: 0,
//     //             bottom: -20,
//     //             left: 10,
//     //         },
//     //     },
//     //     tooltip: {
//     //         y: {
//     //             formatter: function (val) {
//     //                 return val + " million";
//     //             },
//     //         },
//     //     },
//     //     colors: ["#3659cd", "#299bff", "#66b7ff", "#a3d4ff", "#cce7ff", "#f5faff"],
//     // };
    

//     var options = {
//         chart: {
//             height: 300,
//             type: "bar",
//             toolbar: {
//                 show: false,
//             },
//         },
//         dataLabels: {
//             enabled: true,
//             formatter: function(val) {
//                 return val;
//             },
//             style: {
//                 // colors: ['#F44336', '#E91E63', '#9C27B0', '#673AB7', '#3F51B5']
//                 colors: ['rgba(244, 67, 54, 0.7)', 'rgba(233, 30, 99, 0.7)', 'rgba(156, 39, 176, 0.7)', 'rgba(103, 58, 183, 0.7)', 'rgba(63, 81, 181, 0.7)']
//             }
//         },
//         stroke: {
//             curve: "smooth",
//             width: 3,
//         },
//         series: [
//             {
//                 name: "Expected",
//                 data: expectedValues,
//             },
//             {
//                 name: "Actual",
//                 data: actualValues,
//             },
//         ],
//         grid: {
//             borderColor: "#dae1ea",
//             strokeDashArray: 5,
//             xaxis: {
//                 lines: {
//                     show: true,
//                 },
//             },
//             yaxis: {
//                 lines: {
//                     show: false,
//                 },
//             },
//             padding: {
//                 top: 0,
//                 right: 0,
//                 bottom: 10,
//                 left: 0,
//             },
//         },
//         xaxis: {
//             categories: [
//                 "Jan",
//                 "Feb",
//                 "Mar",
//                 "Apr",
//                 "May",
//                 "Jun",
//                 "Jul",
//                 "Aug",
//                 "Sep",
//                 "Oct",
//                 "Nov",
//                 "Dec",
//             ],
//         },
//         yaxis: {
//             labels: {
//                 show: true,
//             },
//         },
//         colors: ["#3659cd", "#299bff", "#66b7ff", "#a3d4ff", "#cce7ff", "#f5faff"],
//         markers: {
//             size: 0,
//             opacity: 0.3,
//             // colors: ['#F44336', '#E91E63', '#9C27B0', '#673AB7', '#3F51B5'],
//             colors : ['#000000','#000000'],  // Set marker color to black
//             strokeColor: "#000000",
//             strokeWidth: 2,
//             hover: {
//                 size: 7,
//             },
//         },
//     };
    

//     const chart = new ApexCharts(document.querySelector("#chart_month"), options);
    
//     chart.render();
//     console.log('chart ready:');
// } catch (e) {
//     console.error('Error parsing JSON data:', e);
// }
// });