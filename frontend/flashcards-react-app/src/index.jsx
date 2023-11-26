import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'

ReactDOM.createRoot(document.getElementById('container')).render(
  <React.StrictMode>
    <App 
      response = {
        {"component": "flashcard",
        "info": [
            {
                "unit_name": "Circular Motion",
                "topic": "Centripetal Force",
                "question": "What is the formula for centripetal force?",
                "answer": "F_centripetal = mv^2/r"
            },
            {
                "unit_name": "Circular Motion",
                "topic": "Centripetal Force",
                "question": "What does the centripetal force cause an object to do?",    
                "answer": "The centripetal force causes an object to move in a circle."  
            },
            {
                "unit_name": "Circular Motion",
                "topic": "Angular Velocity",
                "question": "What is the formula for angular velocity?",
                "answer": "ω = Δθ/Δt"
            },
            {
                "unit_name": "Circular Motion",
                "topic": "Angular Velocity",
                "question": "What is the unit of angular velocity?",
                "answer": "The unit of angular velocity is radians per second (rad/s)."  
            },
            {
                "unit_name": "Circular Motion",
                "topic": "Centripetal Acceleration",
                "question": "What is the formula for centripetal acceleration?",
                "answer": "a_centripetal = v^2/r"
            },
            {
                "unit_name": "Circular Motion",
                "topic": "Centripetal Acceleration",
                "question": "What is the direction of centripetal acceleration?",        
                "answer": "The direction of centripetal acceleration is always towards the center of the circle."
            },
            {
                "unit_name": "Circular Motion",
                "topic": "Tangential Velocity",
                "question": "What is the formula for tangential velocity?",
                "answer": "v_tangential = ωr"
            },
            {
                "unit_name": "Circular Motion",
                "topic": "Tangential Velocity",
                "question": "What is the direction of tangential velocity?",
                "answer": "The direction of tangential velocity is always tangential to the circle."
            },
            {
                "unit_name": "Circular Motion",
                "topic": "Centripetal Force",
                "question": "What is the relationship between centripetal force and centripetal acceleration?",
                "answer": "The centripetal force is equal to the product of mass and centripetal acceleration."
            },
            {
                "unit_name": "Circular Motion",
                "topic": "Angular Momentum",
                "question": "What is the formula for angular momentum?",
                "answer": "L = Iω"
            }
        ]}
    }
    />
  </React.StrictMode>,
)
