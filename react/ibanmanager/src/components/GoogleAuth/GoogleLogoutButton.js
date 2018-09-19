import React, { Component } from "react";
import { GoogleLogout } from "react-google-login";

import gapi from "gapi-client";

class GoogleLogoutButton extends Component {
  componentWillMount() {
    gapi.load("auth2", () => {
      this.auth2 = gapi.auth2.init({
        client_id:
          "361462617390-ccs35t8svmjdpt1k1kj5b91l9337hi25.apps.googleusercontent.com"
      });
    });
  }

  render() {
    const signOut = dispatch => {
      var auth2 = gapi.auth2.getAuthInstance();
      auth2
        .signOut()
        .then(() => {
          console.log("User signed out.");
          localStorage.removeItem("goog_avatar_url");
          localStorage.removeItem("goog_name");
          localStorage.removeItem("goog_email");
        })
        .then(() => this.props.googleLogoutAction())
        .then(() => this.props.history.push("/"));
    };
    return (
      <GoogleLogout
        buttonText="Logout"
        onLogoutSuccess={signOut}
        className="loginBtn loginBtn--google"
      />
    );
  }
}

export default GoogleLogoutButton;
