$(window).load(init());

function init() {
  rnd();
}

function rnd() {
  $.ajax({
    type: 'POST',
    url: 'cgi/rnd.cgi',
    contentType: 'application/json',
    success: function(data) {
      $('#rnd_word').empty();
      var rnd_word = data.rnd_word;
      $('#rnd_word').text(rnd_word);
    }
  });
  return false;
}
