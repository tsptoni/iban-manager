const initialState = {
	userAccountListData: [],
	currentUserAccount: {},
	err: null,
	isFetching: true,
    created: false
};

function bankReducer(state, action) {
	if (!state) {
		state = initialState;
	}
	switch (action.type) {
		case "POSTING_ACCOUNT_DATA":
			return { ...state, err: null, isFetching: true };
		case "UPDATING_ACCOUNT_DATA":
			return { ...state, err: null, isFetching: true };
		case "DELETING_ACCOUNT_DATA":
			return { ...state, err: null, isFetching: true };
		case "RECEIVE_RESPONSE_LIST_ACCOUNT":
			return { ...state, userAccountListData: action.resp, isFetching: false };
		case "RECEIVE_RESPONSE_ACCOUNT":
			return { ...state, currentUserAccount: action.resp, isFetching: false, created: action.created };
		case "RECEIVE_ERROR_ACCOUNT":
			return { ...state, err: action.err, isFetching: false };
		default:
			return state;
	}
}

export default bankReducer;
