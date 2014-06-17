/*-------------------------------------------------------------------------------------------*/
/*                      Script de gestion du graphique                                       */
/*                                                                                           */
/*-------------------------------------------------------------------------------------------*/
function calculer()
{
	// window.document.forms["nomFormulaire"].elements["nomElement"].value;
	var data = [
	{
		value : 45,
		color: "#D97041"
	},
	{
		value : 45,
		color: "#C7604C"
	},
	{
		value : 68,
		color: "#21323D"
	},
	{
		value : 58,
		color: "#9D9B7F"
	},
	{
		value : 82,
		color: "#7D4F6D"
	}
]
	var ctx = document.getElementById("graph").getContext("2d");
	var myNewChart = new Chart(ctx).PolarArea(data);
	new Chart(ctx).PolarArea(data,options);
	console.log(data);
}



