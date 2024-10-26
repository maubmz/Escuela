function generateQRCode() {
    const text = document.getElementById("text").value;
    if (text.trim() === "") {
        alert("Por favor, ingresa un texto o URL.");
        return;
    }

    const qr = new QRious({
        element: document.getElementById("qrCanvas"),
        value: text,
        size: 200,
        background: '#fff',
        foreground: '#222'
    });
}
