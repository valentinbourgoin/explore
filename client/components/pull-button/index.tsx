import React, { useState } from 'react'
import Button from '@material-ui/core/Button';

import UserService from '../../services/user'

const PullButton:React.FC = () => {
    const STATUS_NEUTRAL:string = "neutral"
    const STATUS_LOADING:string = "loading"
    const STATUS_SUCCESS:string = "success"
    const STATUS_ERROR:string = "error"

    const [ status = STATUS_NEUTRAL, setStatus ] = useState <string> ()

    const handlePull = async () => {
        setStatus(STATUS_LOADING)
        try {
            const result = await UserService.pullActivities()
            if (result.success) {
                console.log(result.task_id)
                setStatus(STATUS_SUCCESS)
            } else {
                setStatus(STATUS_ERROR)
            }
        } catch (e) {
            console.log(e)
            setStatus(STATUS_ERROR)
        }
        
    }

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