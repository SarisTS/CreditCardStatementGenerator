import { useState } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import Header from './Header';
import './App.css'
import Footer from './Footer';
import { Route, Routes } from 'react-router-dom';
import CreditCardStatement from './CreditCardStatement';
import Content from './Content';

function App() {
  const [customerId, setCustomerId] = useState('');
  const [language, setLanguage] = useState('');
  const [pdfUrl, setPdfUrl] = useState('');
  const [error, setError] = useState('');

  const generate = async (e) => {
    e.preventDefault();
    setError('');
    setPdfUrl('');

    try {
      const backendUrl = process.env.REACT_APP_BACKEND_URL;
      const res = await axios.get(`${backendUrl}/api/generate-statement/?customer_id=${customerId}&language=${language}`);
      if (res.data.success) {
        setPdfUrl(res.data.pdf_url);
      } else {
        setError(res.data.error);
      }
    } catch (err) {
      setError("Unable to reach backend server.");
    }
  };

  return (
    <div className="app-wrapper">
      <div className="app-content">
      <Header />
      </div>
      <Routes>
        <Route path='/' element={<Content />} />
        <Route path='/creditcardstatement' 
               element={<CreditCardStatement 
               customerId={customerId} 
               setCustomerId={setCustomerId} 
               language={language} 
               setLanguage={setLanguage} 
               pdfUrl={pdfUrl} 
               error={error} 
               generate={generate} />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
