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

  network.on("selectNode", function(params) {
    setEdgeOpacity(network, params.edges, 1);

    var node_id = params.nodes[0];
    var json_data = JSON.parse( $("#"+node_id).val() );

    console.log(json_data["type"]);
  });

  network.on("deselectNode", function(params) {
    setEdgeOpacity(network, params.previousSelection.edges, 0);
  });

  
  var alpha = document.getElementById("alpha_value").innerHTML;
  var size = document.getElementById("size").innerHTML;
  var alpha_lst = JSON.parse("[" + alpha + "]");
  var size_lst = JSON.parse("[" + size + "]");

  // console.log(alpha_lst[0][160]);
  
  var c = document.getElementById("myCanvas");
  var ctx = c.getContext("2d");
  var imgData = ctx.createImageData(size_lst[0][0], size_lst[0][1]);

  var rgba_index = 1;
  var alpha_index = 0;
  
  for (var i = 0; i < imgData.data.length; i += 1) {

      if (rgba_index == 4) {
        imgData.data[i] = alpha_lst[0][alpha_index] * 255;
        rgba_index = 1;
        alpha_index += 1;
      }

      else{
        imgData.data[i] = 0;
        rgba_index += 1;
      }   
  }
  
  ctx.putImageData(imgData, 0, 0);
  var ratio = 5;
  var c2 = document.getElementById("myCanvas2");
  var ctx2 = c2.getContext("2d");
 
  ctx2.scale(ratio, ratio);
  ctx2.drawImage(c,0,0,c2.width,c2.height);
});