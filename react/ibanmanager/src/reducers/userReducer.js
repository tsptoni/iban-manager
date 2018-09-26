const initialState = {
	userListData: [],
	currentUser: {},
	err: null,
	isFetching: true
};

function userReducer(state, action) {
	if (!state) {
		state = initialState;
	}
	switch (action.type) {
		case "SENDING_USER_DATA":
			return { ...state, err: null, isFetching: true };
		case "POSTING_USER_DATA":
			return { ...state, err: null, isFetching: true };
		case "UPDATING_USER_DATA":
			return { ...state, err: null, isFetching: true };
		case "RECEIVE_RESPONSE_LIST_USER":
			return { ...state, userListData: action.resp, isFetching: false };
		case "RECEIVE_RESPONSE_USER":
			return { ...state, currentUser: action.resp, isFetching: false };
		case "RECEIVE_ERROR_USER":
			return { ...state, err: action.err, isFetching: false };
		default:
			return state;
	}
}

export default userReducer;
