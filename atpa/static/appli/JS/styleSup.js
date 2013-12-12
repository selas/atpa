window.onload=function () {
  // On cache les sous-menus :
  $(".navigation ul.subMenu").hide();
  cache();
  
  var chart = new CanvasJS.Chart("chartContainer",
		{
			title:{
				text: "Presidential Election Results"
			},          
			data: [
			{        
				type: "doughnut",
				startAngle: 60,                          
				toolTipContent: "{y} votes", 					

				showInLegend: true,
				dataPoints: [
				{  y: 65899660, label: "Barack Obama 51.06%", legendText: "Barack Obama" },
				{  y: 60929152, label: "Mitt Romney 47.21%", legendText: "Mitt Romney" },
				{  y: 2175850, label: "Others 1.73 %", legendText: "Others" }			

				]
			}
			]
		});

		chart.render();
  
  
}

document.ready=function () {

    // On cache les sous-menus :
    $(".navigation ul.subMenu").hide();

    // On sélectionne tous les items de liste portant la classe "toggleSubMenu"
    // et on remplace l'élément span qu'ils contiennent par un lien :
    $(".navigation li.toggleSubMenu span").each( function () {
        $(this).replaceWith('<a href="">' + $(this).text() + '<\/a>') ;
    }) ;
    
     // On modifie l'évènement "click" sur les liens dans les items de liste
    // qui portent la classe "toggleSubMenu" :
    $(".navigation li.toggleSubMenu > a").click( function () {
        // Si le sous-menu était déjà ouvert, on le referme :
        if ($(this).next("ul.subMenu:visible").length != 0) {
            $(this).next("ul.subMenu").slideUp("normal");
        }
        // Si le sous-menu est caché, on ferme les autres et on l'affiche :
        else {
            $(".navigation ul.subMenu").slideUp("normal");
            $(this).next("ul.subMenu").slideDown("normal");
        }
        // On empêche le navigateur de suivre le lien :
        return false;
    });    

}

function affrRO(){
	$("#AffRepFermee").hide();
	$("#AffRepSaisie").hide();
	$("#AffRepOuverte").show();
	document.getElementById("stylebtn").innerHTML = "<section class=\"alert-info span3\">Question à choix multiple</section><br /><br />";
	$(".navigation ul.subMenu").hide();
}
    
function affrRF(){
	$("#AffRepOuverte").hide();
	$("#AffRepSaisie").hide();
	$("#AffRepFermee").show();
	document.getElementById("stylebtn").innerHTML = "<section class=\"alert-info span2\">Question Fermée</section><br /><br />";
	$(".navigation ul.subMenu").hide();
}  
   
function affrRZS(){
	$("#AffRepFermee").hide();
    $("#AffRepOuverte").hide();
    $("#AffRepSaisie").show();
    document.getElementById("stylebtn").innerHTML = "<section class=\"alert-info span3\">Question avec saisie réponse</section><br /><br />";
    $(".navigation ul.subMenu").hide();
}

function cache(){
  $("#AffRepFermee").hide();
  $("#AffRepOuverte").hide();
  $("#AffRepSaisie").hide();
  document.getElementById("stylebtn").innerHTML = "";
}

