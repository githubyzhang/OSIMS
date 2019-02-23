




















function updateTable() { 
	
	var array = [[1,2,3],[4,5,6],[7,8,9]];
    var content = "";
    array.forEach(function(row) {
        content += "<tr>";
        row.forEach(function(cell) {
            content += "<td>" + cell + "</td>" ;
        });
        content += "</tr>";
    });
    document.getElementById("devicelist").innerHTML = content;
    
//  document.getElementById("demo").innerHTML = "Hello JavaScript!";
//  
//  var array = [[1,2,3],[4,5,6],[7,8,9]];
//  
//	document.getElementById("1").innerHTML = ""; //Clear.
//	
//	for (i = 0; i < array.length; i++) { 
//	document.getElementById("1").innerHTML += "<tr>";
//		for (k = 0; k < array[0].length; k++) {
//		  document.getElementById("1").innerHTML += "<td>" + array[i][k] + "</td>" ;
//		}
//		document.getElementById("1").innerHTML += "</tr>";
//	  }
};

function processData(allText) {
    var allTextLines = allText.split(/\r\n|\n/);
    var headers = allTextLines[0].split(',');
    var lines = [];

    for (var i=1; i<allTextLines.length; i++) {
        var data = allTextLines[i].split(',');
        if (data.length == headers.length) {

            var tarr = [];
            for (var j=0; j<headers.length; j++) {
                tarr.push(headers[j]+":"+data[j]);
            }
            lines.push(tarr);
        }
    }
    // alert(lines);
}

