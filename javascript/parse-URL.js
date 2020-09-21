var parseQueryString = function(url) {
  var urlParams = {};
  url.replace(
    new RegExp("([^?=&]+)(=([^&]*))?", "g"),
    function($0, $1, $2, $3) {
      urlParams[$1] = $3;
    }
  );
  return urlParams;
}

var urlToParse = location.search;  
var result = parseQueryString(urlToParse);  
console.info(JSON.stringify(result)); 
