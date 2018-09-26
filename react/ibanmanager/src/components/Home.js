import React from "react";

const Home = ({ goog_auth }) => {
  return (
    <div>
      {(goog_auth.isAuthenticating)}
    </div>
  );
};

export default Home;
