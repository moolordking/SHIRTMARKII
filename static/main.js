
let spotifyCode = window.location.href.split("?code=")[1];

function setLocation() {
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(getPosition);
	} else {
		document.write("Geolocation is not supported by this browser.");
	}
}

function getPosition(position) {
	let currentPosition =  [position.coords.latitude, position.coords.longitude];
	let place = addRequest(function(position, result) 
	{
		place = result.split(":::")[0]
		songAndImage = result.split(":::");
		songAndImage = songAndImage[Math.floor(Math.random()*songAndImage.length-2)+1];
		song = songAndImage.split("@")[0];
		image = songAndImage.split("@")[1];
		document.getElementById("ArtistAvatar").style.backgroundImage = "url("+image+")";
		loadSong(song);
		addCity(position, place);
	},
	spotifyCode,currentPosition);
}

function loadSong(songid) {
	document.getElementById("Embed").src = "https://open.spotify.com/embed/track/" + songid;
}

function addCity(coordinates,place) {
	document.getElementById("Location").innerHTML = place;
    document.getElementById("Contents").style.display = "block";
    document.getElementById("PermissionsScreen").classList.add("hide");
    initiateMap(coordinates);
}

function initiateMap(latandlong) {
	const lat  = latandlong[0];
	const long = latandlong[1];
	let map = L.map('Map').setView([lat, long], 8);
	let customMarker = L.icon({
	    iconUrl: 'static/CustomMarkerHueRotate.png',
	    iconSize: [34, 49],
	    iconAnchor: [17, 49]
	    // popupAnchor: [-3, -76]
	});

	L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
	    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
	}).addTo(map);

	L.marker([lat, long], {icon: customMarker}).addTo(map).openPopup();
}
