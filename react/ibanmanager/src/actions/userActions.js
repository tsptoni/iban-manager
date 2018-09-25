const url = "http://127.0.0.1:8000";

const requestingUserData = () => ({ type: "SENDING_USER_DATA" });
const postingUserData = () => ({ type: "POSTING_USER_DATA" });
const updatingUserData = () => ({ type: "UPDATING_USER_DATA" });
const receiveResponseListUser = resp => ({ type: "RECEIVE_RESPONSE_LIST_USER", resp });
const receiveResponseUser = resp => ({ type: "RECEIVE_RESPONSE_USER", resp });
const receiveErrorUser = err => ({ type: "RECEIVE_ERROR_USER", err });

function requestUsers() {
  return async function(dispatch) {
    dispatch(requestingUserData());
    try {
      let token_conv =
        (await localStorage.getItem("goog_access_token_conv"));
      let response = await fetch(`${url}/api/v1/users/user/`, {
        method: "GET",
        headers: {
          Accept: "application/json",
          Authorization: `Bearer ${token_conv}`
        }
      });
      if (!response.ok) {
        throw new Error("Authorized Request Failed");
      }
      let responseJson = await response.json();
      responseJson = responseJson['results'];
      return dispatch(receiveResponseListUser(responseJson));
    } catch (err) {
      dispatch(receiveErrorUser(err));
    }
  };
}

function requestUser(uuid) {
  return async function(dispatch) {
    dispatch(requestingUserData());
    try {
      let token_conv =
        (await localStorage.getItem("goog_access_token_conv"));
      let response = await fetch(`${url}/api/v1/users/user/${uuid}/`, {
        method: "GET",
        headers: {
          Accept: "application/json",
          Authorization: `Bearer ${token_conv}`
        }
      });
      if (!response.ok) {
        throw new Error("Authorized Request Failed");
      }
      let responseJson = await response.json();
      return dispatch(receiveResponseUser(responseJson));
    } catch (err) {
      dispatch(receiveErrorUser(err));
    }
  };
}

function postUser() {
  return async function(dispatch) {
    dispatch(postingUserData());
    try {
      let token_conv =
        (await localStorage.getItem("goog_access_token_conv"));
      let response = await fetch(`${url}/api/v1/users/user/`, {
        method: "POST",
        headers: {
          Accept: "application/json",
          Authorization: `Bearer ${token_conv}`
        }
      });
      if (!response.ok) {
        throw new Error("Authorized Request Failed");
      }
      let responseJson = await response.json();
      return dispatch(receiveResponseUser(responseJson));
    } catch (err) {
      dispatch(receiveErrorUser(err));
    }
  };
}

function updateUser(uuid, formData) {
  return async function(dispatch) {
    dispatch(updatingUserData());
    try {
      let token_conv =
        (await localStorage.getItem("goog_access_token_conv"));
      let response = await fetch(`${url}/api/v1/users/user/${uuid}/`, {
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
        console.log('UPDATE USER');
        console.log(responseJson);
      return dispatch(receiveResponseUser(responseJson));
    } catch (err) {
      dispatch(receiveErrorUser(err));
    }
  };
}

export { requestUsers, requestUser, postUser, updateUser };
