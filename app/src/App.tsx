import React from 'react';
import TaskList from './components/TaskList';
import NewTask from './components/NewTask';
import './App.css';

function App() {
    return (
      <div className="App">
        <TaskList/>
        <NewTask/>
      </div>
    );
}

export default App;
