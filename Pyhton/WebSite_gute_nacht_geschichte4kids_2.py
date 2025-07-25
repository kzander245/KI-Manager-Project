<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Gute-Nacht-Geschichten4KIDS</title>
  <style>
    body, html {
      margin: 0;
      padding: 0;
      font-family: 'Comic Sans MS', cursive, sans-serif;
      background: linear-gradient(to bottom, #d0eaff, #ffffff);
      color: #333;
      height: 100%;
    }
    .slideshow-container {
      position: relative;
      width: 100%;
      height: 100vh;
      overflow: hidden;
    }
    .slide {
      position: absolute;
      width: 100%;
      height: 100%;
      background-size: cover;
      background-position: center;
      opacity: 0;
      transition: opacity 1s ease-in-out;
    }
    .slide.active {
      opacity: 1;
    }
    h1 {
      position: absolute;
      top: 20px;
      width: 100%;
      text-align: center;
      font-size: 3em;
      color: #fff;
      text-shadow: 2px 2px 8px #000;
      z-index: 10;
    }
    .stories {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 30px;
      padding: 40px 20px;
      background: #ffffff;
    }
    .story {
      width: 250px;
      border-radius: 15px;
      overflow: hidden;
      box-shadow: 0 4px 8px rgba(0,0,0,0.2);
      background: #fff;
      transition: transform 0.3s;
    }
    .story:hover {
      transform: scale(1.05);
    }
    .story img {
      width: 100%;
      height: 180px;
      object-fit: cover;
    }
    .story-title {
      padding: 10px;
      font-size: 1.2em;
      background: #f4f4f4;
    }
    .story a {
      text-decoration: none;
      color: inherit;
    }
    footer {
      margin-top: 40px;
      padding: 10px;
      font-size: 0.9em;
      color: #777;
      background: #f0f0f0;
    }
  </style>
</head>
<body>
  <div class="slideshow-container">
    <div class="slide active" style="background-image: url('Coverbild_Zauberer_Kindgerecht_5.jpg');"></div>
    <div class="slide" style="background-image: url('Coverbild_Zauberer_Kindgerecht_2.jpg');"></div>
    <div class="slide" style="background-image: url('Coverbild_Zauberer_Kindgerecht_3.jpg');"></div>
    <h1>Gute-Nacht-Geschichten4KIDS</h1>
  </div>

  <main>
    <div class="stories">
      <div class="story">
        <a href="tiere-und-der-wald.html">
          <img src="Coverbild_der_Wald_und_die_Tiere_2.jpg" alt="Tiere und der Wald" />
          <div class="story-title">Tiere und der Wald</div>
        </a>
      </div>
      <div class="story">
        <a href="familie-im-garten.html">
          <img src="Coverbild_Familie_im_Garten_3.jpg" alt="Die Familie im Garten" />
          <div class="story-title">Die Familie im Garten</div>
        </a>
      </div>
      <div class="story">
        <a href="der-grosse-zoo.html">
          <img src="Coverbild_Der_grosse_Zoo_4.jpg" alt="Der große Zoo" />
          <div class="story-title">Der große Zoo</div>
        </a>
      </div>
    </div>
  </main>

  <footer>
    &copy; 2025 Gute-Nacht-Geschichten4KIDS
  </footer>

  <script>
    const slides = document.querySelectorAll('.slide');
    let currentSlide = 0;

    setInterval(() => {
      slides[currentSlide].classList.remove('active');
      currentSlide = (currentSlide + 1) % slides.length;
      slides[currentSlide].classList.add('active');
    }, 5000);
  </script>
</body>
</html>
