import React, { Component } from "react";
import { withStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import {
  Redirect
} from 'react-router-dom';

const styles = theme => ({
  root: {
    width: '100%',
    marginTop: theme.spacing.unit * 3,
    overflowX: 'auto',
  },
  table: {
    minWidth: 700,
  },
});

class UserList extends Component {
  componentDidMount() {
    this.props.requestUsers();

  }


    goUserForm = property => event => {
        this.props.history.push(`/user/${property}`);
  };

  render() {
    return (
        <div>
       <Paper>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>Username</TableCell>
                <TableCell>First name</TableCell>
                <TableCell>Last name</TableCell>
                <TableCell>Email</TableCell>
                <TableCell>IBAN accounts</TableCell>
                <TableCell>Created by</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {this.props.users.userListData.map((user, index) => {
                return (
                  <TableRow key={index} onClick={this.goUserForm(user.id)}>
                    <TableCell component="th" scope="row">
                      {user.username}
                    </TableCell>
                      <TableCell>{user.first_name}</TableCell>
                    <TableCell>{user.last_name}</TableCell>
                    <TableCell>{user.email}</TableCell>
                    <TableCell>{user.accounts.map(function(name, i){
                        return <div>{name.iban}<br/></div>;
                  })}</TableCell>
                  <TableCell>
                      {user.created_by}
                  </TableCell>

                  </TableRow>
                );
              })}
            </TableBody>
          </Table>
        </Paper>
        <button
          onClick={() => this.props.requestUsers()}
          className="btn btn-success">
          Load Users
        </button>
        </div>
    );
  }
}

export default UserList;
