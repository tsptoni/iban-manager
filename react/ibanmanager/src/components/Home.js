import React from "react";

const Home = ({ goog_auth }) => {
  return (
    <div>
      {(goog_auth.isAuthenticating)}
      <h1>Home Page</h1>
    </div>
  );
};

export default Home;
