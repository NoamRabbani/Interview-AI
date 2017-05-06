(function() {
// The width and height of the captured photo. We will set the
// width to the value defined here, but the height will be
// calculated based on the aspect ratio of the input stream.

var width = 320;    // We will scale the photo width to this
var height = 0;     // This will be computed based on the input stream

// |streaming| indicates whether or not we're currently streaming
// video from the camera. Obviously, we start at false.

var streaming = false;

// The various HTML elements we need to configure or control. These
// will be set by the startup() function.

var page_title = null;
var video = null;
var canvas = null;
var user_photo_url = null;

var capture_baseline = null;

var checkbox = null;
var button_assert_posture = null;
var form = null;

function startup() {
	page_title = document.getElementById('page_title').getAttribute("value");
	video = document.getElementById('video');
	canvas = document.getElementById('canvas');
	user_photo_url = document.getElementById('user_photo_url');
	capture_baseline = document.getElementById('capture_baseline');
	form = document.getElementById('form');

	if (page_title == "recorder"){
		capture_baseline = document.getElementById('capture_baseline');

		try{
			capture_baseline.addEventListener('click', function(ev){
				captureBaseline();
				ev.preventDefault();
			}, false);
		}
		catch(e){
			console.log(e)
		}

	}
	else if (page_title == "tracker"){
		button_assert_posture = document.getElementById('button_assert_posture');
		checkbox = document.getElementById('checkbox')

		tracker_interval = setInterval(assertPosture, 2500)
	}

	navigator.getMedia = ( navigator.getUserMedia ||
		navigator.webkitGetUserMedia ||
		navigator.mozGetUserMedia ||
		navigator.msGetUserMedia);

	navigator.getMedia(
	{
		video: true,
		audio: false
	},
	function(stream) {
		if (navigator.mozGetUserMedia) {
			video.mozSrcObject = stream;
		} else {
			var vendorURL = window.URL || window.webkitURL;
			video.src = vendorURL.createObjectURL(stream);
		}
		video.play();
	},
	function(err) {
		console.log("An error occured! " + err);
	}
	);

	video.addEventListener('canplay', function(ev){
		if (!streaming) {
			height = video.videoHeight / (video.videoWidth/width);

	// Firefox currently has a bug where the height can't be read from
	// the video, so we will make assumptions if this happens.

	if (isNaN(height)) {
		height = width / (4/3);
	}

	video.setAttribute('width', width);
	video.setAttribute('height', height);
	canvas.setAttribute('width', width);
	canvas.setAttribute('height', height);
	streaming = true;
}
}, false);

}

// Capture a photo by fetching the current contents of the video
// and drawing it into a canvas, then converting that to a PNG
// format data URL. By drawing it on an offscreen canvas and then
// drawing that to the screen, we can change its size and/or apply
// other changes before drawing it.

function captureBaseline() {
	var context = canvas.getContext('2d');
	if (width && height) {
		canvas.width = width;
		canvas.height = height;
		context.drawImage(video, 0, 0, width, height);

		var data = canvas.toDataURL('image/png');
		user_photo_url.setAttribute('value', data);

	}
}


function assertPosture() {
	if (checkbox.checked == true) {
		var context = canvas.getContext('2d');
		if (width && height) {
			canvas.width = width;
			canvas.height = height;
			context.drawImage(video, 0, 0, width, height);

			var data = canvas.toDataURL('image/png');
			user_photo_url.setAttribute('value', data);

	    button_assert_posture.click();}
	}
}

// Set up our event listener to run the startup process
// once loading is complete.
window.addEventListener('load', startup, false);
})();
