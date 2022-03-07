import React from 'react';
import axios from 'axios';
import ActionButton from './Button';

interface ITask {
  id: number;
  description: string;
  completed: boolean;
}

const defaultTasks:ITask[] = [];

async function DeleteTask(id: String){
  axios
      .delete("http://localhost:8888/tasks/" + id);
}

async function UpdateTask(id: String){
  axios
      .post("http://localhost:8888/tasks/" + id);
}

function TaskList() {

  const [tasks, setTasks]: [ITask[], (tasks: ITask[]) => void] = React.useState(defaultTasks);
  const [loading, setLoading]: [boolean, (loading: boolean) => void] = React.useState<boolean>(true);
  const [error, setError]: [string, (error: string) => void] = React.useState("");

  React.useEffect(() => {
    axios
        .get<ITask[]>("http://localhost:8888/tasks", {
          headers: {
            "Content-Type": "application/json"
          },
        })
        .then(response => {
          setTasks(Object.values(response.data));
          setLoading(false);
        })
        .catch(ex => {
          console.log(ex.response)
          const error =
          ex.response.status === 404
            ? "Resource Not found"
            : "An unexpected error has occurred";
          setError(error);
          setLoading(false);
        });
    }, []);

    return (
      <div className="TaskList">
        <ul className="tasks">
          {tasks.map((task) => (
            <li key={task.id}>
                <p>
                    {task.completed ? <ActionButton onClick={async () => {await UpdateTask(task.id.toString());}} children={"Uncomplete"}/>  : <ActionButton onClick={async () => {await UpdateTask(task.id.toString());}} children={"Complete"}/> } <ActionButton onClick={async () => {await DeleteTask(task.id.toString());}} children={"Delete"}/> {task.completed ? <del>{task.description}</del> : task.description}
                </p>
            </li>
          ))}
        </ul>
        {error && <p className="error">{error}</p>}
      </div>
    );
}

export default TaskList;
