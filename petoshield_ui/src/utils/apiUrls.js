// import dotenv from 'dotenv';
//
// require('dotenv').config();

const API_VERSION = 'api'
const REACT_APP_BACKEND_URL = process.env.REACT_APP_BACKEND_URL
// const REACT_APP_BACKEND_URL = 'https://api.petoshield.com'
const HOST = `${REACT_APP_BACKEND_URL}/${API_VERSION}`

export const API_AUTH_TOKEN = `${HOST}/auth/token`
export const API_AUTH_REFRESH_TOKEN = `${HOST}/auth/token/refresh`
export const API_USER_SELF = `${HOST}/users/me`
export const API_USER_URL = `${HOST}/users/`
export const API_ROLES_URL = `${HOST}/roles/`
export const API_PETS_URL = `${HOST}/pet-profile/pets/`
export const API_PETS_CREATE_WITH_USER_URL = `${HOST}/pet-profile/pets/create_new_account/`
export const API_BREEDS_URL = `${HOST}/pet-profile/breeds/`
export const API_SERVICE_PROVIDERS_URL = `${HOST}/insurance/service-providers/`
export const API_POLICIES_URL = `${HOST}/insurance/policies/`
export const API_INSURANCE_CASES_URL = `${HOST}/insurance/insurance-cases/`
export const API_INCOMING_INVOICES_URL = `${HOST}/insurance/incoming-invoices/`