import React, { Component } from "react";
import { deleteUser } from "../../actions/userActions";
import AccountList from "../../components/Bank/AccountList";
import Paper from '@material-ui/core/Paper';


class ReactFormLabel extends Component {
 constructor(props) {
  super(props)
 }

 render() {
  return(
   <label htmlFor={this.props.htmlFor}>{this.props.title}</label>
  )
 }
}


class UserForm extends Component {

    constructor(props) {
      super(props);

      this.state = {
       first_name: '',
       last_name: '',
       username: '',
       email: ''
      };

      this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
    }

    componentWillReceiveProps(nextProps) {

        if (this.props.match.params.uuid) {
            this.setState(nextProps.users.currentUser);
        }

        if (nextProps.users.created) {
            this.props.history.push(`/users/`);
        }
    }

  componentDidMount() {
      if (this.props.match.params.uuid) {
          this.props.requestUser(this.props.match.params.uuid);
      }
  }



 handleChange = (e) => {
  let newState = {};
  newState[e.target.name] = e.target.value;
  this.setState(newState)
 };


    handleDeleteBtn = (e) => {
        let response = deleteUser(this.props.match.params.uuid);
        response.then( response => {
            if (!response.ok) {
                alert(response.statusText);
            } else {
                alert('Deleted');
                this.props.history.push(`/users/`);
            }
            return response;
        });
    };


    showDeleteButton() {
        if (this.props.match.params.uuid) {
            return [
                <a className="btn btn-warning" onClick={this.handleDeleteBtn}>Delete</a>
            ];
        }
    }

    showAccounts() {
        if (this.props.users.currentUser) {
            return [
                <AccountList user={this.props.users.currentUser.id} accounts={this.props.users.currentUser.accounts} history={this.props.history} />
            ];
        }
    }


 handleSubmit = (e, message) => {
  e.preventDefault();

  let formData = {
   first_name: this.state.first_name,
   last_name: this.state.last_name,
   username: this.state.username,
   email: this.state.email
  };

  if (formData.first_name.length < 1 || formData.last_name.length < 1 || formData.email.length < 1 || formData.username.length < 1) {
   return false
  }

    if (this.props.match.params.uuid) {
        this.props.updateUser(this.props.match.params.uuid, formData);
    } else {
        this.props.postUser(formData);
    }


  this.setState({
   first_name: '',
   last_name: '',
   username: '',
   email: ''
  })
 };

  render() {
    return (
        <div>
            <form className='react-form' onSubmit={this.handleSubmit}>

                <Paper>

                    <fieldset className='form-group'>
                     <ReactFormLabel htmlFor='first_name' title='First Name:' />
                     <input id='first_name' className='form-input' name='first_name' type='text' required onChange={this.handleChange} value={this.state.first_name} />
                    </fieldset>

                   <fieldset className='form-group'>
                     <ReactFormLabel htmlFor='last_name' title='Last Name:' />
                     <input id='last_name' className='form-input' name='last_name' type='text' required onChange={this.handleChange} value={this.state.last_name} />
                    </fieldset>

                   <fieldset className='form-group'>
                     <ReactFormLabel htmlFor='username' title='Username:' />
                     <input id='username' className='form-input' name='username' type='text' required onChange={this.handleChange} value={this.state.username} />
                    </fieldset>

                    <fieldset className='form-group'>
                     <ReactFormLabel htmlFor='email' title='Email:' />
                     <input id='email' className='form-input' name='email' type='email' required onChange={this.handleChange} value={this.state.email} />
                    </fieldset>

                    <div className='form-group'>
                     <input id='formButton' className='btn btn-success' type='submit' placeholder='Create' />
                    {this.showDeleteButton()}
                    </div>

                </Paper>
            </form>
            <Paper>
                {this.showAccounts()}
            </Paper>
        </div>
    );
  }
}

export default UserForm;
