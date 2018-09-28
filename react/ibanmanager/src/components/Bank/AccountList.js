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

class AccountList extends Component {

    constructor(props) {
        super(props);

        console.log('INICIANDO PROPS');
        console.log(props);

        this.state = {
            // user: props.user,
            // accounts: props.accounts
            user: '',
            accounts: []
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

  componentDidMount() {

  }

    componentWillReceiveProps(nextProps) {
        if (this.props.user !== nextProps.user) {
            let state = {
                user: nextProps.user,
                accounts: nextProps.accounts
            }
            this.setState(state);
        }
        console.log('RECEIVE PROPS');
        console.log(nextProps);
    }

    handleSubmit = (e, message) => {
        e.preventDefault();
    };


    handleChange = (e) => {
        let newState = {};
        newState[e.target.name] = e.target.value;
        this.setState(newState)
    };


  render() {
    return (
        <div>
       <Paper>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>UUID</TableCell>
                <TableCell>IBAN</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {this.state.accounts.map((account, index) => {
                return (
                  <TableRow key={index}>
                    <TableCell component="th" scope="row">
                      {account.id}
                    </TableCell>
                      <TableCell>{account.iban}</TableCell>

                  </TableRow>
                );
              })}
            </TableBody>
          </Table>
        </Paper>
        </div>
    );
  }
}

export default AccountList;
