// src/SignUp.js
import React from "react";
import { Link, useNavigate } from "react-router-dom";
import "./Signup.css";

const SignUp = () => {
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    // could add sign-up logic here (API call, Firebase, etc.) if have time
    // on successful sign up, navigate to the home page:
    navigate("/home");
  };

  return (
    <div className="signup-container">
      {/* Left side: Text and Form */}
      <div className="signup-left">
        <h1>Sign Up</h1>
        <form onSubmit={handleSubmit}>
          <div className="name-fields">
            <input type="text" placeholder="First Name" required />
            <input type="text" placeholder="Last Name" required />
          </div>
          <input type="email" placeholder="Email" required />
          <input type="password" placeholder="Password" required />
          <button type="submit">Sign Up</button>
        </form>
        <div className="signup-footer">
          <hr className="divider" />
          <p>
            Already have an account? <Link to="/login">Log in here</Link>
          </p>
        </div>
      </div>

      {/* Right side: Image */}
      <div className="signup-right">
        <img src="/picture.png" alt="Sign Up" />
      </div>
    </div>
  );
};

export default SignUp;
