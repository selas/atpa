
var myCountdown2 = new Countdown({time: 30, width:200, height:80, rangeHi:"minute", onComplete:countdown_finished});
		// -------------------------------------------------
		// Advanced Options
		// -------------------------------------------------
		function countdown_finished(){
			document.getElementById('bouton_oui').disabled='disabled';
			document.getElementById('bouton_non').disabled='disabled';
		}
