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
