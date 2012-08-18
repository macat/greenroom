$(function(){
  $("#camera").webcam({
    width: 320,
    height: 240,
    mode: "save",
    swffile: "/static/scripts/libs/jscam.swf",
    onTick: function() {},
    onSave: function(data) {
      console.log(data);
    },
    onCapture: function(data) {
      webcam.save('/outfit/new');
      console.log(data);
    },
  debug: function(name, message) {console.log('debug:' + name + ' - ' + message)},
    onLoad: function() {}
  });
})
