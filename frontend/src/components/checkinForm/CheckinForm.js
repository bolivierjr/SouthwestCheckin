import React, { useRef, useState, useEffect } from 'react';
import { Container, Form, Message, Transition } from 'semantic-ui-react';
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
    success: false,
    errMessage: '',
    btnDisable: true
  };

  /*
    useState hook for setting and getting
    state of the component
  */
  const [state, setState] = useState({ ...initialState });

  /*
    Hook made for getting current window dimensions.
  */
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
    Input change event handler
  */
  const handleChange = event => {
    const { name, value } = event.target;

    setState({ ...state, [name]: value, btnDisable: false });
  };

  /*
    Form submit event handler
  */
  const handleSubmit = async event => {
    event.preventDefault();
    const validationResult = validate({ ...state });

    setState({ ...validationResult, success: false });

    if (!validationResult.error) {
      const data = await fetchUrl();

      if (data.error) {
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
          btnDisable: true
        });
      }
    }
  };

  const fetchUrl = async () => {
    const { confirmation, firstname, lastname } = state;
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
    <Container id="checkin-container">
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

        <Form.Button
          color="blue"
          position="rightAlign"
          content="Submit"
          disabled={state.btnDisable}
        />
      </Form>
    </Container>
  );
};

export default CheckinForm;
