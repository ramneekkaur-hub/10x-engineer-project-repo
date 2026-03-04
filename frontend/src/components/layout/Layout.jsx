import React from 'react';

const Layout = ({ children }) => {
  return (
    <div>
      <Header />
      <Sidebar />
      <main>{children}</main>
    </div>
  );
};

export default Layout;