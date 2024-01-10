import axios from "axios";

export const baseURL = "http://localhost:5001"; // local
export const api = axios.create({
    baseURL: baseURL,
    withCredentials: true,
});