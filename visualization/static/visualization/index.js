$(document).ready(function() {
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
          ctx.clearRect(0,0,400,400);
        };
    $('#clear').on("click",clear);

    var save = function(){
          var imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
          var data = imageData.data;
          var draw_alpha_data=[];
          for (var i = 3; i < data.length; i+=4) {
            draw_alpha_data.push(data[i]);
          }
          document.getElementById('myField').value = draw_alpha_data;
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

    


  var dotstring = $("#dotstring").val();
  var parsedData = vis.network.convertDot(dotstring);


  var data = {
    nodes : parsedData.nodes,
    edges : parsedData.edges
  }

  var options = parsedData.options;

  options.edges = {
    color : {
      opacity : 0
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
      direction : "LR"
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

  network.on("selectNode", function(params) {
    setEdgeOpacity(network, params.edges, 1);

    var node_id = params.nodes[0];
    var json_data = JSON.parse( $("#"+node_id).val() );

    console.log(json_data["type"]);
  });

  network.on("deselectNode", function(params) {
    setEdgeOpacity(network, params.previousSelection.edges, 0);
  });

  /*
  var alpha = document.getElementById("alpha_value").innerHTML;
  var size = document.getElementById("size").innerHTML;
  var alpha_lst = JSON.parse("[" + alpha + "]");
  var size_lst = JSON.parse("[" + size + "]");

  // console.log(alpha_lst[0][160]);
  var c = document.getElementById("myCanvas");
  var ctx2 = c.getContext("2d");
  var imgData = ctx2.createImageData(size_lst[0][0]*4, size_lst[0][1]*4);

<<<<<<< HEAD
  
=======
  var rgba_index = 1;
  var alpha_index = 0;
  var check =0;
  for (var i = 0; i < imgData.data.length; i+=1) {
      if (rgba_index==4) {
        imgData.data[i] = alpha_lst[0][alpha_index ]*255;
        rgba_index=1;
        if (check==4) {
          check=0;
          alpha_index +=1;
        }
        check +=1;
      }
      else{
        imgData.data[i] = 0;
        rgba_index+=1;
      }   
  }

  ctx2.putImageData(imgData, 0, 0);
  */
});

