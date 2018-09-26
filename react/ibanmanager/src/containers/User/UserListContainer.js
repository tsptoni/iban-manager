import { requestUsers } from "../../actions/userActions";
import UserList from "../../components/User/UserList";

import { connect } from "react-redux";

function mapStateToProps(state) {
  return {
    users: state.users
  };
}

function mapDispatchToProps(dispatch) {
  return {
    requestUsers: () => dispatch(requestUsers())
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(UserList);
