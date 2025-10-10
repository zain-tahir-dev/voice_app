const canvas = document.getElementById('waveCanvas');
const ctx = canvas.getContext('2d');

function drawWaves() {
  const width = canvas.width = canvas.offsetWidth;
  const height = canvas.height = canvas.offsetHeight;
  let t = 0;
  function animate() {
    ctx.clearRect(0, 0, width, height);
    ctx.beginPath();
    for (let x = 0; x < width; x++) {
      let y = height / 2 + Math.sin(x * 0.05 + t) * 30;
      ctx.lineTo(x, y);
    }
    ctx.strokeStyle = "#00ffcc";
    ctx.lineWidth = 2;
    ctx.stroke();
    t += 0.1;
    requestAnimationFrame(animate);
  }
  animate();
}
drawWaves();
