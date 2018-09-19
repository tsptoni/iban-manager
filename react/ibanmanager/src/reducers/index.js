import { combineReducers } from "redux";
import { routerReducer } from "react-router-redux";

import googleTokenReducer from "./googleAuthReducer";
import userReducer from "./userReducer";

const rootReducer = combineReducers({
  router: routerReducer,
  goog_auth: googleTokenReducer,
  users: userReducer
});

export default rootReducer;
