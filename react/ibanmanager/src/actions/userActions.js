const url = "http://127.0.0.1:8000";

const requestingUserData = () => ({ type: "SENDING_USER_DATA" });
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
      return dispatch(receiveResponseUser(responseJson));
    } catch (err) {
      dispatch(receiveErrorUser(err));
    }
  };
}

export { requestUsers };
