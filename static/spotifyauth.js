const CLIENT_ID = '839d0310c3474a8c9d1ca7354f8c5e96';
// Client Secret: b771f53eb6fe4cc288f15d28b44ac762

const REDIRECT_URI = 'http://localhost:5000/index';

const SCOPES = 'user-top-read user-library-read';

const AUTHORIZATION_URL = `https://accounts.spotify.com/authorize?response_type=code&client_id=${CLIENT_ID}&redirect_uri=${encodeURIComponent(REDIRECT_URI)}&scope=${encodeURIComponent(SCOPES)}`;

function spotifyAuth() {
	window.open(AUTHORIZATION_URL);
}
