import Cookies from "universal-cookie/es6";

const cookie = new Cookies()

export const setCookie = (cookieName, value) => {
    cookie.set(cookieName, value)
}

export const getCookie = (cookieName) => {
    return cookie.get(cookieName)
}

export const removeCookie = (cookieName) => {
    cookie.remove(cookieName)
}