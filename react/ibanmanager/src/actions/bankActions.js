const url = "http://127.0.0.1:8000";

const postingAccountData = () => ({ type: "POSTING_ACCOUNT_DATA" });
const updatingAccountData = () => ({ type: "UPDATING_ACCOUNT_DATA" });
const deletingAccount = () => ({ type: "DELETING_ACCOUNT_DATA" });
const receiveResponseListUserAccount = resp => ({ type: "RECEIVE_RESPONSE_LIST_ACCOUNT", resp });
const receiveResponseUserAccount = (resp, created) => ({ type: "RECEIVE_RESPONSE_ACCOUNT", resp, created });
const receiveErrorAccount = err => ({ type: "RECEIVE_ERROR_ACCOUNT", err });

function deleteAccount(uuid) {
    try {
      let token_conv =
        ( localStorage.getItem("goog_access_token_conv"));
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
  return async function(dispatch) {
    dispatch(postingAccountData());
    try {
      let token_conv =
        (await localStorage.getItem("goog_access_token_conv"));
      let response = await fetch(`${url}/api/v1/bank/account/`, {
        method: "POST",
        headers: {
          Accept: "application/json",
            "Content-Type": "application/json",
          Authorization: `Bearer ${token_conv}`
        },
        body: JSON.stringify(formData)
      });
      if (!response.ok) {
        throw new Error("Authorized Request Failed");
      }
      let responseJson = await response.json();
      return dispatch(receiveResponseUserAccount(responseJson, true));
    } catch (err) {
      dispatch(receiveErrorAccount(err));
    }
  };
}

function updateAccount(uuid, formData) {
  return async function(dispatch) {
    dispatch(updatingAccountData());
    try {
      let token_conv =
        (await localStorage.getItem("goog_access_token_conv"));
      let response = await fetch(`${url}/api/v1/bank/account/${uuid}/`, {
        method: "PATCH",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
          Authorization: `Bearer ${token_conv}`
        },
        body: JSON.stringify(formData)
      });
      if (!response.ok) {
        throw new Error("Authorized Request Failed");
      }
      let responseJson = await response.json();
      return dispatch(receiveResponseUserAccount(responseJson));
    } catch (err) {
      dispatch(receiveErrorAccount(err));
    }
  };
}

export { postAccount, updateAccount, deleteAccount };
