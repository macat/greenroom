$(function(){
  $('#show-camera').on('click', function(){
    $('#uploader').hide();
    $("#camera").removeClass('hidden').webcam({
      width: 320,
      height: 240,
      mode: "save",
      swffile: "/static/scripts/libs/jscam.swf",
      onTick: function() {},
      onSave: function(s, data) {
        console.log(s);
        console.log(data);
        console.log(arguments);
        console.log('----------');
      },
      onCapture: function(data) {
        webcam.save('/outfit/new');
        console.log(data);
      },
    debug: function(name, message) {console.log('debug:' + name + ' - ' + message)},
      onLoad: function() {}
    });
  });
  var uploader = new qq.FileUploader({
    element: document.getElementById('uploader'),
    allowedExtensions: ['jpg', 'jpeg', 'png', 'gif'],
    sizeLimit: 8000000,
    action: '/outfit/new',
    onComplete: function(id, fileName, responseJSON){
    	var feedback_form_action = responseJSON['request_feedback_url'];
    	$('#form-ask').attr("action", feedback_form_action);
    	$('#form-ask').css("visibility", "visible");
    	$('#form-ask').show();
    },
  });
})
