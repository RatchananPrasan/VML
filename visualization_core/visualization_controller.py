
class VisualizationController():

    def visualize(self, model_file_path, input_file_path):
        result = {}

        result["data"] = self._get_data()
        result["dotstring"] = self._get_dotstring()
        
        return result

    # returns dictionary with key being id of node or edges and value is its string JSON
    def _get_data(self):
        return {
            "0" : """
                {
                    "type" : "input"
                }
            """,
            "1" : """
                {
                    "type" : "convolution"
                }
            """,
            "2" : """
                {
                    "type" : "convolution"
                }
            """,
            "3" : """
                {
                    "type" : "pooling"
                }
            """,
            "4" : """
                {
                    "type" : "pooling"
                }
            """,
            "5" : """
                {
                    "type" : "dense"
                }
            """,
            "6" : """
                {
                    "type" : "dense"
                }
            """,
            "7" : """
                {
                    "type" : "dense"
                }
            """,
            "8" : """
                {
                    "type" : "dense"
                }
            """,
        }

    def _get_dotstring(self):
        return """
                    dinetwork {
                        0 [ level=1 ];
                        1 [ level=2 ];
                        2 [ level=2 ];
                        3 [ level=3 ];
                        4 [ level=3 ];
                        5 [ level=4 ];
                        6 [ level=4 ];
                        7 [ level=4 ];
                        8 [ level=4 ];
                        0 -> 1 [ id=e0 ];
                        0 -> 2 [ id=e1 ];
                        1 -> 3 [ id=e2 ];
                        2 -> 4 [ id=e3 ];
                        3 -> 5 [ id=e4 ];
                        3 -> 6 [ id=e5 ];
                        3 -> 7 [ id=e6 ];
                        3 -> 8 [ id=e7 ];
                        4 -> 5 [ id=e8 ];
                        4 -> 6 [ id=e9 ];
                        4 -> 7 [ id=e10 ];
                        4 -> 8 [ id=e11 ];
                      }
                """