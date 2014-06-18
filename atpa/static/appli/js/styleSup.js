/*Variables globale*/
// var seconde = 30;//secondes utiliser pour le compteur
// var minute = 0;//minutes utiliser pour le compteur
// var timer = setInterval('decompte()',1000);//lancement du compte à rebourg
// var counter = 0;//compteur de zones de saisies réponses Fausses
// var counter1 = 0;//compteur de zones de saisies réponses Vraies
// /*--------------------------------------------------*/

// /* fonction qui s'execute quand la page web est prête*/
// document.ready=function () {

//     // On cache les sous-menus :
//     $(".navigation ul.subMenu").hide();

	
//     // On sélectionne tous les items de liste portant la classe "toggleSubMenu"
//     // et on remplace l'élément span qu'ils contiennent par un lien :
//     $(".navigation li.toggleSubMenu span").each( function () {
//         $(this).replaceWith('<a href="">' + $(this).text() + '<\/a>') ;
//     }) ;
    
//      // On modifie l'évènement "click" sur les liens dans les items de liste
//     // qui portent la classe "toggleSubMenu" :
//     $(".navigation li.toggleSubMenu > a").click( function () {
//         // Si le sous-menu était déjà ouvert, on le referme :
//         if ($(this).next("ul.subMenu:visible").length != 0) {
//             $(this).next("ul.subMenu").slideUp("normal");
//         }
//         // Si le sous-menu est caché, on ferme les autres et on l'affiche :
//         else {
//             $(".navigation ul.subMenu").slideUp("normal");
//             $(this).next("ul.subMenu").slideDown("normal");
//         }
//         // On empêche le navigateur de suivre le lien :
//         return false;
//     });    
// 	//on ré-active les boutons réponses
//     activebtn(); 
// }

// /* Permet de cacher certains éléments*/
// function cache(){
//   $("#question").hide();
//   $("#repFausse1").hide();$("#repFausse2").hide();$("#repFausse3").hide();
//   $("#repVrai1").hide();$("#repVrai2").hide();$("#repVrai3").hide();
//   document.getElementById("stylebtn").innerHTML = "";
//   document.getElementById('btnAjoutRepF').disabled= false;
//   document.getElementById('btnAjoutRepV').disabled= false;
// }

// /* Compte à rebourg */
// function decompte()
// {
// 	//ajout d'un "s" à seconde quand il y a plus d'une seconde
// 	if(seconde <= 1) {
// 	var pluriel = "";
// 	} else {
// 	pluriel = "s";
// 	}
	
// 	//ajout d'un "s" à minute quand il y a plus d'une minute			
// 	if(minute <= 1) {
// 	var pluriel2 = "";
// 	} else {
// 	pluriel2 = "s";
// 	}
	
// 	// retranche une minute toutes les 60 secondes			
// 	if (seconde > 59){	
// 		minute = parseInt(seconde/60);
// 		var seconde2 = seconde % 60;
// 	}
// 	else{
// 		seconde2=seconde;
// 		minute=0;
// 	}
		
// 	//affichage du compte à rebourg
// 	$("#compt2").html("<span class='digit'>"+minute +"</span>"+" minute"+pluriel2 +" "+"<span class='digit'>" + seconde2 +"</span>"+ " seconde" + pluriel);
// 	$("#compt2").css("font-size","x-large");
	
// 	// si il reste moins de 10 secondes, l'affichage devient rouge+ il y a un 0 devant les secondes (pour avoir 2 chiffres)
// 	if(seconde < 10 || seconde < 0) {
// 		$("#compt2").css("color","red");
// 		$("#compt2").html("<span class='digit'>"+minute +"</span>"+" minute"+pluriel2 +" "+"<span class='digit'>0" + seconde2 +"</span>"+ " seconde" + pluriel);

// 	}
// 	//si il reste moins de 10 minutes, il y a un 0 devant les secondes (pour avoir 2 chiffres)
// 	if(minute < 10 || minute < 0) {
// 		$("#compt2").html("<span class='digit'>0"+minute +"</span>"+" minute"+pluriel2 +" "+"<span class='digit'>" + seconde2 +"</span>"+ " seconde" + pluriel);
// 	}
// 	//si il y a moins de 10 min et moins de 10 secondes -> 0 devant les secondes et minutes
// 	if(minute < 10 && seconde < 10) {
// 		$("#compt2").html("<span class='digit'>0"+minute +"</span>"+" minute"+pluriel2 +" "+"<span class='digit'>0" + seconde2 +"</span>"+ " seconde" + pluriel);
// 	}
// 	/*si plus de 9 secondes affichage normal*/
// 	if(seconde >= 10) {
// 		$("#compt2").css("color","black");
// 	}
	
