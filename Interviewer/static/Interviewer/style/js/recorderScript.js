
window.addEventListener('load', initVars);

var btRec;
var recText;
var recSpan = document.createElement('span');
var togRec = true;
var btSub;
var togSub = false;
var question;
var ques = ["What are your three greatest strengths?", "How do you deal with conflict in the workplace?", "How do you handel a challenge?", "Give an example of how you work in a team?"];

function initVars() {
	btRec = document.getElementById('btnRecord');
	btSub = document.getElementById('button_analyze_speech');
	recText = document.getElementById('recText');
	question = document.getElementById('question');
	btRec.addEventListener('click', toggleRecord);

	switch(Math.floor((Math.random() * 3) + 0)) {
		case 0:
			question.innerHTML = ques[0];
			break;
		case 1:
			question.innerHTML = ques[1];
			break;
		case 2:
			question.innerHTML = ques[2];
			break;
		case 3:
			question.innerHTML = ques[3];
			break;
	}

	

}

function toggleRecord() {
	if (togRec) {
		recText.innerHTML = "Stop";
		recText.style.color="rgba(0, 167, 225, 1)";
		recSpan.style.color="red";
		recSpan.classList.add('glyphicon');
		recSpan.classList.add('glyphicon-record');
		recSpan.classList.add('blink');
		recText.appendChild(recSpan);
		togRec = false;
		togSub = false;
	}
	else {
		btRec.classList.add('btn');
		recText.innerHTML = "Record";
		recText.style.color="rgba(0, 167, 225, 1)";
		recSpan.classList.remove('glyphicon');
		recSpan.classList.remove('glyphicon-record');
		recSpan.classList.remove('blink');
		togRec = true;
		togSub = true;
	}

	if (togSub) {
		btSub.classList.remove('disabled');
		btSub.style.color="rgba(0, 167, 225, 1)";
	}
	else {
		btSub.classList.add('disabled');
		btSub.style.color="rgba(0, 167, 225, 1)";
	}
}
