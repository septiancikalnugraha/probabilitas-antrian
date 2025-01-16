from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def input_page():
    return '''
    <!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Studi Kasus Antrian Konter Handphone</title>
    <link rel="icon" href="https://cdn.jsdelivr.net/gh/PKief/vscode-material-icon-theme/icons/latex.svg">
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
    /* Reset dasar */
body, h1, h2, p, ul, li, a {
    margin: 0;
    padding: 0;
    list-style: none;
    text-decoration: none;
    box-sizing: border-box;
}

body {
    font-family: 'Roboto', sans-serif;
    background-color: #f6f9fc;
    color: #333;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    min-height: 100vh;
    padding: 20px;
}

h1, h2 {
    color: #0056b3;
    text-align: center;
    margin-bottom: 20px;
}

/* General container styling */
.container {
    display: flex;
    justify-content: space-between;
    margin: 20px;
}

/* Styling for the case-study section */
.case-study {
    width: 45%;
    background-color: #f4f4f4;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.case-study h2 {
    font-size: 24px;
    margin-bottom: 10px;
}

.case-study p {
    font-size: 16px;
    line-height: 1.6;
}

/* Styling for the form section */
.form {
    width: 45%;
    background-color: #f4f4f4;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.form h2 {
    font-size: 24px;
    margin-bottom: 20px;
}

.form label {
    font-size: 16px;
    display: block;
    margin-bottom: 8px;
}

.form input {
    width: 99%;
    padding: 8px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
}

.form button {
    width: 102%;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
}

.form button:hover {
    background-color: #45a049;
}

/* New CSS for improved styling */
.footer {
    text-align: center;
    margin-top: 40px;
    font-size: 14px;
    color: #888;
}

.footer a {
    color: #0056b3;
    text-decoration: none;
}

.footer a:hover {
    text-decoration: underline;
}

/* Ensuring the layout is responsive */
@media (max-width: 768px) {
    .container {
        flex-direction: column;
        align-items: center;
    }

    .case-study,
    .form {
        width: 80%;
        margin-bottom: 20px;
    }
}
 </style>
</head>
<body>
    <h1>Simulasi Antrian Konter Handphone</h1>
    <div class="container">
        <div class="case-study">
            <h2>Studi Kasus: Antrian Konter Handphone</h2>
            <p>Di sebuah konter handphone, rata-rata waktu antar kedatangan pelanggan adalah 5 menit, 
                sementara rata-rata waktu pelayanan oleh satu pelayan adalah 8 menit.</p>
            <p>
                Dengan menggunakan metode antrian, Anda bisa menghitung waktu tunggu rata-rata pelanggan 
                dan tingkat pemanfaatan pelayan untuk meningkatkan efisiensi konter.
            </p>
        </div>
        <div class="form">
            <h2>Masukkan Data</h2>
            <form action="/result" method="post">
                <label for="waktu_antar_kedatangan">Waktu Antar Kedatangan (menit):</label>
                <input type="number" step="0.01" name="waktu_antar_kedatangan" required>
                <label for="waktu_pelayanan">Waktu Pelayanan (menit):</label>
                <input type="number" step="0.01" name="waktu_pelayanan" required>
                <button type="submit">Hitung</button>
            </form>
        </div>
    </div>

    <div class="footer">
        <p>&copy; 2025 Simulasi Antrian Konter Handphone</p>
    </div>
</body>
</html>
    '''

