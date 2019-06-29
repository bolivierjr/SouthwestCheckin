import React from 'react';
import { BrowserRouter, Route } from 'react-router-dom';
import { Container, Segment } from 'semantic-ui-react';
import './App.css';
import { Header } from '../header';
import { CheckinForm } from '../checkinForm';
import { InfoScreen } from '../infoScreen';

function App() {
  return (
    <BrowserRouter>
      <Container style={{ margin: 20 }}>
        <Header />
        <Segment className="main-border">
          <Route exact path="/" component={CheckinForm} />
          <Route path="/messages" component={InfoScreen} />
        </Segment>
      </Container>
    </BrowserRouter>
  );
}

export default App;
