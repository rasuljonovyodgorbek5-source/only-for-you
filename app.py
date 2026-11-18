
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#160b19">

<title>Only For You ❤️</title>

<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Poppins:wght@300;400;500;600&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    background: #160b19;
    color: white;
    font-family: 'Poppins', sans-serif;
    overflow-x: hidden;
}

.navbar {
    position: absolute;
    top: 0;
    width: 100%;
    padding: 25px 8%;
    display: flex;
    justify-content: space-between;
    z-index: 10;
}

.logo {
    font-family: 'Playfair Display', serif;
    font-size: 23px;
}

.logo span {
    color: #ff75a6;
}

.nav-text {
    color: #c9aebf;
    font-size: 11px;
    letter-spacing: 2px;
}

.hero {
    min-height: 100svh;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 110px 20px 70px;
    background:
    radial-gradient(ellipse at center, #52203f, transparent 65%),
    linear-gradient(140deg, #160b19, #291024);
}

.hero-content {
    max-width: 650px;
    animation: appear 1.5s ease;
}

.label {
    color: #ff8db4;
    letter-spacing: 4px;
    font-size: 11px;
    margin-bottom: 25px;
}

.heart {
    font-size: 95px;
    color: #ff75a6;
    animation: beat 2s infinite;
}

h1, h2 {
    font-family: 'Playfair Display', serif;
}

h1 {
    font-size: clamp(42px, 8vw, 75px);
    margin: 20px 0;
}

h1 span, h2 span {
    color: #ff8db4;
}

p {
    color: #d5bdcd;
    line-height: 2;
    font-size: 14px;
}

button {
    border: 1px solid #ff8db4;
    border-radius: 40px;
    padding: 15px 27px;
    margin-top: 30px;
    background: linear-gradient(120deg, #ed4b85, #a82d70);
    color: white;
    font-size: 14px;
    cursor: pointer;
    transition: .3s;
}

button:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 30px #ff3c8c65;
}

.scroll {
    color: #9c7b92;
    font-size: 10px;
    letter-spacing: 3px;
    margin-top: 65px;
}

section:not(.hero) {
    padding: 100px 8%;
    text-align: center;
}

.about h2, .qualities h2, .letter h2, .final h2 {
    font-size: clamp(30px, 5vw, 45px);
    margin-bottom: 25px;
}

.about p, .final p {
    max-width: 650px;
    margin: auto;
}

.decorative-heart {
    color: #ff7da9;
    font-size: 75px;
    margin-top: 30px;
}

.qualities {
    background: #21101f;
}

.cards {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 25px;
    margin-top: 50px;
}

.card {
    background: #32172e;
    border: 1px solid #71334f;
    border-radius: 20px;
    padding: 35px 20px;
    transition: .4s;
}

.card:hover {
    transform: translateY(-10px);
    border-color: #ff8db4;
}

.card .emoji {
    font-size: 40px;
    margin-bottom: 20px;
}

.card h3 {
    font-family: 'Playfair Display', serif;
    font-size: 22px;
    margin-bottom: 12px;
}

.letter {
    background: radial-gradient(circle, #4a1d3a, #160b19 75%);
}

.letter-box {
    max-width: 700px;
    margin: 40px auto;
    padding: 45px;
    border-radius: 25px;
    background: #ffffff0b;
    border: 1px solid #ff8db44a;
    box-shadow: 0 20px 70px #00000040;
}

.letter-box p {
    margin: 20px 0;
}

.letter-box h3 {
    color: #ff8db4;
    font-family: 'Playfair Display', serif;
    margin-top: 25px;
}

.final {
    background: #21101f;
}

#secret {
    display: none;
    max-width: 500px;
    margin: 40px auto;
    padding: 35px;
    border: 1px solid #ff8db4;
    border-radius: 20px;
    background: #ffffff0b;
    animation: appear 1s ease;
}

#secret .big {
    font-size: 50px;
    margin-bottom: 15px;
}

footer {
    text-align: center;
    padding: 45px 20px;
    background: #100711;
    color: #b997ac;
}

footer span {
    display: block;
    color: #ff70a4;
    font-size: 30px;
    margin-bottom: 12px;
}

footer small {
    font-size: 9px;
    letter-spacing: 3px;
}

.floating {
    position: fixed;
    bottom: -30px;
    pointer-events: none;
    z-index: 1;
    animation: floatUp 7s linear forwards;
}

@keyframes beat {
    50% { transform: scale(1.15); }
}

@keyframes appear {
    from {
        opacity: 0;
        transform: translateY(35px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes floatUp {
    to {
        transform: translateY(-110vh) rotate(360deg);
        opacity: 0;
    }
}

@media(max-width: 700px) {
    .navbar {
        padding: 20px;
    }

    .logo {
        font-size: 19px;
    }

    .nav-text {
        font-size: 8px;
    }

    .hero {
        padding: 100px 22px 50px;
    }

    .heart {
        font-size: 80px;
    }

    section:not(.hero) {
        padding: 75px 22px;
    }

    .cards {
        grid-template-columns: 1fr;
        gap: 18px;
    }

    .letter-box {
        padding: 25px 20px;
    }

    button {
        max-width: 100%;
    }
}

@media(max-width: 360px) {
    .nav-text {
        display: none;
    }
}
</style>
</head>

<body>

<nav class="navbar">
    <div class="logo">Only For You <span>♥</span></div>
    <div class="nav-text">A SPECIAL LITTLE WORLD</div>
</nav>

<section class="hero">

    <div class="hero-content">

        <div class="label">A LITTLE SURPRISE FOR YOU</div>

        <div class="heart">♡</div>

        <h1>Salom, <span>Go'zal!</span></h1>

        <p>
            Ba'zi insonlar hayotimizga shunchaki kelmaydi.
            Ular oddiy kunlarni ham unutilmas lahzalarga
            aylantiradi.
        </p>

        <button onclick="openLetter()">
            Senga atalgan maktub 💌
        </button>

        <div class="scroll">SCROLL TO EXPLORE ↓</div>

    </div>

</section>

<section class="about">

    <div class="label">01 — A LITTLE MESSAGE</div>

    <h2>Bu sahifa <span>sen uchun</span></h2>

    <p>
        Balki bu oddiy bir saytdek tuyular.
        Ammo uning har bir qismi alohida e'tibor
        bilan tayyorlandi. Chunki ba'zi insonlarga
        oddiy so'zlardan ko'ra ko'proq e'tibor loyiq.
    </p>

    <div class="decorative-heart">♡</div>

</section>

<section class="qualities">

    <div class="label">02 — BEAUTIFUL THINGS</div>

    <h2>Hayotdagi go'zalliklar</h2>

    <div class="cards">

        <div class="card">
            <div class="emoji">🌷</div>
            <h3>Go'zallik</h3>
            <p>Ba'zi narsalar izohga muhtoj emas.</p>
        </div>

        <div class="card">
            <div class="emoji">✨</div>
            <h3>Tabassum</h3>
            <p>Oddiy tabassum ham kunni o'zgartiradi.</p>
        </div>

        <div class="card">
            <div class="emoji">💗</div>
            <h3>E'tibor</h3>
            <p>Kichik e'tibor katta quvonch keltiradi.</p>
        </div>

    </div>

</section>

<section class="letter" id="letter">

    <div class="label">03 — A LETTER FOR YOU</div>

    <div class="letter-box">

        <div style="font-size:50px">💌</div>

        <h2>Aziz inson...</h2>

        <p>
            Bilasanmi, ba'zan inson biror kishiga
            aytmoqchi bo'lgan gaplarini so'z bilan
            ifodalashga qiynaladi.
        </p>

        <p>
            Shuning uchun bu kichik sahifani yaratdim.
            Bu yerda katta va'dalar yo'q, faqat samimiy
            tilaklar va yaxshi niyatlar bor.
        </p>

        <p>
            Hayoting doimo chiroyli lahzalarga,
            quvonchli kunlarga va unutilmas xotiralarga
            boy bo'lsin.
        </p>

        <p>
            Orzularing sari dadil qadam tashla.
            O'zingga bo'lgan ishonchingni yo'qotma.
        </p>

        <h3>Doimo baxtli bo'l! ❤️</h3>

    </div>

</section>

<section class="final">

    <div class="label">04 — ONE LAST THING</div>

    <h2>Bu hali hammasi emas...</h2>

    <p>Senga yana bir kichik xabarim bor.</p>

    <button onclick="showSecret()">
        Yashirin xabarni och ✨
    </button>

    <div id="secret">

        <div class="big">❤️</div>

        <h2>Sen qadrlisan!</h2>

        <p>
            Hech qachon o'zingni kam baholama.
            Dunyoda sening o'rning alohida.
            Eng yaxshi kunlar hali oldinda!
        </p>

        <div style="font-size:35px;margin-top:20px">
            🌹 🌷 🌹
        </div>

    </div>

</section>

<footer>
    <span>♥</span>
    <p>Made with love, just for you.</p>
    <small>ONLY FOR YOU © 2026</small>
</footer>

<script>

function openLetter() {
    document.getElementById("letter").scrollIntoView({
        behavior: "smooth"
    });
}

function showSecret() {

    let secret = document.getElementById("secret");

    secret.style.display = "block";

    secret.scrollIntoView({
        behavior: "smooth",
        block: "center"
    });

}

function createHeart() {

    let heart = document.createElement("div");

    let symbols = ["♥", "♡", "🌸", "✨"];

    heart.className = "floating";

    heart.innerHTML =
        symbols[Math.floor(Math.random() * symbols.length)];

    heart.style.left = Math.random() * 100 + "vw";

    heart.style.color = "#ff80aa";

    heart.style.fontSize =
        (12 + Math.random() * 20) + "px";

    heart.style.animationDuration =
        (5 + Math.random() * 4) + "s";

    document.body.appendChild(heart);

    setTimeout(() => {
        heart.remove();
    }, 9000);

}

setInterval(createHeart, 800);

</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
