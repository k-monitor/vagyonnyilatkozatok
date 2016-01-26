var url = 'PDFadatlapok.json'; // az adatlapokat tartalmazo json elerhetosege, ugyanott, ahol a .py file

getPDF();

function getPDF() {
    $.getJSON(url, function(data) {
        $('button').click(function() {
            // dir a pdf-et tartalmazo konyvtar neve
            var randomItem = data[Math.floor(Math.random() * data.length)],
                randomFile = randomItem.paper,
                randomName = randomItem.name;

            $('#scan').addClass('show');
            $('#person').text(randomName);
            $('#link').attr('href', randomFile);
            $('#link').text('Lássuk ' + randomName + ' vagyonát!');
        });
    });
}


$('form').bind('submit', function(e) {
    alert();
});
