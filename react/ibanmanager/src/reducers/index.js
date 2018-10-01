import { combineReducers } from "redux";
import { routerReducer } from "react-router-redux";

import googleTokenReducer from "./googleAuthReducer";
import userReducer from "./userReducer";
import bankReducer from "./bankReducer";

const rootReducer = combineReducers({
  router: routerReducer,
  goog_auth: googleTokenReducer,
  users: userReducer,
  bank: bankReducer
});

export default rootReducer;