@app.route('/result', methods=['POST'])
def result_page():
    try:
        # Ambil nilai input dari form
        waktu_antar_kedatangan = float(request.form['waktu_antar_kedatangan'])
        waktu_pelayanan = float(request.form['waktu_pelayanan'])

        # Validasi input
        if waktu_antar_kedatangan <= 0 or waktu_pelayanan <= 0:
            return '''
            <!DOCTYPE html>
            <html>
            <body>
                <h2>Kesalahan Input</h2>
                <p>Waktu antar kedatangan dan waktu pelayanan harus lebih besar dari 0.</p>
                <a href="/">Kembali ke Halaman Input</a>
            </body>
            </html>
            '''

        # Perhitungan parameter
        lambda_val = 1 / waktu_antar_kedatangan
        mu = 1 / waktu_pelayanan

        # Validasi kestabilan sistem
        if mu <= lambda_val / 2:
            return '''
            <!DOCTYPE html>
            <html>
            <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
            <body>
                <h2>Kesalahan Sistem</h2>
                <p>Sistem tidak stabil karena laju pelayanan terlalu rendah dibandingkan laju kedatangan.</p>
                <a href="/">Kembali ke Halaman Input</a>
            </body>
            </html>
            '''

        rho = lambda_val / (2 * mu)
        W = 1 / (mu - lambda_val / 2)
        Wq = (lambda_val) / (2 * mu * (mu - lambda_val / 2))

        # Tampilkan hasil
        return f'''
        <!DOCTYPE html>
<html>
<head>
    <title>Hasil Perhitungan</title>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <link rel="icon" href="https://cdn.jsdelivr.net/gh/PKief/vscode-material-icon-theme/icons/latex.svg">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
                .result-container {{
                    padding: 20px;
                    max-width: 600px;
                    margin: 50px auto;
                    background: #fff;
                    border-radius: 10px;
                    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
                    text-align: center;
                }}
                .result-container h1, .result-container p {{
                    margin: 10px 0;
                }}
                .result-container a {{
                    display: inline-block;
                    margin-top: 20px;
                    padding: 10px 20px;
                    background: #007bff;
                    color: #fff;
                    text-decoration: none;
                    border-radius: 5px;
                }}
                .result-container a:hover {{
                    background: #0056b3;
                }}
            </style>
</head>
<body>

    <h1><center>Hasil Perhitungan Antrian</h1>

    <div class="result-container">
        <p><strong>Langkah-langkah Perhitungan:</strong></p>
        <ol>
            <li>Hitung laju kedatangan \\( \\lambda \\):</li>
            <p>\\[ \\lambda = \\frac{{1}}{{\\text{{Waktu Antar Kedatangan}}}} = \\frac{{1}}{{{waktu_antar_kedatangan:.1f}}} = {lambda_val:.2f} \\]</p>

            <li>Hitung laju pelayanan \\( \\mu \\):</li>
            <p>\\[ \\mu = \\frac{{1}}{{\\text{{Waktu Pelayanan}}}} = \\frac{{1}}{{{waktu_pelayanan:.1f}}} = {mu:.3f} \\]</p>

            <li>Hitung tingkat pemanfaatan pelayan \\( \\rho \\):</li>
            <p>\\[ \\rho = \\frac{{\\lambda}}{{2 \\mu}} = \\frac{{{lambda_val:.2f}}}{{2 \\times {mu:.3f}}} = {rho:.3f} \\]</p>

            <li>Hitung waktu total dalam sistem \\( W \\):</li>
            <p>\\[ W = \\frac{{1}}{{\\mu - \\frac{{\\lambda}}{{2}}}} = \\frac{{1}}{{{mu:.3f} - \\frac{{{lambda_val:.2f}}}{{2}}}} = {W:.1f} \\] menit</p>

            <li>Hitung waktu tunggu dalam antrian \\( W_q \\):</li>
            <p>\\[ W_q = \\frac{{\\lambda^2}}{{2 \\mu (\\mu - \\frac{{\\lambda}}{{2}})}} = \\frac{{{lambda_val:.2f}}}{{2 \\times {mu:.3f} \\times \\left({mu:.3f} - \\frac{{{lambda_val:.2f}}}{{2}}\\right)}} = {Wq:.1f} \\] menit</p>
        </ol>

        <p><strong>Hasil Akhir:</strong></p>
        <p>Laju Kedatangan (\\( \\lambda \\)): \\( {lambda_val:.2f} \\) kedatangan/menit</p>
        <p>Laju Pelayanan (\\( \\mu \\)): \\( {mu:.3f} \\) pelayanan/menit</p>
        <p>Pemanfaatan Pelayan (\\( \\rho \\)): \\( {rho:.3f} \\)</p>
        <p>Waktu Total dalam Sistem (\\( W \\)): \\( {W:.1f} \\) menit</p>
        <p>Waktu Tunggu dalam Antrian (\\( W_q \\)): \\( {Wq:.1f} \\) menit</p>

        <a href="/" class="back-link">Kembali ke Halaman Input</a>
    </div>

</body>
</html>

        '''
    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}"

if __name__ == '__main__':
    # Gunakan semua IP lokal dan port 5000 atau lainnya
    app.run(host='0.0.0.0', port=5000, debug=True)
