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
  
});