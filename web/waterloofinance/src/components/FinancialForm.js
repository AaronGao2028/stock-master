import React, { useState, useEffect } from 'react';
import './FinancialForm.css';

const FinancialForm = () => {
  const [formData, setFormData] = useState({
    marketCap: '',
    dividend: '',
    riskTolerance: '',
    sector: '',
    numStocks: 10,
  });

  const [currentStep, setCurrentStep] = useState(1);
  const [submitted, setSubmitted] = useState(false);

  useEffect(() => {
    document.body.classList.add('pulsating');
    return () => {
      document.body.classList.remove('pulsating');
    };
  }, []);

  const handleSquareClick = (choice) => {
    setFormData({
      ...formData,
      [currentStep === 1 ? 'marketCap' :
        currentStep === 2 ? 'dividend' :
          currentStep === 3 ? 'riskTolerance' :
            'sector']: choice,
    });
  };

  const handleSliderChange = (e) => {
    setFormData({
      ...formData,
      numStocks: parseInt(e.target.value, 10),
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmitted(true);

    setTimeout(() => {
      setSubmitted(false);
      if (currentStep < 4) {
        setCurrentStep(currentStep + 1);
      } else {
        setCurrentStep(1);
      }
    }, 10);
  };

  const renderFormStep = () => {
    switch (currentStep) {
      case 1:
        return (
          <div className={`form-group ${submitted ? 'hidden' : ''}`}>
            <label className="label">Market Cap:</label>
            <div className="square-group">
              <div
                className={`square ${formData.marketCap === 'small' ? 'selected' : ''}`}
                onClick={() => handleSquareClick('small')}
              >
                Small
              </div>
              <div
                className={`square ${formData.marketCap === 'medium' ? 'selected' : ''}`}
                onClick={() => handleSquareClick('medium')}
              >
                Medium
              </div>
              <div
                className={`square ${formData.marketCap === 'large' ? 'selected' : ''}`}
                onClick={() => handleSquareClick('large')}
              >
                Large
              </div>
            </div>
          </div>
        );
      case 2:
        return (
          <div className={`form-group ${submitted ? 'hidden' : ''}`}>
            <label className="label">Dividend:</label>
            <div className="square-group">
              <div
                className={`square ${formData.dividend === 'low' ? 'selected' : ''}`}
                onClick={() => handleSquareClick('low')}
              >
                Low
              </div>
              <div
                className={`square ${formData.dividend === 'medium' ? 'selected' : ''}`}
                onClick={() => handleSquareClick('medium')}
              >
                Medium
              </div>
              <div
                className={`square ${formData.dividend === 'high' ? 'selected' : ''}`}
                onClick={() => handleSquareClick('high')}
              >
                High
              </div>
            </div>
          </div>
        );
      case 3:
        return (
          <div className={`form-group ${submitted ? 'hidden' : ''}`}>
            <label className="label">Risk Tolerance:</label>
            <div className="square-group">
              <div
                className={`square ${formData.riskTolerance === 'low' ? 'selected' : ''}`}
                onClick={() => handleSquareClick('low')}
              >
                Low
              </div>
              <div
                className={`square ${formData.riskTolerance === 'medium' ? 'selected' : ''}`}
                onClick={() => handleSquareClick('medium')}
              >
                Medium
              </div>
              <div
                className={`square ${formData.riskTolerance === 'high' ? 'selected' : ''}`}
                onClick={() => handleSquareClick('high')}
              >
                High
              </div>
            </div>
          </div>
        );
      case 4:
        return (
          <div className={`form-group ${submitted ? 'hidden' : ''}`}>
            <label className="label">Sector:</label>
            <div className="square-group">
              <div
                className={`square ${formData.sector === 'technology' ? 'selected' : ''}`}
                onClick={() => handleSquareClick('technology')}
              >
                Technology
              </div>
              <div
                className={`square ${formData.sector === 'finance' ? 'selected' : ''}`}
                onClick={() => handleSquareClick('finance')}
              >
                Finance
              </div>
              <div
                className={`square ${formData.sector === 'industrials' ? 'selected' : ''}`}
                onClick={() => handleSquareClick('industrials')}
              >
                Industrials
              </div>
              <div
                className={`square ${formData.sector === 'consumers' ? 'selected' : ''}`}
                onClick={() => handleSquareClick('consumers')}
              >
                Consumers
              </div>
            </div>
          </div>
        );
      default:
        return null;
    }
  };
  
  const sliderStyle = {
    width: `${(formData.numStocks / 20) * 100}%`,
  };
  

  return (
    <div className={`background ${submitted ? 'fade-out' : ''}`}>
      <div className={`container ${submitted ? 'submitted' : ''}`}>
        <form onSubmit={handleSubmit} className={`financial-form ${submitted ? 'submitted' : ''}`}>
          <h2 className={`form-title ${submitted ? 'fade-in' : ''}`}>Financial Portfolio Preferences - Step {currentStep}</h2>
          <div className={`title ${submitted ? 'fade-in' : ''}`}>STOCK MASTER</div>
          {renderFormStep()}
          {currentStep === 4 && (
            <div className={`form-group ${submitted ? 'hidden' : ''}`}>
              <label className="label">Number of Stocks:</label>
              <div className="slider-container">
                <div className="slider-fill" style={sliderStyle}></div>
                <input
                  type="range"
                  min="1"
                  max="20"
                  value={formData.numStocks}
                  onChange={handleSliderChange}
                  className="input"
                />
              </div>
            </div>
          )}
          <button type="submit" className={`submit-btn ${submitted ? 'hidden' : ''}`}>Submit</button>
        </form>
      </div>
    </div>
  );
};

export default FinancialForm;
