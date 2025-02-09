// src/Login.js
import React from "react";
import { Link, useNavigate } from "react-router-dom";
import "./Login.css";

const Login = () => {
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    // could add login logic here (API call, Firebase, etc.) if have time
    // on successful login, navigate to the home page:
    navigate("/home");
  };

  return (
    <div className="login-container">
      {/* Left side: Text and Form */}
      <div className="login-left">
        <h1>Login</h1>
        <form onSubmit={handleSubmit}>
          <input type="email" placeholder="Email" required />
          <input type="password" placeholder="Password" required />
          <button type="submit">Log in</button>
        </form>
        <div className="login-footer">
          <hr className="divider" />
          <p>
            Don't have an account? <Link to="/">Sign Up Here</Link>
          </p>
        </div>
      </div>

      {/* Right side: Image */}
      <div className="login-right">
        <img src="/picture.png" alt="Login" />
      </div>
    </div>
  );
};

export default Login;
