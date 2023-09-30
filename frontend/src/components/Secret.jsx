import React, { useEffect, useState } from "react";
import { Navigate } from "react-router-dom";
import axios from "../api/axios";
import useAuth from "../hooks/useAuth";
import "./Secret.css";

const SECRET_URL = "/secret";
const LOGOUT_URL = "/logout";

const Secret = () => {
  const [submitted, setSubmitted] = useState(false);
  const [secret, setSecret] = useState("");

  const { auth } = useAuth();

  useEffect(() => {
    console.log('token: ', auth?.token);
    axios.get(SECRET_URL, {headers: {Authorization: `Bearer ${auth?.token}`}}).then((response) => {
        setSecret(response.data);
    });
  }, []);

  const handleClick = () => {
    setSubmitted(true);
  };

  if (submitted) {
    axios.post(LOGOUT_URL, {}, {headers: {Authorization: `Bearer ${auth?.token}`}})
    return <Navigate to="/login" />;
  }

  return (
    <div>
      <h1>Secure Page</h1>
      <p>
        This is a secure page. The server will verify your token before
        returning the secret below.
      </p>
      <h3>Top Secret</h3>
      <p className="line-breaks center-container">{secret.secret_data}</p>
      <button onClick={handleClick}>Logout</button>
    </div>
  );
};

export default Secret;
