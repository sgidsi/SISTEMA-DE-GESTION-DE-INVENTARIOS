import { useState } from "react";

export default function Login() {
  const [usuario, setUsuario] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Intentando iniciar sesión con:", usuario, password);
    // Luego aquí llamaremos al backend
  };

  return (
    <div style={{ width: "100%", height: "100vh", display: "flex", justifyContent: "center", alignItems: "center", background: "#f4f4f4" }}>
      <form onSubmit={handleSubmit} style={{ background: "#fff", padding: "2rem", borderRadius: "8px", width: "320px", boxShadow: "0 0 10px rgba(0,0,0,0.1)" }}>
        <h2 style={{ marginBottom: "1rem", textAlign: "center" }}>Iniciar Sesión</h2>

        <label>Usuario o Email:</label>
        <input
          type="text"
          value={usuario}
          onChange={(e) => setUsuario(e.target.value)}
          required
          style={{ width: "100%", padding: "8px", margin: "5px 0 15px 0" }}
        />

        <label>Contraseña:</label>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
          style={{ width: "100%", padding: "8px", margin: "5px 0 20px 0" }}
        />

        <button type="submit" style={{ width: "100%", padding: "10px", cursor: "pointer" }}>
          Ingresar
        </button>
      </form>
    </div>
  );
}
