/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  content: [],
  theme: {
    extend: {
      colors: {
        'white': {
          100: '#FFFFFF',
          200: '#E5E5E5',
        },
        'grey' :{
          100: '#F3F4F6',
          200: '#6D6E71',
        },
        'black' : {
          100: '#000000',
        },
        'red' : {
          100: '#D6001C',
        },
        'primary': '#FFFFFF',
        'secondary': {
          100: '#E2E2D5',
          200: '#888883',
        },  
      },
      dropShadow: {
        'sm' : '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
        'md' : '0 4px 6px -1px rgba(0, 0, 0, 0.1)',
        'lg' : '0 10px 15px -3px rgba(0, 0, 0, 0.1)',
        'xl' : '0 20px 25px -5px rgba(0, 0, 0, 0.1)',
        '2xl' : '0 25px 50px -12px rgba(0, 0, 0, 0.25)',
      }
    },
  },
  plugins: [],
}

