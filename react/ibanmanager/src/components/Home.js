import React from "react";
import { Redirect, withRouter } from "react-router-dom";

const Home = ({ goog_auth }) => {

    function userIsAuthenticated() {
        if (goog_auth.isAuthenticated) {
            return [
                <Redirect to="/users/">
                </Redirect>
            ];
        }
    }


  return (
    <div>
      {(goog_auth.isAuthenticating)}
      {userIsAuthenticated()}
    </div>
  );
};

export default Home;
