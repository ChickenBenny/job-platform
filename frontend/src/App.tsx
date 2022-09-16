import { Routes, Route } from "react-router-dom"
import { Navbar } from "./components/Navbar"
import { Home } from "./pages/Home"
import { Backend } from "./pages/Backend"
import { DataEngineer } from "./pages/DataEngineer"
import { DataScientist } from "./pages/DataScientist"
import { MLEngineer } from "./pages/MLEngineer"
import { QAEngineer } from "./pages/QAEngineer"

function App() {

  return (
    <>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/backend" element={<Backend />} />
        <Route path="/dataEngineer" element={<DataEngineer />} />
        <Route path="/dataScientist" element={<DataScientist />} />
        <Route path="/mlEngineer" element={<MLEngineer />} />
        <Route path="/qaEngineer" element={<QAEngineer />} />
      </Routes>
    </>
  )
}

export default App
