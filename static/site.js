function setHandlers(){
	$('#headerExecute').click(function(){
		$.ajax({
			url: "execute",
			type: "post",
			data: {
				tags:JSON.stringify($('.tag.selected').map( function (i, e){
					return $(e).text()
				}).get()),
				preset:$('.preset.selected').text()
			}
		})
	});
	
	$('.preset').click(function(){
		if($(this).hasClass('selected')){
			$(this).removeClass('selected')
			return;
		}
		$('.preset').removeClass('selected')
		$(this).addClass('selected')
	})
}

function getTags(root){
	$.ajax({
		url: "getTags",
		type: "get",
		data: {
			root: root
		},
		success: function(data){
			$('#tagColumn').empty()
			tags = JSON.parse(data)
			tags.forEach( function(tag) {
				$('#tagColumn').append("<div class='tag'>"+tag+"</div>")
			})
			$('#tagColumn .tag').click(function(){
				if($(this).hasClass('selected')){
					$(this).removeClass('selected')
					return;
				}
				$(this).addClass('selected')
			})
			
			$('#tagColumn .tag').dblclick(function(){
				getTags($(this).text())
			})
		}
	})
}

function loadData(){
	getTags("Living Space")
}


$(document).ready(function() {
	setHandlers()
	loadData()
})