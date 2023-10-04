import { useState } from 'react'
import './App.css'
import {Routes,Route} from "react-router-dom"
import {CatchData} from "./pages/CatchData"

function App() {

  return (
    <Routes>
      <Route path='/' element={<CatchData /> }/>
    </Routes>
  )
}

export default App
