$(document).ready(function() {
  
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

  // stroke_color can be of rgba(r,g,b,a) or null
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
    setEdgeOpacity(network, params.edges, 1);

    var node_id = params.nodes[0];
    var json_data = JSON.parse( $("#"+node_id).val() );

    output_div.empty();

    if (json_data["type"] == "convolution") {
      var html_val = `
                      <p>
                        Type : ` + json_data["type"] + `<br>
                        Operation : ` + json_data["operation"] + `<br>
                        Activation : ` + json_data["activation"] + `<br>
                      </p>
                      `;
      output_div.append(`<div class="row"><div class="col-12">`+ html_val +`</div></div>`);
      
      for(var i = 0; i < json_data["filters"].length; i++) {
        var temp_id = "temp_id" + i;
        output_div.append(`<div class="row justify-content-center" id="`+ temp_id +`"></div>`);
        var canvas_div_output = $("#"+temp_id);

        // Draw Input
        var input_canvas_id = "input_" + temp_id;
        canvas_div_output.append(`<div class="col-3"><h3>Input</h3><canvas id="`+ input_canvas_id +`"></canvas></div>`);
        drawCanvas(input_canvas_id, 
          json_data["input_size"]["width"],
          json_data["input_size"]["height"],
          json_data["inputs"][i],
          null);

        // Draw Filter
        var filter_canvas_id = "filter_" + temp_id;
        canvas_div_output.append(`<div class="col-3"><h3>Filter</h3><canvas id="`+ filter_canvas_id +`"></canvas></div>`);
        drawCanvas(filter_canvas_id, 
          json_data["filter_size"]["width"],
          json_data["filter_size"]["height"],
          json_data["filters"][i],
          "rgb(220,220,220)");

        // Draw Output
        var output_canvas_id = "output_" + temp_id;
        canvas_div_output.append(`<div class="col-3"><h3>Output</h3><canvas id="`+ output_canvas_id +`"></canvas></div>`);
        drawCanvas(output_canvas_id, 
          json_data["output_size"]["width"],
          json_data["output_size"]["height"],
          json_data["outputs"][i],
          null);
      }
    }
  });

  network.on("deselectNode", function(params) {
    setEdgeOpacity(network, params.previousSelection.edges, 0);
  });

  /*
  var ratio = 20;
  var filter_size_width = 5;
  var filter_size_height = 5;

  var sample_filter = [ 	
                        0,0,0,0,
                        0,0,0,1,
                        0,0,0,1,
                        0,0,0,1,
                        0,0,0,0,
                        0,0,0,0,
                        0,0,0,1,
                        0,0,0,0,
                        0,0,0,1,
                        0,0,0,0,
                        0,0,0,0,
                        0,0,0,1,
                        0,0,0,1,
                        0,0,0,1,
                        0,0,0,0,
                        0,0,0,0,
                        0,0,0,0,
                        0,0,0,0,
                        0,0,0,1,
                        0,0,0,0,
                        0,0,0,0,
                        0,0,0,1,
                        0,0,0,1,
                        0,0,0,1,
                        0,0,0,0,
                      ];
                    
  var c = document.getElementById("output");
  var ctx = c.getContext("2d");
  ctx.strokeStyle = "rgb(220,220,220)";

  var x = 0;
  var y = 0;

  var sample_filter_counter = 0;

  for(var row = 0; row < filter_size_width; row++) {
    for(var col = 0; col < filter_size_height; col++) {
      var r = sample_filter[sample_filter_counter++];
      var g = sample_filter[sample_filter_counter++];
      var b = sample_filter[sample_filter_counter++];
      var a = sample_filter[sample_filter_counter++];
      ctx.fillStyle = "rgba("+r+","+g+","+b+","+a+")";
      ctx.fillRect(x, y, ratio, ratio);
      ctx.strokeRect(x, y, ratio, ratio);
      x += ratio;
      }
    x = 0;
    y += ratio;
    
  }
  */

  /*
  var alpha = document.getElementById("alpha_value").innerHTML;
  var size = document.getElementById("size").innerHTML;
  var alpha_lst = JSON.parse("[" + alpha + "]");
  var size_lst = JSON.parse("[" + size + "]");

  // console.log(alpha_lst[0][160]);
  var c = document.getElementById("myCanvas");
  var ctx2 = c.getContext("2d");
  var imgData = ctx2.createImageData(size_lst[0][0]*4, size_lst[0][1]*4);

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