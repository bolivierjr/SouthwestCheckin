import React, { useRef, useState, useEffect } from 'react';
import { Container, Form, Message, Transition } from 'semantic-ui-react';
import './CheckinForm.css';
import { validate, useWindowDimensions } from '../../utils';

const CheckinForm = () => {
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
    state of the component
  */
  const [formValues, setFormValues] = useState({ ...initialFormValues });
  const [state, setState] = useState({ ...initialState });

  /*
    Hook made for getting current window dimensions.
  */
  const { width } = useWindowDimensions();

  /*
    A reference to the confirmation input
    element to focus on render.
  */
  const inputRef = useRef(null);

  useEffect(() => {
    inputRef.current.focus();
  }, []);

  /*
    Input change event handler.
  */
  const handleChange = event => {
    const { name, value } = event.target;

    setFormValues({ ...formValues, [name]: value });
    setState({ ...state, btnDisable: false });
  };

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
    Form submit event handler
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
            ref={inputRef}
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
