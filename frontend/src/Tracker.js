// src/Tracker.js
import React from 'react';
import './Tracker.css'; // Import the separate CSS file

const Tracker = () => {
  return (
    <div className="tracker-container">
      <h1>Travel Tracker Form</h1>
      <form>
        {/* Travel Section */}
        <div className="section">
          <div className="section-title">Travel 🚗✈️🚲</div>
          <div className="form-group">
            <label htmlFor="start-location">
              Where did you travel today? (Start Location)
            </label>
            <input
              type="text"
              id="start-location"
              name="start-location"
              placeholder="Enter starting location"
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="end-location">
              Where did you travel today? (End Location)
            </label>
            <input
              type="text"
              id="end-location"
              name="end-location"
              placeholder="Enter ending location"
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="miles">
              Or, how many miles did you travel?
            </label>
            <input
              type="number"
              id="miles"
              name="miles"
              placeholder="Enter miles traveled"
            />
          </div>
          <div className="form-group">
            <label htmlFor="transportation">
              What mode of transportation did you use?
            </label>
            <select id="transportation" name="transportation">
              <option value="">--Select--</option>
              <option value="car">Car</option>
              <option value="ev">Electric Vehicle</option>
              <option value="bike">Bike</option>
              <option value="public">Public Transport</option>
              <option value="walking">Walking</option>
            </select>
          </div>
        </div>

        {/* Car Usage Section */}
        <div className="section">
          <div className="section-title">Car Usage</div>
          <div className="form-group">
            <label>Did you use a car today?</label>
            <div className="radio-group">
              <label>
                <input type="radio" name="used-car" value="yes" /> Yes
              </label>
              <label>
                <input type="radio" name="used-car" value="no" /> No
              </label>
            </div>
          </div>
          <div className="form-group">
            <label htmlFor="fuel-type">
              What type of fuel does your car use?
            </label>
            <select id="fuel-type" name="fuel-type">
              <option value="">--Select--</option>
              <option value="gas">Gas</option>
              <option value="hybrid">Hybrid</option>
              <option value="ev">Electric Vehicle</option>
              <option value="diesel">Diesel</option>
            </select>
          </div>
          <div className="form-group">
            <label htmlFor="carpool">
              Did you carpool or drive solo?
            </label>
            <select id="carpool" name="carpool">
              <option value="">--Select--</option>
              <option value="solo">Solo</option>
              <option value="1-2">1-2 passengers</option>
              <option value="3+">3+ passengers</option>
            </select>
          </div>
          <div className="form-group">
            <label htmlFor="fuel-efficiency">
              On a scale of 1 to 10, how fuel-efficient were your chosen route options?
            </label>
            <input
              type="number"
              id="fuel-efficiency"
              name="fuel-efficiency"
              min="1"
              max="10"
              placeholder="Rate from 1 to 10"
            />
          </div>
        </div>

        {/* Public Transport & Shared Rides Section */}
        <div className="section">
          <div className="section-title">
            Public Transport & Shared Rides
          </div>
          <div className="form-group">
            <label>
              Did you use public transportation or ride share today (train, bus, uber)?
            </label>
            <div className="radio-group">
              <label>
                <input type="radio" name="public-transport" value="yes" /> Yes
              </label>
              <label>
                <input type="radio" name="public-transport" value="no" /> No
              </label>
            </div>
          </div>
        </div>

        {/* Walk/Bike Section */}
        <div className="section">
          <div className="section-title">Walk/Bike</div>
          <div className="form-group">
            <label>Did you walk or bike today?</label>
            <div className="radio-group">
              <label>
                <input type="radio" name="walk-bike" value="yes" /> Yes
              </label>
              <label>
                <input type="radio" name="walk-bike" value="no" /> No
              </label>
            </div>
          </div>
        </div>

        {/* Eco-Friendly Travel Choices Section */}
        <div className="section">
          <div className="section-title">
            Eco-Friendly Travel Choices
          </div>
          <div className="form-group">
            <label htmlFor="sustainable-option">
              Would you consider a more sustainable travel option next time?
            </label>
            <select id="sustainable-option" name="sustainable-option">
              <option value="">--Select--</option>
              <option value="yes">Yes</option>
              <option value="no">No</option>
              <option value="unsure">Unsure</option>
            </select>
          </div>
          <div className="form-group">
            <label htmlFor="habit-improve">
              (OPTIONAL) What’s one small transportation habit you’d like to improve tomorrow?
            </label>
            <textarea
              id="habit-improve"
              name="habit-improve"
              rows="3"
              placeholder="Enter your idea..."
            ></textarea>
          </div>
          <div className="form-group">
            <label htmlFor="sustainable-action">
              (OPTIONAL) What was one sustainable action you actively tried today?
            </label>
            <textarea
              id="sustainable-action"
              name="sustainable-action"
              rows="3"
              placeholder="Enter your action..."
            ></textarea>
          </div>
          <div className="form-group">
            <label htmlFor="eco-choice">
              (OPTIONAL) What eco-friendly travel choice did you make today that you’re most proud of?
            </label>
            <textarea
              id="eco-choice"
              name="eco-choice"
              rows="3"
              placeholder="Enter your choice..."
            ></textarea>
          </div>
        </div>

        <button type="submit">Submit Tracker</button>
      </form>
    </div>
  );
};

export default Tracker;
