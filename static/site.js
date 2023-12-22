tagQueue = []
token = ""

function sign_string(key_b64, to_sign) {
	try {
		key = CryptoJS.enc.Base64.parse(key_b64).toString(CryptoJS.enc.Utf8);
	}
	catch {
		key = CryptoJS.enc.Hex.parse(toHex(atob(key_b64)));
	}
	hash = CryptoJS.HmacSHA256(to_sign, key);
	hashInBase64 = CryptoJS.enc.Base64.stringify(hash);
	return hashInBase64;
}

function toHex(str) {
	var result = '';
	for (var i=0; i<str.length; i++) {
	  if (str.charCodeAt(i).toString(16).length === 1) {
		result += '0' + str.charCodeAt(i).toString(16);
	  } else {
		result += str.charCodeAt(i).toString(16);
	  }
	}
	return result;
}


function login(){
	username = $("#usernameBox").val()
	passwd = CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse($("#passwordBox").val()));
	$.ajax({
		url: "nonce",
		type: "get",
		data: {
			username: username
		},
		success: function(nonce) {
			$.ajax({
				url: "token",
				type: "post",
				contentType: "application/json",
				data: JSON.stringify({
					username: username,
					authcode: sign_string(passwd,nonce)
				}),
				success: function(newToken) {
					loadData()
					token = newToken
					$("#auth").hide()
					$("#headerUsername").text(username)
					switchExecuteButton()
					$("#buttons").show()
				}
			})
		}
	})
}

function switchExecuteButton(){
	$('#headerExecute').text("Execute");
	$('#headerExecute').off('click');
	$('#headerExecute').click(function(){
	$.ajax({
		url: "execute",
		type: "post",
		data: {
			tags:JSON.stringify($('.tag.selected').map( function (i, e){
				return $(e).text()
			}).get()),
			preset:$('.preset.selected').text(),
			username: $("#usernameBox").val(),
			token: token
		}
	})
	});
}

function clickPreset(preset){
		if($(preset).hasClass('selected')){
			$(preset).removeClass('selected')
			return;
		}
		$('.preset').removeClass('selected')
		$(preset).addClass('selected')
}

function loadBrightnessOptions(){
		$('#presetColumn .brightness').remove()
		$('#presetColumn').append('<div class="preset">brightest</div><div class="preset">bright</div><div class="preset">brightish</div><div class="preset">dimmish</div><div class="preset">dim</div><div class="preset">dimmest</div>')
		$('.preset').off("click")
		$('.preset').click(function(){clickPreset(this)});
	}

function setHandlers(){
	$('#headerExecute').click(login);
	
	$('.preset').click(function(){clickPreset(this)});
	
	$('.color').click(function(){
		$('#presetColumn .color').remove()
		$('#presetColumn').append('<div class="preset">pink</div><div class="preset">red</div><div class="preset">orange</div><div class="preset">yellow</div><div class="preset">lime</div><div class="preset">green</div><div class="preset">aqua</div><div class="preset">cyan</div><div class="preset">blue</div><div class="preset">indigo</div><div class="preset">violet</div>')

		// Move brightness options back down to the bottom
		$('#presetColumn .brightness').remove()
		$('#presetColumn').append('<div class="brightness">brightness</div>')
		$('.brightness').click(loadBrightnessOptions)

		
		$('.preset').off("click")
		$('.preset').click(function(){clickPreset(this)});
	})
	
	$('.brightness').click(loadBrightnessOptions)
}

function goBack(){
		getTags(tagQueue.pop())
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
			
			$('#tagColumn .tag').on('touchstart', function() {
				tag = $(this).text()
				timeoutId = setTimeout(function(){
					tagQueue.push(root)
					getTags(tag)
				}, 1000);
			}).on('mouseup mouseleave touchend', function() {
				clearTimeout(timeoutId);
			});
			
			$('#tagColumn .back').dblclick(function(){
				goBack()
			})
			
			$('#tagColumn .back').on('touchstart', function() {
				timeoutId = setTimeout(goBack, 1000);
			}).on('mouseup mouseleave touchend', function() {
				clearTimeout(timeoutId);
			});
		}
	})
}

function loadData(){
	$.ajax({
		url: "getRoot",
		type: "post",
		data: {
			username: $("#usernameBox").val()
		},
		success: function(root){
			getTags(root)
		}
	})
}

$(document).ready(function() {
	$("#buttons").hide()
	setHandlers()
})