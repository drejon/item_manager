// import { useState } from 'react'
// import './App.css'
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Home } from './landing/Home';
import { Login } from './login/login';
import { Signup } from './login/signup';

function App() {
  // const [count, setCount] = useState(0)

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App
