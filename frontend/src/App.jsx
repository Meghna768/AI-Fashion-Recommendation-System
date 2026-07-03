import { useState } from "react";
import axios from "axios";
import "./App.css";
function App() {
  const [file, setFile] = useState(null);
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const uploadImage = async () => {
    try {
      const formData = new FormData();

      formData.append("file", file);

      setLoading(true);

const response = await axios.post(
  "http://127.0.0.1:8000/upload-image",
  formData
);

setResults(response.data.recommendations);

setLoading(false);

      console.log(response.data);

      setResults(response.data.recommendations);

    } catch (error) {
      console.error(error);
      alert("Upload failed");
    }
  };

  return (
    <div
      style={{
        padding: "20px",
        fontFamily: "Arial"
      }}
    >
      <h1>Fashion Recommendation System</h1>

      <input
        type="file"
        onChange={(e) =>
          setFile(e.target.files[0])
        }
      />

      <button
        onClick={uploadImage}
        style={{
          marginLeft: "10px",
          padding: "8px 16px"
        }}
      >
        Upload
      </button>

      <div
        style={{
          display: "flex",
          flexWrap: "wrap",
          gap: "20px",
          marginTop: "30px"
        }}
      >
        {results.map((item, index) => (
          <div
            key={index}
            style={{
              width: "250px",
              border: "1px solid #ddd",
              borderRadius: "10px",
              padding: "10px",
              boxShadow: "0 2px 5px rgba(0,0,0,0.1)"
            }}
          >
            <img
              src={`http://127.0.0.1:8000/images/${item.image}`}
              alt={item.name}
              style={{
                width: "100%",
                height: "300px",
                objectFit: "cover",
                borderRadius: "10px"
              }}
              onError={(e) => {
                console.log(
                  "Failed image:",
                  item.image
                );
              }}
            />

            <h4>{item.name}</h4>

            <p>
              <strong>Brand:</strong>{" "}
              {item.brand}
            </p>

            <p>
              <strong>Price:</strong> ₹
              {item.price}
            </p>

            <p>
              <strong>Image:</strong>{" "}
              {item.image}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;