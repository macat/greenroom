$(function(){
  var step = 1;

  var steps = {
    first: function() {
      $('#result-img').empty();
      $('#arrow').animate({left: '-420px'}, 500)
      step = 1;
      $('#placeholder-pic').removeClass('hidden');
      $('.step').addClass('hidden');
      $('#step-1').removeClass('hidden');
      // $('.suggestions').removeClass('hidden');
    },
    second: function() {
      step = 2;
      $('#camera').hide();
      $('#placeholder-pic').addClass('hidden');
      $('.step').addClass('hidden');
      $('#step-2').removeClass('hidden');
    },
    third: function() {
      step = 3;
      $('#arrow').animate({left: '-25px'}, 500)
      $('.step').addClass('hidden');
      $('#step-3').removeClass('hidden');
      $('#mirror').addClass('span-8');
      $('#mirror').removeClass('max-width');
    }
  };
  steps.first();
  
  $('#ok').on('click', steps.third);
  $('.back').on('click', steps.first);

  $('#show-camera').on('click', function(){
    $('#uploader').hide();
    $('#show-camera').hide();
    $('.suggestions').addClass('hidden');
    $('#capture').show();
    $('#camera').removeClass('hidden');
    var pos = 0, ctx = null, saveCB, image = [];

	var canvas = document.createElement("canvas");
	canvas.setAttribute('width', 320);
	canvas.setAttribute('height', 240);
	
	if (canvas.toDataURL) {

		ctx = canvas.getContext("2d");
		
		image = ctx.getImageData(0, 0, 320, 240);
	
		saveCB = function(data) {
			
			var col = data.split(";");
			var img = image;

			for(var i = 0; i < 320; i++) {
				var tmp = parseInt(col[i]);
				img.data[pos + 0] = (tmp >> 16) & 0xff;
				img.data[pos + 1] = (tmp >> 8) & 0xff;
				img.data[pos + 2] = tmp & 0xff;
				img.data[pos + 3] = 0xff;
				pos+= 4;
			}

			if (pos >= 4 * 320 * 240) {
				ctx.putImageData(img, 0, 0);
				$.ajax({
          url: "/outfit/new", 
          data: {type: "data", image: canvas.toDataURL("image/png")}, 
          type: 'POST',
          success: function(response){
            var responseJSON = $.parseJSON(response.responseText);
            var feedback_form_action = responseJSON['request_feedback_url'];
            $('#form-ask').attr("action", feedback_form_action);
            $('<img>', {src: responseJSON.img, MaxWidth: '679', MaxHeight: '605'}).appendTo('#result-img')
            steps.second();
          },
          error: function(response){
            var responseJSON = $.parseJSON(response.responseText);
            var feedback_form_action = responseJSON['request_feedback_url'];
            $('#form-ask').attr("action", feedback_form_action);
            $('<img>', {src: responseJSON.img, MaxWidth: '679', MaxHeight: '605'}).appendTo('#result-img')
            steps.second();
          }});
				pos = 0;
			}
		};

	} else {

		saveCB = function(data) {
			image.push(data);
			
			pos+= 4 * 320;
			
			if (pos >= 4 * 320 * 240) {
				$.post("/outfit/new", {type: "pixel", image: image.join('|')});
				pos = 0;
			}
		};
	}
  $('#capture-btn').on('click', function(){webcam.capture();});
    $("#camera").removeClass('hidden').webcam({
      width: 320,
      height: 240,
      mode: "callback",
      swffile: "/static/scripts/libs/jscam.swf",
      onTick: function() {},
      onSave: saveCB,
      onCapture: function(data) {
        webcam.save();
        console.log(data);
      },
    debug: function(name, message) {console.log('debug:' + name + ' - ' + message)},
      onLoad: function() {}
    });
  });

  var uploader = new qq.FileUploaderBasic({
    element: document.getElementById('uploader'),
    allowedExtensions: ['jpg', 'jpeg', 'png', 'gif'],
    sizeLimit: 8000000,
    action: '/outfit/new',
    multiple: false,
    button:  document.getElementById('uploader'),
    onComplete: function(id, fileName, responseJSON){
      var feedback_form_action = responseJSON['request_feedback_url'];
      $('#form-ask').attr("action", feedback_form_action);
      $('<img>', {src: responseJSON.img, MaxWidth: '679', MaxHeight: '605'}).appendTo('#result-img')
      steps.second();
    },
  });
  $('.rateit').bind('rated', function(){ $('#rating').val($(this).rateit('value')); })
  $("#fb-friends").mCustomScrollbar();
})
