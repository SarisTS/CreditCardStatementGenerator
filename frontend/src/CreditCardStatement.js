import React from 'react'
import './CreditCardStatement.css'

const CreditCardStatement = ({customerId, setCustomerId, language, setLanguage, pdfUrl, error, generate}) => {
  return (
    <main>
        <div className="container mt-5">
        <h2 className="mb-4">Generate Credit Card Statement</h2>
        <form onSubmit={generate}>
            <div className="mb-3">
            <input
                type="number"
                className="form-control"
                placeholder="Enter Customer ID"
                value={customerId}
                onChange={(e) => setCustomerId(e.target.value)}
                required
            />
            <label htmlFor="language" className='form-label'>Select Language</label>
            <select 
                name="language" 
                className='form-select'
                value={language} 
                onChange={(e) => setLanguage(e.target.value)} 
                required>
              <option value="en">English</option>
              <option value="ta">தமிழ் (Tamil)</option>
              <option value="hi">हिंदी (Hindi)</option>
              <option value="ar">العربية (Arabic)</option>
              <option value="zh">中文 (Chinese)</option>
              <option value="fr">Français (French)</option>
              <option value="es">Español (Spanish)</option>
              <option value="ms">Bahasa Melayu (Malay)</option>
              <option value="ja">日本語 (Japanese)</option>
              <option value="de">Deutsch (German)</option>
            </select>
            </div>
            <button className="btn btn-primary">Generate</button>
        </form>

        {pdfUrl && (
            <div className="mt-3">
            <a className="btn btn-success" href={`http://localhost:8000${pdfUrl}`} download target="_blank" rel="noreferrer">Download PDF</a>
            </div>
        )}
        {error && <div className="alert alert-danger mt-3">{error}</div>}
        </div>
    </main>
  )
}

export default CreditCardStatement