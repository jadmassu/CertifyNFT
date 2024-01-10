
import { BrowserRouter, Route, Routes } from "react-router-dom";
import GenerateImage from "./Pages/GenerateImage";
function App() {



  return (
    <>
      {/* <BrowserRouter basename="crm"> */}
      <BrowserRouter>
        <div className="fixed left-0 top-0 w-screen z-20">
          {/* <TopNav /> */}
        </div>

        <div className="flex h-screen  overflow-auto scrollbar-w-thin">

          {/* <div className={`${!showSidebar && "hidden"} lg:block z-50`}> */}
          <div className="fixed top-3 left-0 h-screen z-10 mt-16 w-48">
            {/* <CustomerSideBar /> */}
          </div>

          <div
            className={`flex lg:pl-64"
               pr-5 w-full pt-20 h-screen flex-col`}
          >
            <Routes>
              <Route index element={<GenerateImage />} />


            </Routes>
          </div>
        </div>
      </BrowserRouter>
    </>
  )

}



export default App;