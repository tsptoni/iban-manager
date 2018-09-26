import React from "react";
import ReactDOM from "react-dom";
import { createStore, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import logger from "redux-logger";
import { Provider } from "react-redux";
import { composeWithDevTools } from "redux-devtools-extension";
import { Route, Switch } from "react-router-dom";

import Home from "./containers/HomeContainer";
import Navbar from "./containers/NavbarContainer";
import UserList from "./containers/User/UserListContainer";
import UserForm from "./containers/User/UserFormContainer";
import { PrivateRoute } from "./customRoutes/ProtectedRoutes";
import rootReducer from "./reducers";
import auth_tokens_mw from "./customMiddleware/auth_tokens_mw";

/* Adding React-Router-Redux so I can use dispatch(push('/'))
    in the middleware
*/

import createHistory from "history/createBrowserHistory";
import { ConnectedRouter, routerMiddleware } from "react-router-redux";

// Create a history of your choosing (we're using a browser history in this case)
const history = createHistory();
const routMiddleware = routerMiddleware(history);

let store = createStore(
  rootReducer,
  composeWithDevTools(
    applyMiddleware(routMiddleware, auth_tokens_mw, thunk, logger)
  )
);

if (localStorage.getItem("goog_access_token_conv")) {
  store.dispatch({ type: "GOOG_AUTHENTICATE_ACTION" });
}


ReactDOM.render(
  <Provider store={store}>
    <ConnectedRouter history={history}>
      <div>
        <Navbar />
        <Switch>
          <Route exact path="/" component={Home} />
          <PrivateRoute exact path="/users" component={UserList} />
          <PrivateRoute path="/user/:uuid" component={UserForm} />
          <PrivateRoute path="/user" component={UserForm} />
        </Switch>
      </div>
    </ConnectedRouter>
  </Provider>,
  document.getElementById("root")
);
