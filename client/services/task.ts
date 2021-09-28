import axios from "axios"
import AuthService from './auth'

const API_URL = process.env.NEXT_PUBLIC_API_URL

class TaskService {

    getTaskDetails = async (id:number) => {
        let result = await axios.get(`${API_URL}/tasks/${id}/`, { headers: AuthService.getAuthHeaders() }) 
        return result.data
    }
}

export default new TaskService();