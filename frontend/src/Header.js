import React from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';

const Header = () => {
  const location = useLocation();
  const navigate = useNavigate();

  const goBack = () => {
    navigate('/');
  };

  return (
    <header style={styles.header}>
      <div className="left" style={styles.left}>
        {location.pathname === '/creditcardstatement' && (
          <button style={styles.button} onClick={goBack}>
            ← Back
          </button>
        )}
        <img
          src="https://www.pbebank.com/media/2kwovkhx/pbb.svg"
          alt="Logo"
          height="100px"
          width="200px"
          style={{ marginLeft: location.pathname === '/creditcardstatement' ? '20px' : '0' }}
        />
      </div>

      <div className="right" style={styles.right}>
        {location.pathname === '/' && (
          <Link to="/creditcardstatement">
            <button style={styles.button}>Credit Card Statement</button>
          </Link>
        )}
      </div>
    </header>
  );
};

const styles = {
  header: {
    display: 'flex',
    justifyContent: 'space-around',
    alignItems: 'center',
    padding: '10px 30px',
    backgroundColor: '#f8f9fa',
    borderBottom: '1px solid #ccc',
  },
  left: {
    flex: '1',
    display: 'flex',
    alignItems: 'center',
  },
  right: {
    flex: '1',
    textAlign: 'right',
  },
  button: {
    padding: '10px 20px',
    backgroundColor: '#CC0000',
    border: 'none',
    color: '#fff',
    borderRadius: '5px',
    cursor: 'pointer',
  },
};

export default Header;
