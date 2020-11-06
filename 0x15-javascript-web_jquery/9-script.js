$.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (resp) {
  $('#hello').text(resp.hello);
});
