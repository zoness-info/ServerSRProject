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
    const chartElement1 = document.querySelector("#PVR1Chart");
    const chartpercentage = parseFloat(chartElement1.getAttribute("data-chartpercentage"));
    const chartElement2 = document.querySelector("#PVR2Chart");
    const chartpercentage2 = parseFloat(chartElement2.getAttribute("data-chartpercentage2"));
    const chartElement3 = document.querySelector("#PVR3Chart");
    const chartpercentage3 = parseFloat(chartElement3.getAttribute("data-chartpercentage3"));
    // console.log('PVR3 Percentage',chartpercentage3)    
    const chartElement4 = document.querySelector("#PVR4Chart");
    const chartpercentage4 = parseFloat(chartElement4.getAttribute("data-chartpercentage4"));
    // console.log('PVR4 Percentage',chartpercentage4)
    const chartElement5 = document.querySelector("#PVR5Chart");
    const chartpercentage5 = parseFloat(chartElement5.getAttribute("data-chartpercentage5"));
    // console.log('PVR5 Percentage',chartpercentage5)    
    const chartElement6 = document.querySelector("#PVR6Chart");
    const chartpercentage6 = parseFloat(chartElement6.getAttribute("data-chartpercentage6"));
    // console.log('PVR6 Percentage',chartpercentage6)

    const chartElement7 = document.querySelector("#PVR7Chart");
    const chartpercentage7 = parseFloat(chartElement7.getAttribute("data-chartpercentage7"));
    console.log('PVR7 Percentage',chartpercentage7)    
    const chartElement8 = document.querySelector("#PVR8Chart");
    const chartpercentage8 = parseFloat(chartElement8.getAttribute("data-chartpercentage8"));
    console.log('PVR8 Percentage',chartpercentage8)
      
        const options1 = {
            series: [parseFloat(chartpercentage)],
            chart: {
            height: 150,
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
                    return parseFloat(val) + "%";
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
    series: [parseFloat(chartpercentage2)],
    chart: {
    height: 150,
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
            return parseFloat(val) + "%";
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


  // PVR-3 Chart
const options3 = {
  series: [parseFloat(chartpercentage3)],
  chart: {
  height: 150,
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
          return parseFloat(val) + "%";
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

const chart3 = new ApexCharts(document.querySelector("#PVR3Chart"), options3);
// console.log('3 chart render')
chart3.render();


// PVR-4 Chart
const options4 = {
  series: [parseFloat(chartpercentage4)],
  chart: {
  height: 150,
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
          return parseFloat(val) + "%";
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

const chart4 = new ApexCharts(document.querySelector("#PVR4Chart"), options4);
chart4.render();


// PVR-5 Chart
const options5 = {
                  series: [parseFloat(chartpercentage5)],
                  chart: {
                  height: 150,
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
                          return parseFloat(val) + "%";
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

const chart5 = new ApexCharts(document.querySelector("#PVR5Chart"), options5);
chart5.render();

// PVR-6 Chart
const options6 = {
  series: [parseFloat(chartpercentage6)],
  chart: {
  height: 150,
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
          return parseFloat(val) + "%";
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

const chart6 = new ApexCharts(document.querySelector("#PVR6Chart"), options6);
chart6.render();

// PVR-7 Chart
const options7 = {
  series: [parseFloat(chartpercentage7)],
  chart: {
  height: 150,
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
          return parseFloat(val) + "%";
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

const chart7 = new ApexCharts(document.querySelector("#PVR7Chart"), options7);
chart7.render();

// PVR-8 Chart
const options8 = {
  series: [parseFloat(chartpercentage8)],
  chart: {
  height: 150,
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
          return parseFloat(val) + "%";
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

const chart8 = new ApexCharts(document.querySelector("#PVR8Chart"), options8);
chart8.render();
     
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