import { requestUsers, deleteUser } from "../../actions/userActions";
import UserList from "../../components/User/UserList";

import { connect } from "react-redux";

function mapStateToProps(state) {
  return {
    users: state.users
  };
}

function mapDispatchToProps(dispatch) {
  return {
    requestUsers: () => dispatch(requestUsers()),
    deleteUser: (uuid) => dispatch(deleteUser(uuid)),
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(UserList);
