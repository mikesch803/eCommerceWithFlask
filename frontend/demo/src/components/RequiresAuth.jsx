import React from "react";
import { Navigate, Outlet, useLocation } from "react-router-dom";

export default function RequiresAuth() {
  const token = localStorage.getItem("token");
  const location = useLocation();
  if (!token) {
    return <Navigate to="/" state={{ from: location }} replace />;
  }

  if (window.location.href.includes("login")) {
    return <Navigate to="/welcome" state={{ from: location }} replace />;
  }

  console.log("require auth page.....");

  return <Outlet />;
}
