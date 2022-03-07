import React from 'react';
import { useState } from "react";
import axios from 'axios';
import styled from '@emotion/styled'

const Button = styled.button`
  padding: 4px;
  cursor: pointer;
  background-color: #FB6C6B;
  font-size: 14px;
  border-radius: 4px;
  color: black;
  font-weight: bold;
  &:hover {
    color: white;
  }
`

export const useForm = (callback: any, initialState = {}) => {

    const [values, setValues] = useState(initialState);

    // onChange
    const onChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setValues({ ...values, [event.target.name]: event.target.value });
    };

    const onSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        await callback(values);
    };

    // return values
    return {
        onChange,
        onSubmit,
        values,
    };
}

function NewTask() {

    const initialState = {
        description: "",
    };

    const [loading, setLoading]: [boolean, (loading: boolean) => void] = React.useState<boolean>(true);
    const [error, setError]: [string, (error: string) => void] = React.useState("");

    async function addNewTask(values: { description: String; }) {
        axios
            .post("http://localhost:8888/tasks", {
                description: values.description,
                headers: {
                    "Content-Type": "application/json"
                },
            })
            .then(response => {
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
    }

    const { onChange, onSubmit, values } = useForm(
        addNewTask,
        initialState
    );


    return (
        <form onSubmit={onSubmit}>
            <div>
                <input
                    name='description'
                    id='description'
                    type='text'
                    placeholder='Description'
                    onChange={onChange}
                    required
                    /> <Button type='submit'>Add Task</Button>
            </div>
        </form>
    );
}

export default NewTask;
