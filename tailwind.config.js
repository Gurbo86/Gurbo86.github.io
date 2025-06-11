/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./project_pages/**/*.html",
    "./css/**/*.css",
    "./*.html", 
    "./**/*.html", 
    "./js/**/*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/aspect-ratio')
    // ...otros plugins...
  ],
}

