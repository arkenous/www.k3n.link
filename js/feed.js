$(window).load(init());

function init() {
  read_github();
}


function read_github() {
  $.ajax({
    type: 'POST',
    url: 'cgi/feed.cgi',
    contentType: 'application/json',
    success: function(data) {
      var title = JSON.parse(data).title;
      console.log(title);
    }
  });
  return false;
}