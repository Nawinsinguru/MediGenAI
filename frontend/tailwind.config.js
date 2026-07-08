/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#f8f7ff',
          100: '#ede9ff',
          200: '#ddd5ff',
          300: '#c9b8ff',
          400: '#b09eff',
          500: '#9b7fee',
          600: '#8b62d9',
          700: '#7a4ec9',
          800: '#6a3db8',
          900: '#5a2fa8',
        },
        cream: {
          50: '#fffaf5',
          100: '#fff5eb',
          200: '#ffe8d6',
          300: '#ffdcc1',
          400: '#ffcbaa',
          500: '#ffb896',
          600: '#e8a47a',
          700: '#c68a5c',
          800: '#a67344',
          900: '#8a5c31',
        },
      },
      animation: {
        'fade-in': 'fadeIn 0.3s ease-in',
        'slide-up': 'slideUp 0.3s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(10px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
      },
    },
  },
  plugins: [],
}
