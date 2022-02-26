module.exports = {
  content: [
    './templates/*.html',
    './templates/Info.html',
    './static/js/*.js',
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        sand: {
          100: '#fff2e8',
          200: '#dd8c8a',
          300: '#c3875d'
        }
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [require("daisyui")],
}
