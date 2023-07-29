$(document).ready(function() {
	$('#headerExecute').click(function(){
		$.ajax({
			url: "execute",
			type: "get",
			data: {
				tags:"Parlor",
				preset:$('.preset.selected').text()
			}
		})
	});
	
	$('.tag, .preset').click(function(){
		if($(this).hasClass('selected')){
			$(this).removeClass('selected')
			return;
		}
		if($(this).hasClass('preset')){
			$('.preset').removeClass('selected')
		}
		$(this).addClass('selected')
	})
})