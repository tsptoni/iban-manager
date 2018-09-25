import React, { Component } from "react";
import { withStyles } from '@material-ui/core/styles';
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


const styles = theme => ({
  root: {
    width: '100%',
    marginTop: theme.spacing.unit * 3,
    overflowX: 'auto',
  },
});


class UserForm extends Component {

    constructor(props) {
      super(props);

      this.state = {
       first_name: '',
       last_name: '',
       email: '',
       subject: '',
       message: ''
      };

      this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
    }

    componentWillReceiveProps(nextProps) {
        this.setState(nextProps.users.currentUser);
    }

  componentDidMount() {
        this.props.requestUser(this.props.match.params.uuid);
  }



 handleChange = (e) => {
  let newState = {};

  newState[e.target.name] = e.target.value;

  this.setState(newState)
 };


 handleSubmit = (e, message) => {
  e.preventDefault();

  let formData = {
   formFirstName: this.state.first_name,
   formLastName: this.state.last_name,
   formEmail: this.state.email,
   formSubject: this.state.subject,
   formMessage: this.state.message
  };

  if (formData.formFirstName.length < 1 || formData.formLastName.length < 1 || formData.formEmail.length < 1 || formData.formSubject.length < 1 || formData.formMessage.length < 1) {
   return false
  }

     this.props.updateUser(this.props.match.params.uuid, formData);


  this.setState({
   firstName: '',
   lastName: '',
   email: '',
   subject: '',
   message: ''
  })
 };

  render() {
    return (
        <div>
            <form className='react-form' onSubmit={this.handleSubmit}>
       <Paper>

           {this.props.users.currentUser.id}<br/>
           {this.props.users.currentUser.first_name}<br/>
           {this.props.users.currentUser.last_name}<br/>
           {this.props.users.currentUser.email}<br/>
           {this.props.users.currentUser.type}


    <h1>Say Hi!</h1>

    <fieldset className='form-group'>
     <ReactFormLabel htmlFor='formFirstName' title='First Name:' />

     <input id='formFirstName' className='form-input' name='first_name' type='text' required onChange={this.handleChange} value={this.state.first_name} />
    </fieldset>
   <fieldset className='form-group'>
     <ReactFormLabel htmlFor='formLastName' title='Last Name:' />

     <input id='formLaneName' className='form-input' name='last_name' type='text' required onChange={this.handleChange} value={this.state.last_name} />
    </fieldset>

    <fieldset className='form-group'>
     <ReactFormLabel htmlFor='formEmail' title='Email:' />

     <input id='formEmail' className='form-input' name='email' type='email' required onChange={this.handleChange} value={this.state.email} />
    </fieldset>

    <fieldset className='form-group'>
     <ReactFormLabel htmlFor='formSubject' title='Subject:'/>

     <input id='formSubject' className='form-input' name='subject' type='text' required onChange={this.handleChange} value={this.state.subject} />
    </fieldset>

    <fieldset className='form-group'>
     <ReactFormLabel htmlFor='formMessage' title='Message:' />

     <textarea id='formMessage' className='form-textarea' name='message' required onChange={this.handleChange}></textarea>
    </fieldset>

    <div className='form-group'>
     <input id='formButton' className='btn btn-success' type='submit' placeholder='Create' />
    </div>


        </Paper>
            </form>
        </div>
    );
  }
}

export default UserForm;
