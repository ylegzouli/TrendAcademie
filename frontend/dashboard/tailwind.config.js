/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/routes/**/*.{html,js,svelte}"],
  plugins: [require("@tailwindcss/typography"), require("daisyui")],
}

