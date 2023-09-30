import { Routes, Route } from "react-router-dom";
import "./App.css";
import LandingPage from "./components/LandingPage";
import LoginForm from "./components/LoginForm";
import Unauthorized from "./components/Unauthorized";
import Secret from "./components/Secret";
import RequireAuth from "./components/RequireAuth";

function App() {
  return (
    <>
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/login" element={<LoginForm />} />
      <Route path="/unauthorized" element={<Unauthorized />} />

      <Route element={<RequireAuth />}>
        <Route path="/secret" element={<Secret />} />
      </Route>

      <Route path="*" element={<h1>404 Not Found</h1>} />
    </Routes>
    </>
  );
}

export default App;
