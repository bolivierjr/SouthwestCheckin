import React, { useState } from 'react';
import { BrowserRouter, Route } from 'react-router-dom';
import { Container, Segment } from 'semantic-ui-react';
import { Header } from '../header';
import { CheckinForm } from '../checkinForm';
import { InfoScreen } from '../infoScreen';

function App() {
  const [path, setPath] = useState('/');

  /*
    Path handler, that's passed down as props to components
    for setting state of the router path of which current
    element it's viewing, to be used for setting the active
    header tab in the Header component.
  */
  const handlePath = newPath => {
    setPath(newPath);
  };

  return (
    <BrowserRouter>
      <Container>
        <Header path={path} />
        <Segment color="orange">
          <Route
            exact
            path="/"
            render={props => <CheckinForm {...props} handlePath={handlePath} />}
          />
          <Route
            path="/messages"
            render={props => <InfoScreen {...props} handlePath={handlePath} />}
            handlePath={handlePath}
          />
        </Segment>
      </Container>
    </BrowserRouter>
  );
}

export default App;
