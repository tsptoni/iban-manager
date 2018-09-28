import { requestUser, updateUser, postUser } from "../../actions/userActions";
import UserForm from "../../components/User/UserForm";

import { connect } from "react-redux";

function mapStateToProps(state) {
  return {
    users: state.users
  };
}

function mapDispatchToProps(dispatch) {
  return {
    requestUser: (uuid) => dispatch(requestUser(uuid)),
    updateUser: (uuid, formData) => dispatch(updateUser(uuid, formData)),
    postUser: (formData) => dispatch(postUser(formData))
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(UserForm);
