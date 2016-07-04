$(window).load(init());

function init() {
  read_feeds();
}


function read_feeds() {
  $.ajax({
    type: 'POST',
    url: 'cgi/feed.cgi',
    contentType: 'application/json',
    success: function(data) {
      $('.rss_contents').empty();
      // Read GitHub's feed
      var github = data.github;
      for (var i = 0; i < github.length; i++) {
        $('#github_rss').append(github[i].summary);
        $('#github_rss').append('<a href="'+github[i].link+'" target="_blank">Link is here</a>');
        $('#github_rss').append('<hr class="hr-split" size="1" wigth="75%" align="center" noshade>');
      }
      disable_click_on_github();

      // Read Hatenablog's feed
      var tech = data.tech;
      for (var i = 0; i < tech.length; i++) {
        $('#tech_rss').append('<p>'+tech[i].published+'</p>');
        $('#tech_rss').append('<a href="'+tech[i].link+'" target="_blank">'+tech[i].title+'</a>');
        $('#tech_rss').append('<hr class="hr-split" size="1" wigth="75%" align="center" noshade>');
      }

      // Read Qiita's feed
      var qiita = data.qiita;
      for (var i = 0; i < qiita.length; i++) {
        $('#qiita_rss').append('<p>'+qiita[i].published+'</p>');
        $('#qiita_rss').append('<a href="'+qiita[i].link+'" target="_blank">'+qiita[i].title+'</a>');
        $('#qiita_rss').append('<hr class="hr-split" size="1" wigth="75%" align="center" noshade>');
      }
    }
  });
  return false;
}

function disable_click_on_github() {
  $(".title a").on("click", function(event) {
    event.preventDefault();
  });
  $(".details a").on("click", function(event) {
    event.preventDefault();
  });
}
