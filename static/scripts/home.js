$(function(){
  var step = 1;

  var steps = {
    first: function() {
      $('#arrow').animate({left: '-420px'}, 500)
      step = 1;
      $('#placeholder-pic').removeClass('hidden');
      $('.step').addClass('hidden');
      $('#step-1').removeClass('hidden');
    },
    second: function() {
      step = 2;
      $('#placeholder-pic').addClass('hidden');
      $('.step').addClass('hidden');
      $('#step-2').removeClass('hidden');
    },
    third: function() {
      step = 3;
      $('#arrow').animate({left: '-25px'}, 500)
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
    multiple: false,
    button:  document.getElementById('uploader'),
    onComplete: function(id, fileName, responseJSON){
      var feedback_form_action = responseJSON['request_feedback_url'];
      $('#form-ask').attr("action", feedback_form_action);
      $('<img>', {src: responseJSON.img, width: '679', height: '605'}).appendTo('#result-img')
      steps.second();
    },
  });
  $('.rateit').bind('rated', function(){ $('#rating').val($(this).rateit('value')); })
})
