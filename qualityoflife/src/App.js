import React from 'react';
import { DataProvider } from './DataContext';
import './App.css';
import PreferencesForm from './components/PreferencesForm';
import CountryComparison from './components/CountryComparison';

function App() {
  return (
    <DataProvider>
      <div className="App">
        <h1>Country Comparison App</h1>
        <PreferencesForm />
        <CountryComparison />
      </div>
    </DataProvider>
  );
}

export default App;
