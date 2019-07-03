import React, { useRef, useState, useEffect } from 'react';
import { Container, Segment, Form, Transition, Icon } from 'semantic-ui-react';
import './InfoScreen.css';
import { validate } from '../../utils';

function InfoScreen() {
  const initialState = {
    messages: [],
    btnDisable: false,
    transition: false
  };

  const [state, setState] = useState({ ...initialState });
  const [confirmation, setConfirmation] = useState('');
  /*
    A reference to the confirmation input
    element to focus on render.
  */
  const inputRef = useRef(null);

  useEffect(() => {
    inputRef.current.focus();
  }, []);

  const handleChange = event => {
    setConfirmation(event.target.value);
  };

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
    let fixedMessage = `${message}`;

    return (
      <p key={index}>
        <Icon size="small" name="angle double right" />
        {fixedMessage}
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
          // disabled={state.btnDisable}
        />
      </Form>
    </Container>
  );
}

export default InfoScreen;
