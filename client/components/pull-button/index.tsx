import React, { useState, useEffect } from 'react'
import Button from '@material-ui/core/Button';

import UserService from '../../services/user'
import TaskService from '../../services/task'

const PullButton:React.FC = () => {
    const STATUS_NEUTRAL:string = "neutral"
    const STATUS_LOADING:string = "loading"
    const STATUS_SUCCESS:string = "success"
    const STATUS_ERROR:string = "error"

    const [ status = STATUS_NEUTRAL, setStatus ] = useState <string> ()

    const handlePull = async () => {
        setStatus(STATUS_LOADING)
        try {
            const { success, task_id } = await UserService.pullActivities()
            if (success) {
                console.log(task_id)
                getTaskStatus(task_id)
            } else {
                setStatus(STATUS_ERROR)
            }
        } catch (e) {
            console.log(e)
            setStatus(STATUS_ERROR)
        }  
    }

    // @todo : Websocket or long polling
    const getTaskStatus = async (taskId:number) => {
        const MAX_NUMBER_OF_ITERATIONS = 3
        let i = 0
        const interval = setInterval(async() => {
            if (i++ >= MAX_NUMBER_OF_ITERATIONS) {
                clearInterval(interval)
                setStatus(STATUS_ERROR)
            } else {
                const { task_status } = await TaskService.getTaskDetails(taskId)
                if (task_status === 'SUCCESS') {
                    clearInterval(interval)
                    setStatus(STATUS_SUCCESS)
                }
            }
        }, 1000)
    }

    // Restore neutral status after success or error state
    useEffect(() => {
        if (status === STATUS_SUCCESS || status === STATUS_ERROR) {
            setTimeout(() => {
                setStatus(STATUS_NEUTRAL)
            }, 5000)
        }

    }, [ status ])

    const getColor = (status:string) => {
        switch (status) {
            case STATUS_ERROR:
                return "error"
            case STATUS_LOADING:
                return "info"
            case STATUS_SUCCESS:
                return "success"
            default:
                return "primary"
        }
    }

    const isDisabled = (status:string) => {
        return status === STATUS_SUCCESS
    }

    const getButtonValue = (status:string) => {
        switch (status) {
            case STATUS_LOADING:
                return "..."
            default: 
                return "Sync"
        }
    }

    return (
        <>
            <Button
                variant="contained" 
                color={getColor(status)}
                disabled={isDisabled(status)}
                onClick={() => { handlePull() }}
            >
                {getButtonValue(status)}
            </Button>
        </>
    )
}

export default PullButton