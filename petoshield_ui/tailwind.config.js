/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        poppins: ['Poppins', 'sans-serif'],
        merriweather: ['Merriweather', 'serif'],
        lato: ['Lato', 'sans-serif'],
        dancing: ['Dancing Script', 'cursive'],
      }
    },
    colors: {
      'white': '#ffffff',
      'black-haze': '#f7f7f7',
      'rose': '#ff0083',
      'rose-dark': '#d50269',
      'black': '#4a4a4a',
      'gallery': '#ebebeb',
      'gallery-transparent': 'rgba(0,0,0,0.50)',
      'gallery-dark': '#d7d7d7',
      'dark': '#282828',
      'dark-grey': '#313131',
      'nobel': '#b7b7b7',
    }
  },
  plugins: [],
}

