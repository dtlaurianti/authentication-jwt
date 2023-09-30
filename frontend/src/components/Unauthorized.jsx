import React, { useState } from "react";
import { Navigate } from "react-router-dom";

const Unauthorized = () => {
  const [submitted, setSubmitted] = useState(false);

  const handleClick = () => {
    setSubmitted(true);
  };

  if (submitted) return <Navigate to="/login" />;
  return (
    <div>
      <h1>Unauthorized Access</h1>
      <p>Please login to access this page.</p>
      <button onClick={handleClick}>Login</button>
    </div>
  );
};

export default Unauthorized;
