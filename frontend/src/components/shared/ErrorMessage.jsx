import React from 'react';
import './ErrorMessage.css';

const ErrorMessage = ({ message }) => (
  <div className="error-message">
      {/* Error display */}
    <p>{message}</p>
    </div>
  );
export default ErrorMessage;