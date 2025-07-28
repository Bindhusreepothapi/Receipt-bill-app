import React, { useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return;
    setLoading(true);
    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch("https://your-backend-url.onrender.com/upload/", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();
      setResult(data);
    } catch (error) {
      setResult({ error: "Upload failed" });
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Receipt OCR Uploader</h1>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
        accept="image/*,application/pdf"
      />
      <button onClick={handleUpload}>Upload</button>

      {loading && <p>Processing...</p>}

      {result && (
        <div className="result">
          <h3>Parsed Receipt Data:</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
