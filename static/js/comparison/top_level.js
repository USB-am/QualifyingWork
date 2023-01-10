function open_diagram(site_netloc) {
	top_block = document.getElementById('top-block');
	top_block.style.display = 'flex';
}
$('top-block').on('click', function () {
	alert('All good!');
});

function close_diagram() {
	top_block = document.getElementById('top-block');
	top_block.style.display = 'none';
}

function show_message(text) {
	console.log(text);
}

// $('#close-button').css( "border", "3px solid red" );