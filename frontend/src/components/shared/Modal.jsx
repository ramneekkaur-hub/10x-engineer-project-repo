import React from 'react';

const Modal = ({ show, children }) => {
  if (!show) return null;

  return (
    <div>
      {/* Modal dialog */}
      {children}
    </div>
  );
};

export default Modal;