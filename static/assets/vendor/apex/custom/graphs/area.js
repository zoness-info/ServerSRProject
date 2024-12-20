var options = {
	chart: {
		height: 300,
		type: "area",
		toolbar: {
			show: true,
		},
	},
	dataLabels: {
		enabled: false,
	},
	stroke: {
		curve: "smooth",
		width: 3,
	},
	series: [
		{
			name: "Sales",
			data: [10, 80, 40, 40, 20, 35, 20, 10, 31, 43, 56, 29],
		},
		{
			name: "Revenue",
			data: [2, 8, 25, 7, 20, 20, 51, 35, 42, 20, 33, 67],
		},
	],
	grid: {
		borderColor: "#dae1ea",
		strokeDashArray: 5,
		xaxis: {
			lines: {
				show: true,
			},
		},
		yaxis: {
			lines: {
				show: false,
			},
		},
		padding: {
			top: 0,
			right: 0,
			bottom: 10,
			left: 0,
		},
	},
	xaxis: {
		categories: [
			"Jan",
			"Feb",
			"Mar",
			"Apr",
			"May",
			"Jun",
			"Jul",
			"Aug",
			"Sep",
			"Oct",
			"Nov",
			"Dec",
		],
	},
	yaxis: {
		labels: {
			show: false,
		},
	},
	colors: ["#3659cd", "#299bff", "#66b7ff", "#a3d4ff", "#cce7ff", "#f5faff"],
	markers: {
		size: 0,
		opacity: 0.3,
		colors: ["#3659cd", "#299bff", "#66b7ff", "#a3d4ff", "#cce7ff", "#f5faff"],
		strokeColor: "#ffffff",
		strokeWidth: 2,
		hover: {
			size: 7,
		},
	},
	fill: {
		type: "gradient",
		gradient: {
			shade: "dark",
			gradientToColors: ["#e65729", "#9e6419"],
			shadeIntensity: 1,
			type: "horizontal",
			opacityFrom: 0.7,
			opacityTo: 0,
			stops: [0, 100, 100, 100],
		},
	},
};

var chart = new ApexCharts(document.querySelector("#areaGraph"), options);

chart.render();
