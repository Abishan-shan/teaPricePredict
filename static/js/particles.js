const canvas = document.getElementById("wave-canvas");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

window.addEventListener("resize", () => {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
});

const bubbles = [];
for (let i = 0; i < 25; i++) {
  bubbles.push({
    x: Math.random() * canvas.width,
    y: Math.random() * canvas.height,
    r: 3 + Math.random() * 5,
    speed: 0.3 + Math.random() * 0.5
  });
}

function drawWaves() {
  const time = Date.now() / 1000;


  const grad = ctx.createLinearGradient(0, 0, 0, canvas.height);
  grad.addColorStop(0, "#000");
  grad.addColorStop(1, "#111");
  ctx.fillStyle = grad;
  ctx.fillRect(0, 0, canvas.width, canvas.height);


  ctx.beginPath();
  ctx.moveTo(0, canvas.height * 0.85);
  for (let x = 0; x < canvas.width; x++) {
    const y =
      Math.sin((x + time * 120) / 80) * 20 +
      Math.cos((x + time * 60) / 100) * 10 +
      canvas.height * 0.9;
    ctx.lineTo(x, y);
  }
  ctx.lineTo(canvas.width, canvas.height);
  ctx.lineTo(0, canvas.height);
  ctx.closePath();
  ctx.fillStyle = "#FFD70020";
  ctx.fill();


  ctx.fillStyle = "#FFD70055";
  bubbles.forEach(b => {
    ctx.beginPath();
    ctx.arc(b.x, b.y, b.r, 0, Math.PI * 2);
    ctx.fill();
    b.y -= b.speed;
    if (b.y < -10) {
      b.y = canvas.height + 10;
      b.x = Math.random() * canvas.width;
    }
  });
}

function animate() {
  drawWaves();
  requestAnimationFrame(animate);
}

animate();