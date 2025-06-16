// RedirectIfLoggedIn.js
import { Navigate } from "react-router-dom";

const LoginWrapper = ({children}) => {
  const token = localStorage.getItem("token");
//   const navigate = useNavigate();

  return token ? <Navigate to="/" /> : children;
};

export default LoginWrapper;
