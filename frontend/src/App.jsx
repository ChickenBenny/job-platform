import { BrowserRouter, Routes, Route} from "react-router-dom"
import { Home } from "./pages/Home";
import { Backend } from "./pages/Backend"
import { DataEngineer } from "./pages/DataEngineer"
import { DataScientist } from "./pages/DataScientist"
import { MLEngineer } from "./pages/MLEngineer"
import { QAEngineer } from "./pages/QAEngineer"



const App = () => {
  return (
    <>
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<Home />}/>
      <Route path="/backend" element={<Backend />}/>
      <Route path="/data_engineer" element={<DataEngineer />}/>
      <Route path="/data_scientist" element={<DataScientist />}/>
      <Route path="/ml_engineer" element={<MLEngineer />}/>
      <Route path="/qa_engineer" element={<QAEngineer />}/>
    </Routes>
  </BrowserRouter>
    </>
  )
}

export default App;
