const initialState = {
	userData: [],
	err: null,
	isFetching: false
};

function userReducer(state = initialState, action) {
	switch (action.type) {
		case "SENDING_USER_DATA":
			return { ...state, err: null, isFetching: true };
		case "RECEIVE_RESPONSE_USER":
			return { ...state, userData: action.resp, isFetching: false };
		case "RECEIVE_ERROR_USER":
			return { ...state, err: action.err, isFetching: false };
		default:
			return state;
	}
}

export default userReducer;
