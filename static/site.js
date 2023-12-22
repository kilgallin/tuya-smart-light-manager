tagQueue = []

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
	});
	
	$('.color').click(function(){
		$('#presetColumn').children().last().remove()
		$('#presetColumn').append('<div class="preset">red</div><div class="preset">orange</div><div class="preset">yellow</div>				<div class="preset">lime</div><div class="preset">green</div><div class="preset">aqua</div><div class="preset">cyan</div><div class="preset">blue</div><div class="preset">indigo</div><div class="preset">violet</div><div class="preset">pink</div>')
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
			if (tagQueue.length > 0) {
				$('#tagColumn').append("<div class='back'>Back</div>")
			}
			
			$('#tagColumn .tag').click(function(){
				if($(this).hasClass('selected')){
					$(this).removeClass('selected')
					return;
				}
				$(this).addClass('selected')
			})
			
			$('#tagColumn .tag').dblclick(function(){
				tagQueue.push(root)
				getTags($(this).text())
			})
			
			$('#tagColumn .back').dblclick(function(){
				getTags(tagQueue.pop())
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