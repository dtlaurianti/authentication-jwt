import React from "react";
import { Link } from "react-router-dom";

const LandingPage = () => {

  return (
    <div>
      <h1>Welcome!</h1>
      <p>
        This is the landing page. You should be able to see this without logging
        in.  Please press the button below to navigate to the login page.
      </p>
      <Link to="/login">
        <button>Login</button>
        </Link>
    </div>
  );
};

export default LandingPage;
