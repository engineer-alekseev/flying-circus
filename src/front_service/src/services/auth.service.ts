import axios from 'axios';
import store from './../store';


export const user_auth = async (telegram_id: string) => {
    try {
        const headers = {
            "Content-type": "application/json; charset=utf-8;",
            'X-Telegram-ID': telegram_id,
        }
        const responce = await axios.get(`/auth_service/auth/user`,
        {
            headers: headers
        })
        return responce.data;
    } catch (error) {
        console.error("Ошибка авторизации", error)
    }
}

export const signup = async (email: string) => {
    try {
        const telegram_id = store.getters.getTgId;

        const headers = {
            "Content-type": "application/json; charset=utf-8;",
            'X-Telegram-ID': telegram_id,
        }
        const responce = await axios.post(`/auth_service/auth/register`, {
            telegram_id: `${telegram_id}`,
            email: email,
        },
        {
            headers: headers
        })
        return {data: responce.data, status: responce.status};
    } catch (error) {
        console.error("Ошибка авторизации", error)
    }
}

export const sendCode = async (email: string, txt: string) => {
    try {
        const telegram_id = store.getters.getTgId;
        const headers = {
            "Content-type": "application/json; charset=utf-8;",
            'X-Telegram-ID': telegram_id,
        }
        const responce = await axios.post(`/send_one_message?email=${email}&txt=${txt}`, {
            email: email,
            message: txt
        },
        {
            headers: headers
        })
        return responce.data;
    } catch (error) {
        console.error("Ошибка авторизации", error)
    }
}
