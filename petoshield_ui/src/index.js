import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './static/styles/tailwind-source.css'
import './static/styles/global.css'
import './static/styles/animation.css'

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
