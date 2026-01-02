import './Css/App.css'
import AddEvent from './components/AddEvent.jsx'
import EventList from './components/EventList.jsx'

function App() {

  return (
    <>
      <div className="phone-screen">
          <h1 className="title">
            Your tasks for today!📃
          </h1>
          <div className="container-events">
            <AddEvent/>
            <EventList/>
          </div>
      </div>   
    </>
  )
}

export default App
