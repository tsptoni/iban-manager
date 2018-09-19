import React, { Component } from "react";

class UserList extends Component {
  componentDidMount() {
    this.props.requestUsers();
  }
  render() {
    return (
      <div>
        {this.props.users.userData.map((user, index) => {
          return (
            <li key={index}>
              Name: {user.first_name} Last name: {user.last_name} Email: {user.email} Type: {user.type}
            </li>
          );
        })}
        <button
          onClick={() => this.props.requestUsers()}
          className="btn btn-success"
        >
          Load Users
        </button>
      </div>
    );
  }
}

export default UserList;
