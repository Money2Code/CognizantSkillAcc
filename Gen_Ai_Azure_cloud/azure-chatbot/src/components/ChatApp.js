import { useState } from "react";

export default function ChatApp() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) return;
    const userMessage = { role: "user", content: input };
    setMessages([...messages, userMessage]);
    setInput("");

    try {
        const response = await fetch("http://127.0.0.1:8000/api/chat/", {  // ✅ Correct API URL
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: input }),
          });

      const data = await response.json();
      setMessages([...messages, userMessage, { role: "ai", content: data.reply }]);
    } catch (error) {
      console.error("Error connecting to API:", error);
    }
  };

  return (
    <div style={{ backgroundColor: "#121212", color: "white", height: "100vh", display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center" }}>
      <h1>Radhe'S Chatbot</h1>
      <div style={{ width: "80%", maxHeight: "400px", overflowY: "auto", padding: "10px", border: "1px solid #444" }}>
        {messages.map((msg, index) => (
          <p key={index} style={{ backgroundColor: msg.role === "user" ? "#1E88E5" : "#333", padding: "10px", borderRadius: "5px", margin: "5px 0" }}>
            <strong>{msg.role === "user" ? "You" : "AI"}:</strong> {msg.content}
          </p>
        ))}
      </div>
      <div style={{ marginTop: "10px", display: "flex", width: "80%" }}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type a message..."
          style={{ flex: 1, padding: "10px", borderRadius: "5px", border: "1px solid #444", backgroundColor: "#222", color: "white" }}
        />
        <button onClick={sendMessage} style={{ marginLeft: "10px", padding: "10px", backgroundColor: "#1E88E5", color: "white", border: "none", borderRadius: "5px" }}>
          Send
        </button>
      </div>
    </div>
  );
}
