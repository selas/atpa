window.onload=function () {
 
  
  
  
}

function affichageQuestion(){
	
	$("#newQuestion").hide();
	$("#afficherQuestion").show();

}


/*function rangeSe()
{
	$('rangeSeconde').oninput = function() 
	{
		$('rangeid').innerHTML = this.value; 
	};
	$('rangeSeconde').oninput();
}*/


document.ready=function () {

	//Pour cacher par defaut la section qui contient l'affichage des questions
	//$("#afficherQuestion").hide();
    



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
        
        activebtn();
        
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
  $("#question").hide();

  document.getElementById("stylebtn").innerHTML = "";
}

function conversion()
{
	var seconde=0;// ajouter un get element by id
	var minute=0;// ajouter un get element by id
	var heure=0;// ajouter un get element by id
	
	if (minute>0)
	{
		seconde += (minute*60);
	}
	if (heure>0)
	{
		seconde += (heure*3600);
	}
}

var seconde = 30;
var minute = 0;

function decompte()
{
	if(seconde <= 1) {
	var pluriel = "";
	} else {
	pluriel = "s";
	}
				
	if(minute <= 1) {
	var pluriel2 = "";
	} else {
	pluriel2 = "s";
	}
				
	if (seconde > 59){	
		minute = parseInt(seconde/60);
		var seconde2 = seconde % 60;
	}
	else{
			seconde2=seconde;
			minute=0;
		}
	$("#compt2").html(minute +" minute"+pluriel2 +" "+ seconde2 + " seconde" + pluriel);
	$("#compt2").css("font-size","x-large");
	//$("#compt").html(seconde + " seconde" + pluriel);
	//$("#compt").css("font-size","x-large");
	
	if(seconde <= 10 || seconde < 0) {
		//$("#compt").css("color","red");
		$("#compt2").css("color","red");
	}
		
	if(seconde == 0 || seconde < 0) {
		seconde = 0;minute=0;	
		clearInterval(timer);	
		//$("#compt").html("Terminé");
		$("#compt2").html("Terminé");
		desactivebtn();
	}			
	seconde--;
}
var timer = setInterval('decompte()',1000);

function question(){
	$("#question").toggle("slow");
}

function desactivebtn(){
	document.getElementById('btnEtuYes').disabled= true;
	document.getElementById('btnEtuNo').disabled= true;	
}

function activebtn(){
	document.getElementById('btnEtuYes').disabled= false;
	document.getElementById('btnEtuNo').disabled= false;	
}

function reponse(){
	$("#reponseEns").toggle("slow");
}
function cachereponse(){
	$("#reponseEns").hide();
}

function calculer()
{
	//graphique
	var ctx = document.getElementById("graph").getContext("2d");
	
	
	var data = {
	labels : ["January","February","March","April","May","June","July"],
	datasets : [
		{
			fillColor : "rgba(220,220,220,0.5)",
			strokeColor : "rgba(220,220,220,1)",
			data : [65,59,90,81,56,55,40]
		},
		{
			fillColor : "rgba(151,187,205,0.5)",
			strokeColor : "rgba(151,187,205,1)",
			data : [28,48,40,19,96,27,100]
		}
	]
}

	var options = 
	{
				
	//Boolean - If we show the scale above the chart data			
	scaleOverlay : true,
	
	//Boolean - If we want to override with a hard coded scale
	scaleOverride : false,
	
	//** Required if scaleOverride is true **
	//Number - The number of steps in a hard coded scale
	scaleSteps : null,
	//Number - The value jump in the hard coded scale
	scaleStepWidth : null,
	//Number - The scale starting value
	scaleStartValue : null,

	//String - Colour of the scale line	
	scaleLineColor : "rgba(0,0,0,.1)",
	
	//Number - Pixel width of the scale line	
	scaleLineWidth : 1,

	//Boolean - Whether to show labels on the scale	
	scaleShowLabels : true,
	
	//Interpolated JS string - can access value
	scaleLabel : "<%=value%>",
	
	//String - Scale label font declaration for the scale label
	scaleFontFamily : "'Arial'",
	
	//Number - Scale label font size in pixels	
	scaleFontSize : 12,
	
	//String - Scale label font weight style	
	scaleFontStyle : "normal",
	
	//String - Scale label font colour	
	scaleFontColor : "#666",	
	
	///Boolean - Whether grid lines are shown across the chart
	scaleShowGridLines : true,
	
	//String - Colour of the grid lines
	scaleGridLineColor : "rgba(0,0,0,.05)",
	
	//Number - Width of the grid lines
	scaleGridLineWidth : 1,	

	//Boolean - If there is a stroke on each bar	
	barShowStroke : true,
	
	//Number - Pixel width of the bar stroke	
	barStrokeWidth : 2,
	
	//Number - Spacing between each of the X value sets
	barValueSpacing : 4,
	
	//Number - Spacing between data sets within X values
	barDatasetSpacing : 1,
	
	//Boolean - Whether to animate the chart
	animation : true,

	//Number - Number of animation steps
	animationSteps : 60,
	
	//String - Animation easing effect
	animationEasing : "easeOutQuart",

	//Function - Fires when the animation is complete
	onAnimationComplete : null
	
	}
	var myNewChart = new Chart(ctx).Bar(data,options);
}
