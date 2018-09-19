import React from "react";
import { GoogleLogin } from "react-google-login";

const GoogleLoginButton = props => {
  const responseGoogleSuccess = response => {
    console.log(response);
    if (response.profileObj) {
      localStorage.setItem("goog_avatar_url", response.profileObj.imageUrl);
      localStorage.setItem("goog_name", response.profileObj.name);
      localStorage.setItem("goog_email", response.profileObj.email);
    }
    props.convertGoogleToken(response.Zi.access_token);
  };
  const responseGoogleFailure = response => {
    console.log(response);
  };

  return (
    <GoogleLogin
      clientId="361462617390-ccs35t8svmjdpt1k1kj5b91l9337hi25.apps.googleusercontent.com"
      buttonText="Login with Google"
      onSuccess={responseGoogleSuccess}
      onFailure={responseGoogleFailure}
      className="loginBtn loginBtn--google"
      prompt="select_account"
      redirectUri="http://localhost:3000/secret/"
    />
  );
};

export default GoogleLoginButton;
