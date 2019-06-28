import React from 'react';
import './App.css';
import { Header } from '../header';
import { CheckinForm } from '../checkinForm';
import { InfoScreen } from '../infoScreen';

function App() {
  return (
    <div className="App">
      <Header />
      <CheckinForm />
      <InfoScreen />
    </div>
  );
}

export default App;
