function GerarQRCode(){
    var inputUsuario = document.querySelector('input').value;
    var GoogleChartAPI = 'https://chart.googleapis.com/chart?cht=qr&chs=350x350&chld=H&chl=';
    var conteudoQRCode = GoogleChartAPI + encodeURIComponent(inputUsuario);
    document.querySelector('#QRCodeImage').src = conteudoQRCode;
}
