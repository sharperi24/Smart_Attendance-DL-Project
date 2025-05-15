navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    document.getElementById("video").srcObject = stream;
  })
  .catch(err => console.error("Camera error:", err));

function captureAndSend() {
  const video = document.getElementById("video");
  const canvas = document.createElement("canvas");
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  canvas.getContext("2d").drawImage(video, 0, 0);

  const dataUrl = canvas.toDataURL("image/jpeg");

  fetch("/verify", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ image: dataUrl })
  })
    .then(res => res.json())
    .then(data => {
      document.getElementById("status").textContent = data.message;
      if (data.status === "success" || data.status === "fail") {
        setTimeout(() => window.location.reload(), 2000);
      }
    })
    .catch(err => console.error("Error sending image:", err));
}
