import { Route, Redirect } from "react-router-dom";
import React from "react";

const checkAuth = () => {
  const goog_token = localStorage.getItem("goog_access_token_conv");
  if (!goog_token) {
    return false;
  }
  return true;
};

//If there is a google token in localStorage let them access /secret pages
const PrivateRoute = ({ component: Component, path: path }, ...rest) => (
  <Route
      path={path}
    {...rest}
    render={props => {
      return checkAuth() ? (
        <Component {...props} />
      ) : (
        <Redirect to={{ pathname: "/" }} />
      );
    }}
  />
);

// const AuthenticatedRoute = ({ component: Component }, ...rest) => (
//   <Route
//     {...rest}
//     render={props => {
//       return checkAuth() ? (
//         <Redirect to={{ pathname: "/secret" }} />
//       ) : (
//         <Component {...props} />
//       );
//     }}
//   />
// );

export { PrivateRoute };
