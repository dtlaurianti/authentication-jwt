import { Navigate, Outlet } from "react-router-dom";
import useAuth from "../hooks/useAuth";

const RequireAuth = () => {
  const { auth } = useAuth();

  return auth?.token ? <Outlet /> : <Navigate to="/unauthorized" />;
};

export default RequireAuth;
