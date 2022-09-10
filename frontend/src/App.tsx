import { Routes, Route } from "react-router-dom"
import { Container } from "react-bootstrap"
import { Navbar } from "./components/Navbar"
import { Home } from "./Home"

function App() {

  return (
    <>
      <Navbar />
      <Container>
        <Routes>
          <Route path="/" element={<Home />} />
        </Routes>
      </Container>
    </>
  )
}

export default App
