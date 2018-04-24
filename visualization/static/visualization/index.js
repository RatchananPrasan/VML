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
                      <p>
                        Type : ` + json_data["type"] + `<br>
                        Activation : ` + json_data["activation"] + `<br>
                      </p>
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
                      <p>
                        Type : ` + json_data["type"] + `<br>
                        Size : ` + json_data["output_size"]["width"] + "x" + json_data["output_size"]["height"] + `<br>
                      </p>
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
                      <p>
                        Type : ` + json_data["type"] + `<br>
                        Size : ` + json_data["output_size"]["width"] + "x" + json_data["output_size"]["height"] + `<br>
                      </p>
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

});