var url = 'json/data.json', // az adatlapokat tartalmazo json elerhetosege az index.html-hez kepest
    data;

getPDF();


function getPDF() {
    $.getJSON(url, function(d) {
        data = d;
        clickForLinks();
    });
}


function clickForLinks() {
    $('button').click(function() {
        var item = getRandomItem(data)
            pdf_url = item.pdf_url,
            person_url = item.person_url,
            name = item.name,
            google_url = 'https://docs.google.com/viewer?embedded=true&url=' + encodeURIComponent(pdf_url);

        $('body').addClass('small');
        $('#frames').addClass('show');
        $('#person').text(name);
        $('#person').attr('href', person_url);
        $('#link').attr('src', google_url);
    });
}


function getRandomItem(data) {
    var keys = Object.keys(data);
    var key = keys[Math.floor(Math.random() * keys.length)];
    return data[key];
}
