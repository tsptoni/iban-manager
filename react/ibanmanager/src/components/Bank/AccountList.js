import React, { Component } from "react";
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import { postAccount, updateAccount, deleteAccount } from "../../actions/bankActions";

class AccountList extends Component {

    constructor(props) {
        super(props);

        this.state = {
            user: '',
            accounts: [],
            newAccount: {}
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleDelete = this.handleDelete.bind(this);
    }

  componentDidMount() {

  }

    componentWillReceiveProps(nextProps) {
        if (nextProps.user) {
            let state = {
                user: nextProps.user,
                accounts: nextProps.accounts
            }
            this.setState(state);
        }
    }

    handleSubmit = (index) => {
        let response = null;
        if (index !== null) {
            let account = this.state.accounts[index];
            response = updateAccount(account.id, {"iban": account.iban});
        } else {
            response = postAccount({"iban": this.state.newAccount, "owner": this.state.user});
        }

        response.then( response => {
                if (!response.ok) {
                    alert(response.statusText);
                } else {
                    alert('Success');
                }
                let data = response.json();
                return data;
            }).then( data => {
            if (index === null && response.ok) {
                let accounts = this.state.accounts;
                accounts.push(data);
                this.setState({
                    accounts,
                });
            }
            });
    };

    handleDelete = (index) => {
        let response = null;
        if (index !== null) {
            let account = this.state.accounts[index];
            response = deleteAccount(account.id)
            response.then( response => {
                if (!response.ok) {
                    alert(response.statusText);
                } else {
                    alert('Deleted');
                    let accounts = this.state.accounts;
                    accounts = accounts.filter(acc => acc.id !== account.id)
                    this.setState({
                        accounts,
                    });
                }
                return response;
            });
        }
    };

    handleChange = (index, newValue) => {

        if (index !== null) {
            const accounts = this.state.accounts;
            accounts[index].iban = newValue;

            this.setState({
                accounts,
            });
        } else {
            let newAccount = newValue;
            this.setState({newAccount});
        }
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
                <TableCell></TableCell>
                <TableCell></TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {this.state.accounts.map((account, index) => {
                return (
                  <TableRow key={index}>
                    <TableCell component="th" scope="row">
                      {account.id}
                    </TableCell>
                      <TableCell><input id={index} className='form-input w-60' type="text" onChange={(e) => this.handleChange(index, e.target.value)} defaultValue={account.iban}></input></TableCell>
                      <TableCell><button className="btn btn-success" onClick={() => this.handleSubmit(index)}>Change</button></TableCell>
                      <TableCell><button className="btn btn-danger" onClick={() => this.handleDelete(index)}>Delete</button></TableCell>
                  </TableRow>
                );
              })}
                <TableRow>
                    <TableCell component="th" scope="row">
                        Add new account
                    </TableCell>
                    <TableCell><input id='iban' className='form-input w-60' name='iban' type="text" onChange={(e) => this.handleChange(null, e.target.value)}></input></TableCell>
                    <TableCell><button className="btn btn-success" onClick={() => this.handleSubmit(null)}>Save</button></TableCell>
                    <TableCell></TableCell>
                </TableRow>
            </TableBody>
          </Table>
        </Paper>
        </div>
    );
  }
}

export default AccountList;
