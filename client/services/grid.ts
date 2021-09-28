import axios from "axios"
import AuthService from './auth'

const API_URL = process.env.NEXT_PUBLIC_API_URL

class GridService {

    getGrids = async () => {
        let result = await axios.get(`${API_URL}/grids/`, { headers: AuthService.getAuthHeaders() }) 
        return result.data
    }

    getGridDetails = async (id:number) => {
        let result = await axios.get(`${API_URL}/grids/${id}/`, { headers: AuthService.getAuthHeaders() }) 
        return result.data
    }

    getGridTiles = async (id:number) => {
        let result = await axios.get(`${API_URL}/grids/${id}/tiles/`, { headers: AuthService.getAuthHeaders() }) 
        return result.data
    }
}

export default new GridService();