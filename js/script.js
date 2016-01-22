var url = 'PDFadatlapok.json';

getPDF();

function getPDF() {
    $.getJSON(url, function(data){
        $('button').click(function(){
            // dir a pdf-et tartalmazo konyvtar neve

            var dir = 'http://localhost:8000/pdf/',
                randomFile = data[Math.floor(Math.random()*data.length)],
                filePath = dir + randomFile;

                $('#frame').attr('src', 'https://docs.google.com/viewer?url=' + filePath + '&embedded=true');
            // $('.fallback').attr('href', filePath);
        })
    });
}
