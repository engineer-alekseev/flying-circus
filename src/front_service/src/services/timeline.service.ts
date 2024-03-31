import axios from 'axios';
import store from './../store';

const api_url = "/booking_service"

const telegram_id = store.getters.getTgId;

export const getAllBooking = async () => {
    try {
        const telegram_id = store.getters.getTgId;
        const headers = {
            "Content-type": "application/json; charset=utf-8;",
            'X-Telegram-ID': telegram_id,
        }
        const responce = await axios.get(`${api_url}/booking/`, 
        {
            headers: headers
        })
        return responce.data;
    } catch (error) {
        console.error("Ошибка авторизации", error)
    }
}
export const addBooking = async (start_time: string, end_time: string, room_id: string) => {
    try {
        const telegram_id = store.getters.getTgId;
        const headers = {
            "Content-type": "application/json; charset=utf-8;",
            'X-Telegram-ID': telegram_id,
        }
        const responce = await axios.post(`${api_url}/booking/`, {
            start_time: start_time,
            end_time: end_time,
            room_id: room_id
        },
        {
            headers: headers
        })
        return {data: responce.data, status: responce.status};
    } catch (error) {
        console.error("Ошибка авторизации", error)
    }
}

export const deleteBooking = async (book_id: string) => {
    try {
        const telegram_id = store.getters.getTgId;
        const headers = {
            "Content-type": "application/json; charset=utf-8;",
            'X-Telegram-ID': telegram_id,
        }
        const responce = await axios.delete(`${api_url}/booking/${book_id}`, 
        {
            headers: headers
        })
        return {data: responce.data, status: responce.status};
    } catch (error) {
        console.error("Ошибка авторизации", error)
    }
}

export const getRooms = async () => {
    try {
        const telegram_id = store.getters.getTgId;
        const headers = {
            "Content-type": "application/json; charset=utf-8;",
            'X-Telegram-ID': telegram_id,
        }
        const responce = await axios.get(`${api_url}/rooms/`, 
        {
            headers: headers
        })
        return responce.data;
    } catch (error) {
        console.error("Ошибка авторизации", error)
    }
}

export const getRoomById = async (room_id: string) => {
    try {
        const telegram_id = store.getters.getTgId;
        const headers = {
            "Content-type": "application/json; charset=utf-8;",
            'X-Telegram-ID': telegram_id,
        }
        const responce = await axios.post(`${api_url}/rooms/${room_id}`, {
            id: room_id
        },
        {
            headers: headers
        })
        return responce.data;
    } catch (error) {
        console.error("Ошибка авторизации", error)
    }
}

export const getRoomByIdBooked = async (room_id: string, date: string) => {
    try {
        const headers = {
            "Content-type": "application/json; charset=utf-8;",
            'X-Telegram-ID': telegram_id,
        }
        const responce = await axios.get(`${api_url}/rooms/${room_id}/booked?booking_date=${date}`, 
        {
            headers: headers
        })
        return responce.data;
    } catch (error) {
        console.error("Ошибка авторизации", error)
    }
}

export const createRooms = async (telegram_id: string, email: string) => {
    try {
        const headers = {
            "Content-type": "application/json; charset=utf-8;",
            'X-Telegram-ID': telegram_id,
        }
        const responce = await axios.post(`${api_url}/rooms`, {
            telegram_id: telegram_id,
            email: email,
        },
        {
            headers: headers
        })
        return responce.data;
    } catch (error) {
        console.error("Ошибка авторизации", error)
    }
}