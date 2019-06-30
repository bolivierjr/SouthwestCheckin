import React, { useRef, useState, useEffect } from 'react';
import { Container, Form, Message } from 'semantic-ui-react';
import './CheckinForm.css';
import { validate, useWindowDimensions } from '../../utils';

const CheckinForm = () => {
  const initialState = {
    confirmation: '',
    firstname: '',
    lastname: '',
    email: '',
    phone: '',
    error: false,
    errMessage: ''
  };

  /*
      useState hook for setting and getting
      state of the component
    */
  const [state, setState] = useState({ ...initialState });

  const { width } = useWindowDimensions();

  /*
      A reference to the confirmation input
      element to focus on render.
    */
  const inputConf = useRef(null);

  useEffect(() => {
    inputConf.current.focus();
  }, []);

  /*
      On input change, the new input value 
      is set in state, by input element name.
    */
  const handleChange = event => {
    const { name, value } = event.target;

    setState({ ...state, [name]: value });
  };

  const handleSubmit = event => {
    event.preventDefault();
    const result = validate({ ...state });
    setState({ ...result });

    if (!result.error) {
      setState(initialState);
    }
    console.log(result);
  };

  return (
    <Container id="checkin-container">
      <Form
        size={width > 480 ? 'big' : 'small'}
        onSubmit={handleSubmit}
        error={state.error}
      >
        <Message
          size="mini"
          header="Invalid"
          content={state.errMessage}
          error
        />

        <Form.Field required>
          <label>Confirmation</label>
          <input
            ref={inputConf}
            name="confirmation"
            onChange={handleChange}
            value={state.confirmation}
            placeholder="Confirmation"
          />
        </Form.Field>

        <Form.Field required>
          <label>First Name</label>
          <input
            name="firstname"
            onChange={handleChange}
            value={state.firstname}
            placeholder="First Name"
          />
        </Form.Field>

        <Form.Field required>
          <label>Last Name</label>
          <input
            name="lastname"
            onChange={handleChange}
            value={state.lastname}
            placeholder="Last Name"
          />
        </Form.Field>

        <Form.Field>
          <label>Email</label>
          <input
            name="email"
            onChange={handleChange}
            value={state.email}
            placeholder="Optional Email Notification..."
          />
        </Form.Field>

        <Form.Field>
          <label>Phone</label>
          <input
            name="phone"
            onChange={handleChange}
            value={state.phone}
            placeholder="Optional text notification..."
          />
        </Form.Field>

        <Form.Button color="blue" position="rightAlign" content="Submit" />
      </Form>
    </Container>
  );
};

export default CheckinForm;