// 	// affiche terminé quand il n'y a plus de temps	
// 	if(seconde == 0 || seconde < 0) {
// 		seconde = 0;minute=0;	
// 		clearInterval(timer);	
// 		$("#compt2").html("Terminé");
// 		desactivebtn();
// 	}			
// 	seconde--;
// 	return seconde;
// }

// /* Fonction affichant/masquant la question coté étudiant (pour les personnes mal voyantes)*/
// function question(){
// 	$("#question").toggle("slow");
// }

// /* Fonction de désactivation des réponses vrai/faux coté étudiant*/
// function desactivebtn(){
// 	document.getElementById('btnEtuYes').disabled= true;
// 	document.getElementById('btnEtuNo').disabled= true;	
// }

// /* fonction d'activation des réponses vrai/faux au chargement de la page coté étudiant*/
// function activebtn(){
// 	document.getElementById('btnEtuYes').disabled= false;
// 	document.getElementById('btnEtuNo').disabled= false;	
// }

// /* Fonction affichant/masquant la réponse*/
// function reponse(){
// 	$("#reponseEns").toggle("slow");
// }

// /* fonction cachant la réponse au chargement de la page enseignant_question */
// function cachereponse(){
// 	$("#reponseEns").hide();
// }

// /* Fonction stoppant le compte à rebourg*/
// function stopTime(){
// 	$("#compt2").html("Terminé");
// 	$("#compt2").css("color","red");	
// 	seconde = 0;	
// }

// /* fonction ajoutant des secondes au compte à rebourg*/
// function ajoutSec(){
// 	//on récupère le nombre de secondes réstantes
// 	var sec1 = decompte();
// 	//on récupère le nombre de secondes à ajouter
// 	var sec2 = document.getElementById("rangeS").value;
// 	//on additionne les deux
// 	var ajout = parseInt(sec1)+parseInt(sec2);
// 	//on attribut la valeur additionné à la valeur seconde par défaut
// 	seconde = ajout;
// }

// /* Ajoute une zone de saisie de réponse dans le champs Réponses Fausses */	
// function ajoutRepF(id) {
// 	//ajoute 1 pour afficher la zone de texte suivante
// 	counter++;
// 	//affiche des zones de texte suivant le nombre d'appuit sur le bouton ajout
// 	switch(counter)
// 	{
// 		case 1:
// 		$("#repFausse1").show();
// 		break;
// 		case 2:
// 		$("#repFausse2").show();
// 		break;
// 		case 3:
// 		$("#repFausse3").show();
// 		$("#btnAjoutRepF").hide();
// 		break;
// 		default:
// 		exit();
// 	}
// 	var temp =0;
// 	//ajout des compteurs de réponses vraies et fausses plus les des zones du début
// 	temp = counter + counter1;
// 	temp +=2;
// 	//on ne peut pas avoir plus de 4 zones de saisies de réponses
// 	if (temp>=4){
// 			document.getElementById('btnAjoutRepF').disabled= true;
// 			document.getElementById('btnAjoutRepV').disabled= true;	
// 			$("#btnAjoutRepF").hide();
// 			$("#btnAjoutRepV").hide();
// 	}
// }
	
// /* Ajoute une zone de saisie de réponse dans le champs Réponses Vraies */
// function ajoutRepV(id){
// 	counter1++;
// 	switch(counter1)
// 	{
// 		case 1:
// 		$("#repVrai1").show();
// 		break;
// 		case 2:
// 		$("#repVrai2").show();
// 		break;
// 		case 3:
// 		$("#repVrai3").show();
// 		$("#btnAjoutRepV").hide();
// 		break;
// 		default:
// 		exit();
// 	}
// 	var temp =0;
// 	temp = counter + counter1;
// 	temp +=2;
// 	if (temp>=4){
// 			document.getElementById('btnAjoutRepF').disabled= true;
// 			document.getElementById('btnAjoutRepV').disabled= true;
// 			$("#btnAjoutRepF").hide();
// 			$("#btnAjoutRepV").hide();	
// 	}
// }



	
// }
/* Ajoute une zone de saisie de réponse dans le champs Réponses Vraies */
$(function(){
	$('#enseignant').on('change' , function(){
		var id_ens = $(this).find('option:selected').val();
		window.location.href = "{% url 'question_posee' enseignant_id = id_ens %}";
	});
});
// alert('coucou');
//  Ajoute une zone de saisie de réponse dans le champs Réponses Vraies 
// $("select[name='choiceType']").onChange(function(){
// 	alert('rrrrr');
// });