$(function(){
  var step = 1;

  var steps = {
    first: function() {
      step = 1;
      $('.step').addClass('hidden');
      $('#step-1').removeClass('hidden');
    },
    second: function() {
      step = 2;
      $('.step').addClass('hidden');
      $('#step-2').removeClass('hidden');
    },
    third: function() {
      step = 3;
      $('.step').addClass('hidden');
      $('#step-3').removeClass('hidden');
    }
  };
  steps.first();
  
  $('#ok').on('click', steps.third);
  $('#back').on('click', steps.first);

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
  var uploader = new qq.FileUploaderBasic({
    element: document.getElementById('uploader'),
    allowedExtensions: ['jpg', 'jpeg', 'png', 'gif'],
    sizeLimit: 8000000,
    action: '/outfit/new',
    button:  document.getElementById('uploader'),
    onComplete: function(id, fileName, responseJSON){
      var feedback_form_action = responseJSON['request_feedback_url'];
      $('#form-ask').attr("action", feedback_form_action);
      $('<img>', {src: responseJSON.img}).appendTo('#result-img')
      steps.second();
    },
  });
})
