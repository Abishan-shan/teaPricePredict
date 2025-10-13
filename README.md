🌿 Wave App: Tea Price Predictor

  Welcome to 🌊 Wave,
  an AI-powered Tea Price Prediction app built using Facebook Prophet — a smart forecasting model that predicts daily tea prices based on real market data.
  Wave helps farmers, traders, and tea lovers make better decisions by forecasting future prices of various tea types.

  🍃 What This App Does
  
      Wave predicts the future price of tea by analyzing past data.
      You can simply:
          1. Select your tea type (Ceylon Black, Green Tea, Herbal Tea, etc.)
          2. Pick a future date
          3. Click Predict
  ➡️ The system will instantly show the expected tea price for that day!

  🍃 How It Works
  
        The app uses Facebook Prophet, an AI model developed by Meta for time-series forecasting.
        Think of Prophet as a smart assistant that studies past price trends and predicts future values automatically.
        
        Other models like Linear Regression or etc were tested but didn’t fit well because:
                They don’t handle seasonal changes effectively
                They require heavy manual tuning

        Prophet, on the other hand:
              ✅ Understands seasonal patterns (like daily or monthly price changes)
              ✅ Works even with missing or irregular data
              ✅ Delivers fast, accurate predictions
              ✅ Is ideal for small, real-world datasets like tea markets


  💻 App Overview
      Here’s how to use the Wave App step by step 👇
      
      🏠 Step 1: Open the App
          When you open Wave, you’ll see a simple landing page with navigation links:
              1. Home – App overview
              2. About – Learn about the app
              3. Contact – Send us feedback or questions
          Click " Start Prediction " button to begin.
      🔐 Step 2: Login
          Enter the following demo credentials:
            Username: Admin  
            Password: 1234
            (These credentials are for demonstration only and not linked to any database.)
      📊 Step 3: Go to Dashboard
          After login, you’ll see a sidebar menu:
            🏠 Dashboard – Shows a 7-week price trend for each tea type with easy-to-read graphs and the average price over the past 7 days. 
            💹 Predict Price – Where you make predictions
            🚪 Logout – Exit the app
          Click " Predict Price " button to start forecasting.
      💡 Step 4: Predict the Tea Price
          1. Select your Tea Type (e.g., “Ceylon Black”)
          2. Pick a Date (any future day)
          3. Click Predict
          In seconds, you’ll see:
            📅 Selected Date
            🍵 Tea Type
            💰 Predicted Price (in LKR)
            Example:
              The predicted price for Green Tea on 2025-10-15 → Rs. 502.
      🌈 Step 5: View Results
          The prediction result appears in a neat result card showing your forecast.
          You can modify the date or tea type anytime to explore more predictions.


  📁 Dataset Details
  
      The model is trained on real tea market data, formatted like this:
          Date	Tea Type	Price (LKR)
          2025-09-01	Ceylon Black	450
          2025-09-02	Green Tea	505
          2025-09-03	Herbal Tea	540
     📊 The dataset captures daily price movements of popular teas sold in the Colombo tea market.
        This data helps Prophet learn daily trends, seasonal effects, and market behavior to make accurate forecasts.

 ⚙ Behind the Scenes
 
    🧹 Data Preparation – Tea data is cleaned and formatted
    🧠 Model Training – Prophet learns price trends from history
    💾 Model Saving – The trained model is stored in the backend
    🔄 Prediction Request – User selects tea + date
    📈 AI Forecast – The model predicts and returns the price
   
 
 🧩 Technology Stack
 
    Backend	: Python (Flask)
    Frontend :	HTML, CSS
    AI Model :	Facebook Prophet
    Dataset :	Real Tea Data (CSV - Kaggle: Colombo Tea Market)


🚀 How to Run the App (Local Setup) => for developers

    # 1️⃣ Clone the repository
      git clone https://github.com/Abishan-shan/tea-price-predictor.git
      cd tea-price-predictor
    # 2️⃣ Create virtual environment
      python -m venv venv
      venv\Scripts\activate   # (for Windows)
    # 3️⃣ Install dependencies
      pip install -r requirements.txt
    # 4️⃣ Run the app
      python app.py
Then open your browser and visit 👉 🚀 http://127.0.0.1:5000


🌟 Why Choose Wave

    ✅ Easy-to-use interface
    ✅ Fast & accurate AI predictions
    ✅ Supports multiple tea varieties
    ✅ Works efficiently with small data
    ✅ Designed for real-world users

🔮 Future Improvements

    📉 Add charts showing price trends
    🌦️ Integrate weather & export data
    📊 Include historical comparison graphs

💬 Thank You for Visiting 🌿

    Wave is where tea tradition meets artificial intelligence.
    Predict tea prices smartly, explore market trends, and sip innovation every day! 🍵

👨‍💻 Author

    Abishanthan Sarawanaraja
    Software Engineer
    📧 abishan@example.com

📁 Demo

    visit 👉 : [🎥 Click here to view Model & Demo Video on Google Drive](https://drive.google.com/drive/folders/1NcA3Q83DAScdA0QPWpJKo2VIJviP30SH?usp=sharing)]
