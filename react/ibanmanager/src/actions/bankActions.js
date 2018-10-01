const url = "http://127.0.0.1:8000";

function deleteAccount(uuid) {
    try {
      let token_conv =
        (localStorage.getItem("goog_access_token_conv"));
      let response = fetch(`${url}/api/v1/bank/account/${uuid}/`, {
        method: "DELETE",
        headers: {
          Accept: "application/json",
          Authorization: `Bearer ${token_conv}`
        }
      });
      return response;
    } catch (err) {
        return err;
    }
}

function postAccount(formData) {
    try {
      let token_conv =
        (localStorage.getItem("goog_access_token_conv"));
      let response =  fetch(`${url}/api/v1/bank/account/`, {
        method: "POST",
        headers: {
          Accept: "application/json",
            "Content-Type": "application/json",
          Authorization: `Bearer ${token_conv}`
        },
        body: JSON.stringify(formData)
      });
      return response;
    } catch (err) {
        return err;
    }
};

function updateAccount(uuid, formData) {
    try {
      let token_conv =
        (localStorage.getItem("goog_access_token_conv"));
      let response = fetch(`${url}/api/v1/bank/account/${uuid}/`, {
        method: "PATCH",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
          Authorization: `Bearer ${token_conv}`
        },
        body: JSON.stringify(formData)
      });
      return response;
    } catch (err) {
      return err;
    }
  };

export { postAccount, updateAccount, deleteAccount };
