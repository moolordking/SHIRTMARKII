
function addRequest(_callback, spotifyCode, position) {
	let value = [spotifyCode, position[0], position[1]].join(":::");
    $.ajax({
        url: '/process',
        type: 'POST',
        data: { 'data': value },
        success: function(response) {
            _callback(position, response)
        },
        error: function(error) {
            console.log(error);
            return error;
        }
    });
}
