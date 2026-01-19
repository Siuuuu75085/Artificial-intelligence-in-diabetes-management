async function send() {
  const input = document.getElementById("msg");
  const chatBox = document.getElementById("chat-box");
  const message = input.value.trim();
  if (!message) return;

  chatBox.innerHTML += `<div class="message user">${message}</div>`;
  input.value = "";
  chatBox.scrollTop = chatBox.scrollHeight;

  const res = await fetch("/api/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message })
  });

  const data = await res.json();
  chatBox.innerHTML += `<div class="message bot">${data.reply}</div>`;
  chatBox.scrollTop = chatBox.scrollHeight;
}
