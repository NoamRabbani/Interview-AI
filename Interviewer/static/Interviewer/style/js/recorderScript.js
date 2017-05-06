
window.addEventListener('load', initVars);

var btRec;
var recText;
var recSpan = document.createElement('span');
var togRec = true;
var btSub;
var togSub = false;

function initVars() {
	btRec = document.getElementById('btnRecord');
	btSub = document.getElementById('button_analyze_speech');
	recText = document.getElementById('recText');
	btRec.addEventListener('click', toggleRecord);
}

function toggleRecord() {
	if (togRec) {
		recText.innerHTML = "Stop";
		recSpan.classList.add('glyphicon');
		recSpan.classList.add('glyphicon-record');
		recSpan.classList.add('blink');
		recText.appendChild(recSpan);
		togRec = false;
		togSub = false;
	}
	else {
		recText.innerHTML = "Record";
		recSpan.classList.remove('glyphicon');
		recSpan.classList.remove('glyphicon-record');
		recSpan.classList.remove('blink');
		togRec = true;
		togSub = true;
	}

	if (togSub) {
		btSub.classList.remove('disabled');
	}
	else {
		btSub.classList.add('disabled');
	}
}
