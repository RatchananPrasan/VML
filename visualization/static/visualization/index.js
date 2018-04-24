$(document).ready(function() {
  
  var parsedData = vis.network.convertDot(dotstring);


  var data = {
    nodes : parsedData.nodes,
    edges : parsedData.edges
  }

  var options = parsedData.options;

  var edge_on_opacity = 1;
  var edge_off_opacity = 0.1;

  options.edges = {
    color : {
      opacity : edge_off_opacity
    },
  };
  
  options.nodes = {
    borderWidth : 2,
    shape : "circle",
    fixed : {
      x : true,
      y : true
    }
  };
    
  options.layout = {
    hierarchical : {
      enabled : true,
      direction : "LR",
      levelSeparation : 750
    }
  };
  

  var container = document.getElementById("network");
  var network = new vis.Network(container, data, options);


  var setEdgeOpacity = function(network, edges, opacityVal) {
    for(var i = 0;i < edges.length;i++) {
      var edge = network.body.edges[edges[i]];
      edge.setOptions({
        color : {
          opacity : opacityVal
        }
      });
    }
  };

  // stroke_color can be rgba(r,g,b,a) or null
  var drawCanvas = function(canvas_id, width, height, rgba_vals, stroke_color) {
    var c = document.getElementById(canvas_id);
    var ctx = c.getContext("2d");

    var target_size_width = 250;
    var target_size_height = 250;

    $("#"+canvas_id).attr({
      "width" : target_size_width,
      "height" : target_size_height
    });

    if (stroke_color != null) {
      ctx.strokeStyle = stroke_color;
    }

    var x = 0;
    var y = 0;
    
    var ratio_width = target_size_width / width;
    var ratio_height = target_size_height / height;

    var rgba_vals_counter = 0;

    for(var row = 0; row < width; row++) {
      for(var col = 0; col < height; col++) {
        var r = rgba_vals[rgba_vals_counter++];
        var g = rgba_vals[rgba_vals_counter++];
        var b = rgba_vals[rgba_vals_counter++];
        var a = rgba_vals[rgba_vals_counter++];
        ctx.fillStyle = "rgba("+r+","+g+","+b+","+a+")";
        ctx.fillRect(x, y, ratio_width, ratio_height);
        if (stroke_color != null) {
          ctx.strokeRect(x, y, ratio_width, ratio_height);
        }
        x += ratio_width;
        }
      x = 0;
      y += ratio_height;
    }
  };

  var output_div = $("#output");

  network.on("selectNode", function(params) {
    setEdgeOpacity(network, params.edges, edge_on_opacity);

    var node_id = params.nodes[0];
    var json_data = node_data[node_id];

    output_div.empty();

    if (json_data["type"] == "convolution") {
      var html_val = `
                      <p><b>
                        Type : ` + json_data["type"] + `<br>
                        Activation : ` + json_data["activation"] + `<br>
                      </b></p>
                      `;
      output_div.append(`<div class="row"><div class="col-12">`+ html_val +`</div></div>`);
      
      for(var i = 0; i < json_data["filters"].length; i++) {
        var temp_id = "temp_id_" + i;
        output_div.append(`<div class="row justify-content-center" id="`+ temp_id +`"></div>`);
        var canvas_div_output = $("#"+temp_id);

        // Draw Input
        var input_canvas_id = "input_" + temp_id;
        canvas_div_output.append(`<div class="col-4"><h3>Input</h3><canvas id="`+ input_canvas_id +`"></canvas></div>`);
        var input_node_id = json_data["inputs"][i];
        var input_node_data = node_data[input_node_id];

        drawCanvas(input_canvas_id, 
          input_node_data["output_size"]["width"],
          input_node_data["output_size"]["height"],
          input_node_data["outputs"][0],
          null);

        // Draw Filter
        var filter_canvas_id = "filter_" + temp_id;
        canvas_div_output.append(`<div class="col-4"><h3>Filter</h3><canvas id="`+ filter_canvas_id +`"></canvas></div>`);
        drawCanvas(filter_canvas_id, 
          json_data["filter_size"]["width"],
          json_data["filter_size"]["height"],
          json_data["filters"][i],
          "rgb(220,220,220)");
        }

        // Draw Output
        var result_output_id = "result_output";
        output_div.append(`<div class="row justify-content-center" id="`+ result_output_id +`"></div>`);
        var canvas_div_output = $("#"+result_output_id);

        var output_canvas_id = "output_" + result_output_id;
        canvas_div_output.append(`<div class="col-8"><h3>Output</h3><canvas id="`+ output_canvas_id +`"></canvas></div>`);
        drawCanvas(output_canvas_id, 
          json_data["output_size"]["width"],
          json_data["output_size"]["height"],
          json_data["outputs"][0],
          null);
      
    } else if (json_data["type"] == "input") {
      var html_val = `
                      <p><b>
                        Type : ` + json_data["type"] + `<br>
                        Size : ` + json_data["output_size"]["width"] + "x" + json_data["output_size"]["height"] + `<br>
                      </b></p>
                      `;
      output_div.append(`<div class="row"><div class="col-12">`+ html_val +`</div></div>`);

      var temp_id = "temp_id_" + 0;
      output_div.append(`<div class="row justify-content-center" id="`+ temp_id +`"></div>`);
      var canvas_div_output = $("#"+temp_id);

      var input_canvas_id = "input_" + temp_id;
      canvas_div_output.append(`<div class="col-8"><h3>Output</h3><canvas id="`+ input_canvas_id +`"></canvas></div>`);
      drawCanvas(input_canvas_id, 
        json_data["output_size"]["width"],
        json_data["output_size"]["height"],
        json_data["outputs"][0],
        null);
    } else if (json_data["type"] == "pooling") {
      var html_val = `
                      <p><b>
                        Type : ` + json_data["type"] + `<br>
                        Size : ` + json_data["output_size"]["width"] + "x" + json_data["output_size"]["height"] + `<br>
                      </b></p>
                      `;
      output_div.append(`<div class="row"><div class="col-12">`+ html_val +`</div></div>`);

      var temp_id = "temp_id_" + 0;
      output_div.append(`<div class="row justify-content-center" id="`+ temp_id +`"></div>`);
      var canvas_div_output = $("#"+temp_id);

      // Draw Input
      var input_canvas_id = "input_" + temp_id;
      canvas_div_output.append(`<div class="col-3"><h3>Input</h3><canvas id="`+ input_canvas_id +`"></canvas></div>`);
      var input_node_id = json_data["inputs"][0];
      var input_node_data = node_data[input_node_id];

      drawCanvas(input_canvas_id, 
        input_node_data["output_size"]["width"],
        input_node_data["output_size"]["height"],
        input_node_data["outputs"][0],
        null);

      // Draw Output
      var output_canvas_id = "output_" + temp_id;
      canvas_div_output.append(`<div class="col-3"><h3>Output</h3><canvas id="`+ output_canvas_id +`"></canvas></div>`);
      drawCanvas(output_canvas_id, 
        json_data["output_size"]["width"],
        json_data["output_size"]["height"],
        json_data["outputs"][0],
        null);
    }
  });

  network.on("deselectNode", function(params) {
    setEdgeOpacity(network, params.previousSelection.edges, edge_off_opacity);
  });

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue =   decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

  var canvas,ctx;
  var canvas = document.getElementById('sketchpad');

    // If the browser supports the canvas tag, get the 2d drawing context for this canvas
    if (canvas.getContext)
        var ctx = canvas.getContext('2d');
    if (ctx) {
            canvas.addEventListener('mousedown', sketchpad_mouseDown, false);
            canvas.addEventListener('mousemove', sketchpad_mouseMove, false);
            window.addEventListener('mouseup', sketchpad_mouseUp, false);
    }
    
    
    var clear = function(){
          ctx.clearRect(0,0,280,280);
        };
    $('#clear').on("click",clear);

    var save = function(){


          dataURL = canvas.toDataURL("image/png");

          document.getElementById("out").value = dataURL;
          $.ajax({
            type: 'POST',
            url: 'savepic',
            data: { 
               imgBase64: dataURL
            },

          });
          

        };
    $('#save').on("click",save);


    // Variables to keep track of the mouse position and left-button status 
    var mouseX,mouseY,mouseDown=0;



    // Keep track of the old/last position when drawing a line
    // We set it to -1 at the start to indicate that we don't have a good value for it yet
    var lastX,lastY=-1;

    // Draws a line between the specified position on the supplied canvas name
    // Parameters are: A canvas context, the x position, the y position, the size of the dot
    function drawLine(ctx,x,y,size) {

        // If lastX is not set, set lastX and lastY to the current position 
        if (lastX==-1) {
            lastX=x;
      lastY=y;
        }

        // Let's use black by setting RGB values to 0, and 255 alpha (completely opaque)
        r=0; g=0; b=0; a=255;

        // Select a fill style
        ctx.strokeStyle = "rgba("+r+","+g+","+b+","+(a/255)+")";

        // Set the line "cap" style to round, so lines at different angles can join into each other
        ctx.lineCap = "round";
        //ctx.lineJoin = "round";


        // Draw a filled line
        ctx.beginPath();

  // First, move to the old (previous) position
        ctx.moveTo(lastX,lastY);

        // Now draw a line to the current touch/pointer position
        ctx.lineTo(x,y);

              // Set the line thickness and draw the line
              ctx.lineWidth = size;
              ctx.stroke();

              ctx.closePath();

        // Update the last position to reference the current position
        lastX=x;
        lastY=y;
          } 



    // Keep track of the mouse button being pressed and draw a dot at current location
    function sketchpad_mouseDown() {
        mouseDown=1;
        drawLine(ctx,mouseX,mouseY,12);
    }

    // Keep track of the mouse button being released
    function sketchpad_mouseUp() {
        mouseDown=0;

        // Reset lastX and lastY to -1 to indicate that they are now invalid, since we have lifted the "pen"
        lastX=-1;
        lastY=-1;
    }

    // Keep track of the mouse position and draw a dot if mouse button is currently pressed
    function sketchpad_mouseMove(e) { 
        // Update the mouse co-ordinates when moved
        getMousePos(e);

        // Draw a dot if the mouse button is currently being pressed
        if (mouseDown==1) {
            drawLine(ctx,mouseX,mouseY,12);
        }
    }

    // Get the current mouse position relative to the top-left of the canvas
    function getMousePos(e) {
        if (!e)
            var e = event;

        if (e.offsetX) {
            mouseX = e.offsetX;
            mouseY = e.offsetY;
        }
        else if (e.layerX) {
            mouseX = e.layerX;
            mouseY = e.layerY;
        }
     }
});

