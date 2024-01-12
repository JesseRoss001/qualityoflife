import './App.css';
import React from 'react';
import PreferencesForm from './components/PreferencesForm';
import CountryComparison from './components/CountryComparison';
/// In your React app
import Axios from 'axios';

Axios.get('/custom_endpoint/')
  .then(response => {
    console.log(response.data.data); // Process the combined CSV data
  })
  .catch(error => {
    console.error(error);
  });

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
