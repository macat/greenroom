$(function(){
  $("#camera").webcam({
    width: 320,
    height: 240,
    mode: "callback",
    swffile: "/download/jscam_canvas_only.swf",
    onTick: function() {},
    onSave: function() {},
    onCapture: function() {},
    debug: function() {},
    onLoad: function() {}
  });
})
