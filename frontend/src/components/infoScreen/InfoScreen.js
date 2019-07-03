import React, { useRef, useState, useEffect } from 'react';
import { Container, Segment, Form, Transition, Icon } from 'semantic-ui-react';
import './InfoScreen.css';
import { validate } from '../../utils';

function InfoScreen({ location, handlePath }) {
  const initialState = {
    messages: [],
    btnDisable: false,
    transition: false
  };

  /*
    useState hooks for setting and getting
    state of the component
  */
  const [state, setState] = useState({ ...initialState });
  const [confirmation, setConfirmation] = useState('');

  /*
    useEffect hook that handles the path
    for the header to set active tab item
    through a function prop.
  */
  useEffect(() => {
    handlePath(location.pathname);
  }, [handlePath, location.pathname]);

  /*
    A reference to the confirmation input
    element to focus on render.
  */
  const inputRef = useRef(null);

  useEffect(() => {
    inputRef.current.focus();
  }, []);

  /*
    Input change event handler sets
    new confirmation state vallues
    on every change.
  */
  const handleChange = event => {
    setConfirmation(event.target.value);
  };

  /*
    Event handler when input gets out of
    focus and checks form validation.
  */
  const handleBlur = event => {
    const formValidation = validate('confirmation', confirmation);

    if (formValidation.errMessage === '') {
      setState({
        ...state,
        btnDisable: false,
        transition: true
      });
    } else {
      setState({
        btnDisable: true,
        messages: [formValidation.errMessage],
        transition: true
      });
    }
  };

  /*
    Form submit event handler that checks
    the form input validation and sets the
    messages on the infoscreen.
  */
  const handleSubmit = async event => {
    setState({ ...state, messages: [] });

    const formValidation = validate('confirmation', confirmation);

    if (formValidation.error) {
      setState({
        btnDisable: true,
        messages: [formValidation.errMessage],
        transition: true
      });
      return;
    }

    const data = await fetchUrl();

    if (data.status) {
      setState({
        btnDisable: false,
        messages: [data.status],
        transition: true
      });
    } else if (data.messages) {
      setState({
        btnDisable: false,
        messages: data.messages,
        transition: true
      });
    }
    console.log(data);
  };

  /*
    Function that makes an ajax call to the
    backend to check the status of the autocheckin
    task.
  */
  const fetchUrl = async () => {
    try {
      const response = await fetch(`/info/${confirmation}`, {
        headers: {
          'Content-Type': 'application/json'
        }
      });

      const data = await response.json();

      return data;
    } catch (err) {
      console.log(err);
    }
  };

  const messageItems = state.messages.map((message, index) => {
    return (
      <p key={index}>
        <Icon size="small" name="angle double right" />
        {message}
      </p>
    );
  });

  return (
    <Container className="message-container">
      <Segment className="screen">
        <Transition visible={state.transition} animation="fade" duration={500}>
          <div>{messageItems}</div>
        </Transition>
      </Segment>

      <Form onSubmit={handleSubmit}>
        <Form.Field>
          <label>Confirmation</label>
          <input
            ref={inputRef}
            name="confirmation"
            className="message-input"
            onChange={handleChange}
            onBlur={handleBlur}
            value={confirmation}
            placeholder="Confirmation"
          />
        </Form.Field>
        <Form.Button
          color="blue"
          content="Submit"
          /* 
            Uncomment the line below if you want the
            button to disable on form validations.
          */

          // disabled={state.btnDisable}
        />
      </Form>
    </Container>
  );
}

export default InfoScreen;
