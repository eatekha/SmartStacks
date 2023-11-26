import { useState } from 'react'
import './App.css'

function App (props) {
  const [isFlipped, setIsFlipped] = useState(
    new Array(props.response.info.length).fill(false)
  )
  
  const handleClick = (index) => {
    const newIsFlipped = [...isFlipped]
    newIsFlipped[index] = !newIsFlipped[index]
    setIsFlipped(newIsFlipped)
  }

  console.log(props.response.info)

  const question = props.response.info.map((question, index) => {
    return (
      <div key={index}>
        <div>
          <h1>{question.topic}</h1>
          <h3>{question.question}</h3>
          <input placeholder="Enter your answer here: "></input>
        </div>
        {isFlipped[index] && (
          <div id="back" className="back" onClick={() => handleClick(index)}>
            <h1>{question.answer}</h1>
          </div>
        )}
        {!isFlipped[index] && (
          <button onClick={() => handleClick(index)}>Show Answer</button>
        )}
      </div>
    )
  })

  return (
    <div>
      {question}
    </div>
  )
}

export default App