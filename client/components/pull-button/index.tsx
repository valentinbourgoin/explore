import React from 'react'
import Button from '@material-ui/core/Button';

import UserService from '../../services/user'

const PullButton:React.FC = () => {
    const handlePull = async () => {
        const result = await UserService.pullActivities()
        console.log(result.task_id)
    }

    return (
        <>
            <Button
                variant="contained" 
                color="primary"
                onClick={() => { handlePull() }}
            >
                Sync
            </Button>
        </>
    )
}

export default PullButton