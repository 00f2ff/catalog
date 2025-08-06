import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import './App.css'

function Home() {
  return (
    <div>
      <h1>Catalog</h1>
      <p>Welcome to the catalog application.</p>
    </div>
  )
}

function About() {
  return (
    <div>
      <h1>About</h1>
      <p>
        This is a full-stack catalog application built with FastAPI, PostgreSQL, Neo4j,
        and React.
      </p>
    </div>
  )
}

function App() {
  return (
    <BrowserRouter>
      <div>
        <nav style={{ padding: '1rem', borderBottom: '1px solid #ccc' }}>
          <Link to="/" style={{ marginRight: '1rem' }}>
            Home
          </Link>
          <Link to="/about">About</Link>
        </nav>
        <main style={{ padding: '1rem' }}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  )
}

export default App
