import './App.css';
import React from 'react';
import PreferencesForm from './components/PreferencesForm';
import CountryComparison from './components/CountryComparison';
// Additional imports for other components will go here

function App() {
  return (
    <div className="App">
      <h1>Country Comparison App</h1>
      <PreferencesForm />
      <CountryComparison />
      {/* Routes or links to other components will be added here */}
    </div>
  );
}

export default App;
