import React, { useState, useEffect } from 'react';
import { Container, Form, Message, Transition } from 'semantic-ui-react';
import './CheckinForm.css';
import { validate, useWindowDimensions } from '../../utils';

const CheckinForm = ({ location, handlePath }) => {
  const initialFormValues = {
    confirmation: '',
    firstname: '',
    lastname: '',
    email: '',
    phone: ''
  };

  const initialState = {
    error: false,
    success: false,
    errMessage: '',
    btnDisable: false
  };

  /*
    useState hooks for setting and getting
    state of the component.
  */
  const [formValues, setFormValues] = useState({ ...initialFormValues });
  const [state, setState] = useState({ ...initialState });

  /*
    The useEffect hook that handles the path
    for the header to set active tab item
    through a function prop.
  */
  useEffect(() => {
    handlePath(location.pathname);
  }, [handlePath, location.pathname]);

  /*
    Hook made for getting current window dimensions.
  */
  const { width } = useWindowDimensions();

  /*
    Input change event handler that
    sets new values in formValue state
    on every change in input.
  */
  const handleChange = event => {
    const { name, value } = event.target;

    setFormValues({ ...formValues, [name]: value });
    setState({ ...state, btnDisable: false });
  };

  /*
    Event handler when input gets out of
    focus and checks form validation.
  */
  const handleBlur = event => {
    const { name, value } = event.target;

    const formValidation = validate(name, value);

    setState({
      ...formValues,
      ...formValidation,
      success: false
    });
  };

  /*
    Form submit event handler that checks
    the form input validation and sets the
    error and success alert messages.
  */
  const handleSubmit = async event => {
    for (const [name, value] of Object.entries(formValues)) {
      let formValidation = validate(name, value);

      if (formValidation.error) {
        setState({
          ...formValidation,
          success: false,
          btnDisable: true
        });

        return;
      }
    }

    setState({ ...initialState });

    const data = await fetchUrl();

    if (data.error) {
      console.log(data);
      setState({
        ...state,
        error: true,
        success: false,
        errMessage: data.error,
        btnDisable: true
      });
    } else if (data.status) {
      setState({
        ...initialState,
        error: false,
        success: true,
        errMessage: '',
        btnDisable: true
      });

      setFormValues({ ...initialFormValues });
    }
  };

  /*
    Function that makes a post ajax call to the
    backend to start a checkin task and returns the
    json data back.
  */
  const fetchUrl = async () => {
    // **TODO** add in the email and phone for notifications
    const { confirmation, firstname, lastname } = formValues;
    try {
      const response = await fetch('/checkin', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          confirmation: confirmation,
          firstname: firstname,
          lastname: lastname
        })
      });

      const data = await response.json();

      return data;
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <Container className="checkin-container">
      <Form
        size={width > 480 ? 'big' : 'small'}
        onSubmit={handleSubmit}
        success
        error
      >
        <Transition
          visible={state.success}
          animation="slide down"
          duration={50}
        >
          <Message
            size="mini"
            header="Success"
            content="Your task was sent successfully!"
            success
          />
        </Transition>

        <Transition visible={state.error} animation="slide up" duration={50}>
          <Message
            size="mini"
            header="Invalid"
            content={state.errMessage}
            error
          />
        </Transition>

        <Form.Field required>
          <label>Confirmation</label>
          <input
            name="confirmation"
            onChange={handleChange}
            onBlur={handleBlur}
            value={formValues.confirmation}
            placeholder="Confirmation"
          />
        </Form.Field>

        <Form.Field required>
          <label>First Name</label>
          <input
            name="firstname"
            onChange={handleChange}
            onBlur={handleBlur}
            value={formValues.firstname}
            placeholder="First Name"
          />
        </Form.Field>

        <Form.Field required>
          <label>Last Name</label>
          <input
            name="lastname"
            onChange={handleChange}
            onBlur={handleBlur}
            value={formValues.lastname}
            placeholder="Last Name"
          />
        </Form.Field>

        <Form.Field>
          <label>Email</label>
          <input
            name="email"
            onChange={handleChange}
            onBlur={handleBlur}
            value={formValues.email}
            placeholder="Optional Email Notification..."
          />
        </Form.Field>

        <Form.Field>
          <label>Phone</label>
          <input
            name="phone"
            onChange={handleChange}
            onBlur={handleBlur}
            value={formValues.phone}
            placeholder="Optional text notification..."
          />
        </Form.Field>

        <Form.Button
          color="blue"
          size="large"
          content="Submit"
          disabled={state.btnDisable}
        />
      </Form>
    </Container>
  );
};

export default CheckinForm;
