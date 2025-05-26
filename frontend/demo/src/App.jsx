import {
  BrowserRouter as Router,
  Route,
  Routes,
  Link,
  Outlet,
} from "react-router-dom";
import Login from "./components/login/Login";
import Home from "./components/Home/Home";
import Welcome from "./components/Welcome/Welcome";
import RequiresAuth from "./components/RequiresAuth";
import Header from "./components/Header";
import LoginWrapper from "./components/login/LoginWrapper";
import Register from "./components/Register/Register";
function App() {
  // const token = localStorage.getItem("token ");

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>React + Flask App</h1>
      <Router>
        <Routes>
          <Route
            element={
              <>
                <Header />
                <Outlet />
              </>
            }
          >
            <Route path="/" element={<Home />} />

            <Route
              path="/login"
              element={
                <LoginWrapper>
                  <Login />
                </LoginWrapper>
              }
            />
            <Route path="/register" element={<Register />} />
            <Route element={<RequiresAuth />}>
              <Route path="/welcome" element={<Welcome />} />
            </Route>
          </Route>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
