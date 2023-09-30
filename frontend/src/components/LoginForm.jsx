import React, { useState} from "react";
import { Navigate } from "react-router-dom"
import axios from "../api/axios";
import useAuth from "../hooks/useAuth";

const LOGIN_URL = "/login";

const LoginForm = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [submitted, setSubmitted] = useState(false);
    const { setAuth } = useAuth();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const formData = new FormData();
            formData.append("grant_type", "password");
            formData.append("username", username);
            formData.append("password", password);
            setUsername("");
            setPassword("");

            const response = await axios.post(LOGIN_URL, formData, {
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                },
            });
            console.log(JSON.stringify(response.data));

            const token = response?.data?.token;
            setAuth({ username, password, token });

            setSubmitted(true);
        } catch (error) {
            if (error.response?.status === 401) {
                alert("Invalid username or password");
            } else {
                alert("An error occurred. Please try again later.");
            }
        }
    };

    if (submitted) return (<Navigate to="/secret" />);

    return (
        <section>
            <h2>Login</h2>
            <form onSubmit={handleSubmit}>
                <label htmlFor="username">Username</label>
                <input
                    type="text"
                    id="username"
                    value={username}
                    autoComplete="off"
                    onChange={(e) => setUsername(e.target.value)}
                    required
                />
                <label htmlFor="password">Password</label>
                <input
                    type="password"
                    id="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />
                <button type="submit">Login</button>
            </form>
        </section>
    )
}
export default LoginForm;