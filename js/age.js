$(window).load(init());

function init() {
  age();
}

function age() {
  $.ajax({
    type: 'POST',
    url: 'cgi/age.cgi',
    contentType: 'application/json',
    success: function(data) {
      $('#age').empty();
      var age = data.age;
      $('#age').text(age);
    }
  });
  return false;
}