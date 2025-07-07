import React from 'react';
import logo from './assets/Apel logo.png';
import './App.css';
import UploadForm from './UploadForm';

function App() {
  return (
    <div className="app-container">
      <h1 className="title">Deteksi Kesegaran Buah Apel</h1>
      <UploadForm />
    </div>
  );
}

export default App;
